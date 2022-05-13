## Black Box assembly and setup guide

Note: This document is still in development and I am replicating setup for black box to write each and every step, currently due to undervoltage issue, I have not completed it, will be finishing it soon once new stock of battery arrives.

## Components required:

1. Raspberry Pi 4B (I will be using 8GB RAM version)
2. Waveshare UPS HAT(B) & 8.4 charger (Provided by waveshare)
3. Two good 18650 Cells (Choose a good quality Li - ion cells, else after few uses you might get undervoltage warning in Pi, you can check that here: ```vcgencmd get_throttled``` or ```dmesg```)
4. Argon Fan Hat
5. Micro SD Card (I am using 64 GB Sandisk extreme)
6. External Hard Disk for server (I am using WD 2TB HDD)


## Step 1: 

Assemble Raspberry Pi 4B with Waveshare UPS Hat (B). Before turnig on the supply, make sure you charge the 18650 cells to the full through 8.4 v charger provided.

## Step 2:

Attach the Argon Fan Hat along with External HDD on USB 3.0 port.

## Step 3: 

Flash Raspberry Pi 64 bit lite os image. You can do it through Raspberry Pi Imager, or using the image file from raspberry pi org. Since we won't be needing the GUI environment here, we will be limiting oursefls to a lite version.

### NOTE: At this point, you should have your battery fully charged, with all hardwares assembled, and SD Card flashed with raspberry pi os. You are now ready for Step 4.

## Step 4: 

We will be using monitor to set up the raspberry pi initially, you can use the headless way too. 

Plug the raspberry pi to the monitor, and then switch the Power Button ON on UPS, and then press the boot button on UPS hat. Let the Pi boot. Setup username and password, and then enable SSH and I2C. After that change logic mode to always ask password, from raspi-config (```sudo raspi-config```). Now update the Pi using ```sudo apt update && sudo apt upgrade -y```

## Step 5: 

Now ssh into raspberry pi and follow OMV installation guide from here: https://wiki.omv-extras.org/doku.php?id=installing_omv6_raspberry_pi.

## Important:

Monitor in screen: if the pi takes a long time to boot: connect in monitor, check the status: Failed to start wait for network to be configured, network interface failed

If it is mentioned as above: follow this link: https://forum.openmediavault.org/index.php?thread/32358-failed-to-start-wait-for-network-to-be-configured-network-interface-failed/

Steps to solve: enter sudo omv-firstaid, the configure wireless network, enter password in psk.



