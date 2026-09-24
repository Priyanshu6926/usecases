#!/usr/bin/env python3
"""
Automated Usability & Accessibility Testing Runner using Google Lighthouse CLI.
Experiment 07 - Usability Testing
"""

import os
import sys
import json
import time
import socket
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(PROJECT_DIR, "usability_reports")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(REPORT_DIR, exist_ok=True)

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # suppress standard access logs

def start_server(port):
    server = HTTPServer(('127.0.0.1', port), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server

def run_lighthouse(url, report_basename, preset="desktop"):
    html_out = os.path.join(REPORT_DIR, f"{report_basename}.html")
    json_out = os.path.join(REPORT_DIR, f"{report_basename}.json")
    
    cmd = [
        "npx", "-y", "lighthouse",
        url,
        "--no-enable-error-reporting",
        f"--output=html,json",
        f"--output-path={os.path.join(REPORT_DIR, report_basename)}",
        f"--chrome-flags=--headless=new --no-sandbox --disable-gpu",
    ]
    if preset == "desktop":
        cmd.append("--preset=desktop")
    
    env = os.environ.copy()
    env["CHROME_PATH"] = CHROME_PATH
    
    print(f"[*] Running Lighthouse ({preset}) on {url}...")
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[-] Lighthouse error on {url}:\n{res.stderr}")
    else:
        print(f"[+] Audit completed: {report_basename}")

def main():
    port = find_free_port()
    print(f"[*] Starting local server on port {port}...")
    server = start_server(port)
    time.sleep(1)

    audits = [
        ("index.html", "index_desktop", "desktop"),
        ("index.html", "index_mobile", "mobile"),
        ("dashboard.html", "dashboard_desktop", "desktop"),
        ("monitoring.html", "monitoring_desktop", "desktop"),
    ]

    for page, basename, preset in audits:
        url = f"http://127.0.0.1:{port}/{page}"
        run_lighthouse(url, basename, preset)

    server.shutdown()
    print("[*] All usability audits completed! Analyzing results...")

    # Summary table
    results = {}
    for _, basename, preset in audits:
        json_file = os.path.join(REPORT_DIR, f"{basename}.report.json")
        if not os.path.exists(json_file):
            json_file = os.path.join(REPORT_DIR, f"{basename}.json")
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                cats = data.get("categories", {})
                audits_data = data.get("audits", {})
                results[basename] = {
                    "preset": preset,
                    "performance": int((cats.get("performance", {}).get("score") or 0) * 100),
                    "accessibility": int((cats.get("accessibility", {}).get("score") or 0) * 100),
                    "best_practices": int((cats.get("best-practices", {}).get("score") or 0) * 100),
                    "seo": int((cats.get("seo", {}).get("score") or 0) * 100),
                    "fcp": audits_data.get("first-contentful-paint", {}).get("displayValue", "N/A"),
                    "lcp": audits_data.get("largest-contentful-paint", {}).get("displayValue", "N/A"),
                    "cls": audits_data.get("cumulative-layout-shift", {}).get("displayValue", "N/A"),
                    "tbt": audits_data.get("total-blocking-time", {}).get("displayValue", "N/A"),
                    "speed_index": audits_data.get("speed-index", {}).get("displayValue", "N/A"),
                }

    summary_file = os.path.join(REPORT_DIR, "audit_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print("\n================== USABILITY AUDIT SUMMARY ==================")
    print(f"{'Page / Run':<22} | {'Perf':<5} | {'A11y':<5} | {'BestPr':<6} | {'SEO':<5} | {'FCP':<8} | {'LCP':<8} | {'CLS':<8}")
    print("-" * 75)
    for name, r in results.items():
        print(f"{name:<22} | {r['performance']:<5} | {r['accessibility']:<5} | {r['best_practices']:<6} | {r['seo']:<5} | {r['fcp']:<8} | {r['lcp']:<8} | {r['cls']:<8}")
    print("=============================================================")

if __name__ == "__main__":
    main()
