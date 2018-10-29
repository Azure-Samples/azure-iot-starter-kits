# temperature-sensor

This project provides a hands-on introduction to Azure IoT Edge by setting up a Raspberry Pi 3 as an Azure IoT Edge device and deploying code to it that sends temperature data to Azure IoT Hub. This project is designed for developers who have an interest in learning more about Azure IoT Edge capabilities. Code for IoT Edge modules in this project is written in Python.

While this is a proof-of-concept project designed for instructional purposes, it does provide you with a fully functional IoT Edge device that sends temperature data to Azure IoT Hub.

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

In this project, your Raspberry Pi 3 will be configured as an Azure IoT Edge device that reads from the Temp & Humidity & Barometer sensor and sends telemetry to IoT Hub. To prepare your Raspberry Pi 3, you'll need to attach the following components from your Grove Starter Kit for Azure IoT Edge:

- Micro SD card
- Keyboard and monitor
- Grove - Temp & Humidity & Barometer Sensor (BME280)
- ReSpeaker 4-Mic Array for Raspberry Pi
- A 5V Power Supplly with Micro USB interface

After attaching the above components you will boot the Raspberry Pi 3 and enable the barometer interface. Step-by-step instructions are below.

### Physical assembly

1. Remove Raspberry Pi 3 (including USB/micro USB power cable) and micro SD card from packaging.
1. Insert the micro SD card into micro SD card port on the Raspberry Pi 3.
1. Attach the keyboard (via one of the USB ports) and monitor (via HDMI port) to the Raspberry Pi 3.
1. Remove ReSpeaker 4-Mic Array for Raspberry Pi from its packaging and attach it to the Raspberry Pi 3 via the 40-Pin Headers along the top edge of the board.
1. Remove the barometer sensor from its packaging and attach it to the port labeled `I2C` on the ReSpeaker 4-Mic Array for Raspberry Pi.

### Setup device

Complete steps in [Setup your device](../SETUP-DEVICE.md).

### Configure your device as an Azure IoT Edge device

Complete steps in [Configure your device as an Azure IoT Edge device](../CONFIG-EDGE-DEVICE.md).

## Deploy modules to your device

Now you should be ready to get the code and deploy it to your device. (For a video overview of deploying code, download and watch the following: [Deploying pre-built modules](https://iotcompanionapp.blob.core.windows.net/videos/temp-sensor-deploy-code.mp4).)

1. Get the code and open the solution in VS Code:

    `git clone git@github.com:Azure-Samples/azure-iot-starter-kits.git`

    `cd azure-iot-starter-kits/seeed/1-temperature-sensor`

    `code .`

    **NOTE**: You will find multiple subdirectories in the cloned repository, each of which contains code for a different Azure IoT Edge project. This document describes how to use the code in the `1-temperature-sensor` directory. For information about the other projects, see [Hands-on Azure IoT Edge](../README.md).

1. Complete the steps in [Deploy modules](../DEPLOY-MODULES.md).

## Monitor your running code

After the deployment finishes, you can use VS Code to view messages sent from your device to Azure IoT Hub.

1. In VS Code, press **Command+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows) to open the command palette.
1. Start typing `IoT: Start monitoring D2C message`. Select that option when it is available.

In the VS Code output window, you should see continuous output similar to this:

```json
{
  "machine": {
    "pressure": 999.4675396488489,
    "temperature": 25.492859615018823
  },
  "id": {
    "int": 2.909123055429278e+37
  },
  "timeCreated": "2018-04-26 22:58:28.388264",
  "ambient": {
    "temperature": 25.492859615018823,
    "humidity": 30.788229851672618
  }
}
```

You can verify that messages are reaching Azure IoT Hub by navigating to your IoT Hub in the [Azure portal](https://portal.azure.com) and observing the incoming message count.

## Clean up

If you plan to work through other projects in this repository, you can use the Azure resources you used in this project (Resource Group, IoT Hub, Edge Device, Container Registry). However, you should delete your IoT Edge deployment and delete idle images on your device. To do this, complete the steps in [Delete Edge deployment](../DELETE-EDGE-DEPLOYMENT.md), then delete the `azureiotedge-seeed-temperature-sensor` image by executing the following command on your device:

`sudo docker image rm azureiotedge-seeed-temperature-sensor`

If you don't plan to work through other projects in this repository, you can delete all the resources you have created by following the steps in [Clean up all resources](../CLEAN-UP-RESOURCES.md).
