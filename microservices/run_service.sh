#!/usr/bin/env bash
# ==============================================================================
# HeatAware AI: Advisory & Early Warning Microservice Launch Script
# Target Port: 8001
# Interactive Swagger Documentation: http://127.0.0.1:8001/docs
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "======================================================================"
echo " Starting HeatAware AI Advisory Microservice"
echo " Working Directory: $ROOT_DIR"
echo " Endpoint: http://127.0.0.1:8001"
echo " Swagger UI: http://127.0.0.1:8001/docs"
echo "======================================================================"

cd "$ROOT_DIR"

# Free port 8001 if already occupied by a background process
EXISTING_PID=$(lsof -ti :8001 2>/dev/null || true)
if [ -n "$EXISTING_PID" ]; then
  echo "Port 8001 is already occupied by PID(s): $EXISTING_PID. Freeing port..."
  kill -9 $EXISTING_PID 2>/dev/null || true
  sleep 1
fi

python3 -m uvicorn microservices.advisory_service:app --host 127.0.0.1 --port 8001 --reload
