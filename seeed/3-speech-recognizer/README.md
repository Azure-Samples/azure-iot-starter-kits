# speech-recognizer

This project provides a hands-on introduction to Azure IoT Edge by setting up a Raspberry Pi 3 as an Azure IoT Edge device and deploying code to it that captures speech from the Pi microphone, uses an AI module to recognize the speech and determine intent, and respond with an appropriate response on the OLED display. This project is designed for developers who have an interest in learning more about Azure IoT Edge capabilities. Code for IoT Edge modules in this project is written in Python.

While this is a proof-of-concept project designed for instructional purposes, it does provide you with a fully functional IoT Edge device that that does (limited) speech recognition.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Required hardware

You will need the following hardware to complete this project:

- A laptop (**Note**: The instructions in this document have been tested on Mac and Windows.)
- The Grove Starter Kit for Azure IoT Edge
- A 5V Power Supply with Micro USB interface
- A monitor + HDMI cable
- A keyboard with USB interface

## Set up your dev environment

Complete the steps in [Set up your development environment](../SETUP-DEV-ENV.md).

## Assemble and configure your device

In this project, your Raspberry Pi 3 will be configured as an Azure IoT Edge device that captures speech from the Pi microphone, uses an AI module to recognize the speech and determine intent, and respond with an appropriate response on the OLED display. To prepare your Raspberry Pi 3, you'll need to attach the following components from your Grove Starter Kit for Azure IoT Edge:

- Micro SD card
- Keyboard and monitor
- ReSpeaker 4-Mic Array for Raspberry Pi
- Grove - OLED Display 0.96''
- 5V Power Supply with Micro USB interface

After attaching the above components you will boot the Raspberry Pi 3, enable SSH connectivity, and enable the OLED interface. Step-by-step instructions are below.

### Physical assembly

1. Remove Raspberry Pi 3 (including USB/micro USB power cable) and micro SD card from packaging.
1. Insert the micro SD card into micro SD card port on the Raspberry Pi 3.
1. Attach the keyboard (via one of the USB ports) and monitor (via HDMI port) to the Raspberry Pi 3.
1. Remove ReSpeaker 4-Mic Array for Raspberry Pi from its packaging and attach it to the Raspberry Pi 3 via the 40-Pin Headers along the top edge of the board.
1. Remove the OLED Display from its packing and attach it (via its attached cord) to the port labeled `I2C` on the ReSpeaker 4-Mic Array for Raspberry Pi.

### Setup device

Complete steps in [Setup your device](../SETUP-DEVICE.md).

### Configure your device as an Azure IoT Edge device

If you **HAVE NOT** completed this section in a previous project, complete steps in [Configure your device as an Azure IoT Edge device](../CONFIG-EDGE-DEVICE.md).

If you **HAVE** completed this section in another project, you only need to complete the steps in [Delete Edge deployment](../DELETE-EDGE-DEPLOYMENT.md), then delete the idle images on your device by listing images on your device...

`sudo docker image ls`

...and deleting each idle image on your device (do not delete the `edgeAgent` or `edgeHub` images):

`sudo docker image rm <IMAGE NAME OR ID>`

## (OPTIONAL) Deploy pre-built modules to your device

You can deploy pre-built modules (built from the code in this project) to your device by following the steps here: [Deploy pre-built modules][../DEPLOY-MODULES.md]. (If you completed the `1-temperature-sensor` project, you've already deployed pre-built modules. In the next section below, you'll make code changes, build and push containers to your own registry, and deploy those.)

After the deployment is complete, you can press and hold the button on the Pi HAT, speak into the microphone, and release the button. A response will be displayed on the OLED display.

If you deploy pre-built modules, [Delete your deployment](../DELETE-EDGE-DEPLOYMENT.md) before moving on to the next section.

## Build and deploy your own code

