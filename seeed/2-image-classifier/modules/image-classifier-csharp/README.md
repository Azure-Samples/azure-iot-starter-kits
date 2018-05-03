# Tensorflow image classifier
[Tensorflow image classifier](https://www.tensorflow.org/tutorials/image_recognition) that recognizes 1000 classes of objects from the [ImageNet](http://image-net.org/) data source.  The model uses [MobileNet v2](https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet), which is optimized for mobile/constrained/low-power scenarios and is around 14 MB in size.

Build the container for MobileNet v2 1.0 with 224x224 images:

```
%> docker build --rm -t image-classifier-csharp:v2-1.0-224-arm32v7 -f Dockerfile.arm32v7 .
```

Run the container:

```
// Run built container on arm32v7 (e.g. Raspberry Pi 3):
%> docker run --rm -p 8080:8080 image-classifier-csharp:v2-1.0-224-arm32v7
```

Classify a .jpg image:

```
%> curl -X POST http://localhost:8080/classify -F 'image=@banana.jpg'
```
