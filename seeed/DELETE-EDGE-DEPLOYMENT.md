# Delete Edge deployment

Follow the steps below to delete the modules deployed to your device:

1. Sign in to the Azure Portal: [https://portal.azure.com](https://portal.azure.com).
1. Navigate to your IoT Hub
1. Select **Iot Edge (preview)**
1. Click on your device
1. Select **Set Modules**
1. Check the box next to each deployed module (hover next to modules to see boxes)
1. Click **Delete**
1. Click **Next** at the bottom of the page
1. Click **Next** again
1. Click **Submit**

Run `sudo docker ps` on your Raspberry Pi 3 to verify that the modules have been deleted. It may take a few minutes for all modules to be deleted. (The `edgeAgent` and `edgeHub` modules will continue to run.)