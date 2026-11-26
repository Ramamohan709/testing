#!/usr/bin/env bash
set -euo pipefail

CONTAINER_NAME="devops-practice"

if docker container inspect "${CONTAINER_NAME}" >/dev/null 2>&1; then
  echo "A container named ${CONTAINER_NAME} already exists."
  echo "Stop and remove it with: docker rm -f ${CONTAINER_NAME}"
  exit 1
fi

docker run -d --name "${CONTAINER_NAME}" -p 8080:8080 devops-practice:latest
echo "Application started: http://localhost:8080"
echo "Health check: curl http://localhost:8080/health"
