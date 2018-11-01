import json
import requests
import signal
import sys

import devicecheck
import hubmanager
import mic
import oleddisplay
from iothub_client import IoTHubModuleClient, IoTHubMessage


oled_display = None
hub_client = None


def mic_callback(text):
    if text:
        if oled_display:
            oled_display.println(text)
        
        # Use spaCy to generate a chat response to the request.
        response = get_response(text)

        if oled_display:
            oled_display.println('> {}'.format(response))

        # Send chat messages to IoT Edge.
        send_chat_to_iothub(text, response)


def get_response(text):
    try:
        res = requests.post('http://natural-language-processing:8080/chat', text)
        if res.content and type(res.content) is str:
            content = res.content.replace('"', '')
            print('> {}'.format(content))
            return content
    except Exception as e:
        print(e)

    return "I don't understand"


def send_chat_to_iothub(request, response):
    chat = { 'request': request, 'response': response }
    chat_json = json.dumps(chat, default=lambda o: o.__dict__)

    message = IoTHubMessage(chat_json)
    hub_client.send_event_async(
        "chat", message, send_confirmation_callback, chat_json)


def send_confirmation_callback(message, result, user_context):
    print("Confirmation received with result: {} message: {}".format(result, user_context))


if __name__ == "__main__":
    # Check if the OLED is connected.
    if devicecheck.check_for_oled():
        oled_display = oleddisplay.OledDisplay()
        oled_display.println('Hold button and speak')
    else:
        print('WARNING: OLED is not connected.  Text will not be displayed.')

    # Create the IoT Edge connection.
    hub = hubmanager.HubManager()
    hub_client = hub.client

    # Start a background thread to parse audio from the microphone.
    mic = mic.MicrophoneThread(mic_callback)

    def signal_handler(signal, frame):
        mic.stop()

    signal.signal(signal.SIGINT, signal_handler)

    mic.start()
    mic.join()
