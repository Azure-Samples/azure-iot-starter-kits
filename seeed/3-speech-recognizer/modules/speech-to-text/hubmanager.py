import os
import sys

from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider

# messageTimeout - the maximum time in milliseconds until a message times out.
# The timeout period starts at IoTHubClient.send_event_async.
# By default, messages do not expire.
MESSAGE_TIMEOUT = 10000

class HubManager(object):

    def __init__(self, connection_string = None, protocol = IoTHubTransportProvider.MQTT):
        if not connection_string:
            connection_string = os.environ['EdgeHubConnectionString']

        print("\nPython %s\n" % sys.version)
        print("IoT Hub Client for Python")
        print("Starting the IoT Hub Python sample using protocol %s..." % protocol)

        self.client_protocol = protocol
        self.client = IoTHubClient(connection_string, protocol)

        # set the time until a message times out
        self.client.set_option("messageTimeout", MESSAGE_TIMEOUT)
        # some embedded platforms need certificate information
        self.set_certificates()

    def set_certificates(self):
        CERT_FILE = os.environ['EdgeModuleCACertificateFile']
        print("Adding TrustedCerts from: {0}".format(CERT_FILE))

        # this brings in x509 privateKey and certificate
        with open(CERT_FILE) as file:
            try:
                self.client.set_option("TrustedCerts", file.read())
                print("set_option TrustedCerts successful")
            except IoTHubClientError as iothub_client_error:
                print("set_option TrustedCerts failed (%s)" % iothub_client_error)
