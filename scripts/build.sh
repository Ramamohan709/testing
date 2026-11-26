#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="devops-practice"
IMAGE_TAG="${1:-latest}"

docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
echo "Built image ${IMAGE_NAME}:${IMAGE_TAG}"
