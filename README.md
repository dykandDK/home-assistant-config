[![Home Assistant version][img-ha-version]][link-ha-version]
![Project Maintenance][maintenance-shield]
[![license][license-shield]](LICENSE.md)

[![GitHub Activity][commits-shield]][commits]
[![GitHub Last Commit][last-commit-shield]][commits]

![GitHub Stars][stars-shield]
![GitHub Watchers][watchers-shield]
![GitHub Forks][forks-shield]

<a href="https://www.buymeacoffee.com/dykandDK" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# Home Assistant - configuration and automations
This repository contains a collection of my personnal Home Assistant (HA) configuration and automations.

It may not include the full configuration needed to replicate my setup, but it does include relevant examples of my configuration and automations.

Please feel free to use and change as you like for your own HA setup.

---
<p align="center">
  <a href="#hardware">Hardware</a> •
  <a href="#integrated-smart-devices">Integrated smart devices</a> •
  <a href="#addons">Addons</a> •
  <a href="#lovelace-dashboards">Lovelace dashboards</a> •
  <a href="#custom-components">Custom components</a> •
  <a href="#automations">Automations</a> •
  <a href="#license">License</a>
</p>

---

## Hardware
This is my current hardware setup:

- Intel NUC i7 with 16 Gb RAM and 500 Gb SSD
	- Running Home Assistant in Proxmox VM with 2 cores, 32 Gb HDD and 4 Gb RAM allocated
- Sonoff Zigbee 3.0 USB Dongle Plus (P version with CC2652P chipset)
- Lenovo P11, M10 and M8 tablets for dashboard display using Fully Kiosk browser

## Integrated smart devices
My current setup includes the following integrated devices:

|Lights                                |Sensors                       |Media                     |Other                           |
|--------------------------------------|------------------------------|--------------------------|--------------------------------|
|Hue lights, remotes and buttons       |Hue Motion Sensors            |Apple TVs                 |Roborock S5 Max robot vacuum    |
|IKEA TRÅDFRI bulbs, plugs and remotes |Aqara Door/Window sensors     |Marantz SR7010 AV receiver|Bosch Indego 400 lawnmover      |
|Nordtronic Zigbee Box Dimmers & Relays|Aqara Multi sensors           |Sonos speakers            |Ubiquiti Unifi network equipment|
|Koogeek Smart plugs                   |Netatmo Weather Station       |                          |Reolink IP cameras              |
|Innr Smart plugs                      |VELUX Active Sensors          |                          |Easee EV charging station       |
|Shelly S Smart plugs                  |Sonoff TH16 og DS18B20 sensors|                          |Smart-me energy meter           |

## Addons
I use the following addons:

- ESPHome
- MariaDB
- Zigbee2MQTT
- Mosquitto broker
- Node-RED
- File editor
- Visual Studio Code
- Samba share
- Samba Backup
- phpMyAdmin
- Mealie

## Lovelace dashboards
I use different Lovelace dashboards:

### Tablet dashboard
This dashboard is optimized for viewing on tablet with screen resolution 1280x800:

![Main view](https://github.com/dykandDK/home-assistant-config/blob/master/screenshots/HA-dashboard.gif)

See more screenshots [HERE](/screenshots/screenshots.md)

### Smart clock radio dashboard
This dashboard is designed to replace and extend the functionality of an old clock radio. It is designed for viewing on a 8" tablet and includes four different views:

1) Large digital clock display
2) Set alarm timer
3) Play music
4) View weather information

The Swipe-card custom component is used to swipe between the clock and other views.

In addition an icon bar provides easy access to:

- Open CCTV app
- View and enable/disable alarm timer
- View and control home alarm system
- Turn off main lights
- View/set home state

