# Black-Box
A journey of raspberry pi being used as NAS and media server.


## What is Black-Box?

It is a NAS which is run by the beast (where beast = Raspberry Pi 4B (8GB)).

## Functionalities:

1. Can be shutdown with Argon Fan Hat. (Can be used in case of no wifi present, no need to ssh into pi to shut it down)
2. It shuts down with based on Battery Percentage (This needs to be implemented)
3. Hosts a NAS that can be used to store files from your end devices
4. Acts as a media center (Uses plex)

## Contents of Black box hardware wise:

1. Raspberry Pi 4B (8GB): The main core of the project.
2. UPS Hat (B) from waveshare: UPS comes as an important factor, since NAS can crash in case of power fluctuations
3. Argon40 Fan Hat & heat sinks: To keep the system cool and steady. This maintains a CPU temperature < 40 'C. 
4. Sandisk Extreme SD Card 64 GB: For operating system. You can use any based on your needs. Even a boot from SSD will work.
5. 2 TB Hard Disk Drive (HDD): For data storage. Size if based on users need.
6. A power adapter (Comes with UPS hat): Power source to the UPS. Update: This power source is not reliable, ordered another power source.

## Docker containers:

1. Nextcloud
2. RPi Monitor
3. Calibre (https://dbtechreviews.com/2020/05/how-to-install-calibre-on-omv-and-docker/)
