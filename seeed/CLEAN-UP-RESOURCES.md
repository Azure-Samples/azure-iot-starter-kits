# Clean all resources

If you are finished with projects in this repository, you should clean up all the resources you have created.

**NOTE**: Instructions in this document will guide you through deleting IoT Edge resources on your device and associated resources in your Azure account. You should only do this if you are finished with projects in this repository.

1. Delete the IoT Edge runtime on device.

    To delete delete running deployments and reset the IoT Edge runtime, execute the following command on your device:

    `sudo iotedgectl uninstall`

    To delete the `edgeAgent` container on your device, execute the following commands:

    `sudo docker stop edgeAgent`

    `sudo docker rm edgeAgent`

1. Delete idle Docker images

    To free up space on the SD card for your device, you can delete idle Docker images. To list the images, execute the following command on your device:

    `sudo docker image ls`

    To delete an image, run the following command:

    `sudo docker image rm <IMAGE ID>`

    Repeat the above command for each image you want to delete.

1. Delete Azure resources

    To delete the Azure resources you created (Resource Group, IoT Hub, Edge Device, Container Registry), execute the following command on your laptop:

    `az group delete --name {resource group name} --no-wait --yes`

    It may take several minutes for all resources to be deleted.