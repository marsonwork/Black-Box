# Welcome to UPS Hat setup

UPS Hat works straight forward when you connect it to Raspberry Pi. In order to view the UPS stats you will need to configure few things.

## What is the setup used for?

ups-server.py: It can be used to view UPS stats on a local web page.
ups-datalogger.py:    The stats can also be logged using another script.

For continuous monitoring, you will have to enable run on boot for both the script (ups-server.py and ups-datalogger.py).



## Pre-requisites: 

1. If smbus is not found: You will have to install smbus module which is used by INA219.py using : ```sudo apt-get install python3-smbus```
2. pip by default won't be there: if you enter pip you will be prompt with this error: pip: command not found, install it using following command: ```sudo apt-get install python3-pip```
3. Flask for web server: ```pip install flask```

## How to use it?

1. First connect to Raspberry Pi and enable I2C via ```sudo raspi-config```.

2. After that download the INA219.py script provided by waveshare (I have provided the same script here for convenience)

3. Then create a directory (ex: ```mkdir ups-hat```) and place that script (INA219.py) into that. After that download the scripts: ups-server.py, ups-datalogger.py and templates folder. Move all these into the ups-hat directory. (Hint: For downloading and moving, you can also use another linux system and scp the files from there to ups-hat directory).

4. Now you can any of the following using commands are: ```python ups-server.py``` or ```python ups-datalogger.py```

