#!/usr/bin/with-contenv bash
set -euo pipefail

IP="$(bashio::config 'ip')"
LOG_LEVEL="$(bashio::config 'log')"
FILE_LOG="$(bashio::config 'fileLog')"
MODE="$(bashio::config 'mode')"
PORT="$(bashio::config 'port')"
PROFILE="$(bashio::config 'profile')"
BITRATE="$(bashio::config 'bitRate')"
BANDWIDTH="$(bashio::config 'bandWidth')"
MTYPE="$(bashio::config 'mtype')"
FORCE_DEVICE_CHANGE="$(bashio::config 'forceDeviceChange')"

ARGS=(
  "/opt/genidtv/genidtv.py"
  "-i" "${IP}"
  "-l" "${LOG_LEVEL}"
  "-m" "${MODE}"
  "--port" "${PORT}"
  "--profile" "${PROFILE}"
  "--bitRate" "${BITRATE}"
  "--bandWidth" "${BANDWIDTH}"
  "--mtype" "${MTYPE}"
)

if [[ "${FILE_LOG}" == "true" ]]; then
  ARGS+=( "--filelog" )
fi

if [[ "${FORCE_DEVICE_CHANGE}" == "true" ]]; then
  ARGS+=( "--forceDeviceChange" )
fi

echo "Starting Geniatech DTV Bridge AAC"
echo "IP=${IP} PORT=${PORT} PROFILE=${PROFILE}"

exec python3 "${ARGS[@]}"
