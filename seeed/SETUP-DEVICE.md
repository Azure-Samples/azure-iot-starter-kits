# Setup your device

Instructions below assume that you have completed the physical assembly of your Raspberry Pi 3.

## Enable interfaces

1. Power on the Raspberry Pi 3 by connecting the USB/micro USB power cord to the Raspberry Pi 3 (via micro USB) and to a power source (via USB).

    **NOTE**: In some cases, after powering on your Raspberry Pi 3, you may encounter `undervoltage detected` warnings. If this happens, try using a wall socket (with USB adapter) instead of your laptop as the power source. If that doesn't eliminate the warnings, try using a different USB cable.

1. Let the Raspberry Pi 3 boot. When boot is complete, you will see the OS GUI.
1. After booting, press `CTRL+ALT+F1` to go to a terminal window.
1. Launch raspi-config:

    `sudo raspi-config`

1. Enable SSH:
    - Select option 5 for `Interfacing Options`.
    - Select option P2 (`SSH`) to enable SSH.
1. Enable the camera:
    - Again select option 5 for `Interfacing Options`.
    - Select option P1 (`Camera`) to enable the camera.
1. Enable the I2C interface:
    - Select option 5 for `Interfacing Options`.
    - Select option P5 (`I2C`) to enable the I2C interface.
1. Connect to the internet:
    - If connecting via Wi-Fi:
        - Select option 2 for `Network Options`
        - Select N2 for `Wi-Fi`
        - If prompted for the country, select it from the list
        - Enter the name of the Wi-Fi network you would like to join
        - Enter the passphrase for the Wi-Fi network
    - If connecting via ethernet
        - Attach ethernet cable
1. Set your keyboard layout to the appropriate setting (Raspberry Pi 3 ships with UK layout)
    - Select option 4 for `Localisation Options`
    - Select I3 for `Change Keyboard Layout`
    - Select the appropriate values from the following screens, e.g. 'English (US)', pressing `ENTER` on each screen to make a selection
1. Press `ESC` to exit raspi-config.

1. Configure the Pi HAT Microphone:

    **NOTE**: The steps below are taken from [http://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/](http://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/), which includes steps for validating the microphone and button setup that aren't shown here.

    Execute the following commands on your Raspberry Pi 3:

    `git clone https://github.com/respeaker/seeed-voicecard.git`

    `cd seeed-voicecard`

    `sudo ./install.sh`

1. Reboot:

    `sudo shutdown -r now`

## Configure your device as a wireless access point

Steps in this section are taken from [https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md). For a video overview of these steps, see [http://link-to-WAP-steps](http://link-to-WAP-steps).

1. Connect your device to the internet. You should have done this in the previous section, but if not, you can do this in one of two ways:

    - If you have access to an ethernet port and ethernet cable, use the ethernet port on your device and your ethernet cable to connect to the internet.
    - If you have a mouse with a USB interface, connect it to your device and use it to connect to a WiFi network (via the device GUI).

        **NOTE**: If your device is in terminal mode, press `CTRL-ALT-F7` to put it back in GUI mode.  You can switch back to console mode with `CTRL-ALT-F1`.

1. Update your device by running the following commands in a terminal window:

    `sudo apt-get update`

    `sudo apt-get upgrade`

    `sudo apt update`

    **NOTE**: `sudo apt-get upgrade` can take up to 20 minutes to complete.

1. Install `dnsmasq` and `hostapd`:

    `sudo apt-get install dnsmasq hostapd`

1. Stop the `dnsmasq` and `hostapd` services:

    `sudo systemctl stop dnsmasq`

    `sudo systemctl stop hostapd`

1. Open the `dhcpcd.conf` file for editing:

    `sudo nano /etc/dhcpcd.conf`

1. Add the following text to the end of the file:

    ```text
    interface wlan0
    static ip_address=192.168.4.1/24
    ```
1. Save the file by pressing `CTRL + X`, then `y`, then `ENTER`.
1. Restart the `dhcpcd` daemon and set up the new `wlan0` configuration:

    `sudo service dhcpcd restart`

1. The DHCP service is provided by `dnsmasq`. By default, the configuration file contains a lot of information that is not needed, and it is easier to start from scratch. Rename this configuration file, and edit a new one:

    `sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig`

    `sudo nano /etc/dnsmasq.conf`

1. Add the following text to the file:

    ```text
    interface=wlan0
    dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
    ```
1. Save the file by pressing `CTRL + X`, then `y`, then `ENTER`.
1. Edit the hostapd configuration file, located at `/etc/hostapd/hostapd.conf`, to add the various parameters for your wireless network. After initial install, this will be a new/empty file.

    `sudo nano /etc/hostapd/hostapd.conf`

1. Add the required information to the configuration file. The example below assumes we are using channel 7, creating a Wi-Fi network with the name `NameOfNetwork`, and a passphrase `AardvarkBadgerHedgehog`. You should replace the network name and passphrase with your own values.  Note that the name and passphrase should *not* have quotes around them. **The passphrase must be between 8 and 64 characters in length.**

    ```text
    interface=wlan0
    driver=nl80211
    ssid=NameOfNetwork
    hw_mode=g
    channel=7
    wmm_enabled=0
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_passphrase=AardvarkBadgerHedgehog
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP
    rsn_pairwise=CCMP
    ```

1. Save the file by pressing `CTRL + X`, then `y`, then `ENTER`.

1. Tell the system where to find this configuration file.

    `sudo nano /etc/default/hostapd`

1. Find the line with #DAEMON_CONF, and replace it with this:

    `DAEMON_CONF="/etc/hostapd/hostapd.conf"`

1. Save the file by pressing `CTRL + X`, then `y`, then `ENTER`.
1. Start up the remaining services:

    `sudo systemctl start hostapd`

    `sudo systemctl start dnsmasq`

1. Remove internet access

    - If you are using an ethernet cable, disconnect it
    - If you are using Wi-fi
        - Edit the wpa_supplicant configuration file using `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
        - You will see a section similar to this:

        ```text
        network={
            ssid=xxx
            ...
        }
        ```
        - Remove the entire `network` section from the file.
        - Save the file using `CTRL + X` then `y`, then `ENTER`.

1. Reboot the device:

    `sudo shutdown -r now`

1. Once the reboot is complete, check that the Wi-Fi network is visible.
    - Search for wireless networks using your laptop. The network SSID you specified in the `hostapd` configuration should now be present
    - If you wish you can test that you can connect to the network using the configured passphrase, but make sure you disconnect before moving on to later steps.