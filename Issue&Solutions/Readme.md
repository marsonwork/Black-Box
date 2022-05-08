# List of issues I encountered while setting up blackbox:

## Pi not rebooting with Argon Fan hat

So I am using argon fan hat along with waveshare ups hat(b). Sometimes I have noticed while being plugged in, rasberry pi does not boot up back after switch is pressed for reboot, or from a soft shutdonw.

It is not observered always. Many times it works perfectly.

### Solution: 

No possible solution as of now.

## Pi "not booting / Not able to connect to network" after OMV 6 flash:

If you have not connected monitor, you will find that Pi is not assigned with any IP address, when you log in through a monitor, you will see as Pi is stuck as: 

"A start job is running for wait for Network to be configured (Some time / No limit)"

At the end of it, you will get a message as: 

"Failed to start wait for network to be configured, network interface failed"

### Solution:

Be on monitor, log into Pi, then enter sudo omv-firstaid, then configure wireless interface, and enter your ssid and password (in place of PSK).

## OMV 6 Not starting after Pi reboots:

So I have observed on 24th April 2022, that I restarted my pi, but could not log into OMV. The OMV page on IP address was not showing up. Since I have used OMV6, thought might be some glitches, then searched in forums a bit, and found few possible fixes for it. Here are list of fixes mentioned: https://forum.openmediavault.org/index.php?thread/21269-solutions-to-common-problems/

### Solution: 

The one worked for me was restarting browser, so it is not OMV issue.
