FROM resin/rpi-raspbian:stretch

RUN [ "cross-build-start" ]

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
        git \
        python3 \
        python3-pip \
        python3-dev \
        wget \
        swig \
        build-essential \
        i2c-tools \
        libpulse-dev \
        libboost-python1.62.0 \
        libasound2-dev \
        libopenjp2-7-dev \
        libjpeg-dev \
        portaudio19-dev \
        python-pyaudio \
        python-pil \
        python-requests \
        python-pocketsphinx \
        pocketsphinx

COPY requirements.txt ./

RUN pip3 install --upgrade pip 
RUN pip3 install --upgrade setuptools 
RUN pip3 install --no-cache-dir -r requirements.txt

# RUN git clone --recursive https://github.com/jessebenson/pocketsphinx-python \
#    && cd /app/pocketsphinx-python \
#    && python3 setup.py install \
#    && rm -rf /app/pocketsphinx-python

# Expose the port
EXPOSE 80

COPY fonts/. ./fonts/
COPY *.py ./

RUN [ "cross-build-end" ]

# Run the flask server for the endpoints
CMD ["python3", "-u", "main.py"]
