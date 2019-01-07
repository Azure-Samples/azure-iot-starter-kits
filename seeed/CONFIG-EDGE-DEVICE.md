# Configure your device as an Azure IoT Edge device

You will use the Azure IoT Starter Kit companion CLI to configure your device as and Azure IoT Edge device. The Azure IoT Starter Kit companion CLI will provision Azure resources for you (e.g. Azure IoT Hub, Azure Edge device, etc) and connect your device to Azure IoT Hub. If you have existing Azure resources you want to use, see the notes after the last step in this section.

For a video overview of these steps, see [Configuring your device as an Azure IoT Edge device](https://iotcompanionapp.blob.core.windows.net/videos/configure-device.mp4).

1. Login to your Azure account using the Azure CLI 2.0:

    `az login`

1. (OPTIONAL) If you have multiple subscriptions, set the subscription you want to use:

    `az account set --subscription <subscription Name or ID>`

1. Use the Azure IoT Starter Kit companion CLI to configure your device:

    `iot configure-device`

    Follow the prompts to create or select Azure resources, then connect to the SSID of your device to allow the CLI to run the necessary configuration scripts.

    Default Wi-Fi setting of Raspberry Pi:  
    SSID : `SeeedGroveKit`      
    Passphase : `SeeedGroveKit`  

    **NOTE**: One Azure resource that the Azure IoT Starter Kit companion CLI will create or select is an Azure IoT Hub. If you choose to create a new Azure IoT Hub (you can choose not to by giving the name of an existing IoT Hub), the default SKU is `F1` (Free). This SKU is limited to one per subscription. If you have used the `F1` SKU for an existing IoT Hub, you can choose a different SKU (`S1`, `S2`, `S3`) by using the `--iothub-sku` flag. For example: `iot --iothub-sku S1 configure-device`.

    **NOTE**: If you are using ethernet to connect to your Raspberry Pi 3, please specify IP Address of your Raspberry Pi 3 by using `--device-ip`
    To find the IP address of the device, run `ifconfig` on the device and look for the IP address of the `wlan0` interface for WiFi and the `eth0` interface for Ethernet. (You should be able to SSH to the device using this address and the default Raspberry Pi 3 credentials.)  
    For example : `iot --device-ip 12.168.1.10 configure-device`  

1. After the Azure IoT Starter Kit companion CLI has connected to your Raspberry Pi 3, you can run `tail -f ~/connect.log` on your Raspberry Pi 3 to follow the configuration progress.  You can run the command in console or through SSH.    
You'll know the configuration is complete when you see this message in the log:

        Sending tags: {"status":"Completed"}

**NOTES on IOT CLI usage**:

- Options must be passed *before* the command. For example, to see help for the `configure-device` command, run the following:

    `iot --help configure-device`

- Your laptop must be connected to the internet when you initially run the tool.
- The first two items you will be prompted for are SSID and Password. These are the SSID and password of the wireless network that the device will connect to after it is configured as an edge device.  

- You will be prompted to create a new (or select an existing) Azure Resource Group, Azure IoT Hub, and Azure IoT Edge device, and Azure Container Registry (ACR).
- You can bypass options by providing information in options. For example, if you know the name of the resource group and IoT Hub that you want to target, you can run a command similar to this:

    `iot --resource-group {resource group name} --iothub {IoT Hub name} configure-device`

    Or, you can simply provide the name of an existing resource when prompted.

- After the tool finishes creating Azure resources (or getting necessary information from existing Azure resources), you will be prompted to connect to the SSID of your device.
- The tool will configure your device and connect it to the SSID that you supplied when running the tool. When this happens, your laptop may automatically connect to your default wireless network.  

- The following warning can be ignored: `The behavior of this command has been altered by the following extension: azure-cli-iot-ext`. It indicates that the behavior of the `azure-iot-cli-ext` extension is overriding the default behavior for the `az` CLI.
- Source code for the Azure IoT Starter Kit companion CLI is here: [https://github.com/Azure-Samples/azure-iot-starterkit-cli](https://github.com/Azure-Samples/azure-iot-starterkit-cli).
