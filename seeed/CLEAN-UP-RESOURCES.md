# Clean resources

## Delete running modules

To delete the modules running on your device, follow the steps in [Delete your Edge deployment](delete-edge-deployment.md).

## Stop IoT Edge runtime on device

To delete the `edgeAgent` and `edgeHub` containers running on your device, execute the following command on your device:

`sudo iotedgectl stop`

## Delete Docker images

To free up space on the SD card for your device, you can delete idle Docker images on your device. To list the images, execute the following command on your device:

`sudo docker image ls`

To delete an image, run the following command:

`sudo docker image rm <IMAGE ID>`

## Delete Azure resources

To delete the Azure resources you created (IoT Hub, Edge Device, Container Registry), execute the following command on your laptop:

`az group delete --name {resource group name} --no-wait --yes`

It may take several minutes for all resources to be deleted.