#!/usr/bin/env python

import sys
import os
import bme280
import json
import requests
import time

# import local devicecheck module and iothub_client
import devicecheck
import hubmanager
from bme280sensor import BME280Sensor
from iothub_client import IoTHubModuleClient, IoTHubMessage


BME280_SEND_ENABLED = True
BME280_SEND_INTERVAL_SECONDS = 5


def stream_sensor_data(hub_client, bme280_sensor):
    global BME280_SEND_ENABLED
    global BME280_SEND_INTERVAL_SECONDS
    COUNTER = 0

    while True:
        sensor_data = bme280_sensor.get_sample()
        json_sensor_data = json.dumps(sensor_data, default=lambda o: o.__dict__)

        if BME280_SEND_ENABLED:
            COUNTER = COUNTER + 1
            print("Sending message: {}, Body: {}".format(COUNTER, json_sensor_data))

            message = IoTHubMessage(json_sensor_data)
            hub_client.send_event_async(
                "temperatureOutput", message, send_confirmation_callback, COUNTER)

        time.sleep(BME280_SEND_INTERVAL_SECONDS)


def send_confirmation_callback(message, result, user_context):
    print("Confirmation[{}] received with result: {}".format(user_context, result))


# module_twin_callback is invoked when twin's desired properties are updated.
def module_twin_callback(update_state, payload, user_context):
    global BME280_SEND_ENABLED
    global BME280_SEND_INTERVAL_SECONDS

    print("\nTwin callback called with:\nupdateStatus = {}\npayload = {}".format(update_state, payload))
    data = json.loads(payload)
    if "desired" in data:
        data = data["desired"]

    if "SendData" in data:
        BME280_SEND_ENABLED = bool(data["SendData"])
    if "SendInterval" in data:
        BME280_SEND_INTERVAL_SECONDS = int(data["SendInterval"])


if __name__ == '__main__':
    # Verify the temperature sensor is connected.
    if not devicecheck.check_for_bme280():
        sys.exit("ERROR: BME280 temperature sensor is not detected. Please power off the device and attach it to the i2c port to use this module.")

    # Create the temperature sensor.
    bme280_sensor = BME280Sensor()

    # Create the IoT Edge connection.
    hub = hubmanager.HubManager()
    hub.client.set_module_twin_callback(module_twin_callback, 0)

    # Start streaming sensor data.
    stream_sensor_data(hub.client, bme280_sensor)
