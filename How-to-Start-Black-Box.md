# Black Box assembly and setup guide

## Components required:

1. Raspberry Pi 4B (I am using 8GB RAM version).
2. Waveshare UPS HAT(B)(https://rarecomponents.com/store/rpi-ups-hat-b).
3. A good Power Supply (https://thinkrobotics.in/products/60w-3-12v-5a-adjustable-power-supply-voltage-display?_pos=8&_sid=c91302f5c&_ss=r)
   The power supply 8.4 provided by waveshare gives undervoltage issue, so better use some other power adapter. I am using the above shown, setting it at 9v. 	
4. Two good 18650 Cells, I am using Panasonic's 18650 cells (https://robu.in/product/panasonic-ncr-18650b-3400-mah-li-ion-battery/) 
   (Choose a good quality Li - ion cells, else after few uses you might get undervoltage warning in Pi, you can check that here: ```vcgencmd get_throttled``` or ```dmesg```)
5. Argon Fan Hat (https://www.tanotis.com/products/sparkfun-argon40-fan-hat-for-raspberry-pi-4-3b-and-3b?gclid=EAIaIQobChMIyrqg0suv-AIVTgwrCh23_QY7EAQYASABEgKPJfD_BwE)
6. Micro SD Card (I am using 64 GB Sandisk extreme)
7. External Hard Disk for server (I am using WD 2TB HDD)


## Step 1: 

Assemble Raspberry Pi 4B with Waveshare UPS Hat (B). Before turnig on the supply, make sure you charge the 18650 cells to the full.

## Step 2:

Attach the Argon Fan Hat & External HDD on USB 3.0 port. Argon Fan hat will work at 50% speed by default, in order to configure and use its all functionality you can refer to Argon-Fan-Hat section under Initial-Setup. 

## Step 3: 

Download Raspberry Pi Imager. Select 64 bit os lite, and in settings, do the configurations for Wi-Fi and SSH, & user creations (Headless setup). Then flash into SD card.

### NOTE: At this point, you should have your battery fully charged, with all hardwares assembled, and SD Card flashed with raspberry pi os. You are now ready for Step 4.

## Step 4: 

Since till now we have setup raspberry pi os in headless way, we do not need to connect monitor.

Connect the power source to Raspberry pi and then switch the Power Button ON on UPS, and then press the boot button on UPS hat. Wait for raspberry pi to boot up and connect to internet, and check for IP on your router page. SSH into Pi with the username set in imager.

Enable I2C using & change login mode to always ask password, from raspi-config ```sudo raspi-config```

Now update the Pi using ```sudo apt update && sudo apt upgrade -y```

## Step 5: 


* Following this: (OMV installation guide from here: https://wiki.omv-extras.org/doku.php?id=installing_omv6_raspberry_pi)

* Enter ``` wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash ```
 
## Step 6:

* Now go to raspberry pi's IP on browser, then enter user id as : admin, password as: openmediavault.
* Then follow the video guide.

## Important:

Monitor in screen: if the pi takes a long time to boot: connect in monitor, check the status: Failed to start wait for network to be configured, network interface failed

If it is mentioned as above: follow this link: https://forum.openmediavault.org/index.php?thread/32358-failed-to-start-wait-for-network-to-be-configured-network-interface-failed/

Steps to solve: enter ```sudo omv-firstaid```, the configure wireless network, enter password in psk.

## Step 6:





