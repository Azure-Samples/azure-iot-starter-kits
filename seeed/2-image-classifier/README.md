# image-classifier

This project provides a hands-on introduction to Azure IoT Edge by setting up a Raspberry Pi 3 as an Azure IoT Edge device and deploying code to it that does image recognition from streaming video. This project is designed for developers who have an interest in learning more about Azure IoT Edge capabilities. Code for IoT Edge modules in this project is written in Python.

While this is a proof-of-concept project designed for instructional purposes, it does provide you with a fully functional IoT Edge device that does (limited) image recognition from streaming video.

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

In this project, your Raspberry Pi 3 will be configured as an Azure IoT Edge device that captures images from a video stream and classifies objects in the captured images. To prepare your Raspberry Pi 3, you'll need to attach the following components from your Grove Starter Kit for Azure IoT Edge:

- Micro SD card
- Keyboard and monitor
- Raspberry Pi Camera Module V2
- ReSpeaker 4-Mic Array for Raspberry Pi
- Grove - OLED Display 0.96"
- A 5V Power Supply with Micro USB interface

After attaching the above components you will boot the Raspberry Pi 3, enable SSH connectivity, and enable the camera interface. Step-by-step instructions are below.

### Physical assembly

1. Remove Raspberry Pi 3 (including USB/micro USB power cable) and micro SD card from packaging.
1. Insert the micro SD card into micro SD card port on the Raspberry Pi 3.
1. Attach the keyboard (via one of the USB ports) and monitor (via HDMI port) to the Raspberry Pi 3.
1. Remove the camera from its packaging and attach it (via its attached ribbon) to the port labeled `Camera` on the Raspberry Pi 3.

    **NOTE**: The blue portion of the ribbon's end should be facing the ethernet port on the board, so that the exposed metal contacts of the ribbon touch the metal contacts of the camera port.

1. Remove ReSpeaker 4-Mic Array for Raspberry Pi from its packaging and attach it to the Raspberry Pi 3 via the 40-Pin Headers along the top edge of the board.
1. Remove the OLED from its packing and attach it (via its attached cord) to the port labeled `I2C` on the ReSpeaker 4-Mic Array for Raspberry Pi.

### Setup device

Complete steps in [Setup your device](../SETUP-DEVICE.md).

### Configure your device as an Azure IoT Edge device

If you **HAVE NOT** completed this section in a previous project, complete steps in [Configure your device as an Azure IoT Edge device](../CONFIG-EDGE-DEVICE.md).

If you **HAVE** completed this section in another project, you only need to complete the steps in [Delete Edge deployment](../DELETE-EDGE-DEPLOYMENT.md), then delete the idle images on your device by listing images on your device...

`sudo docker image ls`

...and deleting each idle image on your device (do not delete the `edgeAgent` or `edgeHub` images):

`sudo docker image rm <IMAGE NAME OR ID>`

## Get the code

Now get the code and open the solution in VS Code:

`git clone https://github.com/Azure-Samples/azure-iot-starter-kits.git`

`cd azure-iot-starter-kits/seeed/2-image-classifier`

`code .`

**NOTE**: You will find multiple subdirectories in the cloned repository, each of which contains code for a different Azure IoT Edge project. This document describes how to use the code in the `2-image-classifier` directory. For information about the other projects, see [Hands-on Azure IoT Edge](../README.md).

## (OPTIONAL) Deploy pre-built modules to your device

You can deploy pre-built modules (built from the code in this project) to your device by following the steps here: [Deploy Modules](../DEPLOY-MODULES.md). (If you completed the `1-temperature-sensor` project, you've already deployed pre-built modules. In the next section below, you'll make code changes, build and push containers to your own registry, and deploy those.)

After a few minutes, you should start seeing output on the OLED display similar to this:

```text
L: planetarium, P: 0.23
```

"L" indicates the label for the identified image and "P" indicates the probability that the label is correct. The text will change every few seconds depending on where the camera is pointed.

If you deploy pre-built modules, [Delete your deployment](../DELETE-EDGE-DEPLOYMENT.md) before moving on to the next section.

## Build and deploy your own code

In this section you will make a (trivial) code change, build and push modules to your own container registry, and deploy them to your Raspberry Pi 3.

1. Make a (trivial) code change: Open the `camera-capture/main.py` file and change "L" to "C" (for "Classification") in the `c_request_response` method:

    `text = 'C: {}, P: {:.2f}'.format(label, probability)`

    Save the file.

1. Edit the `module.json` file for each of the 3 project modules: Replace the public registry name with your registry name. For example, in the `camera-capture` module, update the following line in the `module.json` file:

    `"repository": "{your registry name}.azurecr.io/azureiotedge-seeed-camera-capture"`

    Be sure to save each file.

1. Sign into your Azure Container Registry (ACR): Run the following command _in the VS Code terminal window_:

    `az acr credential show --name {your registry name} --resource-group {your resource group name}`

    Copy the user name and password from the command output and run the following command to login:

    `docker login {your registry name}.azurecr.io -u {user name} -p {password}`

1. Build your modules: In VS Code Explorer, right click the `deployment.template.json` file and select `Build Iot Edge Solution`. This will build the modules in the solution, create images from them, and push them to your registry.

    **NOTE**: This step can take a few minutes as it downloads base images.

1. The previous step created a deployment manifest file: `/config/deployment.json`. In the VS Code Explorer, right click the `/config/deployment.json` file and select `Create deployment for Edge device`. In the command palette that opens, select your edge device. As in the previous section, this will deploy the modules to your device. However, this time the modules will be pulled from *your* container registry.

After a few minutes, you should start seeing output on the OLED display similar to this:

```text
C: planetarium, P: 0.23
```

"C" indicates the classification for the identified image and "P" indicates the probability that the classification is correct. The text will change every few seconds depending on where the camera is pointed.

You can verify and trouble shoot the deployment by using combinations of the following `docker` commands on the Raspberry Pi 3:

`sudo docker ps`
`sudo docker logs -f edgeAgent`
`sudo docker logs -f <container name>`

## Monitor your running code

After the deployment finishes, you can use VS Code to view messages sent from your device to Azure IoT Hub.

1. In VS Code, press **Command+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows) to open the command palette.
1. Start typing `IoT: Start monitoring D2C message`. Select that option when it is available.

In the VS Code output window, you should see continuous output similar to this:

```json
[
  {
    "label": "iron, smoothing iron",
    "score": 0.6750053
  },
  {
    "label": "sewing machine",
    "score": 0.0183520187
  },
  {
    "label": "joystick",
    "score": 0.0131918853
  }
]
```

You can verify that messages are reaching Azure IoT Hub by navigating to your IoT Hub in the [Azure portal](https://portal.azure.com) and observing the incoming message count.

## Clean up

If you plan to work through other projects in this repository, you can use the Azure resources that you used in this project (Resource Group, IoT Hub, Edge Device, Container Registry). However, you should delete your IoT Edge deployment and delete idle images on your device. To do this, complete the steps in [Delete Edge deployment](../DELETE-EDGE-DEPLOYMENT.md), then delete the idle images by listing images on your device...

`sudo docker image ls`

...and deleting each idle image on your device (do not delete the `edgeAgent` or `edgeHub` images):

`sudo docker image rm <IMAGE NAME OR ID>`

If you don't plan to work through other projects in this repository, you can delete all the resources you have created by following the steps in [Clean up all resources](../CLEAN-UP-RESOURCES.md).
