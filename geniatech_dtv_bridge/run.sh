#!/usr/bin/with-contenv bashio
set -euo pipefail

cd /opt/bridge

cat > default.json <<EOF
{
  "ip": ["$(bashio::config 'ip')"],
  "log": "$(bashio::config 'log')",
  "fileLog": $(bashio::config 'fileLog'),
  "mode": "$(bashio::config 'mode')",
  "port": $(bashio::config 'port'),
  "profile": "$(bashio::config 'profile')",
  "bitRate": $(bashio::config 'bitRate'),
  "bandWidth": $(bashio::config 'bandWidth'),
  "mtype": "$(bashio::config 'mtype')",
  "forceDeviceChange": $(bashio::config 'forceDeviceChange')
}
EOF

echo "Generated default.json:"
cat default.json

python3 /opt/bridge/scan.py || true
#!/usr/bin/with-contenv bashio
set -euo pipefail

cd /opt/bridge

cat > default.json <<EOF
{
  "ip": ["$(bashio::config 'ip')"],
  "log": "$(bashio::config 'log')",
  "fileLog": $(bashio::config 'fileLog'),
  "mode": "$(bashio::config 'mode')",
  "port": $(bashio::config 'port'),
  "profile": "$(bashio::config 'profile')",
  "bitRate": $(bashio::config 'bitRate'),
  "bandWidth": $(bashio::config 'bandWidth'),
  "mtype": "$(bashio::config 'mtype')",
  "forceDeviceChange": $(bashio::config 'forceDeviceChange')
}
EOF

echo "Generated default.json:"
cat default.json

echo "=== RUN SCAN ==="
python3 /opt/bridge/scan.py --ip 192.168.0.252 || true
echo "=== SCAN END ==="

exec python3 /opt/bridge/genidtv.py
