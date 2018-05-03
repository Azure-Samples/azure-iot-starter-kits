# Clean resources

To delete the modules running on your device, follow the steps in [Delete your Edge deployment](delete-edge-deployment.md).

To delete the `edgeAgent` and `edgeHub` containers running on your device, exectue the following command on your device:

`sudo iotedgectl stop`

To delete the Azure resources you created (IoT Hub, Edge Device, Container Registry), execute the following command on your laptop:

`az group delete --name {resource group name} --no-wait --yes`

It may take several minutes for all resources to be deleted.