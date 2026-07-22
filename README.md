# Heatwave Watch: Climate Intelligence & Early Warning System (HeatAware AI)

[![Platform Status](https://img.shields.io/badge/Status-Live-success.svg)](#)
[![Collaboration](https://img.shields.io/badge/Collaborators-IMD%20Pune%20%7C%20Somaiya%20Vidyavihar-orange.svg)](#)
[![Technology](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20ES6%20JS-blue.svg)](#)

An AI- and IoT-driven climate intelligence system designed for forecasting, monitoring, and generating early warnings for heatwaves. Developed in collaboration with the **India Meteorological Department (IMD) Pune** and **Somaiya Vidyavihar University**, the HeatAware AI platform integrates macro-scale meteorological predictions with localized ground-level Automated Weather Station (AWS) sensors.

---

## 📖 Table of Contents

- [Overview & The Challenge](#-overview--the-challenge)
- [System Architecture](#-system-architecture)
- [Key Features & Pages](#-key-features--pages)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Local Setup & Deployment](#-local-setup--deployment)
- [Collaborators](#-collaborators)

---

## 🌡️ Overview & The Challenge

Heatwaves are extreme weather events that pose a critical risk to public health, agriculture, municipal grids, and local economies. Traditional meteorological forecasting operates on macro-scales, which often overlooks regional topography variations and urban heat islands that cause highly localized micro-climate fluctuations.

**HeatAware AI** addresses this gap by:
1. **Bridging Macro and Micro Data:** Marrying state-level IMD grid forecasting with real-time, ground-level Automated Weather Station (AWS) sensor arrays.
2. **Dynamic Validation:** Continuously assessing the correlation between AI forecasting models and physical ground-truth measurements (currently maintaining a ~97% correlation rating).
3. **Actionable Alerts:** Translating complex meteorological indices (e.g., Heat Index, Wet Bulb Temperature) into customized, stakeholder-specific emergency instructions.

---

## 🏗️ System Architecture

The platform is structured into three main layers:

```
┌────────────────────────────────────────────────────────┐
│ 1. Data Acquisition Layer (IMD GRD + Deployed AWS Grid) │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. Analytics & Intelligence (Spatio-Temporal AI Model)  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. Validation & Support (UI Dashboard & LLM Advisor)   │
└────────────────────────────────────────────────────────┘
```

1. **Data Acquisition Layer:** Collects historical climate datasets (1951–present) from IMD Pune alongside live streams (temperature, humidity, pressure, solar radiation) from IoT-enabled Automated Weather Stations.
2. **Analytics & Intelligence Layer:** Employs AI/ML models to perform spatio-temporal predictions, forecasting maximum temperatures and classifying heatwave severity grades (Normal, Heatwave, Severe Heatwave).
3. **Validation & Decision Support Layer:** Performs real-time correlation tests against physical weather station readings, feeds verified inputs to an LLM advisory engine, and displays metrics on a high-fidelity web dashboard.

---

## 💻 Key Features & Pages

The application is built as a responsive, modern glassmorphic dashboard with the following portals:

*   **Overview (`index.html`):** The homepage outlining project goals, core challenges, layers of architecture, and primary beneficiary demographics (Disaster Authorities, Agricultural Agencies, Public Health Workers).
*   **Forecast Watch Dashboard (`dashboard.html`):** An interactive UI illustrating max forecasted temperatures, warning signals, and heatwave hotspots across India's meteorological zones.
*   **Live AWS Monitoring (`monitoring.html`):** A portal displaying real-time telemetry from deployed weather stations (e.g., Somaiya Campus Station, KJSAC Station). It displays the real-time heat index and system validation scores.
*   **Alerts & Advisories (`advisories.html`):** Features an **AI Advisory Simulator** that mimics LLM translation. Users can configure the target stakeholder (e.g., Agricultural Workers, Disaster Teams, High-Risk Citizens) and heat parameters to instantly generate contextual, actionable safety guidelines.
*   **Data & Research Portal (`research.html`):** Repository for research documentation, scholarly articles, sensor schematics, and CSV datasets.

---

## 🛠️ Technology Stack

*   **Markup:** HTML5 (Semantic and accessible structure)
*   **Styling:** Custom Vanilla CSS (Modern CSS variables, Flexbox/Grid layouts, glassmorphism, responsive queries, and animations)
*   **Logic & Interactivity:** Modern ES6+ JavaScript (Dynamic DOM manipulation, form simulators, active page highlights, and live clock synchronizations)
*   **Icons:** [FontAwesome 6.4](https://fontawesome.com/)
*   **Typography:** [Google Fonts](https://fonts.google.com/) (Outfit and Plus Jakarta Sans)

---

## 📂 Project Structure

```
usecases/
├── index.html            # Main landing page & Architecture Overview
├── dashboard.html        # Forecast Dashboard & Hotspot tracking
├── monitoring.html       # Real-time IoT Weather Station Telemetry
├── advisories.html       # AI LLM Advisory Generator Portal
├── research.html         # Data repositories & Research publications
├── css/
│   └── style.css         # Main stylesheet with styling variables & styles
└── js/
    ├── app.js            # General utilities & common UI functionality
    ├── dashboard.js      # Dashboard animations & charts/stats simulations
    ├── monitoring.js     # Live telemetry data simulation & AWS feeds
    └── advisories.js     # AI Advisory generation & stakeholder filters
```

---

## 🚀 Local Setup & Deployment

Since the platform is built using standard client-side technologies, running it locally requires no complex installation:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Priyanshu6926/usecases.git
    cd usecases
    ```
2.  **Run a local development server:**
    To bypass browser CORS restrictions and run it smoothly, use a local server tool.
    *   Using **Python** (built-in):
        ```bash
        python3 -m http.server 8080
        ```
    *   Using **Node.js** (e.g., `serve` or `http-server`):
        ```bash
        npx serve .
        ```
3.  **View in browser:**
    Open [http://localhost:8080](http://localhost:8080) (or the port specified by your dev server) to view the application.

---

## 🤝 Collaborators

*   **India Meteorological Department (IMD) Pune** - Meteorological data support, forecasting methodology, validation checks.
*   **Somaiya Vidyavihar University** - IoT sensor design, AWS network deployment, and frontend platform development.
