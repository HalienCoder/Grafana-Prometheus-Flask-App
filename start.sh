#!/usr/bin/env bash
set -e

# Configuration
NETWORK="notes-monitoring-net"
APP_IMAGE="flask-notes-app"
PROM_IMAGE="prom/prometheus"
GRAFANA_IMAGE="grafana/grafana"
PROM_CONFIG="prometheus.yml"

# 1. Create a Docker network (if it doesn't exist)
if ! docker network ls --format '{{.Name}}' | grep -w "${NETWORK}" >/dev/null; then
  echo "Creating Docker network: ${NETWORK}"
  docker network create "${NETWORK}"
else
  echo "Network ${NETWORK} already exists"
fi

# 2. Build your Flask app image
echo "Building Flask app image: ${APP_IMAGE}"
docker build -t "${APP_IMAGE}" .

# 3. (Re)start the Flask app container
docker rm -f notes-app 2>/dev/null || true
echo "Starting Flask app container"
docker run -d \
  --name notes-app \
  --network "${NETWORK}" \
  -p 5000:5000 \
  "${APP_IMAGE}"

# 4. (Re)start Prometheus
docker rm -f prometheus 2>/dev/null || true
echo "Starting Prometheus container"
docker run -d \
  --name prometheus \
  --network "${NETWORK}" \
  -p 9090:9090 \
  -v "$(pwd)/${PROM_CONFIG}:/etc/prometheus/prometheus.yml" \
  "${PROM_IMAGE}"

# 5. (Re)start Grafana
docker rm -f grafana 2>/dev/null || true
echo "Starting Grafana container"
docker run -d \
  --name grafana \
  --network "${NETWORK}" \
  -p 3100:3000 \
  "${GRAFANA_IMAGE}"

echo
echo "✅ All services are up!"
echo "   - Flask app:    http://localhost:5000"
echo "   - Prometheus:   http://localhost:9090"
echo "   - Grafana:      http://localhost:3100"
