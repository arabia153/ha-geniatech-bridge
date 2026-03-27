ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache git bash \
    && pip install --no-cache-dir urllib3 requests python-daemon \
    && git clone https://github.com/runawaysheep/Geniatech-DTV-Bridge.git /opt/bridge

WORKDIR /opt/bridge
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
