ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache bash python3 py3-pip ffmpeg \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir requests

COPY run.sh /run.sh
COPY scanner.py /scanner.py
RUN chmod +x /run.sh /scanner.py

CMD [ "/run.sh" ]
