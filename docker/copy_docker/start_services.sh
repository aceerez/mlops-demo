#!/bin/sh

# Start Loki
/usr/local/bin/loki -config.file=/app/loki-config.yaml &

# Start Promtail
/usr/local/bin/promtail -config.file=/app/promtail-config.yaml &

# Start the Flask app
python /app/app.py