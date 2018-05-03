FROM resin/raspberrypi3-debian:stretch

WORKDIR /app

# disable python buffering to console out (https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED)
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN echo "deb http://deb.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    libboost-python1.55-dev \
    libcurl4-openssl-dev \
    libffi-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libpulse-dev \
    libssl-dev \
    libssl1.0.0 \
    python-dev \
    python-picamera \
    python-pil \
    python-pip \
    python-pyaudio \
    python-requests \
    python-setuptools \
    python-smbus \
    python-wheel \
    swig \
    zlib1g-dev

RUN pip install --no-cache-dir \
    azure-iothub-device-client==1.4.0.0b0 \
    flask==0.12.3 \
    luma.oled \
    RPi.bme280 \
    RPi.GPIO
