================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | STQA (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/STQA/2026-27
================================================================================

Batch: A2                Roll No.: 16010423075                Experiment No.: 06
Title: Performance Testing using Apache JMeter

________________________________________________________________________________
Aim: To perform performance testing using JMeter.
________________________________________________________________________________
Resources needed: Internet, Computer System (macOS / Linux / Windows), 
OpenJDK 21+ / Java Runtime Environment (JRE), Apache JMeter 5.6.3 / 4.0, 
Python 3 (Local Web Application Server), HeatAware AI Web Application (`usecases`).
________________________________________________________________________________

================================================================================
1. THEORY
================================================================================

Performance Testing is a subset of performance engineering, an evaluative software testing 
practice executed to determine how a system performs in terms of responsiveness, throughput, 
resource utilization, and stability under a particular workload. Rather than finding defects 
in functionality (like functional or unit testing), performance testing seeks to eliminate 
performance bottlenecks and establish baseline operational thresholds.

Apache JMeter is a 100% pure Java open-source application originally designed by Stefano 
Mazzocchi of the Apache Software Foundation. Initially created for load testing Web and FTP 
applications, JMeter has evolved into an industry standard for measuring dynamic web 
applications, RESTful APIs, SOAP web services, database connections (via JDBC), LDAP, JMS, 
and message brokers.


--------------------------------------------------------------------------------
Primary Types of Performance Testing
--------------------------------------------------------------------------------
1. Load Testing:
   Evaluates system behavior under anticipated normal and peak user loads. It verifies if 
   the system satisfies Service Level Agreements (SLAs) regarding response times and throughput.

2. Stress Testing:
   Evaluates the application beyond its normal operational limits to identify breaking points, 
   behavior under extreme load, and graceful degradation/recovery characteristics.

3. Spike Testing:
   Subjecting the target system to sudden, dramatic surges and drops in user concurrency 
   (e.g., flash sales or emergency heatwave alert broadcasts).

4. Endurance / Soak Testing:
   Sustains an expected operational workload over a prolonged period (hours or days) to detect 
   memory leaks, slow resource depletion, database connection starvation, and log file bloat.

5. Scalability & Capacity Testing:
   Measures the system's ability to scale out (horizontal scaling) or scale up (vertical 
   hardware additions) to handle incremental traffic growth.


--------------------------------------------------------------------------------
Key Performance Metrics & Parameters
--------------------------------------------------------------------------------
- Response Time / Elapsed Time: Total duration (in ms) from sending an HTTP request to receiving the full response.
- Latency (Time to First Byte - TTFB): Duration from request dispatch to receipt of the initial response byte.
- Throughput (Transactions / Requests per Second): Rate at which the application handles client requests.
- Error Rate (%): Ratio of failed requests (HTTP 4xx/5xx or assertion failures) relative to total transactions.
- Concurrency (Active Virtual Users / Threads): Number of simultaneous users executing requests.
- Bandwidth Utilization (KB/sec): Volume of inbound (received) and outbound (sent) network data per second.
- APDEX (Application Performance Index): Standardized numerical metric (0.0 to 1.0) grading user satisfaction based on response time thresholds ($T$ and $4T$).


================================================================================
2. APACHE JMETER CORE ARCHITECTURE & EXPERIMENT COMPONENTS
================================================================================

```
+-----------------------------------------------------------------------------------+
|                     APACHE JMETER TEST EXECUTION FLOW PIPELINE                    |
+-----------------------------------------------------------------------------------+

     [ Test Plan ]
          |
          v
     [ Thread Group ]  (Virtual Users, Ramp-Up Time, Loop Count)
          |
          +---> [ Config Elements ]        (HTTP Request Defaults, HTTP Header Manager)
          |
          +---> [ Timers ]                 (Constant Timer: User Think Time Simulation)
          |
          +---> [ Logic Controllers ]      (Loop Controller: Iterative Polling Logic)
          |          |
          |          v
          +---> [ Samplers ]               (HTTP Request Proxies: GET /index, /monitoring, etc.)
          |          |
          |          +---> [ Pre-Processors ]  (Pre-Execution Setup / Parameterization)
          |          |
          |          +---> [ Post-Processors ] (Regex Extractor: Dynamic Value Extraction)
          |          |
          |          +---> [ Assertions ]      (Response Assertion: Code 200, Body Text)
          |
          v
     [ Listeners ]                         (View Results Tree, Aggregate Report, Dashboard)
```

