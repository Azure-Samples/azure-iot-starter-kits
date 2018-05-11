# Hands-on Grove Starter Kit for Azure IoT Edge

![](https://catalogstorageprod.blob.core.windows.net/devicecatalogimageserver/2d78c72d9c3144a983434712f37ee830_SEEED%20Kit.JPG)

Projects in this repository provide hands-on introductions for setting up the [Grove Starter Kit for Azure IoT Edge](https://catalog.azureiotsuite.com/details?title=Grove-Starter-Kit-for-Azure-IoT-Edge&source=home-page) as an Edge device and deploying code to it that performs example IoT Edge tasks. Each project highlights different tasks and is described in more detail below. (For step-by-step instructions for each project, see each project's README.md file.) While these are proof-of-concept projects designed for instructional purposes, each one provides you with a fully functional IoT Edge device.

Projects in this repository are designed for developers who have an interest in learning more about Azure IoT Edge. Code for IoT Edge modules in these projects is written in Python.

## Concepts

At a conceptual level, deploying code to an IoT edge device involves the following steps:

1. Write code that does what you want your IoT edge device to do.
1. Build a module (a Docker container) based on your code that is compatible with your device.
1. Push your module to a container registry.
1. Register a device in an Azure IoT Hub. This will include specifying the location of the container from the previous step. When you register a device, you will get a connection string for it.
1. Install Azure IoT Edge runtime on your device.
1. Configure the device by using the registered device's connection string. This allows the IoT Edge runtime to pull down and start the target container(s).

Projects in this repository have pre-published some of the modules you will use. For information on Azure IoT Edge and how to publish your own modules, see [What is Azure IoT Edge](https://docs.microsoft.com/en-us/azure/iot-edge/how-iot-edge-works).

For more detailed information about Azure IoT Edge concepts, see [Understanding Azure IoT Edge modules - preview](https://docs.microsoft.com/en-us/azure/iot-edge/iot-edge-modules).

For an overview of Azure IoT Edge terms, see [Glossary of IoT Edge Terms](https://docs.microsoft.com/en-us/azure/iot-edge/iot-edge-glossary).

## Project 1: temperature-sensor

When deployed to a device, code in the temperature-sensor project collects temperature and barometric data from the Raspberry Pi temperature sensor and sends it to an Azure IoT Hub. In this project you will do the following:

1. Attach the required accessories to your Raspberry Pi 3.
1. Configure your Raspberry Pi 3 as an Azure IoT Edge device.
1. Deploy pre-built modules (built from code in the project) to your device from a public container registry.
1. Use VS Code to monitor your running modules.

For step-by-step instructions, see [temperature-sensor README.md](1-temperature-sensor/README.md).

## Project 2: image-classifier

When deployed to a device, code in the image-classifier project captures video from the Raspberry Pi camera, sends images from the video to an AI module running image classification, displays the results on the OLED display, and sends results to an Azure IoT Hub. In this project you will do the following:

1. Attach the required accessories to your Raspberry Pi 3.
1. Configure your Raspberry Pi 3 as an Azure IoT Edge device.
1. Modify the code in the project, build and push the images to your own container registry.
1. Deploy your modified modules to your device.
1. Use VS Code to monitor your running modules.

For step-by-step instructions, see [image-classifier README.md](2-image-classifier/README.md).

## Project 3: speech-recognizer

When deployed to a device, code in the speech-recognizer project captures audio from the Raspberry Pi microphone, uses an AI module to recognize the speech and determine intent, responds with an appropriate response on the OLED display, and sends results to an Azure IoT Hub. In this project you will do the following:

1. Attach the required accessories to your Raspberry Pi 3.
1. Configure your Raspberry Pi 3 as an Azure IoT Edge device.
1. Modify the code in the project, build and push the images to your own container registry.
1. Deploy your modified modules to your device.
1. Iteratively update the code and redeploy.

For step-by-step instructions, see [speech-recognizer README.md](3-speech-recognizer/README.md).

---
Projects in this repository have adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
