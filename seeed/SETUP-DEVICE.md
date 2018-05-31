# Setup your device

Instructions below assume that you have completed the physical assembly of your Raspberry Pi 3.

## Network setting
You may use your Raspberry Pi 3 with WiFi only, Ethernet only, or both WiFi and Ethernet.

* Using Eternet  

    **NOTE**: Please make sure your netowrk address is not 192.168.4.x subnet.  The Raspberry Pi 3 is preconfigured with 192.168.4.1 WiFi Access Point.  

    When boot is complete, you can see IP Address of your Raspberry Pi 3 on the screen.
    
    Example

        My IP address is [IP Address of Raspberry Pi 3] 
        [  OK  ] Started Session c1 of user root.  
        Starting User Manager for UID 0...  
        [  OK  ] Started /etc/rc.local Compatibility.  
        Starting Terminate Plymouth Boot Screen...  
        Starting Hold until boot process finishes up...  
          
        Raspbian GNU/Linux 9 raspberrypi tty1  
        raspberrypi login:  

    You can also find the IP address of the device, run `ifconfig` on the device and look for the IP address of the `wlan0` interface for WiFi and the `eth0` interface for Ethernet. (You should be able to SSH to the device using this address and the default Raspberry Pi 3 credentials.)

    Example
    IP address of the Ethernet is 192.168.1.10
    IP address of the Wi-Fi is 192.168.4.1

        pi@raspberrypi:~ $ ifconfig
        eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.1.10  netmask 255.255.254.0  broadcast 10.123.13.255
            inet6 fe80::577d:2969:1bb3:c9fb  prefixlen 64  scopeid 0x20<link>
            inet6 2001:4898:e0:1027:e5a8:a3eb:f5c9:7ba6  prefixlen 64  scopeid 0x0<global>
            ether b8:27:eb:a0:7e:8b  txqueuelen 1000  (Ethernet)
            RX packets 8435  bytes 12467515 (11.8 MiB)
            RX errors 0  dropped 1  overruns 0  frame 0
            TX packets 4456  bytes 425644 (415.6 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 16  bytes 2048 (2.0 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 16  bytes 2048 (2.0 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.4.1  netmask 255.255.255.0  broadcast 192.168.4.255
            inet6 fe80::3738:4d9:eb92:704f  prefixlen 64  scopeid 0x20<link>
            ether b8:27:eb:f5:2b:de  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 30  bytes 4694 (4.5 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

* Using WiFi 

    You can specify your SSID and passphase later with the Azure IoT Starter Kit companion CLI

## Enable interfaces

1. Power on the Raspberry Pi 3 by connecting the USB/micro USB power cord to the Raspberry Pi 3 (via micro USB) and to a power source (via USB).

    **NOTE**: In some cases, after powering on your Raspberry Pi 3, you may encounter `undervoltage detected` warnings. If this happens, try using a wall socket (with micro USB connector) instead of your laptop as the power source. If that doesn't eliminate the warnings, try using a different USB cable.

1. Let the Raspberry Pi 3 boot. When boot is complete, you will see the console.

1. Launch raspi-config

    `sudo raspi-config`

1. Set your keyboard layout to the appropriate setting (Raspberry Pi 3 ships with UK layout)
    - Select option 4 for `Localisation Options`
    - Select I3 for `Change Keyboard Layout`
    - Select the appropriate values from the following screens, e.g. 'English (US)', pressing `ENTER` on each screen to make a selection

1. Select Wi-Fi country
    - Select option 2 for `Network Options`
    - Select N2 for `Wi-Fi`
    - If prompted for the country, select it from the list
    - Select `Cancel` where you are prompted for SSID


1. Press `ESC` to exit raspi-config.

1. Reboot:

    `sudo shutdown -r now`

1. Once the reboot is complete, check that the Wi-Fi network is visible.
    - Search for wireless networks using your laptop.
        - SSID : `SeeedGroveKit`
        - Passphrase : `SeeedGroveKit`


## Rebuilding Raspbian Settings

In case you need to rebuild your Raspberry Pi 3 with Raspbian, you need to download and install Raspbinan Stretech Lite

- Download Raspbian Stretch Lite [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/).
    
- Install instruction

    For the detailed steps to install Raspbian Stretch Lite, please refer to the instruction here : [https://www.raspberrypi.org/documentation/installation/installing-images/README.md](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)


## Enabling interfaces on fresh install of Raspbian
In addition to steps above, you need to enable additional interfaces.

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

Once you complete steps described above, follow the instruction in the begineeing of this document.