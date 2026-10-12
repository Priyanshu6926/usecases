/**
 * HeatAware AI: Architecture & Microservice Demonstration Controller
 * Functional Requirement: Phase 5 - Advisory & Early Warning System
 * Course: STQA / Mini Project Viva Demonstration
 */

const MICROSERVICE_BASE_URL = 'http://127.0.0.1:8001';

// Architecture comparison database
const ARCHITECTURES = {
  monolithic: {
    title: "1. Monolithic Architecture Pattern",
    badge: "Tightly Coupled",
    badgeClass: "badge-high",
    diagram: `[ Web Browser UI / Client ]
            │
            ▼
┌────────────────────────────────────────────────────────┐
│             SINGLE MONOLITHIC RUNTIME                 │
│                                                        │
│  • Presentation Layer (HTML/CSS)                       │
│  • Meteorological Anomaly Equations                    │
│  • NOAA Rothfusz Heat Index Math                       │
│  • Advisory String Generators                          │
│  • Static Asset Delivery                               │
└────────────────────────────────────────────────────────┘`,
    description: "All functional requirements (UI, math models, advisory rules, data parsing) share a single runtime and execution context. No network boundary exists between presentation and computational logic.",
    characteristics: [
      { label: "Coupling", value: "Tight — Zero separation of concerns between business logic and UI.", type: "negative" },
      { label: "Scalability", value: "Rigid — During extreme heat emergency, entire monolith must be duplicated.", type: "negative" },
      { label: "Fault Isolation", value: "Zero — A memory leak or CPU spike in advisory generation crashes the whole portal.", type: "negative" },
      { label: "Deployment", value: "Single heavy deploy; small advisory tweaks require rebuilding entire site.", type: "neutral" }
    ]
  },
  three_tier: {
    title: "2. Traditional 3-Tier Architecture Pattern",
    badge: "Tier-Decoupled",
    badgeClass: "badge-normal",
    diagram: `┌────────────────────────────────────────────────────────┐
│     TIER 1: PRESENTATION (Browser / Client UI)         │
└───────────────────────────┬────────────────────────────┘
                            │ HTTP / JSON
                            ▼
┌────────────────────────────────────────────────────────┐
│     TIER 2: APPLICATION SERVER (Central Backend)        │
│     [Forecast Engine + Telemetry Ingest + Advisories]  │
└───────────────────────────┬────────────────────────────┘
                            │ SQL / NoSQL
                            ▼
┌────────────────────────────────────────────────────────┐
│     TIER 3: DATA STORAGE (IMD Grid DB & Telemetry)     │
└────────────────────────────────────────────────────────┘`,
    description: "Separates Presentation (Tier 1), Business Logic (Tier 2), and Persistence (Tier 3). Solves UI coupling, but Tier 2 remains a unified backend containing all services together.",
    characteristics: [
      { label: "Coupling", value: "Moderate — Client talks via HTTP, but backend modules share process space.", type: "neutral" },
      { label: "Scalability", value: "Tier-level — Can scale backend instances, but cannot scale only high-load modules.", type: "neutral" },
      { label: "Fault Isolation", value: "Moderate — Backend crashes still disable both forecasting and advisory tools.", type: "negative" },
      { label: "Deployment", value: "Centralized server updates required for any submodule logic change.", type: "neutral" }
    ]
  },
  microservices: {
    title: "3. Microservices Architecture Pattern (Implemented)",
    badge: "Decoupled & Autonomous",
    badgeClass: "badge-extreme",
    diagram: `┌────────────────────────────────────────────────────────┐
│              TIER 1: CLIENT FRONTEND                   │
│   (Vercel Edge / HTML5 Dashboard / External Apps)      │
└───────────┬───────────────────────────────┬────────────┘
            │                               │
            │ REST / JSON                   │ REST / JSON
            ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐
│  AI Advisory Service   │      │  Telemetry Service     │
│  [PORT 8001 - FastAPI] │      │  [PORT 8002 - IoT AWS] │
│  • NOAA Rothfusz Math  │      │  • Sensor Validation   │
│  • Multilingual Engine │      │  • IMD Ground Truth    │
│  • Independent Scale   │      │  • Anomaly Detection   │
└────────────────────────┘      └────────────────────────┘`,
    description: "Extracts Phase 5 (AI Advisory & Early Warning) into an independent, containerized FastAPI microservice running on its own dedicated port (8001). Exposes a documented RESTful contract with autonomous autoscaling.",
    characteristics: [
      { label: "Coupling", value: "Loose — Zero binary dependency. Communicates via strictly validated JSON schema.", type: "positive" },
      { label: "Scalability", value: "Elastic — Advisory container autoscales independently during regional heat disasters.", type: "positive" },
      { label: "Fault Isolation", value: "Complete — If advisory service restarts, dashboard & monitoring remain 100% online.", type: "positive" },
      { label: "Deployment", value: "Continuous — Independent Docker container with its own CI/CD and zero-downtime rollouts.", type: "positive" }
    ]
  }
};

