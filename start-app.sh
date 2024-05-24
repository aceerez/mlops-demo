#!/bin/bash

# Start Docker Compose services
docker compose -f docker/docker-compose.yml up -d

# Wait for services to start
echo -n "App is starting"
for i in {1..10}; do
  echo -n "."
  sleep 1
done
echo

# Get the server's IP address
SERVER_IP=$(hostname -I | awk '{print $1}')

# Print the IP addresses and URLs
echo "Server IP: $SERVER_IP"
echo "Grafana: http://$SERVER_IP:3001/d/cdmjozaykvd34f/"
echo "API: http://$SERVER_IP:5000"