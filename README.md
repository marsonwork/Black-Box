# Black-Box
A journey of raspberry pi being used as NAS


## What is Black-Box?

It is a NAS which is run by the beast (where beast = Raspberry Pi 4B (8GB).

## Functionalities:

1. Can be shutdown with Argon Fan Hat. (Can be used in case of no wifi present, no need to ssh into pi to shut it down)
2. It shuts down with based on Battery Percentage (This needs to be implemented)

## Contents of Black box hardware wise:

1. Raspberry Pi 4B (8GB): The main core of the project.
2. UPS Hat (B) from waveshare: UPS comes as an important factor, since NAS can crash in case of power fluctuations
3. Argon40 Fan Hat & heat sinks: To keep the system cool and steady. This maintains a CPU temperature < 40 'C. 
4. SD Card: For operating system.
5. 2 TB Hard Disk Drive (HDD): For data storage.
6. A power adapter (Comes with UPS hat): Power source to the UPS.

## Softwares required to run into Black-Box:

1. Raspberry Pi 64 bit OS (CLI).
2. Rpi Health Monitor script.
3. Argon40 Fan hat script.
4. .....
5. .....