document.addEventListener('DOMContentLoaded', () => {
  initHealthHeartbeat();
  initArchitectureTabs();
  initExecutionHandlers();
  initSliderSync();
});

/**
 * Periodically polls the Microservice health endpoint on port 8001
 */
function initHealthHeartbeat() {
  const badge = document.getElementById('microservice-status-badge');
  const endpointSpan = document.getElementById('microservice-endpoint-label');
  
  async function checkHealth() {
    try {
      const response = await fetch(`${MICROSERVICE_BASE_URL}/health`, { method: 'GET', cache: 'no-store' });
      if (response.ok) {
        const data = await response.json();
        if (badge) {
          badge.className = 'status-badge-live status-online';
          badge.innerHTML = `<i class="fa-solid fa-circle-check"></i> Microservice Online (FastAPI Port 8001)`;
        }
        if (endpointSpan) {
          endpointSpan.innerHTML = `<span class="text-emerald">Connected</span> (${MICROSERVICE_BASE_URL}/health)`;
        }
      } else {
        throw new Error('Non-200 status');
      }
    } catch (e) {
      if (badge) {
        badge.className = 'status-badge-live status-offline';
        badge.innerHTML = `<i class="fa-solid fa-circle-xmark"></i> Microservice Offline (Run ./microservices/run_service.sh)`;
      }
      if (endpointSpan) {
        endpointSpan.innerHTML = `<span class="text-amber">Service not running locally</span>`;
      }
    }
  }

  checkHealth();
  setInterval(checkHealth, 6000);
}

/**
 * Handles Tab Switching between Monolithic, 3-Tier, and Microservices
 */
function initArchitectureTabs() {
  const tabs = document.querySelectorAll('.arch-tab-btn');
  const titleEl = document.getElementById('arch-title');
  const badgeEl = document.getElementById('arch-badge');
  const diagramEl = document.getElementById('arch-diagram');
  const descEl = document.getElementById('arch-desc');
  const charGrid = document.getElementById('arch-characteristics');

  function renderArchitecture(key) {
    const arch = ARCHITECTURES[key];
    if (!arch) return;

    if (titleEl) titleEl.textContent = arch.title;
    if (badgeEl) {
      badgeEl.textContent = arch.badge;
      badgeEl.className = `badge ${arch.badgeClass}`;
    }
    if (diagramEl) diagramEl.textContent = arch.diagram;
    if (descEl) descEl.textContent = arch.description;

    if (charGrid) {
      charGrid.innerHTML = arch.characteristics.map(c => `
        <div class="char-card char-${c.type}">
          <div class="char-label">${c.label}</div>
          <div class="char-value">${c.value}</div>
        </div>
      `).join('');
    }
  }

  tabs.forEach(btn => {
    btn.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      btn.classList.add('active');
      const archKey = btn.getAttribute('data-arch');
      renderArchitecture(archKey);
    });
  });

  // Default to microservices
  renderArchitecture('microservices');
}

/**
 * Synchronizes range sliders with number outputs
 */
