ARG BUILD_FROM=ghcr.io/home-assistant/{arch}-base:3.22
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    bash \
    curl \
    python3 \
    py3-pip \
    ffmpeg \
 && mkdir -p /opt/genidtv

# Pull upstream bridge source at build time.
RUN curl -L https://raw.githubusercontent.com/runawaysheep/Geniatech-DTV-Bridge/main/genidtv.py -o /opt/genidtv/genidtv.py \
 && curl -L https://raw.githubusercontent.com/runawaysheep/Geniatech-DTV-Bridge/main/scan.py -o /opt/genidtv/scan.py \
 && curl -L https://raw.githubusercontent.com/runawaysheep/Geniatech-DTV-Bridge/main/requirements.txt -o /opt/genidtv/requirements.txt \
 && pip3 install --no-cache-dir -r /opt/genidtv/requirements.txt

COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
