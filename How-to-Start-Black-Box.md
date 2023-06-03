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

Assemble Raspberry Pi 4B with any hats available. 

If using UPS hat: Before turnig on the supply, make sure you charge the 18650 cells to the full.

For argon hat setup: Attach the Argon Fan Hat & External HDD on USB 3.0 port. Argon Fan hat will work at 50% speed by default, in order to configure and use its all functionality you can refer to Argon-Fan-Hat section under Initial-Setup. 

## Step 2:

Format SD card with ext4 format. (I am using gparted in Ubuntu for the same).

## Step 3: 

Download Raspberry Pi Imager. Select 64 bit os lite, and in settings, do the configurations for Wi-Fi and SSH, & user creations (Headless setup). Then flash into SD card.

### NOTE: At this point, you should have your battery fully charged, with all hardwares assembled, and SD Card flashed with raspberry pi os. You are now ready for Step 4.

## Step 4: 

Since till now we have setup raspberry pi os in headless way, we do not need to connect monitor.

Connect the power source to Raspberry pi and then switch the Power Button ON on UPS, and then press the boot button on UPS hat. Wait for raspberry pi to boot up and connect to internet, and check for IP on your router page. SSH into Pi with the username set in imager.

Enable I2C using & change login mode to always ask password, from raspi-config ```sudo raspi-config```

Now update the Pi using ```sudo apt update && sudo apt upgrade -y```

## Step 5: 


* Following this: (OMV installation guide from here: https://wiki.omv-extras.org/doku.php?id=omv6:raspberry_pi_install)

* OMV installation command: Enter ``` wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash ```

While running the above script you might encounter with the error: Resolving raw.githubusercontent.com, to solve this: https://www.debugpoint.com/failed-connect-raw-githubusercontent-com-port-443/

Steps to do using above link:

enter: sudo nano /etc/hosts

At the end enter: 185.199.108.133 raw.githubusercontent.com
 
Then save and exit. Now re run the OMV installation command.
 
## Step 6:

* Now go to raspberry pi's IP on browser, then enter user id as : admin, password as: openmediavault.
* Then follow the video guide.

## Step 7: Setting up OMV

* Setup network interfaces with static IPv4 address.

* After successful setup of OMV, open up and install docker and then portainer from OMV extras.

* If prompt with DNS error: Add DNS server IP address under interfacs option under network.

* Go to storage, then see the external disk if your disk is showing up. Then go to file system, and then add existing file system and then add your drive.

* Steps to add user access based shared folder over network:
   Now add shared folder: Go to shared folder > Create > Give name, File system, Path, Under permissions: Admin: read/write, users: read/write, others: no access
                         Now go to services > SMB / CISF > Settings > Tick Enable
                         Now go to services > SMB / CISF > Shares > Create > Add the shared folder created, public: NO > Save.
                         Now go to Storage > Shared Folders > Permissions > Give pi as type user for permission to read / write > Save.
                         Now try to access the local shared folder from your pc over the same network.

## Step 8: Adding duplicati in docker

* https://www.youtube.com/watch?v=-NyzdAYMarw&list=PLhMI0SExGwfAU-UMeKxd1Lu5_a60AlA9N

## Step 9: Adding nextcloud in docker

Follow ref 1, only for writing the stack in docker. DO NOT DEPLOY YET: Keep the stack ready as per the external disk directory, then follow Video 2 for improving the directories and database (mariadb). Then deploy.


* Ref Video 1: https://www.youtube.com/watch?v=7EoEll0lVXc&list=PLhMI0SExGwfAU-UMeKxd1Lu5_a60AlA9N
* Ref video 2: https://www.youtube.com/watch?v=p0I8pikm2P4

## Step 10: Setting up cloudflare tunnel for nextcloud

Follow this video: https://youtu.be/p0I8pikm2P4

### For one of the error: Strict-Transport-Security” HTTP header is not set to at least “15552000” seconds. For enhanced security, it is recommended to enable HSTS

Solution:

Enter the terminal of nextcloud app, then go to: ls /etc/apache2/sites-available/

Under that, there might be multiple .conf file, for in one, you add(for me 000......conf): 

Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains; preload"
Save and close the conf file, restart the nextcloud app container.


Refer this to add: https://docs.nextcloud.com/server/17/admin_manual/installation/harden_server.html#enable-http-strict-transport-security
Discussion related to this issue: https://help.nextcloud.com/t/the-strict-transport-security-http-header-is-not-set-to-at-least-15552000-seconds-for-enhanced-security-it-is-recommended-to-enable-hsts/66568



## Important:

Monitor in screen: if the pi takes a long time to boot: connect in monitor, check the status: Failed to start wait for network to be configured, network interface failed

If it is mentioned as above: follow this link: https://forum.openmediavault.org/index.php?thread/32358-failed-to-start-wait-for-network-to-be-configured-network-interface-failed/


Steps to solve: enter ```sudo omv-firstaid```, the configure wireless network, enter password in psk.






