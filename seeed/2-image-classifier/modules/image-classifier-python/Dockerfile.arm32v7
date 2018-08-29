FROM microsoft/azureiotedge-seeed-image-classifier-python:1.0-deps-arm32v7

WORKDIR /app

# Download model
RUN mkdir /model \
    && apt-get update && apt-get install -y wget \
    && wget https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_1.0_224.tgz \
    && wget https://raw.githubusercontent.com/tensorflow/models/master/research/inception/inception/data/imagenet_lsvrc_2015_synsets.txt -O /model/imagenet_lsvrc_2015_synsets.txt \
    && wget https://raw.githubusercontent.com/tensorflow/models/master/research/inception/inception/data/imagenet_metadata.txt -O /model/imagenet_metadata.txt \
    && tar -xvf mobilenet_v2_1.0_224.tgz -C /model ./mobilenet_v2_1.0_224_frozen.pb \
    && rm mobilenet_v2_1.0_224.tgz

COPY *.py ./

ENTRYPOINT [ "python", "main.py" ]