The laboratory assignment specifically requires incorporating five essential JMeter elements:

1. Performance Test Plan & Thread Group:
   - Root container element defining global variables (host, port) and thread pool parameters.
   - Simulates 25 concurrent users ramping up across 5 seconds with multiple iteration loops.

2. Constant Timer (User Think Time):
   - Real human users pause to read content before clicking another link. The Constant Timer 
     delays request dispatch by a specified interval (configured to 300 ms).
   - Prevents unnatural, instantaneous bursts and accurately mimics genuine human user behavior.

3. Response Assertion:
   - Verifies that responses comply with functional integrity and SLAs.
   - Assertions applied:
     * Status Code Assertion: Validates HTTP Status Code equals `200`.
     * Content Assertion: Verifies page markup contains mandatory text (e.g., "Heatwave Watch").

4. Loop Controller:
   - Controls how many times child samplers iterate within a single thread loop.
   - Used to simulate high-frequency IoT polling on the `/monitoring.html` weather telemetry 
     endpoint (3 iterations per parent loop).

5. Post Processor (Regular Expression Extractor):
   - Executes after sampler completion to parse the response body/headers and capture dynamic data.
   - Configured Regex: `<title>([^<]+)</title>` extracting the page title into `${EXTRACTED_TITLE}`, 
     and `<h3>([^<]+)</h3>` extracting the active weather station name into `${EXTRACTED_STATION}`.


================================================================================
3. TEST ENVIRONMENT & TARGET SYSTEM SPECIFICATIONS
================================================================================

- Host Environment: Apple Silicon (macOS Darwin 25.3.0)
- Java Runtime: OpenJDK 64-Bit Server VM (build 25.0.3+9-LTS)
- JMeter Engine: Apache JMeter Version 5.6.3
- Target Web Application: HeatAware AI Climate Intelligence Web Application
  * Local URL: `http://localhost:8000`
  * Architecture: Multi-page responsive web platform (HTML5, Vanilla CSS3, ES6 JavaScript)
  * Endpoints Under Test:
    1. `/index.html`       (System Overview & Beneficiaries)
    2. `/dashboard.html`   (Heatwave Hotspot Tracking & Zone Forecasts)
    3. `/monitoring.html`  (Live Ground IoT Station Telemetry - Iterated via Loop Controller)
    4. `/advisories.html`  (AI Stakeholder Advisory Simulator)
    5. `/research.html`    (Data Repositories & IMD Publication Archives)


================================================================================
4. JMETER TEST PLAN IMPLEMENTATION DETAILS
================================================================================

Test Plan File: `performance_tests/heataware_performance_test.jmx`

Configured Element Hierarchy:
```
HeatAware AI Performance Test Plan
 ├── HTTP Request Defaults (Server: localhost, Port: 8000, Protocol: http)
 ├── HTTP Header Manager (User-Agent, Accept, Accept-Language)
 └── Climate Platform Users - Load Simulation (Thread Group)
      ├── Constant Timer (300 ms delay think-time)
      ├── HTTP Request - GET Homepage (/index.html)
      │    ├── Response Assertion (Response Code == 200)
      │    ├── Response Assertion (Contains "Heatwave Watch")
      │    └── Post Processor - Regex Extractor (Extracts <title> to $EXTRACTED_TITLE)
      ├── HTTP Request - GET Dashboard (/dashboard.html)
      │    └── Response Assertion (Response Code == 200)
      ├── Loop Controller - High Frequency Telemetry Poll (3 loops)
      │    └── HTTP Request - GET AWS Monitoring (/monitoring.html)
      │         ├── Response Assertion (Response Code == 200)
      │         └── Post Processor - Regex Extractor (Extracts station header)
      ├── HTTP Request - GET Advisories (/advisories.html)
      │    └── Response Assertion (Response Code == 200)
      ├── HTTP Request - GET Research (/research.html)
      │    └── Response Assertion (Response Code == 200)
      ├── Listener: View Results Tree
      ├── Listener: Summary Report
      └── Listener: Aggregate Report
```


