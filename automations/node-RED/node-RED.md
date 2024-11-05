# Node-RED automations
This folder contains examples of home automations created in node-RED.

Each JSON file in this folder represents a seperate flow.

Use the following steps to import a specific automation example:

1. Open Node-RED
2. Select "Import" from the menu in the top right corner of the screen
3. Copy the code from the specific JSON file and paste it into the textbox
4. Click the "Import" button

Below you will find an overview and short description of each flow.

## Vacuum Control
This [flow](vacuum_control.json) automates control over my S5 robot vacuum cleaner. It does the following:

 * Starts cleaning of selected rooms when cleaning is started from Lovelace
 * Use actionable notification to ask if cleaning should start when nobody is home
 * Pause cleaning when the doorbell is pressed
 * Use actionable notification to ask to empty dustbin when the robot has cleaned 200m2 or more

### **Screenshot**
![Vacuum Control](https://github.com/dykandDK/home-assistant-config/blob/master/automations/node-RED/screenshots/vacuum_control.png)

### **Requirements**
This flow requires the following additional configuration to work:

 * Definition of IOS push categories for actionable notifications
 * Definition of input booleans for room selection

## Doorbell
[Flow](doorbell.json) for doorbell automation that:

 * plays doorbell sound and TTS message over Sonos speaker when doorbell is pressed between 07.00 - 19.00 if somebody is home
 * sends notification to mobile if nobody is home or if it is after 19.00 with image snapshot from camera as an attachment
 * display live camera feed on tablet running FullyKioskBrowser

### **Screenshot**
![Doorbell](https://github.com/dykandDK/home-assistant-config/blob/master/automations/node-RED/screenshots/doorbell.png)

## EV Charging
This [flow](EV_charging.json) automates control over charging of my EV at home using our Easee EV charger. The flow provides the following functionality:

* Send notrification with reminder to plug-in cable when both electricity prices and current SoC are low
* Use actionable notification to ask if charging should continue or be postponed to a time where electricity prices are lowest, when the car is plugged into the EV charger
* Start charging at scheduled time

### **Screenshot**
![EV Charging](https://github.com/dykandDK/home-assistant-config/blob/master/automations/node-RED/screenshots/EV_charging.png)

## Mealie
This [flow](Mealie.json) imports the weekly dinner recipes from the Mealie addon including all ingredients required for each recipe. The data is stored as attributes in a sensor and can then be displayed on your dashboard or used in automations.

### **Screenshot**
![Mealie](https://github.com/dykandDK/home-assistant-config/blob/master/automations/node-RED/screenshots/Mealie.png)