In this section you will make a code changes, build and push modules to your own container registry, and deploy them to your Raspberry Pi 3. The code changes suggested below are designed to improve the functionality of your edge device as a "chat bot". As it is, the device can recognize simple greetings (e.g. "Hello") and respond with a simple response (e.g. "Hey!). You will add functionality that allows the device to recognize farewells (e.g. "Goodbye") and respond appropriately. After you have added this functionality, you should have a basic understanding of how to add more (and richer) functionality.

For a video overview of the steps below, see [Deploying the speech-recognizer](https://iotcompanionapp.blob.core.windows.net/videos/deploy-speech-recognizer.mp4).

1. Get the code and open the solution in VS Code:

    `git clone git@github.com:Azure-Samples/azure-iot-starter-kits.git`

    `cd azure-iot-starter-kits/seeed/3-speech-recognizer`

    `code .`

    **NOTE**: You will find multiple subdirectories in the cloned repository, each of which contains code for a different Azure IoT Edge project. This document describes how to use the code in the `3-speech-recognizer` directory. For information about the other projects, see [Hands-on Azure IoT Edge](../README.md).

1. Edit `natural-language-processing/command.py`: Add the following class to the file:

```python
class GoodbyeCommand(Command):
    """
    The command to say goodbye
    """

    def __init__(self):
        """
        Default constructor which will create list of goodbyes to be picked
        randomly to make our bot more human-like
        """
        self.goodbyes = ["Goodbye.", "Hope to see you soon.", "Until we meet again.", "Safe travels."]

    def do(self, bot, entity):
        return(random.choice(self.goodbyes))
```

Save the file.

1. Edit `natural-language-processing/intent.py`: Add the following to the end of the file:

```python
class GoodbyeIntent(Intent):
    def initCommands(self):
        self.commands.append(command.GoodbyeCommand())
```

Save the file.

1. Edit `natural-language-processing/classification.py`: Add the following intent to the `self.intents` object in the `__init__` method:

```python
    "goodbye"     : intent.GoodbyeIntent(self, context)
```

Save the file.

1. Edit `natural-language-processing/training_data.json`: Add the following JSON to the file:

```json
{
    "text": "bye",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "goodbye",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "good bye",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "stop",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "end",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "farewell",
    "intent": "goodbye",
    "entities": []
},
{
    "text": "Bye bye",
    "intent": "goodbye",
    "entities": []
}
```

Save the file.

1. Edit the `module.json` file for each of the 2 project modules: Replace the public registry name with your registry name. For example, in the `speech-to-text` module, update the following line in the `module.json` file:

    `"repository": "{your registry name}.azurecr.io/azureiotedge-seeed-speech-to-text"`

    Save each file.

1. Sign into your Azure Container Registry (ACR): Run the following command _in the VS Code terminal window_:

    `az acr credential show --name {your registry name} --resource-group {your resource group name}`

    Copy the user name and password from the command output and run the following command to login:

    `docker login {registry name}.azurecr.io -u {user name} -p {password}`

1. Build your modules: In VS Code Explorer, right click the `deployment.template.json` file and select `Build Iot Edge Solution`. This will build the modules in the solution, create images from them, and push them to your registry.

    **NOTE**: The first time you build the project the base image must be downloaded, which can take several minutes. Subsequent builds will take only a matter of seconds.

1. The previous step created a deployment manifest file: `/config/deployment.json`. In the VS Code Explorer, right click the `/config/deployment.json` file and select `Create deployment for Edge device`. In the command palette that opens, select your edge device.

When deployment is complete (after a few minutes), you will see the following message displayed on the OLED display: "Hold button and speak". Press the button and hold it while you speak. Release the button. In a few seconds you should see a response on the OLED display. The code you have deployed will recognize simple greetings and goodbyes. You can also try phrases like "tell me a joke" or "what time is it" to get interesting responses.

By using the steps above as a guide, you can add more functionality, deploy it quickly (subsequent builds will be much faster), and try it out. Be creative and have fun!

## Monitor your running code

After the deployment finishes, you can use VS Code to view messages sent from your device to Azure IoT Hub.

1. In VS Code, press **Command+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows) to open the command palette.
1. Start typing `IoT: Start monitoring D2C message`. Select that option when it is available.

You should see messages appear in the VS Code output window.

## Clean up

If you plan to work through other projects in this repository, you can use the Azure resources that you used in this project (Resource Group, IoT Hub, Edge Device, Container Registry). However, you should delete your IoT Edge deployment and delete idle images on your device. To do this, complete the steps in [Delete Edge deployment](../DELETE-EDGE-DEPLOYMENT.md), then delete the idle images by listing images on your device...

`sudo docker image ls`

...and deleting each idle image on your device (do not delete the `edgeAgent` or `edgeHub` images):

`sudo docker image rm <IMAGE NAME OR ID>`

If you don't plan to work through other projects in this repository, you can delete all the resources you have created by following the steps in [Clean up all resources](../CLEAN-UP-RESOURCES.md).
