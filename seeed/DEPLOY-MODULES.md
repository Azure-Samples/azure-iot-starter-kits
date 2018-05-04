# Deploy modules

[Configuring your device as an Edge device](CONFIG-EDGE-DEVICE.md) started the `edgeAgent` module (running as a Docker container) on the device. The `edgeAgent` has connection information for your IoT Hub, Edge device, and Azure Container Registry. Deploying code to your device requires pushing a deployment manifest (which contains information about which modules a device will run, the routes between modules, etc) to Azure IoT Edge (preview). After you push the deployment manifest to Azure IoT Edge, the `edgeAgent` pulls down the manifest and the specified containers, starts the containers, and routes messages between them.

You can use Visual Studio Code to push configuration changes to Azure IoT Edge (i.e. create an Edge deployment). The configuration can reference modules hosted in a public container registry or in a private registry (assuming the `iotedge` runtime was deployed to your device with credentials to the private registry).

1. Sign into your Azure account: In VS Code, press **Command+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows) to open the command palette.  Type and select `Azure: Sign In` and follow the prompts for signing into your Azure account.
1. Select your Azure subscriptions: In VS Code, press **Command+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows) to open the command palette.  Type and select `Azure: Select Subscriptions` and select the subscriptions you want to use.
1. Select your Azure IoT Hub: In the VS Code Explorer, Right click ellipses ("...") to the right of `AZURE IOT HUB DEVICES`, then select `Select IoT Hub`. In the command palette that opens, select the Azure subscription associated with the Azure IoT Hub that you created (or selected) earlier, then select your Azure IoT Hub.
1. Generate a deployment manifest. In the VS Code Explorer, right click the `deployment.template.json` file and select `Generate IoT Edge Deployment Manifest`. This will create a deployment manifest file: `/config/deployment.json`. Look at the `modules` object in this file to view information about the modules you will publish (e.g. you can see the registry in which the images are stored).

    **NOTE**: If you select `Build IoT Edge solution`, this will also generate a deployment manifest file, but it will first build module images and push them to the container registries specified in each project's `module.json` file.  This will only work in scenarios where you have modified the `module.json` files to point to your own repository since you will not have permissions to push to the public repositories.

1. Deploy modules: In the VS Code Explorer, right click the `/config/deployment.json` file and select `Create deployment for Edge device`. In the command palette that opens, select your edge device.

It will take a few minutes for the `edgeAgent` to pull down the manifest, the `edgeHub` and `temperature-sensor` modules, and start them. If you still have your keyboard and monitor connected to the Raspberry Pi 3, you can use the following `docker` commands to monitor the deployment progress:

`sudo docker ps`
`sudo docker logs -f edgeAgent`
`sudo docker logs -f <container name>`