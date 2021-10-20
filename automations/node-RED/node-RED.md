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
This flow automates control over my S5 robot vacuum cleaner. It does the following:

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
Flow for doorbell automation that:

 * plays doorbell sound and TTS message over Sonos speaker when doorbell is pressed between 07.00 - 19.00 if somebody is home
 * sends notification to mobile if nobody is home or if it is after 19.00 with image snapshot from camera as an attachment
 * display live camera feed on tablet running FullyKioskBrowser

### **Screenshot**
![Doorbell](https://github.com/dykandDK/home-assistant-config/blob/master/automations/node-RED/screenshots/doorbell.png)

