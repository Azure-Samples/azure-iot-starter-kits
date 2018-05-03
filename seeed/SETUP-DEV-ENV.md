# Set up your development environment

You will use a laptop to provision resources in Azure (e.g. Azure IoT Hub), configure the Raspberry Pi 3 as an Azure IoT Edge device, and deploy code to the edge device. To accomplish these objectives, you'll need the following tools installed on your laptop:

1. Docker: [https://www.docker.com/community-edition#/download](https://www.docker.com/community-edition#/download)
1. Git: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
1. Python 3.6: [https://www.python.org/downloads](https://www.python.org/downloads)

    Note: You also need to install `pip`, which is included with Python 3.6. If you are installing Python on Windows, check the box in the installer that adds `pip` to your path. On a Mac, you can install pip with `sudo apt install python-pip`.

1. Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
1. The following VS Code extensions:
    - Azure IoT Edge
    - Azure IoT Toolkit
    - Docker

    For information about finding and installing VS Code extensions, see [https://code.visualstudio.com/docs/editor/extension-gallery](https://code.visualstudio.com/docs/editor/extension-gallery).
1. Azure CLI 2.0: [https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

1. IoT extension for Azure CLI 2.0: After installing the Azure CLI 2.0, execute the following command:

    `az extension add --name azure-cli-iot-ext`

    After installation, use `az extension list` to validate the currently installed extensions or `az extension show --name azure-cli-iot-ext` to see details about the IoT extension.

1. Azure IoT Starter Kit companion CLI: After you have installed Python/pip, execute the following command:

    `pip install azure-iot-starterkit-cli`