================================================================================
5. STEP-BY-STEP PROCEDURE (CLI AUTOMATION & GUI MANUAL MODE)
================================================================================

### Method A: Automated CLI Execution & HTML Dashboard Generation

1. Ensure the web application server is running:
   ```bash
   python3 -m http.server 8000 &
   ```

2. Execute the complete performance test suite via the dedicated runner:
   ```bash
   ./performance_tests/run_performance_test.sh
   ```
   Alternatively, invoke JMeter CLI directly:
   ```bash
   jmeter -n -t performance_tests/heataware_performance_test.jmx \
          -l performance_tests/results/results.jtl \
          -e -o performance_tests/results/dashboard_report
   ```

3. Open the generated interactive HTML performance report in any browser:
   ```bash
   open performance_tests/results/dashboard_report/index.html
   ```

---

### Method B: Manual Interactive Execution via Apache JMeter GUI

For manual lab evaluation or taking GUI screenshots for the journal:

1. Launch JMeter in GUI Mode:
   - In macOS / Linux Terminal:
     ```bash
     jmeter
     ```
   - In Windows Command Prompt:
     ```cmd
     cd C:\apache-jmeter-5.6.3\bin
     jmeter.bat
     ```

2. Load the Pre-configured Test Plan:
   - Click `File` -> `Open` (or press `Ctrl+O` / `Cmd+O`).
   - Navigate to the project directory and open `performance_tests/heataware_performance_test.jmx`.

3. Step-by-Step Manual Creation (if building from scratch in JMeter GUI):
   - **Step 3.1: Create Test Plan & Thread Group**:
     * Right-click `Test Plan` -> `Add` -> `Threads (Users)` -> `Thread Group`.
     * Set `Number of Threads (users)`: `25`.
     * Set `Ramp-Up Period (seconds)`: `5`.
     * Set `Loop Count`: `2`.
   - **Step 3.2: Add HTTP Request Defaults & Header Manager**:
     * Right-click `Test Plan` -> `Add` -> `Config Element` -> `HTTP Request Defaults`.
     * Set `Server Name or IP`: `localhost`, `Port Number`: `8000`.
   - **Step 3.3: Add Constant Timer (Item 2 from Lab Manual)**:
     * Right-click `Thread Group` -> `Add` -> `Timer` -> `Constant Timer`.
     * Set `Thread Delay (in milliseconds)`: `300`.
   - **Step 3.4: Add HTTP Request Samplers**:
     * Right-click `Thread Group` -> `Add` -> `Sampler` -> `HTTP Request`.
     * Set `Name`: `GET Homepage`, `Path`: `/index.html`, `Method`: `GET`.
   - **Step 3.5: Add Response Assertion (Item 3 from Lab Manual)**:
     * Right-click `GET Homepage` -> `Add` -> `Assertions` -> `Response Assertion`.
     * In `Field to Test`, select `Response Code`.
     * Under `Pattern Matching Rules`, select `Equals`.
     * Click `Add` in patterns table and type `200`.
     * Add a second Response Assertion: select `Text Response`, choose `Substring`, enter `Heatwave Watch`.
   - **Step 3.6: Add Loop Controller (Item 4 from Lab Manual)**:
     * Right-click `Thread Group` -> `Add` -> `Logic Controller` -> `Loop Controller`.
     * Set `Loop Count`: `3`.
     * Under the Loop Controller, add an `HTTP Request` sampler with `Path`: `/monitoring.html`.
   - **Step 3.7: Add Post Processor (Item 5 from Lab Manual)**:
     * Right-click `GET Homepage` (or `/monitoring.html`) -> `Add` -> `Post Processors` -> `Regular Expression Extractor`.
     * Set `Name of created variable`: `EXTRACTED_TITLE`.
     * Set `Regular Expression`: `<title>([^<]+)</title>`.
     * Set `Template`: `$1$`.
     * Set `Match No.`: `1`.
     * Set `Default Value`: `NOT_FOUND`.
   - **Step 3.8: Add Listeners**:
     * Right-click `Test Plan` -> `Add` -> `Listener` -> `View Results Tree`.
     * Right-click `Test Plan` -> `Add` -> `Listener` -> `Summary Report`.
     * Right-click `Test Plan` -> `Add` -> `Listener` -> `Aggregate Report`.