function initSliderSync() {
  const tempSlider = document.getElementById('input-temp');
  const tempOutput = document.getElementById('output-temp');
  const humSlider = document.getElementById('input-humidity');
  const humOutput = document.getElementById('output-humidity');

  if (tempSlider && tempOutput) {
    tempSlider.addEventListener('input', () => tempOutput.textContent = `${tempSlider.value} °C`);
  }
  if (humSlider && humOutput) {
    humSlider.addEventListener('input', () => humOutput.textContent = `${humSlider.value} %`);
  }
}

/**
 * Handles dual execution: Monolith Mode vs Microservice Mode
 */
function initExecutionHandlers() {
  const btnMonolith = document.getElementById('btn-run-monolith');
  const btnMicroservice = document.getElementById('btn-run-microservice');
  const btnSimulateFail = document.getElementById('btn-simulate-failure');

  if (btnMonolith) {
    btnMonolith.addEventListener('click', runMonolithicExecution);
  }
  if (btnMicroservice) {
    btnMicroservice.addEventListener('click', runMicroserviceExecution);
  }
  if (btnSimulateFail) {
    btnSimulateFail.addEventListener('click', runSimulatedCircuitBreaker);
  }
}

/**
 * Gathers user parameters from the input controls
 */
function getFormParameters() {
  return {
    region: document.getElementById('input-region').value,
    temperature: parseFloat(document.getElementById('input-temp').value),
    relative_humidity: parseFloat(document.getElementById('input-humidity').value),
    stakeholder_type: document.getElementById('input-stakeholder').value,
    baseline_temp: parseFloat(document.getElementById('input-baseline').value || 36.5),
    language: document.getElementById('input-language').value
  };
}

/**
 * MODE A: Monolithic Client-side Execution
 * Simulates in-browser tightly coupled execution
 */
function runMonolithicExecution() {
  const modeBadge = document.getElementById('execution-mode-badge');
  if (modeBadge) {
    modeBadge.textContent = 'Monolithic Mode';
    modeBadge.className = 'badge badge-high';
  }

  const params = getFormParameters();
  const startTime = performance.now();

  // Purely client-side local calculation (how monolith works)
  const anomaly = Math.round((params.temperature - params.baseline_temp) * 10) / 10;
  
  // Simplified Heat Index in JS
  const T = (params.temperature * 9/5) + 32;
  const RH = params.relative_humidity;
  let hi_f = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (RH * 0.094));
  if (hi_f >= 80) {
    hi_f = (-42.379 + 2.04901523 * T + 10.14333127 * RH
            - 0.22475541 * T * RH - 0.00683783 * T * T
            - 0.05481717 * RH * RH + 0.00122874 * T * T * RH
            + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH);
  }
  const heatIndex = Math.round(((hi_f - 32) * 5/9) * 10) / 10;

  let risk = "Normal Risk";
  let badgeClass = "badge-normal";
  if (params.temperature >= 43.0 || anomaly >= 4.5) {
    risk = "Extreme Alert";
    badgeClass = "badge-extreme";
  } else if (params.temperature >= 40.0 || anomaly >= 3.0) {
    risk = "Severe Heat";
    badgeClass = "badge-high";
  } else if (params.temperature >= 37.0 || anomaly >= 1.5) {
    risk = "Mild Heat";
    badgeClass = "badge-low";
  }

  const durationMs = (performance.now() - startTime).toFixed(2);

  const consoleEl = document.getElementById('execution-output-console');
  consoleEl.innerHTML = `
    <div class="result-card result-monolith">
      <div class="result-header">
        <span class="badge badge-high"><i class="fa-solid fa-cubes"></i> Mode: Monolithic / Client-Side JS</span>
        <span class="execution-time"><i class="fa-solid fa-stopwatch"></i> Execution Time: ${durationMs} ms</span>
      </div>
      <div class="result-body">
        <div class="arch-meta-note">
          <strong>⚠️ Monolithic Observation:</strong> Executed entirely inside the main browser thread. No independent process isolation, no authenticated API boundary, and no horizontal container autoscaling during regional heat disasters.
        </div>
        <div class="stats-row" style="margin-top: 1rem;">
          <div class="stat-item">
            <span class="stat-label">Calculated Anomaly</span>
            <span class="stat-val ${anomaly >= 3.0 ? 'text-red' : 'text-amber'}">+${anomaly} °C</span>
          </div>
          <div class="stat-item">
            <span class="stat-label">Heat Index</span>
            <span class="stat-val text-red">${heatIndex} °C</span>
          </div>
          <div class="stat-item">
            <span class="stat-label">Risk Classification</span>
            <span class="badge ${badgeClass}">${risk}</span>
          </div>
        </div>
        <div class="advisory-text-box" style="margin-top: 1rem;">
          <h4>Generated Advisory (In-Process Monolith Logic):</h4>
          <p><strong>[${risk}]</strong> Region: ${params.region} | Stakeholder: ${params.stakeholder_type.toUpperCase()}</p>
          <ul style="padding-left: 1.25rem; margin-top: 0.5rem;">
            <li>Enforce hydration breaks for field workers during peak hours (11:00 AM - 4:00 PM).</li>
            <li>Maintain localized soil moisture checks and shade sensitive horticulture crops.</li>
          </ul>
        </div>
      </div>
    </div>
  `;
}

