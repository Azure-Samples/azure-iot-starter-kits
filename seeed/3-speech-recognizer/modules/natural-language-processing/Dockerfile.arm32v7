FROM microsoft/azureiotedge-seeed-natural-language-processing:1.0-deps-arm32v7

WORKDIR /app

COPY training_*.json ./
COPY *.py ./

ENTRYPOINT [ "python", "main.py" ]
