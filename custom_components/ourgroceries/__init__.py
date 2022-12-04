"""Support for Our Groceries."""
from datetime import timedelta
from functools import wraps
import logging

from ourgroceries import OurGroceries
import voluptuous as vol

from homeassistant.components import http
from homeassistant.components.http.data_validator import RequestDataValidator
from homeassistant.const import (CONF_USERNAME, CONF_PASSWORD)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.entity_component import EntityComponent


__version__ = '1.3.13'
_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=300)
DOMAIN = 'ourgroceries'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string
    })
}, extra=vol.ALLOW_EXTRA)

SERVICE_ADD_TO_LIST = 'add_to_list'
SERVICE_REMOVE_FROM_LIST = 'remove_from_list'
SERVICE_COPY_TO_LIST = 'copy_to_list'

ATTR_LIST_ID = 'list_id'
ATTR_ITEMS = 'items'

ITEMS_SCHEMA = vol.Schema({
    vol.Required(ATTR_LIST_ID): cv.string,
    vol.Required(ATTR_ITEMS): vol.All(cv.ensure_list, [str])
})

SERVICE_TO_METHOD = {
    SERVICE_ADD_TO_LIST: {
        'method': 'async_add_to_list',
        'schema': ITEMS_SCHEMA},
    SERVICE_REMOVE_FROM_LIST: {
        'method': 'async_remove_from_list',
        'schema': ITEMS_SCHEMA},
    SERVICE_COPY_TO_LIST: {
        'method': 'async_copy_to_list',
        'schema': vol.Schema({
            vol.Required(ATTR_LIST_ID): cv.string,
            vol.Required('from_list_id'): cv.string,
            'unique_only': cv.boolean})}
}

async def async_setup(hass, config):
    """Add API for interacting with Our Groceries."""

    _LOGGER.debug('creating og instance')
    conf = config[DOMAIN]
    hass.data[DOMAIN] = og = OurGroceries(
        username=conf.get(CONF_USERNAME),
        password=conf.get(CONF_PASSWORD))

    _LOGGER.debug('logging into og')
    await og.login()

    _LOGGER.debug('setting up sensor')
    hass.async_create_task(async_load_platform(hass, 'sensor', DOMAIN, {}, config))

    hass.http.register_view(OurGroceriesView(og))
    _LOGGER.debug('registered view')

    services = OurGroceriesServices(og)

    async def async_service_handler(service):
        """Map services to methods on OurGroceriesServices."""
        method = SERVICE_TO_METHOD.get(service.service)
        if not method:
            return

        params = {
            key: value for key, value in service.data.items()}

        await getattr(services, method['method'])(**params)

    for service in SERVICE_TO_METHOD:
        schema = SERVICE_TO_METHOD[service]['schema']
        hass.services.async_register(
            DOMAIN, service, async_service_handler, schema=schema)

    _LOGGER.debug('registered services')

    return True

def _handle_api_errors(handler):
    """Webview decorator to handle errors."""
    @wraps(handler)
    async def error_handler(view, request, *args, **kwargs):
        """Handle exceptions that raise from the wrapped request handler."""
        try:
            result = await handler(view, request, *args, **kwargs)
            return result
        except Exception as err:
            _LOGGER.error(err)
            return view.json_message(message=err, status_code=500, message_code=err.__class__.__name__.lower())

    return error_handler