4. Run the Test:
   - Ensure local python server is running on port 8000 (`python3 -m http.server 8000`).
   - Click the green **Start** button (play icon) on the top toolbar or press `Cmd+R` / `Ctrl+R`.
   - Observe real-time execution in `View Results Tree` (green checkmarks for successful HTTP 200 responses) and tabular metrics in `Summary Report` / `Aggregate Report`.


================================================================================
6. RESULTS & PERFORMANCE DATA ANALYSIS
================================================================================

### Tabular Performance Metrics (Aggregate Summary)

The performance test executed 350 transactions across 25 concurrent threads with 0.00% error rate:

| Endpoint Under Test                     | Samples | Avg Time (ms) | Min (ms) | Max (ms) | 90th % (ms) | 95th % (ms) | 99th % (ms) | Throughput (req/s) | Network Recv (KB/s) | Error % |
|:----------------------------------------|:-------:|:-------------:|:--------:|:--------:|:-----------:|:-----------:|:-----------:|:------------------:|:-------------------:|:-------:|
| `GET /index.html` (Homepage)            | 50      | 1.92          | 0.0      | 14.0     | 2.0         | 3.0         | 14.0        | 7.26 req/s         | 71.4 KB/s           | 0.00%   |
| `GET /dashboard.html` (Forecast Watch)  | 50      | 1.74          | 0.0      | 5.0      | 2.0         | 3.0         | 5.0         | 7.28 req/s         | 97.1 KB/s           | 0.00%   |
| `GET /monitoring.html` (IoT Telemetry)  | 150     | 1.40          | 0.0      | 5.0      | 2.0         | 2.0         | 4.0         | 20.03 req/s        | 139.1 KB/s          | 0.00%   |
| `GET /advisories.html` (AI Advisories)  | 50      | 1.30          | 0.0      | 4.0      | 2.0         | 2.0         | 4.0         | 7.28 req/s         | 73.6 KB/s           | 0.00%   |
| `GET /research.html` (Data Archive)     | 50      | 1.44          | 0.0      | 5.0      | 2.0         | 3.0         | 5.0         | 7.28 req/s         | 93.4 KB/s           | 0.00%   |
| **TOTAL (Aggregated Platform Workload)**| **350** | **1.51 ms**   | **0.0**  | **14.0** | **2.0 ms**  | **2.45 ms** | **4.0 ms**  | **40.08 req/s**    | **374.13 KB/s**     | **0.00%**|

### Interpretation of Results:
1. **Response Time Stability**: Average latency across all web endpoints stayed well below 2 milliseconds, with a 99th percentile of 4.0 ms. This confirms zero perceptible UI lag.
2. **Throughput Efficiency**: Sustained an aggregated throughput of 40.08 requests per second across concurrent threads, transferring ~374.13 KB/sec without dropping connections.
3. **Loop Controller Behavior**: The Loop Controller successfully tripled the load on `/monitoring.html` (150 samples vs 50 samples for other routes), demonstrating effective targeted stress simulation for high-frequency IoT streaming telemetry.
4. **Assertion Verification**: 100% of responses returned status code 200 and verified required page identifiers. Zero assertion errors were recorded.
5. **Think-Time Realism**: The 300 ms Constant Timer smoothed traffic distribution, preventing artificial burst contention and mirroring natural human click patterns.


================================================================================
7. ANSWERS TO QUESTIONS (LAB MANUAL QUESTIONS)
================================================================================

--------------------------------------------------------------------------------
Question 1: Why performance testing is considered highly important for web applications? 
Outline the performance parameters against which testing can be performed.
--------------------------------------------------------------------------------

