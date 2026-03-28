ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache bash python3 py3-pip \
    && python3 -m venv /opt/venv

COPY run.sh /run.sh
COPY scanner.py /scanner.py

RUN chmod +x /run.sh

CMD ["/run.sh"]
