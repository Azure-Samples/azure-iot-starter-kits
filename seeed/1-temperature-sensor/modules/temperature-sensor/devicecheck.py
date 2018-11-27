#!/usr/bin/env python

import smbus2


def check_for_bme280():
    bme280_device_address = '0x76'
    is_bme280_found = look_for_device_address(bme280_device_address)

    return is_bme280_found


def look_for_device_address(address):
    bus = smbus2.SMBus(1)
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
