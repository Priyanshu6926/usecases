# Heatwave Watch: Climate Intelligence & Early Warning System (HeatAware AI)

[![Platform Status](https://img.shields.io/badge/Platform%20Status-Live%20on%20Vercel-success.svg?style=for-the-badge&logo=vercel)](https://usecases-pearl.vercel.app/)
[![PyTest Suite](https://img.shields.io/badge/PyTest-70%20Passed%20%7C%20100%25-brightgreen.svg?style=for-the-badge&logo=pytest)](file:///Users/priyanshu/Desktop/Projects/usecases/tests/)
[![Microservice API](https://img.shields.io/badge/Microservice-FastAPI%20%7C%20Port%208001-blue.svg?style=for-the-badge&logo=fastapi)](file:///Users/priyanshu/Desktop/Projects/usecases/microservices/advisory_service.py)
[![Mutation Score](https://img.shields.io/badge/Mutation%20Score-100%25%20(101%2F101%20Killed)-blueviolet.svg?style=for-the-badge)](file:///Users/priyanshu/Desktop/Projects/usecases/mutation_runner.py)
[![Lighthouse Score](https://img.shields.io/badge/Lighthouse-100%20Perf%20%7C%20100%20A11y%20%7C%20100%20SEO-success.svg?style=for-the-badge&logo=lighthouse)](file:///Users/priyanshu/Desktop/Projects/usecases/usability_reports/)
[![JMeter Performance](https://img.shields.io/badge/JMeter-1.51ms%20Latency%20%7C%200%25%20Error-informational.svg?style=for-the-badge&logo=apachejmeter)](file:///Users/priyanshu/Desktop/Projects/usecases/performance_tests/)
[![Security Grade](https://img.shields.io/badge/OWASP%20ZAP-Audited%20%26%20Hardened-green.svg?style=for-the-badge&logo=owasp)](file:///Users/priyanshu/Desktop/Projects/usecases/2026-09-03-ZAP-Report-.html)

An end-to-end, AI- and IoT-driven climate intelligence platform engineered for localized heatwave prediction, continuous Automated Weather Station (AWS) telemetry monitoring, and automated LLM emergency advisory generation. Developed in collaborative research between the **India Meteorological Department (IMD) Pune** and **Somaiya Vidyavihar University (K J Somaiya School of Engineering)**.

Beyond operational climate monitoring, this repository serves as a verified engineering testbed implementing the full laboratory curricula for **Software Testing & Quality Assurance (STQA)** and **Digital Marketing (DiM)** (Sem-VII, 2026–27).

---

## 🌐 Live Production Deployment

- **Production Application URL:** [https://usecases-pearl.vercel.app/](https://usecases-pearl.vercel.app/)
- **GitHub Repository:** [https://github.com/Priyanshu6926/usecases](https://github.com/Priyanshu6926/usecases)
- **Primary Domain Route:** [`index.html`](file:///Users/priyanshu/Desktop/Projects/usecases/index.html)
- **Microservice Demo Portal:** [`microservices.html`](file:///Users/priyanshu/Desktop/Projects/usecases/microservices.html)
- **Analytics Property:** Google Analytics 4 (`G-3TN6PC8751`)

---

## 📑 Table of Contents

1. [Executive Summary & Problem Statement](#-executive-summary--problem-statement)
2. [System Architecture](#-system-architecture)
3. [Interactive Web Portals](#-interactive-web-portals)
4. [Microservices Architecture Implementation (Phase 5 Decoupling)](#-microservices-architecture-implementation-phase-5-decoupling)
5. [Climate Analytics Engine (`weather_analytics.py`)](#-climate-analytics-engine-weather_analyticspy)
6. [Software Testing & Quality Assurance (STQA) Engineering](#-software-testing--quality-assurance-stqa-engineering)
   - [PyTest Unit & Parameterized Suite](#1-pytest-unit--parameterized-suite)
   - [AST Mutation Testing Engine (`mutation_runner.py`)](#2-ast-mutation-testing-engine-mutation_runnerpy)
   - [Security Testing & Vulnerability Assessment (OWASP ZAP & SAST)](#3-security-testing--vulnerability-assessment-owasp-zap--sast)
   - [Performance & Load Testing (Apache JMeter 5.6.3)](#4-performance--load-testing-apache-jmeter-563)
   - [Usability & Accessibility Testing (Google Lighthouse Automated Pipeline)](#5-usability--accessibility-testing-google-lighthouse-automated-pipeline)
   - [End-to-End GUI Automation (Selenium IDE Suite)](#6-end-to-end-gui-automation-selenium-ide-suite)
7. [Digital Marketing & Search Engine Optimization (DiM)](#-digital-marketing--search-engine-optimization-dim)
   - [Google Analytics 4 (GA4) Telemetry & Events](#1-google-analytics-4-ga4-telemetry--events)
   - [Robots Exclusion Protocol & XML Sitemap Architecture](#2-robots-exclusion-protocol--xml-sitemap-architecture)
   - [AI-Based Customer Persona Generation (K-Means)](#3-ai-based-customer-persona-generation-k-means)
8. [Academic Experiment Reports Matrix](#-academic-experiment-reports-matrix)
9. [Repository Directory Structure](#-repository-directory-structure)
10. [Local Setup & Verification Guide](#-local-setup--verification-guide)
11. [Deployment & Production Security Configuration](#-deployment--production-security-configuration)
12. [Collaborators & Academic Credits](#-collaborators--academic-credits)

---

## 🌡️ Executive Summary & Problem Statement

Extreme heat events constitute one of the deadliest and most economically disruptive climate risks facing South Asia. Conventional weather forecasting models operate on coarse synoptic grids ($0.25^\circ \times 0.25^\circ \approx 25 \text{ km} \times 25 \text{ km}$), which inherently fail to capture:

- **Urban Heat Island (UHI) Effects:** High-density concrete, asphalt, and industrial emissions amplify local temperatures by $3^\circ\text{C}$ to $7^\circ\text{C}$ compared to surrounding rural baselines.
- **Microclimate Topography:** Thermal variations caused by coastal wind shifts, river basins, and vegetation cover.
- **Latency in Actionable Alerts:** Meteorological bulletins frequently express risk in raw temperatures rather than physiological impact indices (Heat Index, Wet-Bulb Temperature) tailored to vulnerable sectors.

### HeatAware AI Solution:
1. **Macro-to-Micro Data Fusion:** Bridges historical multi-decadal gridded datasets (1951–present) from IMD Pune with localized IoT-enabled Automated Weather Stations (AWS) deployed across academic and urban campuses.
2. **Ground-Truth Cross-Validation:** Continuously computes real-time Pearson correlation ratings between spatio-temporal AI model forecasts and physical sensor readings (currently sustaining $\sim 97.4\%$ accuracy).
3. **Demographic-Specific AI Advisories:** Synthesizes meteorological anomalies into targeted mitigation instructions for Agricultural Workers, Disaster Authorities, Urban Municipalities, and High-Risk Citizens.

---

## 🏗️ System Architecture

The platform follows a resilient, decoupled three-tier architectural topology:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       1. DATA ACQUISITION LAYER                             │
│                                                                             │
│  ┌─────────────────────────┐               ┌─────────────────────────────┐  │
│  │   IMD Pune Data Grid    │               │ Localized IoT AWS Stations  │  │
│  │  (Gridded 1951-Present) │               │ (Somaiya Campus, KJSAC Grid)│  │
│  └────────────┬────────────┘               └──────────────┬──────────────┘  │
│               │                                           │                 │
│               │ (REST APIs / NetCDF / CSV)                │ (MQTT / JSON)   │
└───────────────┼───────────────────────────────────────────┼─────────────────┘
                ▼                                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                   2. ANALYTICS & INTELLIGENCE ENGINE                        │
│                     (Python Core: weather_analytics.py)                     │
│                                                                             │
│  • NOAA Rothfusz Heat Index Regression     • Anomaly Deviation Engine       │
│  • Spatio-Temporal Risk Classification     • Pearson Telemetry Correlator   │
│  • AST Mutation Validation Engine          • Defensive Schema Sanitizers    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 3. PRESENTATION, DECISION & SEM LAYER                       │
│                     (Modern Vanilla HTML5 / CSS3 / ES6)                     │
│                                                                             │
│  ┌───────────────────────┐ ┌──────────────────────┐ ┌────────────────────┐  │
│  │   Forecast Dashboard  │ │  Live AWS Telemetry  │ │ LLM Advisory Engine│  │
│  │   (dashboard.html)    │ │  (monitoring.html)   │ │ (advisories.html)  │  │
│  └───────────────────────┘ └──────────────────────┘ └────────────────────┘  │
│  ┌───────────────────────┐ ┌──────────────────────┐ ┌────────────────────┐  │
│  │ Research Data Portal  │ │ Customer Personas Hub│ │ Microservice Demo  │  │
│  │ (research.html)       │ │ (personas.html)      │ │ (microservices.html│  │
│  └───────────────────────┘ └──────────────────────┘ └────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 Interactive Web Portals

| Page | URL Path | Primary Purpose | Key Features |
|---|---|---|---|
| **Overview & Architecture** | [`index.html`](file:///Users/priyanshu/Desktop/Projects/usecases/index.html) | System introduction & stakeholder mapping | 3-layer architecture visualizer, beneficiary breakdown, core climate statistics, live clock & active status badges. |
| **Forecast Watch Dashboard** | [`dashboard.html`](file:///Users/priyanshu/Desktop/Projects/usecases/dashboard.html) | Regional synoptic forecast & hazard radar | Zone selector (Northwest, Gangetic Plain, Central, Coastal), dynamic heat anomaly metrics, warning severity cards, and interactive trend indicators. |
| **Live AWS Monitoring** | [`monitoring.html`](file:///Users/priyanshu/Desktop/Projects/usecases/monitoring.html) | IoT Automated Weather Station telemetry | Real-time sensor telemetry (Air Temp, Relative Humidity, Solar Radiation, Wind Speed, Pressure), 5-second polling loop simulation, ground-truth correlation graphs ($\sim 97.4\%$). |
| **Alerts & AI Advisories** | [`advisories.html`](file:///Users/priyanshu/Desktop/Projects/usecases/advisories.html) | AI-powered decision support & guidelines | Dynamic LLM text streaming simulation, persona selection (Agriculture, Urban Health, Disaster Teams, Municipal), severity filters, multi-lingual output (English, Hindi, Marathi). |
| **Research & Open Data** | [`research.html`](file:///Users/priyanshu/Desktop/Projects/usecases/research.html) | Scientific archives & open datasets | Downloadable sample CSV telemetry datasets, IMD methodology papers, hardware sensor circuit schematics, calibration protocols. |
| **Customer Personas & AI Clustering** | [`personas.html`](file:///Users/priyanshu/Desktop/Projects/usecases/personas.html) | AI Customer Segmentation & K-Means Portal | Interactive KPI metrics, 2D PCA cluster scatter plots, silhouette analysis, and multi-attribute persona radar charts. |
| **Architecture & Microservice Demo** | [`microservices.html`](file:///Users/priyanshu/Desktop/Projects/usecases/microservices.html) | Monolithic vs 3-Tier vs Microservices comparison | Interactive sandbox, real-time FastAPI REST API calls (port 8001), JSON telemetry inspection, latency metrics, and circuit-breaker fault tolerance. |

---

## ⚙️ Microservices Architecture Implementation (Phase 5 Decoupling)

To fulfill the curriculum requirements of **KJS-CES-01** and demonstrate advanced software engineering principles, the **Phase 5: Advisory, Early Warning, and Decision Support Layer** was decoupled from the monolithic web application into an independent, containerizable **FastAPI Microservice** ([`microservices/advisory_service.py`](file:///Users/priyanshu/Desktop/Projects/usecases/microservices/advisory_service.py)).

### 1. Architectural Evolution Comparison

| Feature | Monolithic Architecture | 3-Tier Architecture | Microservice Architecture (Implemented) |
|---|---|---|---|
| **Structure** | Presentation, math, and advisories bundled in a single app bundle | Tier 1: UI, Tier 2: Unified App Server, Tier 3: Database | Independent, loosely-coupled autonomous services communicating via REST APIs |
| **Coupling** | **Tight** (Zero separation between UI and math logic) | **Moderate** (Client decoupled, but backend logic bundled) | **Loose** (Autonomous process lifecycle, JSON contract) |
| **Scalability** | Must scale entire web server stack | Can scale Tier 2 instances, but all modules scale together | **Elastic Horizontal Autoscaling** (Scale advisory container 10x during emergency alerts) |
| **Fault Isolation** | **Zero** (Crash in advisory computation halts the whole portal) | **Low** (Backend bottleneck hangs telemetry & forecasts) | **Complete** (If advisory service restarts, dashboard & monitoring remain 100% online) |
| **Deployment** | Single heavy release cycle | Monolithic backend redeployment | Autonomous CI/CD, Docker containerized on Port 8001 |

### 2. Microservice REST API Endpoints

The microservice runs by default on `http://127.0.0.1:8001` and exposes interactive OpenAPI/Swagger documentation at `http://127.0.0.1:8001/docs`:

| Method | Endpoint | Description | Request / Response Contract |
|---|---|---|---|
| `GET` | `/` | Service identification & routing metadata | Returns active endpoints and architecture layer details |
| `GET` | `/health` | Container liveness & readiness probe | Returns `{"status": "healthy", "port": 8001}` |
| `POST` | `/api/v1/advisory/generate` | Core advisory calculation & synthesis | Accepts JSON payload with `temperature`, `humidity`, `region`, `stakeholder_type`, `language` |
| `GET` | `/api/v1/advisory/specs` | Academic architectural comparison data | Machine-readable comparison of Monolith vs 3-Tier vs Microservices |
| `GET` | `/docs` | Interactive Swagger UI | OpenAPI interactive test console |

### 3. Sample REST API Request & Response

#### Request Payload (`POST /api/v1/advisory/generate`):
```json
{
  "region": "Coastal Maharashtra",
  "temperature": 43.5,
  "relative_humidity": 65.0,
  "stakeholder_type": "agriculture",
  "baseline_temp": 36.5,
  "language": "en"
}
```

#### Response Contract (`200 OK` in ~0.02 ms):
```json
{
  "service": "heataware-advisory-microservice",
  "version": "1.0.0",
  "status": "success",
  "timestamp": 1791013535.08,
  "execution_time_ms": 0.02,
  "region": "Coastal Maharashtra",
  "stakeholder_type": "agriculture",
  "language": "en",
  "metrics": {
    "temperature_celsius": 43.5,
    "baseline_celsius": 36.5,
    "anomaly_celsius": 7.0,
    "heat_index_celsius": 84.2,
    "risk_status": "Extreme Alert",
    "risk_level": 4,
    "badge_class": "badge-extreme"
  },
  "advisory_headline": "[Action Required: Extreme Heat Alert (Level 4)] Region: Coastal Maharashtra | Heat Index: 84.2°C",
  "action_items": [
    "CRITICAL [Coastal Maharashtra]: Implement emergency crop shading & double irrigation frequency.",
    "Deploy emergency cooling hubs and prioritize heat stroke prevention in Coastal Maharashtra.",
    "Enforce mandatory rest and hydration intervals for agriculture personnel."
  ],
  "disclaimer": "Automated advisory generated by HeatAware AI Microservice in research collaboration with IMD Pune."
}
```

### 4. Running the Microservice Locally
```bash
# 1-Click Startup Script (runs on port 8001 with hot reload):
./microservices/run_service.sh

# Or launch directly with uvicorn:
python3 -m uvicorn microservices.advisory_service:app --host 127.0.0.1 --port 8001 --reload
```

---

## 🧮 Climate Analytics Engine (`weather_analytics.py`)

The mathematical core of the platform is housed in [`weather_analytics.py`](file:///Users/priyanshu/Desktop/Projects/usecases/weather_analytics.py), providing type-safe, validated functions for meteorological calculations:

### 1. Temperature Anomaly Calculation
$$\Delta T = T_{\text{current}} - T_{\text{baseline}}$$
Computes deviation against multi-year climate normals (1981–2010 base period), rounded to 1 decimal place with strict type checking preventing boolean coercion or non-numeric inputs.

### 2. NOAA Rothfusz Heat Index Regression
Implements the National Oceanic and Atmospheric Administration (NOAA) multi-parameter polynomial for physiological apparent temperature ($HI$ in ${}^\circ\text{F}$, converted to ${}^\circ\text{C}$):

$$HI_F = -42.379 + 2.04901523 T + 10.14333127 RH - 0.22475541 T \cdot RH - 0.00683783 T^2 - 0.05481717 RH^2 + 0.00122874 T^2 \cdot RH + 0.00085282 T \cdot RH^2 - 0.00000199 T^2 \cdot RH^2$$

Includes boundary validation rejecting relative humidity values $< 0\%$ or $> 100\%$.

### 3. Risk Classification Matrix
Categorizes meteorological hazard into actionable tiers based on absolute temperatures and baseline anomalies:
- **Level 4 — Extreme Alert:** $T \ge 43.0^\circ\text{C}$ or $\Delta T \ge +4.5^\circ\text{C}$
- **Level 3 — Severe Heat:** $T \ge 40.0^\circ\text{C}$ or $\Delta T \ge +3.0^\circ\text{C}$
- **Level 2 — Mild Heat:** $T \ge 37.0^\circ\text{C}$ or $\Delta T \ge +1.5^\circ\text{C}$
- **Level 1 — Normal Risk:** Standard seasonal baseline

### 4. Stakeholder Advisory Generator & Telemetry Filter
- Generates contextual safety instructions tailored for `agriculture`, `urban_health`, `municipal`, and `general` groups.
- Sanitizes raw IoT telemetry arrays by rejecting incomplete payloads, missing identifiers, or non-physical temperature readings.

---

## 🧪 Software Testing & Quality Assurance (STQA) Engineering

The repository embeds a comprehensive, multi-paradigm software testing suite adhering to IEEE 829 and ISO/IEC/IEEE 29119 testing standards.

### 1. PyTest Unit & Parameterized Suite
- **Location:** [`tests/test_weather_analytics.py`](file:///Users/priyanshu/Desktop/Projects/usecases/tests/test_weather_analytics.py), [`tests/test_standard_unittest.py`](file:///Users/priyanshu/Desktop/Projects/usecases/tests/test_standard_unittest.py), [`tests/test_security.py`](file:///Users/priyanshu/Desktop/Projects/usecases/tests/test_security.py), [`tests/test_microservice.py`](file:///Users/priyanshu/Desktop/Projects/usecases/tests/test_microservice.py)
- **Total Tests:** **70 passed in 0.13 seconds**
- **Test Categories:**
  - Boundary Value Analysis (BVA) for temperature transitions ($36.9^\circ\text{C}$, $37.0^\circ\text{C}$, $39.9^\circ\text{C}$, $40.0^\circ\text{C}$, $42.9^\circ\text{C}$, $43.0^\circ\text{C}$)
  - Equivalence Class Partitioning (ECP) for humidity ranges ($0\%$, $50\%$, $100\%$, and out-of-bounds negative/overflow values)
  - Negative testing & TypeError / ValueError enforcement
  - Parameterized test vectors across all stakeholder groups
  - Microservice FastAPI endpoint tests, Pydantic boundary validation, and multilingual translations

Run the unit tests:
```bash
pytest -v
```

---

### 2. AST Mutation Testing Engine (`mutation_runner.py`)
*(STQA Experiment 03)*
To rigorously evaluate test suite adequacy and prove the tests do not suffer from false passes, a custom Python Abstract Syntax Tree (AST) Mutation Testing Engine ([`mutation_runner.py`](file:///Users/priyanshu/Desktop/Projects/usecases/mutation_runner.py)) was developed.

#### Mutation Operators Implemented:
- **Decision Mutators:** Relational inversion ($\ge \leftrightarrow \le$, $> \leftrightarrow <$, $== \leftrightarrow !=$) across boundary conditionals.
- **Logical Mutators:** Inverting boolean connectives (`and` $\leftrightarrow$ `or`).
- **Value Mutators:** Off-by-one perturbations to float thresholds ($43.0 \to 44.0$, $3.0 \to 2.0$, $80.0 \to 81.0$).
- **Statement Mutators:** Return statement mutations and function bypasses.

#### Mutation Testing Results:
```
================================================================================
                    AST MUTATION TESTING BENCHMARK REPORT                       
================================================================================
Total Mutants Generated : 101
Mutants Killed          : 101
Mutants Survived        : 0
MUTATION SCORE          : 100.00%
Evaluation Status       : PERFECT COVERAGE (Zero Surviving Mutants)
================================================================================
```

Execute the mutation testing engine:
```bash
python3 mutation_runner.py
```

---

### 3. Security Testing & Vulnerability Assessment (OWASP ZAP & SAST)
*(STQA Experiment 05)*
Security testing evaluated both client-side presentation and analytical backend layers against OWASP Top 10 vulnerabilities.

- **Dynamic Analysis (DAST) via OWASP ZAP 2.14.0:** Full active and passive vulnerability scan recorded in [`2026-09-03-ZAP-Report-.html`](file:///Users/priyanshu/Desktop/Projects/usecases/2026-09-03-ZAP-Report-.html). Zero high-severity vulnerabilities identified.
- **Static Security Scanner (`security_scanner.py`):** Automated tool performing SAST audits across DOM sinks, credential leaks, script injections, and header policies:
  ```bash
  python3 security_scanner.py
  ```
  *(Audit output recorded in [`security_audit_report.json`](file:///Users/priyanshu/Desktop/Projects/usecases/security_audit_report.json))*
- **PyTest Security Scenario Suite ([`tests/test_security.py`](file:///Users/priyanshu/Desktop/Projects/usecases/tests/test_security.py)):**
  - **SQL Injection Resilience:** 5 malicious SQL injection vectors (`' OR '1'='1`, `DROP TABLE`, `UNION SELECT`) verified for strict type rejection.
  - **Cross-Site Scripting (XSS) Neutralization:** 5 aggressive XSS payloads (`<script>`, `<img onerror>`, SVG tokens) verified for input sanitization and DOM escaping.
  - **Numeric Out-of-Bounds Rejection:** Rejects infinite (`inf`, `-inf`), NaN, and extreme values.
  - **HTTP Security Headers:** Production deployment in [`vercel.json`](file:///Users/priyanshu/Desktop/Projects/usecases/vercel.json) enforces `X-Content-Type-Options: nosniff` and `X-Frame-Options: DENY`.

---

### 4. Performance & Load Testing (Apache JMeter 5.6.3)
*(STQA Experiment 06)*
Performance testing validated concurrency resilience, throughput, and latency characteristics under simulated peak emergency load conditions.

- **Test Harness:** [`performance_tests/heataware_performance_test.jmx`](file:///Users/priyanshu/Desktop/Projects/usecases/performance_tests/heataware_performance_test.jmx)
- **Workload Model:** Concurrently simulated concurrent emergency response workers across 5 core endpoints (`/index.html`, `/dashboard.html`, `/monitoring.html`, `/advisories.html`, `/research.html`).
- **Execution Script:** [`performance_tests/run_performance_test.sh`](file:///Users/priyanshu/Desktop/Projects/usecases/performance_tests/run_performance_test.sh)

#### Aggregated Performance Benchmark Results:
| Endpoint / Sampler | Samples | Avg Latency | Max Latency | Throughput | Error Rate |
|---|---|---|---|---|---|
| `GET /monitoring.html` (Telemetry Stream) | 150 | 1.40 ms | 5.00 ms | 20.03 req/s | **0.00%** |
| `GET /advisories.html` (AI Advisory Hub) | 50 | 1.30 ms | 4.00 ms | 7.28 req/s | **0.00%** |
| `GET /dashboard.html` (Forecast Radar) | 50 | 1.74 ms | 5.00 ms | 7.28 req/s | **0.00%** |
| `GET /index.html` (Platform Landing Page) | 50 | 1.92 ms | 14.00 ms | 7.26 req/s | **0.00%** |
| `GET /research.html` (Data Repository) | 50 | 1.44 ms | 5.00 ms | 7.28 req/s | **0.00%** |
| **TOTAL (Aggregated Load Benchmark)** | **350** | **1.51 ms** | **14.00 ms** | **40.08 req/s** | **0.00%** |

Display the performance benchmark summary:
```bash
python3 performance_tests/print_summary.py
```

---

### 5. Usability & Accessibility Testing (Google Lighthouse Automated Pipeline)
*(STQA Experiment 07)*
Conducted automated accessibility (a11y), responsive UX, and Core Web Vitals audits using Google Lighthouse 13.5.0 headless automation ([`run_usability_audit.py`](file:///Users/priyanshu/Desktop/Projects/usecases/run_usability_audit.py)).

#### Lighthouse Usability Audit Scorecard:
| Audited Page | Target Device | Performance | Accessibility | Best Practices | SEO | Core Web Vitals (FCP / LCP / CLS) |
|---|---|---|---|---|---|---|
| **Overview (`index.html`)** | Desktop | **100 / 100** | **100 / 100** | **96 / 100** | **100 / 100** | FCP: 0.2s \| LCP: 0.2s \| CLS: 0.004 |
| **Overview (`index.html`)** | Mobile | **100 / 100** | **100 / 100** | **96 / 100** | **100 / 100** | FCP: 0.9s \| LCP: 0.9s \| CLS: 0.003 |
| **Dashboard (`dashboard.html`)** | Desktop | **100 / 100** | **91 / 100** | **96 / 100** | **100 / 100** | FCP: 0.2s \| LCP: 0.2s \| CLS: 0.012 |
| **Monitoring (`monitoring.html`)**| Desktop | **100 / 100** | **88 / 100** | **96 / 100** | **100 / 100** | FCP: 0.2s \| LCP: 0.2s \| CLS: 0.003 |

All HTML reports and raw JSON metrics are archived under [`usability_reports/`](file:///Users/priyanshu/Desktop/Projects/usecases/usability_reports/).

---

### 6. End-to-End GUI Automation (Selenium IDE Suite)
- **Suite File:** [`selenium_test_suite.side`](file:///Users/priyanshu/Desktop/Projects/usecases/selenium_test_suite.side)
- Automates user journey workflows:
  1. Regional zone switching on the dashboard.
  2. Stakeholder persona dropdown selection & AI advisory text generation.
  3. Interactive tab navigation across all 6 pages.

---

## 📈 Digital Marketing & Search Engine Optimization (DiM)

The platform incorporates production-grade Digital Marketing and Search Engine Marketing (SEM) architectures.

### 1. Google Analytics 4 (GA4) Telemetry & Events
*(DiM Experiment 02)*
- **Measurement ID:** `G-3TN6PC8751`
- **Global Tag (`gtag.js`):** Embedded asynchronously across the `<head>` of all 6 web pages.
- **Tracked Telemetry:**
  - Standard user acquisition, geolocation, session duration, and page view flow.
  - Custom event hooks for **Advisory Generation**, **Region Filter Toggle**, and **Telemetry CSV Downloads**.

### 2. Robots Exclusion Protocol & XML Sitemap Architecture
*(DiM Experiment 04)*
- **Robots Directives ([`robots.txt`](file:///Users/priyanshu/Desktop/Projects/usecases/robots.txt)):**
  - Whitelists public-facing pages (`/index.html`, `/dashboard.html`, `/monitoring.html`, `/advisories.html`, `/research.html`, `/personas.html`, `/microservices.html`, `/css/`, `/js/`).
  - Explicitly blocks search spiders from indexing test suites, AST mutants, and backend caches (`/tests/`, `/mutants/`, `/.pytest_cache/`, `/__pycache__/`, `/weather_analytics.py`).
  - Configures rate limiting (`Crawl-delay: 10`) for aggressive crawlers (AhrefsBot) and blocks known scrapers (`BadBot`).
  - Declares canonical XML sitemap location.
- **XML Sitemap ([`sitemap.xml`](file:///Users/priyanshu/Desktop/Projects/usecases/sitemap.xml)):**
  - Full RFC-compliant schema declaring priorities (`1.0` for home, `0.8` for subportals), change frequencies, and parameter URLs.

### 3. AI-Based Customer Persona Generation (K-Means)
*(DiM Experiment 08)*
- **Interactive Persona Portal:** Built directly into [`personas.html`](file:///Users/priyanshu/Desktop/Projects/usecases/personas.html).
- **Machine Learning Pipeline:** [`customer_persona_clustering.py`](file:///Users/priyanshu/Desktop/Projects/usecases/customer_persona_clustering.py) evaluates 250 profiles across 5 quantitative dimensions.
- **Normalization & Clustering:** `StandardScaler` + `KMeans(K=5, n_init=15)` achieving an optimal silhouette score of **0.464**.
- **Visual Analytics:** Outputs high-resolution cluster distribution scatter plots, elbow curves, and spider radar charts under [`persona_assets/`](file:///Users/priyanshu/Desktop/Projects/usecases/persona_assets/).

---

## 📚 Academic Experiment Reports Matrix

All experiments conducted within this repository are documented with formal academic lab reports:

| Exp No. | Course | Experiment Title | Methodology & Tools | Report File |
|:---:|:---:|---|---|---|
| **01** | **DiM** | Website Building and Hosting It | HTML5/CSS3/ES6, Glassmorphic UI, Vercel & GitHub Pages | [`EXPERIMENT_01_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_01_REPORT.md) |
| **02** | **DiM** | Google Analytics 4 (GA4) Setup | GA4 Tag (`G-3TN6PC8751`), Measurement Protocol, User Events | [`EXPERIMENT_02_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_02_REPORT.md) |
| **03** | **STQA**| Mutation Testing for Test Coverage | Python AST Engine, 101 Mutants Generated, 100% Score | [`EXPERIMENT_03_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_03_REPORT.md) |
| **04** | **DiM** | Robots.txt and XML Sitemap Engineering | Web Crawlability, Sitemaps Schema, Robots Exclusion Protocol | [`EXPERIMENT_04_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_04_REPORT.md) |
| **05** | **STQA**| Security Testing & Vulnerability Assessment | OWASP ZAP 2.14.0, SAST Engine, PyTest Security Assertions | [`EXPERIMENT_05_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_05_REPORT.md) |
| **06** | **STQA**| Performance & Load Testing with Apache JMeter | JMeter 5.6.3, 350 Samples, 1.51ms Avg Latency, 0% Error | [`EXPERIMENT_06_STQA_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_06_STQA_REPORT.md) |
| **06** | **DiM** | Google AdWords Search Campaign & AdSense | Google Ads (`AW-16010423075`), SERP Previews, CPC/AdSense Hub | [`EXPERIMENT_06_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_06_REPORT.md) |
| **07** | **STQA**| Usability & Accessibility Testing | Google Lighthouse 13.5.0, 100/100 A11y, Core Web Vitals | [`EXPERIMENT_07_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_07_REPORT.md) |
| **08** | **DiM** | AI-Based Customer Persona Generation | StandardScaler, K-Means (K=5), Silhouette (0.464), Persona Profiling | [`EXPERIMENT_08_REPORT.md`](file:///Users/priyanshu/Desktop/Projects/usecases/EXPERIMENT_08_REPORT.md) |

---

## 📂 Repository Directory Structure

```
usecases/
├── index.html                       # System landing page & 3-layer architecture
├── dashboard.html                   # Regional synoptic forecast watch & hazard radar
├── monitoring.html                  # IoT weather station telemetry & correlation graphs
├── advisories.html                  # AI LLM advisory generation portal
├── research.html                    # Academic papers, sensor schematics & CSV data downloads
├── personas.html                    # Interactive AI Customer Persona Generation & K-Means Portal (Exp 08)
├── microservices.html               # Architecture & Microservice demonstration sandbox
├── customer_persona_clustering.py   # Machine Learning pipeline: StandardScaler, K-Means (K=5), Silhouette
├── experiment_08_customer_persona.ipynb # Interactive Jupyter Notebook for Experiment 08
├── customer_marketing_data.csv      # Customer marketing tabular dataset (250 profiles)
├── persona_assets/                  # Generated cluster scatter plots, elbow diagnostics, and radar charts
│   ├── customer_clusters_scatter.png
│   ├── elbow_method_analysis.png
│   ├── cluster_feature_distribution.png
│   └── persona_radar_chart.png
│
├── microservices/                   # Decoupled Phase 5 Microservice Suite
│   ├── advisory_service.py          # FastAPI REST microservice (NOAA Rothfusz + Multilingual)
│   ├── Dockerfile                   # Container definition for independent deployment
│   ├── requirements.txt             # Python dependencies (FastAPI, Uvicorn, Pydantic)
│   └── run_service.sh               # 1-click startup shell script (Port 8001)
│
├── weather_analytics.py             # Core meteorological math, heat index & risk engine
├── mutation_runner.py               # Custom AST mutation testing runner (100% score)
├── security_scanner.py              # SAST security vulnerability scanner
├── run_usability_audit.py           # Automated Google Lighthouse audit execution script
├── 2026-09-03-ZAP-Report-.html       # OWASP ZAP 2.14.0 full vulnerability assessment report
├── security_audit_report.json       # Structured machine-readable SAST vulnerability output
├── selenium_test_suite.side         # Selenium IDE end-to-end browser test suite
│
├── sitemap.xml                      # Search engine XML sitemap (RFC 0.9 compliant)
├── robots.txt                       # Crawler directives and search indexation policies
├── vercel.json                      # Vercel deployment config with HTTP security headers
├── pytest.ini                       # PyTest configuration settings
├── setup.cfg                        # Flake8 and linter configurations
├── conftest.py                      # PyTest shared fixtures
│
├── css/
│   └── style.css                    # Glassmorphism design tokens, CSS grid/flex, animations
│
├── js/
│   ├── app.js                       # Navigation, live time clock & common utilities
│   ├── dashboard.js                 # Regional temperature anomaly and forecast simulations
│   ├── monitoring.js                # AWS 5-second telemetry polling & correlation calculations
│   ├── advisories.js                # AI advisory generation simulator with streaming output
│   └── microservices.js             # Architecture comparison & live FastAPI integration controller
│
├── tests/
│   ├── test_weather_analytics.py    # 36 comprehensive BVA, ECP & parameterized unit tests
│   ├── test_security.py             # 22 SQLi, XSS, type confusion & boundary security tests
│   ├── test_standard_unittest.py    # Standard Python unittest implementation tests
│   └── test_microservice.py         # 9 FastAPI endpoint, validation & multilingual integration tests
│
├── performance_tests/
│   ├── heataware_performance_test.jmx # Apache JMeter 5.6.3 load testing test plan
│   ├── run_performance_test.sh      # Bash script executing non-GUI JMeter load test
│   ├── print_summary.py             # Tabular summary generator for JMeter statistics
│   └── results/                     # JMeter raw CSV logs and dashboard HTML artifacts
│
├── usability_reports/
│   ├── audit_summary.json           # Aggregated Lighthouse Core Web Vitals & scores
│   ├── index_desktop.report.html    # Homepage desktop Lighthouse audit report
│   ├── index_mobile.report.html     # Homepage mobile Lighthouse audit report
│   ├── dashboard_desktop.report.html# Dashboard desktop Lighthouse audit report
│   └── monitoring_desktop.report.html# Monitoring desktop Lighthouse audit report
│
└── EXPERIMENT_*_REPORT.md           # Formal academic laboratory reports (Exps 01 through 07)
```

---

## 🚀 Local Setup & Verification Guide

### 1. Prerequisites
- **Python:** Python 3.9+ (Python 3.11+ recommended)
- **Node.js (Optional, for Lighthouse):** Node.js 18+ and `npx`
- **Web Browser:** Google Chrome / Chromium / Safari / Firefox
- **Git CLI**

### 2. Clone the Repository
```bash
git clone https://github.com/Priyanshu6926/usecases.git
cd usecases
```

### 3. Launch Local Development Server
To preview the web platform locally with functional asset paths and zero CORS errors:
```bash
# Using Python 3 built-in HTTP server:
python3 -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser.

Alternatively, with Node.js:
```bash
npx -y serve .
```

### 4. Running the Advisory Microservice (Port 8001)
Launch the FastAPI microservice in a dedicated terminal window:
```bash
./microservices/run_service.sh
```
The microservice starts at `http://127.0.0.1:8001` and interactive Swagger docs are accessible at `http://127.0.0.1:8001/docs`.

### 5. Running the Quality Assurance Test Suites

#### A. Execute Unit, Security & Microservice Tests (PyTest)
```bash
pytest -v
```
*(All 70 tests will execute and pass)*

#### B. Execute AST Mutation Testing
```bash
python3 mutation_runner.py
```
*(Runs 101 mutant programs through the test harness and outputs the mutation score)*

#### C. Run the Static Security Scanner
```bash
python3 security_scanner.py
```
*(Inspects HTML, JavaScript, and Python files for security vulnerabilities)*

#### D. View JMeter Performance Benchmark Results
```bash
python3 performance_tests/print_summary.py
```

#### E. Run Automated Usability Audits (Requires Google Chrome & Lighthouse)
```bash
python3 run_usability_audit.py
```

---

## 🔒 Deployment & Production Security Configuration

The platform is deployed globally via Vercel edge networks. Strict HTTP response security headers are enforced in [`vercel.json`](file:///Users/priyanshu/Desktop/Projects/usecases/vercel.json):

```json
{
  "headers": [
    {
      "source": "/(.*)\\.(css|js|woff2|woff|ttf|svg|png|jpg|ico)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        }
      ]
    }
  ]
}
```

- **MIME Sniffing Prevention:** `X-Content-Type-Options: nosniff` prohibits browsers from interpreting content types other than the declared MIME type.
- **Clickjacking Protection:** `X-Frame-Options: DENY` disables framing of any portal inside unauthorized `<iframe>` elements.
- **Aggressive Edge Caching:** Static assets (CSS, JS, fonts) are cached immutably for 365 days (`max-age=31536000`).

---

## 🤝 Collaborators & Academic Credits

- **India Meteorological Department (IMD) Pune**  
  *Meteorological data support, historical gridded datasets, synoptic forecast validation, and climate risk thresholds.*
- **Somaiya Vidyavihar University — K J Somaiya School of Engineering**  
  *Department of Information Technology — IoT Automated Weather Station network deployment, analytical algorithm development, software test engineering, and digital marketing implementation.*
- **Lead Developer & Researcher:** Priyanshu Sharma ([GitHub: @Priyanshu6926](https://github.com/Priyanshu6926))