Answer:

### A. Importance of Performance Testing for Web Applications:

1. **Direct Impact on User Retention and Conversion Rates**:
   Research by Akamai and Google reveals that every 100-millisecond delay in page load time 
   drops conversion rates by up to 7%. 53% of mobile visits are abandoned if pages take longer 
   than 3 seconds to load. Performance testing guarantees that applications meet modern speed 
   expectations.

2. **System Scalability and Revenue Protection**:
   Web applications frequently experience sudden traffic surges during events like flash sales, 
   critical news broadcasts, or natural disaster warnings (e.g., heatwave alerts). Performance 
   testing identifies infrastructure bottlenecks before catastrophic outages occur, saving 
   millions in lost revenue and brand degradation.

3. **Infrastructure Cost Optimization**:
   Through capacity and load testing, engineering teams can fine-tune container limits, 
   auto-scaling policies, and database connection pool sizes. This avoids over-provisioning 
   expensive cloud resources while preventing under-provisioned service degradation.

4. **Ensuring High Availability and Reliability (SLAs)**:
   Enterprise contracts mandate strict Service Level Agreements (e.g., 99.99% uptime with 
   sub-500ms latency). Performance testing validates that the system fulfills contractual 
   obligations under peak concurrent usage.

5. **Detection of Latent Architectural and Memory Flaws**:
   Many severe defects—such as memory leaks, database deadlocks, unindexed queries, and 
   thread contention—only manifest when the application is subjected to sustained concurrent 
   traffic. Performance testing detects these issues early in the testing lifecycle.

---

### B. Key Performance Parameters Against Which Testing is Performed:

1. **Response Time / Round-Trip Time (RTT)**:
   The elapsed time between the client sending an HTTP request and receiving the complete response. 
   Measured as Mean, Median, 90th, 95th, and 99th percentile values.

2. **Throughput (Transactions Per Second / TPS)**:
   The number of discrete requests or business transactions the application successfully processes 
   per second.

3. **Latency / Time to First Byte (TTFB)**:
   The duration from request transmission until the client browser receives the very first byte of 
   the response, reflecting web server and network routing efficiency.

4. **Error Rate (%)**:
   The percentage of failed transactions (HTTP 5xx server errors, HTTP 4xx errors, connection timeouts, 
   or assertion failures) relative to total attempts. Acceptable thresholds are typically < 0.1%.

5. **Resource Utilization (Hardware & Infrastructure)**:
   - CPU Utilization (%): Percentage of server CPU consumed during test load.
   - Memory Consumption (RAM): Heap and non-heap memory consumption; monitoring for garbage collection pauses.
   - Disk I/O: Rate of read/write operations on disk storage.
   - Network Bandwidth / I/O: Megabits/sec sent and received across network interfaces.

6. **Concurrency & Thread Capacity**:
   The maximum number of simultaneous active virtual users the system sustains without degrading 
   performance beyond acceptable thresholds.

7. **Database Performance Parameters**:
   Connection pool utilization, query execution latency, transaction lock wait times, and deadlock frequency.


--------------------------------------------------------------------------------
Question 2: What are the major challenges in performance testing?
--------------------------------------------------------------------------------

Answer:

The execution of rigorous performance testing encounters several major technical, operational, 
and organizational challenges:

1. **Accurately Replicating Real-World Production Environments (Test Bed Parity)**:
   - Creating a test environment that mirrors production in hardware, network topology, 
     firewalls, CDN configurations, and database scale is cost-prohibitive for many organizations.
   - Testing on downscaled staging environments requires complex mathematical extrapolations 
     that often fail to predict production-grade bottlenecks accurately.

2. **Realistic User Behavior Modeling & Workload Modeling**:
   - Real users do not execute requests uniformly in lockstep. They navigate unpredictably, have 
     variable think-times, utilize different network speeds (4G, 5G, Wi-Fi), and execute mixed 
     ratios of read vs. write operations.
   - Designing test scripts that accurately simulate this heterogeneous user mix requires deep 
     analytics data and sophisticated test plan scripting.

