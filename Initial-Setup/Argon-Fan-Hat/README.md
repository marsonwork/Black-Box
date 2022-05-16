# How to use Argon Fan hat

Here I will be describing how to use the argon fan hat with raspberry pi.

First of all it runs at default of 50 % fan speed when connected, and Power button on board is only functional after the script installation.

Below are the steps to use the fan hat along with script.

## Steps to configure Argon Fan Hat:

### Step 1: 

Attach the fan hat while raspberry pi is turned off. Make sure you slide the heat sink on top of main processor to slightly on right side (since the screw on bottom of fan hat interfers with the heat sink.)

### Step 2: 

Turn on Pi, default speed will be 50 % fan speed, without script installation.

### Step 3: 

Install this script, instead of the one mentioned in the document:

		curl https://download.argon40.com/argon1.sh | bash

### Step 4: 

Reboot the Pi

To access configuration: argonone-config

To uninstall it: argonone-uninstall


### Source: https://github.com/okunze/Argon40-ArgonOne-Script