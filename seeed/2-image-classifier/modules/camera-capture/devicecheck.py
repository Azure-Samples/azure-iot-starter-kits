#!/usr/bin/env python

import smbus


def check_for_oled():
    oled_device_address = '0x3c'
    is_oled_found = look_for_device_address(oled_device_address)

    return is_oled_found
   

def look_for_device_address(address):
    bus = smbus.SMBus(1)
    is_device_found = False

    for device in range(128):
        try:
            bus.read_byte(device)
            if hex(device) == address:
                is_device_found = True
                return is_device_found
        except:
            pass  # discard errors that we get when trying to read from empty address

    return is_device_found
