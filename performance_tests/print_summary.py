#!/usr/bin/env python3
"""
Summarizes JMeter performance test results from statistics.json
"""
import json
import sys
import os

stats_path = os.path.join("performance_tests", "results", "dashboard_report", "statistics.json")

if not os.path.exists(stats_path):
    print(f"Error: Statistics file {stats_path} not found.")
    sys.exit(1)

with open(stats_path, "r", encoding="utf-8") as f:
    stats = json.load(f)

print("")
print("=" * 110)
print(f"{'Endpoint / Sampler':<42} | {'Samples':<8} | {'Avg (ms)':<9} | {'Max (ms)':<9} | {'Throughput (/s)':<15} | {'Error %':<8}")
print("=" * 110)

# Sort so Total appears last
keys = [k for k in stats.keys() if k != "Total"]
for key in sorted(keys):
    item = stats[key]
    count = item.get("sampleCount", 0)
    avg_t = item.get("meanResTime", 0)
    max_t = item.get("maxResTime", 0)
    tps = item.get("throughput", 0)
    err = item.get("errorPct", 0)
    short_label = (key[:39] + "...") if len(key) > 42 else key
    print(f"{short_label:<42} | {count:<8} | {avg_t:<9.2f} | {max_t:<9.2f} | {tps:<15.2f} | {err:<8.2f}%")

print("-" * 110)
if "Total" in stats:
    item = stats["Total"]
    count = item.get("sampleCount", 0)
    avg_t = item.get("meanResTime", 0)
    max_t = item.get("maxResTime", 0)
    tps = item.get("throughput", 0)
    err = item.get("errorPct", 0)
    print(f"{'TOTAL (Aggregated Load Summary)':<42} | {count:<8} | {avg_t:<9.2f} | {max_t:<9.2f} | {tps:<15.2f} | {err:<8.2f}%")
print("=" * 110)