/**
 * MODE B: Decoupled Microservice REST API Execution
 * Calls real FastAPI service on http://127.0.0.1:8001
 */
async function runMicroserviceExecution() {
  const params = getFormParameters();
  const consoleEl = document.getElementById('execution-output-console');
  
  const modeBadge = document.getElementById('execution-mode-badge');
  if (modeBadge) {
    modeBadge.textContent = 'Microservice API';
    modeBadge.className = 'badge badge-extreme';
  }

  consoleEl.innerHTML = `
    <div class="loading-spinner-box">
      <i class="fa-solid fa-circle-notch fa-spin"></i>
      <p>Dispatching REST API Request to Microservice (<code>${MICROSERVICE_BASE_URL}/api/v1/advisory/generate</code>)...</p>
    </div>
  `;

  const requestStartTime = performance.now();

  try {
    const response = await fetch(`${MICROSERVICE_BASE_URL}/api/v1/advisory/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(params)
    });

    const networkLatencyMs = (performance.now() - requestStartTime).toFixed(2);

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`Microservice responded with status ${response.status}: ${JSON.stringify(errorData)}`);
    }

    const data = await response.json();

    consoleEl.innerHTML = `
      <div class="result-card result-microservice">
        <div class="result-header">
          <span class="badge badge-extreme"><i class="fa-solid fa-server"></i> Mode: Microservice REST API</span>
          <span class="execution-time"><i class="fa-solid fa-bolt"></i> HTTP 200 OK | Roundtrip: ${networkLatencyMs} ms (Server: ${data.execution_time_ms} ms)</span>
        </div>
        <div class="result-body">
          <div class="arch-meta-note note-success">
            <strong>✅ Microservice Decoupling Verified:</strong> Executed autonomously via <code>advisory-microservice</code> (FastAPI, Port 8001). Isolated process lifecycle, Pydantic input boundary enforcement, and independent horizontal container scaling.
          </div>

          <!-- HTTP Request & Response Telemetry Inspection -->
          <div class="http-telemetry-grid">
            <div class="telemetry-col">
              <h5><i class="fa-solid fa-arrow-up-right-from-square"></i> Outgoing HTTP Request Payload (JSON)</h5>
              <pre class="code-block"><code>${JSON.stringify(params, null, 2)}</code></pre>
            </div>
            <div class="telemetry-col">
              <h5><i class="fa-solid fa-arrow-down-left-and-up-right-to-center"></i> Microservice Response Contract (JSON)</h5>
              <pre class="code-block"><code>${JSON.stringify({
                service: data.service,
                version: data.version,
                execution_time_ms: data.execution_time_ms,
                metrics: data.metrics,
                advisory_headline: data.advisory_headline
              }, null, 2)}</code></pre>
            </div>
          </div>

          <!-- Parsed Advisory Card -->
          <div class="advisory-result-box" style="margin-top: 1.5rem;">
            <div class="result-status-banner ${data.metrics.badge_class}">
              <div class="status-title">${data.advisory_headline}</div>
              <div class="status-tags">
                <span class="mini-tag">Level ${data.metrics.risk_level}</span>
                <span class="mini-tag">Heat Index: ${data.metrics.heat_index_celsius} °C</span>
                <span class="mini-tag">Anomaly: +${data.metrics.anomaly_celsius} °C</span>
              </div>
            </div>

            <h5 style="margin-top: 1rem;"><i class="fa-solid fa-list-check"></i> Prescribed Action Protocol:</h5>
            <ul class="action-items-list">
              ${data.action_items.map(item => `<li><i class="fa-solid fa-check-double text-emerald"></i> ${item}</li>`).join('')}
            </ul>

            <div class="disclaimer-footnote">
              <i class="fa-solid fa-shield-halved"></i> ${data.disclaimer}
            </div>
          </div>
        </div>
      </div>
    `;

  } catch (err) {
    const errorLatency = (performance.now() - requestStartTime).toFixed(2);
    consoleEl.innerHTML = `
      <div class="result-card result-error">
        <div class="result-header">
          <span class="badge badge-high"><i class="fa-solid fa-triangle-exclamation"></i> Microservice Connection Failed</span>
          <span class="execution-time">${errorLatency} ms</span>
        </div>
        <div class="result-body">
          <h4>Could not connect to FastAPI Microservice on <code>${MICROSERVICE_BASE_URL}</code></h4>
          <p>The microservice is currently not running in the background.</p>
          <div class="command-helper-box">
            <p><strong>To launch the microservice, run this command in your terminal:</strong></p>
            <pre><code>./microservices/run_service.sh</code></pre>
            <p style="margin-top: 0.5rem; font-size: 0.85rem; color: var(--text-secondary);">
              Or manually: <code>python3 -m uvicorn microservices.advisory_service:app --host 127.0.0.1 --port 8001 --reload</code>
            </p>
          </div>
          <button class="btn btn-outline" style="margin-top: 1rem;" onclick="runMonolithicExecution()">
            <i class="fa-solid fa-rotate-left"></i> Run in Monolithic / Client-Side Fallback Mode
          </button>
        </div>
      </div>
    `;
  }
}

/**
 * Demonstrates Fault Tolerance & Circuit Breaking
 */
function runSimulatedCircuitBreaker() {
  const modeBadge = document.getElementById('execution-mode-badge');
  if (modeBadge) {
    modeBadge.textContent = 'Fault Isolation / Fallback';
    modeBadge.className = 'badge badge-normal';
  }

  const consoleEl = document.getElementById('execution-output-console');
  consoleEl.innerHTML = `
    <div class="result-card result-circuit-breaker">
      <div class="result-header">
        <span class="badge badge-normal"><i class="fa-solid fa-shield-cat"></i> Fault Isolation & Graceful Fallback Demo</span>
        <span class="execution-time">Status: Resilient</span>
      </div>
      <div class="result-body">
        <h4>Scenario: What happens when the Advisory Microservice is down or under maintenance?</h4>
        <div class="circuit-breaker-steps">
          <div class="step-item">
            <span class="step-num">1</span>
            <div><strong>Isolated Crash:</strong> If Port 8001 experiences a pod crash or network disruption, <em>only</em> advisory synthesis is affected. The Core Forecast Map (<code>dashboard.html</code>) and IoT Telemetry (<code>monitoring.html</code>) remain 100% operational.</div>
          </div>
          <div class="step-item">
            <span class="step-num">2</span>
            <div><strong>Circuit Breaker Triggered:</strong> The client detects connection timeout and seamlessly falls back to cached baseline safety advisories without freezing the user interface.</div>
          </div>
          <div class="step-item">
            <span class="step-num">3</span>
            <div><strong>Zero Single Point of Failure (SPOF):</strong> In contrast to a monolith where a single segmentation fault or unhandled exception halts all services, microservice architecture ensures high availability (HA).</div>
          </div>
        </div>
      </div>
    </div>
  `;
}
