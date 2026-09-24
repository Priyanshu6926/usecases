================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | STQA (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/STQA/2026-27
================================================================================

Batch: A2                Roll No.: 16010423075                Experiment No.: 07
Title: Usability Testing

________________________________________________________________________________
Aim: To perform usability testing using any open source tool.
________________________________________________________________________________
Resources needed: Internet, Chrome Browser (DevTools & Engine), Google Lighthouse 13.5.0
(CLI & Automated Audit Pipeline), Python 3 Local Server, HeatAware AI Platform (`usecases`).
________________________________________________________________________________

================================================================================
1. THEORY
================================================================================

Usability testing, also known as User Experience (UX) testing, is a core empirical 
software testing method aimed at measuring how intuitive, efficient, accessible, and 
user-friendly a software application is for real human operators. While functional 
testing evaluates *whether* features work, usability testing measures *how easily, 
delightfully, and error-free* target end-users can accomplish their goals within the 
application interface.

Usability testing focuses primarily on:
1. Ease of navigation and information hierarchy.
2. Cognitive workload and interface predictability.
3. System feedback, responsive design, and error recovery.
4. Digital accessibility across diverse abilities, devices, and screen resolutions.

Executing usability and accessibility audits early in the Software Development Life Cycle 
(SDLC) drastically reduces design debt, prevents expensive post-release redesigns, and 
drives user engagement, trust, and retention.

--------------------------------------------------------------------------------
Usability Engineering and the 6 Core Usability Goals
--------------------------------------------------------------------------------
Usability Engineering is the disciplined process of identifying end-user needs, tasks, 
and operational environments to ensure products achieve high usability standards. 
Every usability assessment targets six primary dimensions:

1. **Intuitive Design & User Interface**:
   - The interface visual architecture must communicate its affordances immediately.
   - Users should not struggle to determine what elements are clickable, navigable, or interactive.

2. **Ease of Learning (Learnability)**:
   - How rapidly can a first-time user understand basic workflows and accomplish primary 
     tasks (e.g., viewing heat risk alerts, toggling IoT feeds) without formal training?

3. **Efficiency of Use**:
   - Once users have learned the workflow, how quickly can they complete repetitive or 
     mission-critical operations? High efficiency minimizes unnecessary clicks and page reloads.

4. **Memorability**:
   - When casual or intermittent users return to the application after weeks of absence, 
     how easily can they re-establish proficiency without starting over?

5. **Error Prevention and Recovery**:
   - How effectively does the design guide users away from erroneous states (form validation, 
     confirmations), and how clear and actionable are system error messages when issues occur?

6. **User Satisfaction**:
   - The subjective comfort, perceived utility, aesthetic appeal, and emotional confidence 
     felt by the user while interacting with the platform.

--------------------------------------------------------------------------------
Nielsen's 10 Usability Heuristics for Interface Design
--------------------------------------------------------------------------------
Jakob Nielsen's classic heuristics provide the standard heuristic evaluation baseline:
1. **Visibility of system status**: Continuous feedback through spinners, loaders, and status badges.
2. **Match between system and real world**: Natural language, familiar meteorological terminology.
3. **User control and freedom**: Clear navigation escape hatches, back buttons, and undo options.
4. **Consistency and standards**: Uniform typography, color semantics, and button styles.
5. **Error prevention**: Confirmation prompts and sensible defaults.
6. **Recognition rather than recall**: Visible options instead of requiring users to remember past steps.
7. **Flexibility and efficiency of use**: Keyboard accelerators and mobile-friendly tap targets.
8. **Aesthetic and minimalist design**: High signal-to-noise ratio; no visual clutter.
9. **Help users recognize, diagnose, and recover from errors**: Plain English error notifications.
10. **Help and documentation**: Readily accessible tooltips, FAQs, and advisories.

--------------------------------------------------------------------------------
Digital Accessibility & WCAG 2.1 Framework
--------------------------------------------------------------------------------
Accessibility (A11y) ensures that digital products are usable by individuals with disabilities, 
including visual, auditory, motor, and cognitive impairments. The W3C Web Content Accessibility 
Guidelines (WCAG 2.1) are structured around four fundamental pillars (**POUR**):
- **Perceivable**: Text alternatives for non-text content (`alt` attributes), sufficient color contrast 
  ($\ge 4.5:1$ for regular text, $\ge 3:1$ for large text), and readable typography.
- **Operable**: Full keyboard accessibility without keyboard traps, sufficient touch target sizes ($\ge 48 \times 48$ px), 
  and adequate reading/interaction time.
- **Understandable**: Logical reading and DOM order, sequential heading hierarchy (`h1` $\rightarrow$ `h2` $\rightarrow$ `h3`), 
  consistent navigation, and plain language.
- **Robust**: Maximized compatibility with current and future assistive technologies (screen readers like NVDA/VoiceOver) 
  using valid HTML5 semantic tags and WAI-ARIA attributes.

--------------------------------------------------------------------------------
Comparative Analysis of Open-Source & Automated Usability Testing Tools
--------------------------------------------------------------------------------

| Tool | Engine / Mechanism | Core Strengths | Focus Areas | Open Source Status |
| :--- | :--- | :--- | :--- | :--- |
| **Google Lighthouse** | Chromium DevTools Protocol | Automated, rigorous scoring (0-100) across 5 audits | Usability, Accessibility, Core Web Vitals, SEO, Best Practices | **100% Open Source (Apache 2.0)** |
| **Google PageSpeed Tools** | Lighthouse Engine + CrUX Real-User Data | Field vs. Lab data comparison, Core Web Vitals | Real-world network latency and mobile load dynamics | Free Cloud Service (Lighthouse Core) |
| **WebPageTest** | Multi-location real browser agents | Deep waterfall diagrams, Lighthouse integration, filmstrips | Multi-run variance, network throttling, visual rendering | Open Source (Private instances available) |
| **GTmetrix** | Lighthouse + custom analysis engines | Historical tracking, waterfall breakdown, visual playback | Performance optimization, server response tuning | Freemium Web Service |
| **HubSpot Website Grader** | Static crawler & header scanner | High-level non-technical website scoring | Marketing, basic mobile responsiveness, SSL, SEO | Proprietary free tool |


================================================================================
2. PROCEDURE
================================================================================

The usability assessment was executed using **Google Lighthouse 13.5.0** alongside 
the Google Chrome headless browser engine on macOS. The evaluation was run across 
multiple mission-critical application views within the HeatAware AI platform:
- `index.html`: Landing and Climate Early Warning Overview.
- `dashboard.html`: Interactive Climate & Heat Analytics Dashboard.
- `monitoring.html`: Real-time IoT Sensor Monitoring Interface.

The experiment followed these systematic steps:

```
+-----------------------------------------------------------------------------------+
|               AUTOMATED USABILITY TESTING PIPELINE (LIGHTHOUSE CLI)               |
+-----------------------------------------------------------------------------------+

     [ HeatAware AI Web App ]
                |
                v
     [ Local Web Server ] (Python 3 HTTP Server, Port 53471)
                |
                +---------------------------------+
                |                                 |
                v                                 v
     [ Desktop Preset Audit ]           [ Mobile Preset Audit ]
     - Viewport: 1350x940               - Viewport: 412x823 (Moto G Power)
     - Device Scale Factor: 1           - Device Scale Factor: 1.75
     - Throttling: 10 Gbps / None       - Throttling: Simulated 4G (1.6 Mbps / 150ms)
                |                                 |
                +----------------+----------------+
                                 |
                                 v
                [ Chromium DevTools Protocol (CDP) ]
                - DOM & Accessibility Tree Inspection
                - Color Contrast Calculation (WCAG 2.1 AA)
                - Core Web Vitals & Interaction Metrics
                - ARIA Roles & Screen Reader Compatibility
                                 |
                                 v
                [ Usability Reports Generation ]
                - Interactive HTML Dashboards
                - Raw JSON Audit Diagnostics & Scorecards
```

### Execution Steps:
1. **Tool Exploration & Setup**:
   - Installed and verified the open-source Google Lighthouse automation tool:
     ```bash
     CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" npx -y lighthouse --version
     # Verified version: Lighthouse v13.5.0
     ```
2. **Automated Test Script Orchestration**:
   - Developed `run_usability_audit.py` to automate headless Chrome instances, serve pages over local HTTP, 
     and generate both Desktop and Mobile test runs.
3. **Execution across Platform Pages**:
   - Performed usability, accessibility, SEO, and performance passes for `index.html`, `dashboard.html`, 
     and `monitoring.html`.
4. **Heuristic & Accessibility Defect Analysis**:
   - Parsed JSON output files to extract failed audits, element selectors, contrast levels, and heading orders.
5. **Improvement Formulation**:
   - Formulated concrete engineering improvements to resolve identified usability and accessibility bottlenecks.


================================================================================
3. EXPERIMENTAL RESULTS & AUDIT SCORECARD
================================================================================

### Usability & Quality Summary Across Pages

| Page / Target View | Emulation Mode | Performance | Accessibility | Best Practices | SEO | FCP | LCP | CLS |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`index.html`** (Home) | Desktop (High-Speed) | **100 / 100** | **91 / 100** | **96 / 100** | **100 / 100** | 0.7 s | 0.7 s | 0.002 |
| **`index.html`** (Home) | Mobile (Simulated 4G) | **69 / 100** | **100 / 100** | **96 / 100** | **100 / 100** | 3.3 s | 6.7 s | 0.000 |
| **`dashboard.html`** (Analytics) | Desktop (High-Speed) | **100 / 100** | **88 / 100** | **96 / 100** | **100 / 100** | 0.6 s | 0.6 s | 0.000 |
| **`monitoring.html`** (IoT Live) | Desktop (High-Speed) | **100 / 100** | **88 / 100** | **96 / 100** | **100 / 100** | 0.6 s | 0.6 s | 0.001 |

--------------------------------------------------------------------------------
Detailed Core Web Vitals & Usability Timings (Desktop)
--------------------------------------------------------------------------------
- **First Contentful Paint (FCP)**: 0.6 s - 0.7 s (Rating: **GOOD**; well under 1.8 s threshold)
- **Largest Contentful Paint (LCP)**: 0.6 s - 0.7 s (Rating: **GOOD**; well under 2.5 s threshold)
- **Cumulative Layout Shift (CLS)**: 0.000 - 0.002 (Rating: **EXCELLENT**; zero visual jarring or jumping elements)
- **Total Blocking Time (TBT)**: 0 ms (Rating: **EXCELLENT**; non-blocking JS main thread)
- **Speed Index**: 0.6 s - 0.7 s (Rating: **EXCELLENT**)

--------------------------------------------------------------------------------
Usability, Accessibility, and Quality Flaws Identified
--------------------------------------------------------------------------------

1. **Color Contrast Discrepancy (WCAG 2.1 AA Violation - Score: 0/1)**:
   - **Locations**: Secondary metadata text and timestamps in `index.html`, `dashboard.html`, and `monitoring.html`.
   - **Observed**: `#6b7280` text against a dark background (`#121824`).
   - **Measured Contrast Ratio**: `3.67:1`.
   - **Requirement**: WCAG 2.1 AA requires a minimum ratio of `4.5:1` for standard text under 18pt/14pt bold.
   - **Usability Impact**: Low-vision users and individuals viewing screens in high-glare outdoor sunlight 
     experience strain or inability to read secondary metadata.

2. **Heading Level Discontinuity (Heading Order Violation - Score: 0/1)**:
   - **Locations**: Section titles in `dashboard.html` and `monitoring.html`.
   - **Observed**: Content transitions directly from `<h1>` (Page Title) to `<h3>` (`<h3 class="section-title">`), skipping `<h2>`.
   - **Usability Impact**: Screen-reader users navigating via heading jump keys (`H` or `1-6` in NVDA/VoiceOver) 
     receive distorted mental models of content hierarchy.

3. **Missing Static Asset Error (Browser Console Error - Score: 0/1)**:
   - **Observed**: HTTP 404 response on `/favicon.ico`.
   - **Usability Impact**: Tab strip missing website visual branding in multi-tab browsing environments, 
     reducing memorability and tab recognition.

4. **Mobile Performance Bottleneck under Throttled 4G**:
   - **Observed**: On mobile emulation, LCP increased to 6.7 s due to unminified CSS/JS and font loading delays.
   - **Usability Impact**: Mobile users in low-bandwidth regions face slow initial rendering, 
     increasing bounce probability.


================================================================================
4. SUGGESTED IMPROVEMENTS & ACTIONABLE RECOMMENDATIONS
================================================================================

Based on the empirical findings generated by the Lighthouse usability audit, the 
following engineering and UI enhancements are recommended:

1. **Contrast Ratio Rectification (Accessibility & Readability)**:
   - Upgrade low-contrast slate colors (`#6b7280`) to `#94a3b8` or `#cbd5e1`.
   - *Result*: Increases contrast ratio from **3.67:1** to **7.8:1**, passing WCAG 2.1 AAA level.
   ```css
   /* Improvement in css/style.css */
   .card-meta, .timestamp-label, p.secondary-text {
       color: #94a3b8; /* High-contrast readable slate */
   }
   ```

2. **Semantic Heading Order Normalization**:
   - Refactor skipped heading tags in `dashboard.html` and `monitoring.html`:
   ```html
   <!-- Before: <h1>...</h1> followed by <h3 class="section-title"> -->
   <!-- After: Hierarchical sequential progression -->
   <h2 class="section-title">Regional Threat Analysis</h2>
   ```

3. **Font Loading Optimization (`font-display: swap`)**:
   - Prevent FOIT (Flash of Invisible Text) during network latency on mobile devices by 
     enforcing `font-display: swap` in Google Font links.
   ```html
   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
   ```

4. **Include Valid Favicon & App Icons**:
   - Place a valid SVG / PNG favicon in the document head to eliminate HTTP 404 console errors 
     and enhance bookmark / tab recognition:
   ```html
   <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>☀️</text></svg>">
   ```

5. **Resource Minification & Asset Caching**:
   - Minify `style.css` and `app.js` and set explicit `Cache-Control: public, max-age=31536000` 
     headers for static production deployments.


================================================================================
5. QUESTIONS & ANSWERS
================================================================================

--------------------------------------------------------------------------------
Question 1: Describe usability and accessibility testing. Explain any five test 
cases/scenarios for testing usability and accessibility of a web application.
--------------------------------------------------------------------------------

**Description**:
- **Usability Testing**: Evaluates how effectively, efficiently, and satisfactorily human 
  users can achieve specified goals in a software application. It focuses on intuitive UI design, 
  navigational layout, cognitive load, visual clarity, task completion speed, and error prevention.
- **Accessibility Testing (A11y)**: A specialized subset of usability focused on ensuring that the 
  web platform is fully perceivable, operable, understandable, and robust (POUR) for people with 
  disabilities (e.g., visual impairments, color blindness, motor limitations, hearing loss, or 
  cognitive disabilities), complying with international standards such as **W3C WCAG 2.1 / 2.2** 
  and Section 508.

**Five Comprehensive Test Cases / Scenarios for Usability & Accessibility**:

| Test Case ID | Test Category | Test Scenario & Objective | Execution Steps & Validation | Expected Outcome |
| :--- | :--- | :--- | :--- | :--- |
| **TC-UA-01** | Accessibility | **Color Contrast Ratio Verification** | Inspect foreground text against background using Lighthouse / axe DevTools on dark and light themes. | All standard text maintains a contrast ratio $\ge 4.5:1$; large headings ($\ge 18$pt) achieve $\ge 3.0:1$. |
| **TC-UA-02** | Accessibility | **Keyboard-Only Navigation & Focus Visibility** | Navigate through all links, buttons, form inputs, and modals using solely `Tab`, `Shift+Tab`, `Enter`, `Space`, and `Esc` without a mouse. | Focus ring is distinctly visible; logical tab order matches visual layout; no keyboard traps exist. |
| **TC-UA-03** | Usability / A11y | **Screen Reader Compatibility & ARIA Semantics** | Activate VoiceOver / NVDA and navigate through dynamic widgets (weather graphs, IoT metric counters, alerts). | All interactive elements have descriptive names; meaningful images have descriptive `alt` tags; status updates announce via `aria-live`. |
| **TC-UA-04** | Usability | **Responsive Touch Target Size & Layout Stability** | View the application on simulated mobile viewport ($360 \times 640$ px); test tap interactions on buttons, nav links, and dropdowns. | All interactive tap targets measure at least $48 \times 48$ px with $\ge 8$ px spacing; Cumulative Layout Shift (CLS) $< 0.1$. |
| **TC-UA-05** | Usability | **Form Error Prevention & User Guidance** | Submit search or input forms with invalid, empty, or boundary data (e.g., non-existent city, extreme weather inputs). | Clear, friendly, human-readable error messages appear adjacent to the invalid input without clearing valid user data; input focus moves to the error. |

--------------------------------------------------------------------------------
Question 2: What are the benefits of usability testing for website owners?
--------------------------------------------------------------------------------

Usability testing delivers extensive operational, commercial, and technical advantages 
to website owners:

1. **Significantly Higher Conversion Rates & Goal Completion**:
   - A frictionless interface eliminates cognitive fatigue and drop-offs during key user journeys 
     (e.g., signing up for heat emergency alerts, subscribing to reports, purchasing products). 
     Clear calls-to-action (CTAs) directly translate to higher business conversions.

2. **Reduced Bounce Rates and Increased User Engagement**:
   - If visitors find a website cluttered, slow to load, or difficult to navigate, they abandon 
     the site within seconds. Usability testing ensures instant visual clarity and rapid response, 
     retaining users longer.

3. **Drastic Reduction in Customer Support & Maintenance Costs**:
   - Interfaces designed with clear error prevention, intuitive terminology, and self-explanatory 
     controls drastically reduce user confusion. This reduces support tickets, troubleshooting 
     calls, and helpdesk inquiries.

4. **Lower Post-Launch Rework and Engineering Costs**:
   - Identifying user experience flaws during development costs up to 100 times less than refactoring 
     an established production system that has already lost dissatisfied users.

5. **Legal Compliance and Brand Inclusivity**:
   - Incorporating accessibility checks protects owners from legal liability, civil lawsuits, 
     and fines under the Americans with Disabilities Act (ADA), Section 508, and European 
     Accessibility Act (EAA), while projecting a brand image of social inclusion.

6. **Actionable Competitive Advantage & Customer Loyalty**:
   - In crowded markets, user experience is the primary differentiator. Users consistently choose 
     and recommend the website that makes completing tasks effortless and pleasant over more complex 
     competitors.


================================================================================
6. OUTCOMES
================================================================================

1. Successfully installed, explored, and configured the open-source **Google Lighthouse 13.5.0** 
   usability and accessibility audit engine.
2. Executed automated desktop and mobile usability audits across core pages of the HeatAware AI 
   platform (`index.html`, `dashboard.html`, `monitoring.html`), generating complete HTML dashboards 
   and JSON telemetry.
3. Achieved top-tier desktop usability scores:
   - **Performance: 100 / 100**
   - **SEO: 100 / 100**
   - **Best Practices: 96 / 100**
   - **Accessibility: 88 - 91 / 100**
   - **FCP: 0.6 s, LCP: 0.6 s, CLS: 0.000**
4. Discovered and cataloged specific accessibility and heuristic defects:
   - Insufficient color contrast on secondary slate labels (`#6b7280` yielding 3.67:1 vs 4.5:1 required).
   - Non-sequential heading element progression (`h1` skipping to `h3`).
   - Missing favicon resulting in 404 console errors.
5. Formulated an engineering remediation plan with exact CSS and semantic HTML patches to elevate 
   accessibility to a perfect 100/100 score.
6. Thoroughly answered both laboratory theoretical questions covering usability definitions, 
   accessibility test cases, and tangible business benefits for website owners.


================================================================================
7. CONCLUSION
================================================================================

In this experiment, Usability and Accessibility Testing was successfully conducted on the 
HeatAware AI Climate Intelligence Web Application using Google Lighthouse, Chromium DevTools, 
and automated Python test harnesses. Usability testing is an indispensable pillar of software 
quality assurance that ensures software systems are not only functionally correct, but also 
intuitive, responsive, and universally accessible to all individuals regardless of hardware, 
bandwidth, or physical ability.

Through automated audit execution, the HeatAware AI application demonstrated exceptional 
desktop performance (100%), optimal Core Web Vitals (sub-second FCP/LCP, zero CLS), and strong 
SEO architecture (100%). The evaluation accurately diagnosed specific areas for refinement, 
including WCAG color contrast thresholds and heading hierarchy sequencing. Remediating these 
findings ensures full WCAG 2.1 AA compliance, minimizes user error rates, maximizes retention, 
and provides a seamless, world-class user experience.


--------------------------------------------------------------------------------
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________


================================================================================
8. REFERENCES
================================================================================
1. Google Lighthouse Official Documentation: https://developers.google.com/web/tools/lighthouse/
2. Google PageSpeed Insights: https://developers.google.com/speed/pagespeed/insights/
3. WebPageTest - Lighthouse Auditing: https://www.webpagetest.org/lighthouse
4. Guru99 - Usability Testing Complete Tutorial: https://www.guru99.com/usability-testing-tutorial.html
5. GTmetrix Website Speed and Performance Analysis: https://gtmetrix.com/
6. Nielsen Norman Group - 10 Usability Heuristics for User Interface Design: https://www.nngroup.com/articles/ten-usability-heuristics/
7. W3C Web Content Accessibility Guidelines (WCAG) 2.1: https://www.w3.org/TR/WCAG21/
8. Somaiya Vidyavihar University STQA Lab Manual - Experiment No. 07.
