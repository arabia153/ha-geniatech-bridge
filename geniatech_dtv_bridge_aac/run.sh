#!/usr/bin/with-contenv bash

set -e

INPUT_IP=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["ip"])')
LOG_LEVEL=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["log"])')
FILE_LOG=$(python3 -c 'import json; print(str(json.load(open("/data/options.json"))["fileLog"]).lower())')
MODE=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["mode"])')
PORT=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["port"])')
PROFILE=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["profile"])')
BITRATE=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["bitRate"])')
BANDWIDTH=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["bandWidth"])')
MTYPE=$(python3 -c 'import json; print(json.load(open("/data/options.json"))["mtype"])')
FORCE_DEVICE_CHANGE=$(python3 -c 'import json; print(1 if json.load(open("/data/options.json"))["forceDeviceChange"] else 0)')

cd /opt/genidtv

ARGS=(
  -i "${INPUT_IP}"
  -l "${LOG_LEVEL}"
  -m "${MODE}"
  --port "${PORT}"
  --profile "${PROFILE}"
  --bitRate "${BITRATE}"
  --bandWidth "${BANDWIDTH}"
  --mtype "${MTYPE}"
  -F "${FORCE_DEVICE_CHANGE}"
)

if [ "${FILE_LOG}" = "true" ]; then
  ARGS+=(--filelog)
fi

exec /opt/venv/bin/python /opt/genidtv/genidtv.py "${ARGS[@]}"
