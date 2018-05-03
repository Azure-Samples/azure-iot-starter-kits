# Tensorflow image classifier
[Tensorflow image classifier](https://www.tensorflow.org/tutorials/image_recognition) that recognizes 1000 classes of objects from the [ImageNet](http://image-net.org/) data source.  The model uses [MobileNet v2](https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet), which is optimized for mobile/constrained/low-power scenarios and is around 14 MB in size.

Build the container for MobileNet v2 1.0 with 224x224 images:

```
%> docker build --rm -t image-classifier-python:v2-1.0-224-arm32v7 -f Dockerfile.arm32v7 .
```

Run the container:

```
// Run the container on arm32v7 (e.g. Raspberry Pi 3):
%> docker run --rm -p 8080:8080 image-classifier-python:v2-1.0-224-arm32v7
```

Classify a .jpg image:

```
%> curl -X POST http://localhost:8080/classify -F 'image=@banana.jpg'
```

# Tensorflow nightly builds for Raspberry Pi:
Tensorflow publishes nightly builds for Raspberry Pi (python/python3 and pi/pi zero):

```
http://ci.tensorflow.org/view/Nightly/job/nightly-pi/176/artifact/output-artifacts/tensorflow-1.5.0-cp27-none-any.whl
http://ci.tensorflow.org/view/Nightly/job/nightly-pi/223/artifact/output-artifacts/tensorflow-1.6.0-cp27-none-any.whl
http://ci.tensorflow.org/view/Nightly/job/nightly-pi/238/artifact/output-artifacts/tensorflow-1.7.0-cp27-none-any.whl


http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/122/artifact/output-artifacts/tensorflow-1.5.0-cp34-none-any.whl
http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/166/artifact/output-artifacts/tensorflow-1.6.0-cp34-none-any.whl
http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/179/artifact/output-artifacts/tensorflow-1.7.0-cp34-none-any.whl
```

# MobileNet models
Different MobileNet models can be used in this container.  Numerous containers are pre-built with the below models.

## MobileNet V2
https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet

- [microsoft/azureiotedge-seeed-image-classifier-python:v2-1.0-224-arm32v7](https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_1.0_224.tgz): 14 MB @ 2.3s
- [microsoft/azureiotedge-seeed-image-classifier-python:v2-0.5-224-arm32v7](https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_0.5_224.tgz): 8 MB @ 2.0s
- [microsoft/azureiotedge-seeed-image-classifier-python:v2-1.0-160-arm32v7](https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_1.0_160.tgz): 14 MB @ 2.1s
- [microsoft/azureiotedge-seeed-image-classifier-python:v2-0.5-160-arm32v7](https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_0.5_160.tgz): 8 MB @ 1.9s

## MobileNet V1
https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md

- [microsoft/azureiotedge-seeed-image-classifier-python:v1-1.0-224-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224.tgz): 17 MB @ 2.3s
- [microsoft/azureiotedge-seeed-image-classifier-python:v1-0.5-224-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224.tgz): 5.4 MB @ 1.8s
- [microsoft/azureiotedge-seeed-image-classifier-python:v1-0.25-224-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224.tgz): 2 MB @ 1.6s
- [microsoft/azureiotedge-seeed-image-classifier-python:v1-1.0-160-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160.tgz): 17 MB @ 2.2s
- [microsoft/azureiotedge-seeed-image-classifier-python:v1-0.5-160-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160.tgz): 5.4 MB @ 1.7s
- [microsoft/azureiotedge-seeed-image-classifier-python:v1-0.25-160-arm32v7](http://download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160.tgz): 2 MB @ 1.6s
