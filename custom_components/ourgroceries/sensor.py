"""Support for Our Groceries."""
import logging

from . import DOMAIN
from homeassistant.helpers.entity import Entity


_LOGGER = logging.getLogger(__name__)

ATTR_RECIPES = 'recipes'
ATTR_SHOPPING_LISTS = 'shopping_lists'


async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the OurGroceries sensor platform."""
    _LOGGER.debug('add_entities')
    og = hass.data[DOMAIN]
    add_entities([OurGroceriesSensor(og)], True)


class OurGroceriesSensor(Entity):
    """Representation of an Our Groceries sensor."""

    def __init__(self, og):
        """Initialize the sensor."""
        self._og = og
        self._lists = []

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'our_groceries'

    @property
    def state(self):
        """Return the state of the sensor."""
        _LOGGER.debug('get og state')
        shopping_lists = len(self._lists.get('shoppingLists', []))
        recipes = len(self._lists.get('recipes', []))
        return shopping_lists + recipes

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        _LOGGER.debug({
            ATTR_RECIPES: self._lists.get('recipes'),
            ATTR_SHOPPING_LISTS: self._lists.get('shoppingLists')
        })
        return {
            ATTR_RECIPES: self._lists.get('recipes'),
            ATTR_SHOPPING_LISTS: self._lists.get('shoppingLists')
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes (depricated)."""
        _LOGGER.debug({
            ATTR_RECIPES: self._lists.get('recipes'),
            ATTR_SHOPPING_LISTS: self._lists.get('shoppingLists')
        })
        return {
            ATTR_RECIPES: self._lists.get('recipes'),
            ATTR_SHOPPING_LISTS: self._lists.get('shoppingLists')
        }

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return 'mdi:format-list-bulleted'

    async def async_update(self):
        """Update data from API."""
        _LOGGER.debug('updating og state')
        self._lists = await self._og.get_my_lists()