![Clock radio](https://github.com/dykandDK/home-assistant-config/blob/master/screenshots/Clock-radio01.png)

### Mobile device dashboard 
This dashboard is mainly used on mobile devices, and includes additional elements, such as a universal remote:

![Universal remote](https://github.com/dykandDK/home-assistant-config/blob/master/screenshots/06_remote.jpg)

For the time being, only my tablet dashboards are included in this repository.

I prefer to maintain dashboards in YAML mode and I use `!include` statements to make it easier to maintain and re-use relevant parts of each dashboard.

This means that the dashboards are divided into seperate files that are located in the [/include](/include) folder. 

If you prefer to edit your Lovelace dashboard in UI mode, I've created a consolidated version of my tablet dashboard that can be used as a starting point. The file is called `tablet_ui.yaml` and includes most - but not all features - from my YAML version. However, the dashboard should be enough to get get you started.

I still highly recommend to use the YAML version if you are serious about creating a personalized dashboard. The main reasoning behind my recommendation is:

- The YAML version allows you to use include statements to split your file into smaller and more manageable files, which makes it easier to move stuff around or exclude certain elements of the dashboards. It also allows you to reuse code across multiple views or dashboards and just maintain the code one place. This is particularly useful for the header bar that is used in each view of the dashboard

- The YAML version also supports insertion of comments in the code. This is useful to document your code but can also be use to quickly disable parts of your code without having to delete it entirely. 

## Custom components
I use several custom frontend compontents that are installed via [HACS](https://hacs.xyz/):

- [Browser_mod](https://github.com/thomasloven/hass-browser_mod)
- [Kiosk mode](https://github.com/NemesisRE/kiosk-mode)
- [Layout Card](https://github.com/thomasloven/lovelace-layout-card)
- [Custom button card](https://github.com/custom-cards/button-card)
- [Vertical Stack-in](https://github.com/ofekashery/vertical-stack-in-card)
- [Our Groceries card](https://github.com/ljmerza/our-groceries-card)
- [Xiaomi Vacuum card](https://github.com/benct/lovelace-xiaomi-vacuum-card)
- [Mini media-player](https://github.com/kalkih/mini-media-player)
- [Mini graph card](https://github.com/kalkih/mini-graph-card)
- [Auto-entities card](https://github.com/thomasloven/lovelace-auto-entities)
- [Multiple Entity Row](https://github.com/benct/lovelace-multiple-entity-row)
- [Collapsable cards](https://github.com/RossMcMillan92/lovelace-collapsable-cards)
- [Atomic Calendar Revive card](https://github.com/marksie1988/atomic-calendar-revive)
- [Slider Entity Row](https://github.com/thomasloven/lovelace-slider-entity-row)
- [Swipe card](https://github.com/bramkragten/swipe-card)
- [EV Charger Card](https://github.com/tmjo/charger-card)
- [ApexCharts Card](https://github.com/RomRider/apexcharts-card)
- [Bar Card](https://github.com/custom-cards/bar-card)
- [Sonos Playlist Card](https://github.com/ChrisK91/sonos-playlist-card)
- [Compass Card](https://github.com/tomvanswam/compass-card)
- [History Explorer Card](https://github.com/alexarch21/history-explorer-card)
- [Sankey Chart](https://github.com/MindFreeze/ha-sankey-chart/)
- [Power Flow Plus](https://github.com/flixlix/power-flow-card-plus)

My lovelace dashboards would simply not be possible without these custom cards. So a special shout out and million thanks goes out to all developers for their contributions to the Home Assistant community.

## Automations
I mainly use node-RED for automations. HA scripts and automations are excluded from this repository.

Examples of my node-RED automations can be found [HERE](/automations/node-RED/node-RED.md).

## License
**MIT License**

Copyright (c) 2019 - present

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[commits-shield]: https://img.shields.io/github/commit-activity/m/dykandDK/home-assistant-config.svg
[commits]: https://github.com/dykandDK/home-assistant-config/commits/master
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/dykandDK/home-assistant-config.svg
[stars-shield]: https://img.shields.io/github/stars/dykandDK/home-assistant-config.svg?style=social&label=Stars
[forks-shield]: https://img.shields.io/github/forks/dykandDK/home-assistant-config.svg?style=social&label=Forks
[watchers-shield]: https://img.shields.io/github/watchers/dykandDK/home-assistant-config.svg?style=social&label=Watchers
[link-ha-version]: https://github.com/home-assistant/core/releases/tag/2023.9.2
[img-ha-version]: https://img.shields.io/badge/Home_Assistant_release-2023.9.2-53c1f1.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxLjgsMTNIMjBWMjFIMTNWMTcuNjdMMTUuNzksMTQuODhMMTYuNSwxNUMxNy42NiwxNSAxOC42LDE0LjA2IDE4LjYsMTIuOUMxOC42LDExLjc0IDE3LjY2LDEwLjggMTYuNSwxMC44QTIuMSwyLjEgMCAwLDAgMTQuNCwxMi45TDE0LjUsMTMuNjFMMTMsMTUuMTNWOS42NUMxMy42Niw5LjI5IDE0LjEsOC42IDE0LjEsNy44QTIuMSwyLjEgMCAwLDAgMTIsNS43QTIuMSwyLjEgMCAwLDAgOS45LDcuOEM5LjksOC42IDEwLjM0LDkuMjkgMTEsOS42NVYxNS4xM0w5LjUsMTMuNjFMOS42LDEyLjlBMi4xLDIuMSAwIDAsMCA3LjUsMTAuOEEyLjEsMi4xIDAgMCwwIDUuNCwxMi45QTIuMSwyLjEgMCAwLDAgNy41LDE1TDguMjEsMTQuODhMMTEsMTcuNjdWMjFINFYxM0gyLjI1QzEuODMsMTMgMS40MiwxMyAxLjQyLDEyLjc5QzEuNDMsMTIuNTcgMS44NSwxMi4xNSAyLjI4LDExLjcyTDExLDNDMTEuMzMsMi42NyAxMS42NywyLjMzIDEyLDIuMzNDMTIuMzMsMi4zMyAxMi42NywyLjY3IDEzLDNMMTcsN1Y2SDE5VjlMMjEuNzgsMTEuNzhDMjIuMTgsMTIuMTggMjIuNTksMTIuNTkgMjIuNiwxMi44QzIyLjYsMTMgMjIuMiwxMyAyMS44LDEzTTcuNSwxMkEwLjksMC45IDAgMCwxIDguNCwxMi45QTAuOSwwLjkgMCAwLDEgNy41LDEzLjhBMC45LDAuOSAwIDAsMSA2LjYsMTIuOUEwLjksMC45IDAgMCwxIDcuNSwxMk0xNi41LDEyQzE3LDEyIDE3LjQsMTIuNCAxNy40LDEyLjlDMTcuNCwxMy40IDE3LDEzLjggMTYuNSwxMy44QTAuOSwwLjkgMCAwLDEgMTUuNiwxMi45QTAuOSwwLjkgMCAwLDEgMTYuNSwxMk0xMiw2LjlDMTIuNSw2LjkgMTIuOSw3LjMgMTIuOSw3LjhDMTIuOSw4LjMgMTIuNSw4LjcgMTIsOC43QzExLjUsOC43IDExLjEsOC4zIDExLjEsNy44QzExLjEsNy4zIDExLjUsNi45IDEyLDYuOVoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=21600