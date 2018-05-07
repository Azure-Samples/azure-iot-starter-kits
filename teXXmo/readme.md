# Hands-on teXXmo button Starter Kit for Azure IoT

The teXXmo button is an Azure IoT Starter kit that allows you to send predefined messages to your cloud by a click of the button.  

This page contains information to help you get familiar with the Azure IoT Starter Kit – teXXmo button.  You will find the resources required to configure the Azure IoT Starter kit to connect to an Azure subscription and invoke an Azure Function.

Projects in this repository have adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Concepts

At a conceptual level, enabling the teXXmo button involves the following steps:

1. Configuring the button
1. Provisioning and registering the device in an Azure IoT Hub. When you register a device, you will get a connection string for it.
1. Writing an Azure Function to receive messages from the button when clicked
1. Binding the button to the Azure Function

## Configuring the teXXmo button

You will use the Azure IoT Starter Kit companion App or CLI to configure your device as an Azure IoT device.  The App or CLI will connect your device to a wireless network, provision Azure resources for you, and bind the button to an Azure Function.

For step-by-step instructions for the Azure IoT Starter Kit companion app, see https://github.com/Azure-Samples/azure-iot-starterkit-companionapp

For step-by-step instruction for the Azure IoT Starter Kit companion CLI, see https://github.com/Azure-Samples/azure-iot-starterkit-cli

## Writing an Azure Function

For step by step instructions, see https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function

## Additional Resources

teXXmo button product page - https://catalog.azureiotsuite.com/details?title=teXXmo-IoT-Button&source=home-page&kit=teXXmo-IoT-Button-Starter-Kit

teXXmo button project code - https://github.com/teXXmo/TheButtonProject




