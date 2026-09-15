#!/bin/bash
# ================================================================================
# Performance Testing Automation Script for HeatAware AI Web Application
# Course: STQA | Experiment 06 | Apache JMeter
# ================================================================================

set -e

PORT=8000
RESULTS_DIR="performance_tests/results"
DASHBOARD_DIR="$RESULTS_DIR/dashboard_report"
JTL_FILE="$RESULTS_DIR/results.jtl"
TEST_PLAN="performance_tests/heataware_performance_test.jmx"

echo "=================================================================="
echo " Starting HeatAware AI Performance Test Suite (JMeter)"
echo "=================================================================="

# 1. Start Python HTTP Server if not already running
SERVER_STARTED=false
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "[INFO] Web server already running on port $PORT."
else
    echo "[INFO] Starting local Web Application server on http://localhost:$PORT..."
    python3 -m http.server $PORT > /dev/null 2>&1 &
    SERVER_PID=$!
    SERVER_STARTED=true
    sleep 2
    echo "[INFO] Server started with PID $SERVER_PID"
fi

# Ensure cleanup on exit
cleanup() {
    if [ "$SERVER_STARTED" = true ] && [ -n "$SERVER_PID" ]; then
        echo "[INFO] Shutting down temporary web server (PID $SERVER_PID)..."
        kill $SERVER_PID 2>/dev/null || true
    fi
}
trap cleanup EXIT INT TERM

# Cleanup previous test run results
echo "[INFO] Cleaning previous test results..."
rm -rf "$RESULTS_DIR"/*

# 2. Run Apache JMeter in Non-GUI mode and generate Dashboard Report
echo "[INFO] Executing JMeter Non-GUI Performance Test..."
jmeter -n -t "$TEST_PLAN" \
       -l "$JTL_FILE" \
       -e -o "$DASHBOARD_DIR"

echo "=================================================================="
echo " Performance Test Completed Successfully!"
echo " Raw Results (JTL)    : $JTL_FILE"
echo " HTML Dashboard Report: $DASHBOARD_DIR/index.html"
echo "=================================================================="

# Print summary table using python
python3 performance_tests/print_summary.py

echo "All performance testing tasks finished successfully."
