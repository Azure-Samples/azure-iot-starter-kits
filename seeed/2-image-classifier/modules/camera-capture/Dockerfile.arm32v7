FROM microsoft/azureiotedge-seeed-camera-capture:1.0-deps-arm32v7

WORKDIR /app

COPY fonts/. ./fonts/
COPY *.py ./

ENTRYPOINT [ "python", "main.py" ]