3. **Dynamic Data Parameterization & State Management**:
   - Web applications heavily utilize dynamic security tokens (CSRF tokens, OAuth 2.0 JWTs, 
     session cookies) and dynamic parameters (IDs, timestamps).
   - Testers must configure complex Regular Expression Extractors, JSON Path Post-Processors, 
     and Correlation rules to parse dynamic response tokens and inject them into subsequent 
     requests without causing 401/403 session errors.

4. **Test Data Management at Scale**:
   - Performance tests require massive datasets to test realistic database queries.
   - If multiple virtual users query or insert identical records, artificial database deadlocks 
     or unrealistic cache hits occur. Maintaining unique, sanitized test data pools across millions 
     of transactions is a major logistics hurdle.

5. **Identifying Root Causes of Bottlenecks (Pinpointing the Bottleneck)**:
   - High response times observed in JMeter can stem from numerous layers: client-side network 
     saturation, DNS resolution delay, reverse proxy limits, application code bugs, database lock 
     contention, JVM garbage collection pauses, or microservice dependencies.
   - Correlating JMeter output with Application Performance Monitoring (APM) tools (e.g., Dynatrace, 
     New Relic, Prometheus) requires high cross-domain engineering expertise.

6. **Network Bandwidth and Load Generator Saturation**:
   - If the machine running JMeter runs out of memory, CPU, or open socket descriptors (ephemeral ports), 
     the load generator itself becomes the bottleneck, generating skewed, false-positive latency spikes.
   - Large-scale load testing requires orchestrating distributed JMeter master-slave client architectures.


================================================================================
8. OUTCOMES
================================================================================

1. Successfully installed, configured, and operated Apache JMeter 5.6.3 in both CLI and 
   interactive GUI modes for load testing web applications.
2. Formulated a comprehensive Performance Test Plan incorporating all required laboratory elements:
   - **Thread Group**: 25 concurrent users with 5-second ramp-up and multi-iteration execution.
   - **Constant Timer**: Enforced 300 ms think-time to mirror human browsing patterns.
   - **Response Assertion**: Verified HTTP 200 OK status and verified critical response body markers.
   - **Loop Controller**: Controlled high-frequency polling on real-time AWS IoT monitoring endpoints.
   - **Post Processor (Regex Extractor)**: Extracted dynamic HTML metadata and page titles.
3. Executed 350 transactions against the HeatAware AI platform, achieving a 0.00% error rate, 
   1.51 ms average latency, and an aggregate throughput of 40.08 requests/second.
4. Generated an automated HTML performance dashboard providing visual APDEX ratings, 
   response time distributions, and throughput curves.
5. Analyzed the critical importance of performance parameters and addressed major real-world 
   performance engineering challenges.


================================================================================
9. CONCLUSION
================================================================================

In this experiment, Performance Testing was successfully conducted on the HeatAware AI 
Climate Intelligence Web Application using Apache JMeter. Performance testing is essential 
in the software lifecycle to ensure that web platforms remain responsive, robust, and available 
under concurrent user traffic. By configuring Thread Groups, Constant Timers, Response Assertions, 
Loop Controllers, and Post Processors, realistic user workloads and validation rules were 
established. The experimental evaluation confirmed that the HeatAware AI web server handles 
concurrent workloads with sub-2ms average response times and zero failure rate. Applying 
regular load, stress, and endurance testing ensures optimal system reliability, customer 
satisfaction, and operational resilience.


--------------------------------------------------------------------------------
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________


================================================================================
10. REFERENCES
================================================================================
1. Apache JMeter Official Documentation & User Manual: https://jmeter.apache.org/
2. Guru99 - JMeter Performance Testing Complete Guide: https://www.guru99.com/jmeter-performance-testing.html
3. DZone Performance Zone - JMeter Performance & Load Testing: https://dzone.com/articles/jmeter-performance-and-load-testing
4. Somaiya Vidyavihar University STQA Lab Manual - Experiment No. 06.
5. W3C Web Performance Working Group Standards: https://www.w3.org/webperf/
6. High Performance Browser Networking, Ilya Grigorik, O'Reilly Media.
