# Welcome to UPS Hat setup

UPS Used: https://www.waveshare.com/ups-hat-b.htm

UPS Hat works straight forward when you connect it to Raspberry Pi. In order to view the UPS stats you will need to configure few things.

## What is the setup used for?

ups-monitor.py : It grabs the UPS Hat stats, and then displays on local apache web server along with logging into csv.

## Pre-requisites: 

1. If smbus is not found: You will have to install smbus module which is used by INA219.py using : ```sudo apt-get install python3-smbus```
2. pip by default won't be there: if you enter pip you will be prompt with this error: pip: command not found, install it using following command: ```sudo apt-get install python3-pip```
3. Flask for web server: ```pip install flask```

## How to use it?

1. First connect to Raspberry Pi and enable I2C via ```sudo raspi-config```.

2. After that download the INA219.py script provided by waveshare (I have provided the same script here for convenience)

3. Then create a directory (ex: ```mkdir UPS-Hat```) and place that script (INA219.py) into that. 
   
   * After that download the script: ups-monitor.py into the UPS-Hat directory. (Hint: For downloading and moving, you can also use another linux system and scp the files from there to ups-hat directory).

4. Now install apache web server & configure using:
	```sudo apt install apache2 -y```
	```sudo usermod -a -G www-data pi```
	```sudo chown -R -f www-data:www-data /var/www/html```

5. Now to enable run on boot enter: ```echo 'sudo python /home/pi/UPS-Hat/ups-monitor.py &' >> /home/pi/.bashrc```

