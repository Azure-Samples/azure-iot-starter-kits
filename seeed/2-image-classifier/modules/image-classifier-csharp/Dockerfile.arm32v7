FROM microsoft/dotnet:2.0-sdk AS build-env
WORKDIR /app

# Download model
RUN mkdir /model \
    && wget https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_1.0_224.tgz \
    && wget https://raw.githubusercontent.com/tensorflow/models/master/research/inception/inception/data/imagenet_lsvrc_2015_synsets.txt -O /model/imagenet_lsvrc_2015_synsets.txt \
    && wget https://raw.githubusercontent.com/tensorflow/models/master/research/inception/inception/data/imagenet_metadata.txt -O /model/imagenet_metadata.txt \
    && tar -xvf mobilenet_v2_1.0_224.tgz -C /model ./mobilenet_v2_1.0_224_frozen.pb \
    && rm mobilenet_v2_1.0_224.tgz

COPY *.csproj ./
RUN dotnet restore

COPY . ./
RUN dotnet publish -c Release -o out

FROM microsoft/dotnet:2.0-runtime-stretch-arm32v7
WORKDIR /app

COPY --from=build-env /app/out ./
COPY --from=build-env /model /model

ENTRYPOINT [ "dotnet", "image-classifier-csharp.dll", "--urls", "http://*:8080" ]
