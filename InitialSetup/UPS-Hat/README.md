# Welcome to UPS Hat setup

UPS Hat works straight forward when you connect it to Raspberry Pi. In order to view the UPS stats you will need to configure few things.

## What is the setup used for?

ups-server.py: It can be used to view UPS stats on a local web page.
ups-datalogger.py:    The stats can also be logged using another script.

For continuous monitoring, you will have to enable run on boot for both the script (ups-server.py and ups-datalogger.py).

## How to use it?

Pre-requisites: You will have to install smbus module which is used by INA219.py using : sudo apt-get install python3-smbus

1. First connect to Raspberry Pi and enable I2C via ```sudo raspi-config```.

2. After that download the INA219.py script provided by waveshare (I have provided the same script here for convenience)

3. Then create a directory and place that script (INA219.py) into that. After that download the scripts: ups-server.py and ups-datalogger.py.

4. Now you can any of the following using commands are: ```python ups-server.py``` or ```python ups-datalogger.py```

