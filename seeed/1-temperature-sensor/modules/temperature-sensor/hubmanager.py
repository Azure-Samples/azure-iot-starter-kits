import os
import sys
import iothub_client
from iothub_client import IoTHubModuleClient, IoTHubClientError, IoTHubTransportProvider

# messageTimeout - the maximum time in milliseconds until a message times out.
# The timeout period starts at IoTHubClient.send_event_async.
# By default, messages do not expire.
MESSAGE_TIMEOUT = 10000

class HubManager(object):

    def __init__(self, protocol = IoTHubTransportProvider.MQTT):

        print("\nPython %s\n" % sys.version)
        print("IoT Hub Client for Python")
        print("Starting the IoT Hub Python sample using protocol %s..." % protocol)

        self.client_protocol = protocol
        self.client = IoTHubModuleClient()
        self.client.create_from_environment(protocol)

        # set the time until a message times out
        self.client.set_option("messageTimeout", MESSAGE_TIMEOUT)
        # some embedded platforms need certificate information
