#!/usr/bin/env bash
set -e

# Containers & network names
CONTAINERS=(notes-app prometheus grafana)
NETWORK="notes-monitoring-net"

# 1. Stop & remove containers
for c in "${CONTAINERS[@]}"; do
  if docker ps -a --format '{{.Names}}' | grep -w "$c" >/dev/null; then
    echo "Stopping & removing container: $c"
    docker rm -f "$c"
  fi
done

# 2. Remove the Docker network
if docker network ls --format '{{.Name}}' | grep -w "${NETWORK}" >/dev/null; then
  echo "Removing network: ${NETWORK}"
  docker network rm "${NETWORK}"
fi

echo
echo "🛑 All services stopped and cleaned up."