class OurGroceriesView(http.HomeAssistantView):
    """View to retrieve Our Groceries content."""

    url = '/api/ourgroceries'
    name = 'api:ourgroceries:ourgroceries'

    def __init__(self, og):
        """Initialize ourgroceries view."""
        self._og = og

    @_handle_api_errors
    @RequestDataValidator(vol.Schema({
        vol.Required('command'): str,
        vol.Optional('list_id'): str,
        vol.Optional('list_type'): str,
        vol.Optional('name'): str,
        vol.Optional('value'): str,
        vol.Optional('item_id'): str,
        vol.Optional('cross_off'): bool,
    }))
    async def post(self, request, data):
        """Run an our groceries command."""
        _LOGGER.debug(data)
        command = data.get('command')
        _LOGGER.debug('web post command {}'.format(command))
        api_data = None

        if command == 'get_my_lists':
            _LOGGER.debug('web post get_my_lists')
            api_data = await self._og.get_my_lists()

        if command == 'get_list_items':
            list_id = data.get('list_id')

            _LOGGER.debug('web post get_list_items list_id:{}'.format(list_id))
            if list_id is None:
                return self.json({'error': 'missing list_id'}, status_code=400)
            api_data = await self._og.get_list_items(list_id)

        if command == 'create_list':
            name = data.get('name')
            list_type = data.get('list_type')

            _LOGGER.debug('web post get_list_items name:{}, list_type:{}'.format(name, list_type))
            if name is None or list_type is None:
                return self.json({'error': 'missing name or list_type'}, status_code=400)
            api_data = await self._og.create_list(name, list_type)

        if command == 'toggle_item_crossed_off':
            list_id = data.get('list_id')
            item_id = data.get('item_id')
            cross_off = data.get('cross_off')

            _LOGGER.debug('web post get_list_items list_id:{}, item_id:{}, cross_off:{}'.format(list_id, item_id, cross_off))
            if list_id is None or item_id is None or cross_off is None:
                return self.json({'error': 'missing name, item_id, or cross_off'}, status_code=400)
            api_data = await self._og.toggle_item_crossed_off(list_id, item_id, cross_off)

        if command == 'add_item_to_list':
            list_id = data.get('list_id')
            value = data.get('value')

            _LOGGER.debug('web post get_list_items list_id:{}, value:{}'.format(list_id, value))
            if list_id is None or value is None:
                return self.json({'error': 'missing list_id'}, status_code=400)
            api_data = await self._og.add_item_to_list(list_id, value, None)
        
        if command == 'remove_item_from_list':
            list_id = data.get('list_id')
            item_id = data.get('item_id')

            _LOGGER.debug('web post get_list_items list_id:{}, item_id:{}'.format(list_id, item_id))
            if list_id is None or item_id is None:
                return self.json({'error': 'missing list_id or item_id'}, status_code=400)
            api_data = await self._og.remove_item_from_list(list_id, item_id)
        
        status_code = 200
        if api_data is None:
            api_data = {'error': 'Invalid command'}
            status_code = 400

        hass = request.app['hass']
        await hass.helpers.entity_component.async_update_entity('sensor.our_groceries')

        return self.json(api_data)

class OurGroceriesServices:
    def __init__(self, og):
        """Initialize ourgroceries services."""
        self._og = og

    async def _lookup_list(self, id_or_name):
        response = await self._og.get_my_lists()

        # Check if any list matches the given name
        for data in response['shoppingLists']:
            if data['name'] == id_or_name:
                return data['id']

        # Otherwise use the given ID as-is
        return id_or_name

    def _lookup_data(self, data_list, value_key, values):
        lookup = {}
        
        # Create lookup map from value to ID
        for data in data_list:
            lookup[data[value_key]] = data['id']
        
        # Lookup each value in the list, if a mapping exists
        return map(lambda x: lookup[x] if x in lookup else x, values)

    async def _lookup_lists(self, lists):
        response = await self._og.get_my_lists()
        return self._lookup_data(response['shoppingLists'], 'name', lists)

    async def _lookup_items(self, list_id, items):
        response = await self._og.get_list_items(list_id)
        return self._lookup_data(response['list']['items'], 'value', items)

    async def _get_active_items(self, list_id):
        response = await self._og.get_list_items(list_id)
        return [item['value'] for item in response['list']['items'] if 'crossedOff' not in item or not item['crossedOff']]

    async def async_add_to_list(self, list_id, items):
        """Add items to the given list."""
        _LOGGER.debug('adding to list')

        internal_id = await self._lookup_list(list_id)

        for item in items:
            await self._og.add_item_to_list(internal_id, item, None)

        return True

    async def async_remove_from_list(self, list_id, items):
        """Removes items from the given list."""
        _LOGGER.debug('removing from list')

        internal_id = await self._lookup_list(list_id)
        internal_items = await self._lookup_items(internal_id, items)

        for item in internal_items:
            await self._og.remove_item_from_list(internal_id, item)
        
        return True

    async def async_copy_to_list(self, list_id, from_list_id, unique_only=False):
        """Copies items from one list to another."""
        _LOGGER.debug('copying to list')

        internal_src, internal_dest = await self._lookup_lists([from_list_id, list_id])

        items_to_copy = await self._get_active_items(internal_src)

        if unique_only:
            items_in_dest = await self._get_active_items(internal_dest)
            items_to_copy = [x for x in items_to_copy if x not in items_in_dest]

        for item in items_to_copy:
            await self._og.add_item_to_list(internal_dest, item, None)

        return True
