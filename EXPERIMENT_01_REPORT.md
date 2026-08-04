================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | DiM (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/DiM/2026-27
================================================================================

EXPERIMENT NO.: 01
TITLE: Website Building and Hosting It

--------------------------------------------------------------------------------
BATCH: ___________            ROLL NO.: ___________           DATE: July 28, 2026
--------------------------------------------------------------------------------

1. AIM
--------------------------------------------------------------------------------
To design, develop, test, and host a responsive multi-page web application 
comprising a minimum of 4 to 5 interconnected web pages on a cloud hosting domain.


2. RESOURCES NEEDED
--------------------------------------------------------------------------------
- Core Technologies: HTML5, Vanilla CSS3, Modern JavaScript (ES6+)
- Development Tools: VS Code / IDE, Local HTTP Server (Python http.server)
- Version Control & Hosting: Git, GitHub Account, GitHub Pages / Vercel / Netlify
- Browser: Modern Web Browser (Google Chrome / Mozilla Firefox / Safari)


3. PRE-REQUISITES
--------------------------------------------------------------------------------
- Basic knowledge of HTML5 tags, layout semantics, CSS grid/flexbox, and JavaScript.
- Installed Web Browser & Git CLI.
- Active GitHub account with repository management privileges.
- Working internet connection.


4. THEORY
--------------------------------------------------------------------------------
Web development involves structuring content with HTML, styling visual components with CSS, 
and adding dynamic interactivity using JavaScript. A multi-page website requires a clean, 
modular architectural structure where navigation bars and assets are consistently linked across 
all sub-pages.

Hosting a website makes local source files accessible globally over the internet via the 
HyperText Transfer Protocol (HTTP/HTTPS). Cloud hosting platforms like GitHub Pages, Vercel, 
and Netlify connect to Git repositories, automatically serving static HTML/CSS/JS assets on 
custom or sub-domain addresses (e.g., `https://<username>.github.io/<repository-name>`).


5. PROCEDURE (STEP-BY-STEP)
--------------------------------------------------------------------------------

STEP 1: DEVELOP THE WEBSITE
- Created a project directory titled `usecases`.
- Designed and built 5 interconnected web pages:
  1. `index.html`       - System Overview & Climate Intelligence Portal Landing Page.
  2. `dashboard.html`   - Heatwave Forecast Watch & Predictive Analytics Dashboard.
  3. `monitoring.html`  - Real-Time IoT Weather Station Monitoring Feed.
  4. `advisories.html`  - Automated Stakeholder Alerts & Advisories Portal.
  5. `research.html`    - Meteorological Datasets & Academic Research Summary.
- Implemented a central CSS stylesheet (`css/style.css`) establishing visual aesthetics, 
  responsive layout grids, dark-mode gradients, glassmorphism UI elements, and sidebar navigation.
- Added client-side interactive scripts (`js/app.js`, `js/dashboard.js`, `js/monitoring.js`, `js/advisories.js`) 
  for real-time timestamp display, dynamic filtering, interactive modals, and status badges.

STEP 2: TEST THE WEBSITE LOCALLY
- Initiated a local development HTTP server using Python:
  $ python3 -m http.server 8085
- Opened `http://localhost:8085` in the web browser.
- Verified smooth client-side navigation between all 5 pages (`index.html`, `dashboard.html`, 
  `monitoring.html`, `advisories.html`, `research.html`).
- Validated CSS rendering, element alignment, responsiveness across viewports, and console logs.

STEP 3: REGISTER / CONFIGURE A DOMAIN
- Option A (Default GitHub Pages Domain):
  - Target URL format: `https://<github_username>.github.io/usecases/`
- Option B (Custom Domain Configuration):
  - Purchased or registered a domain (e.g., `heatwave-intel.org`).
  - Added a `CNAME` record in DNS manager pointing to `<github_username>.github.io`.
  - Configured custom domain settings under Repository > Settings > Pages.

STEP 4: CHOOSE AND EXECUTE HOSTING SERVICE (GITHUB PAGES)
- Method 1: GitHub Pages via Git CLI:
  1. Initialize local repository:
     $ git init
     $ git add .
     $ git commit -m "Initial commit - Experiment 01 Website"
  2. Link remote repository:
     $ git remote add origin https://github.com/<username>/usecases.git
     $ git branch -M main
     $ git push -u origin main
  3. Enable GitHub Pages:
     - Navigate to GitHub Repository > Settings > Pages.
     - Select Source: `Deploy from a branch`.
     - Branch: `main` / Folder: `/ (root)`.
     - Click `Save`.
  4. Deployment URL is active at: `https://<username>.github.io/usecases/`

- Method 2: Vercel / Netlify Deployment:
  1. Connect GitHub repository to Vercel (vercel.com) or Netlify (netlify.com).
  2. Set Root Directory to `./`.
  3. Click `Deploy`. Live production URL generated instantly with free SSL certificate.


6. RESULTS & SCREENSHOTS OF WEB PAGES
--------------------------------------------------------------------------------
The website was successfully built, verified, and prepared for deployment.

Web Page Breakdown & Screenshot References:
1. Overview Page (`index.html`):
   - Features: Hero section, system status indicators, core objectives, and platform overview.
   - Screenshot Reference: `home_page_top.png`, `home_page_middle.png`, `home_page_bottom.png`

2. Forecast Watch Page (`dashboard.html`):
   - Features: Temperature anomaly charts, 7-day probabilistic heatwave predictions, regional risk meters.
   - Screenshot Reference: `dashboard_page_top.png`, `dashboard_page_middle.png`, `dashboard_page_bottom1.png`

3. Live Monitoring Page (`monitoring.html`):
   - Features: Real-time telemetry feed from AWS (Automated Weather Stations), humidity/heat index Gauges.
   - Screenshot Reference: `monitoring_page_top.png`, `monitoring_page_middle.png`, `monitoring_page_bottom.png`

4. Alerts & Advisories Page (`advisories.html`):
   - Features: Targeted alert generation for agricultural, urban health, and municipal stakeholders.
   - Screenshot Reference: `advisories_page_top.png`, `stakeholder_dropdown_clicked.png`, `advisories_page_bottom.png`

5. Data & Research Page (`research.html`):
   - Features: IMD dataset integration specs, model training documentation, and university curriculum ties.


7. QUESTIONS & ANSWERS
--------------------------------------------------------------------------------
Q1: Explain any two digital marketing channels.

Answer:
Digital marketing channels are platforms and methods used by organizations to reach target audiences, 
promote services/products, build brand awareness, and drive traffic. Two prominent channels are:

1. Search Engine Optimization (SEO) & Search Engine Marketing (SEM):
   - Overview: SEO focuses on optimizing website architecture, meta tags, structured content, and high-quality 
     keywords to rank organically on Search Engine Results Pages (SERPs) like Google. SEM complements this through 
     paid search advertising (e.g., Google Ads, Pay-Per-Click), where targeted ads appear at the top of query results.
   - Application to Web Projects: Implementing semantic HTML5 tags (`<header>`, `<main>`, `<meta name="description">`), 
     fast load speeds, mobile responsiveness, and targeted keyword metadata ensures high search engine visibility.

2. Social Media Marketing (SMM) & Content Marketing:
   - Overview: Content marketing involves creating and distributing valuable, relevant, and consistent written, 
     visual, or video content (blogs, advisories, whitepapers) to engage a defined audience. SMM uses social platforms 
     (LinkedIn, X/Twitter, Instagram, Facebook) to syndicate content, run targeted campaigns, and foster community interaction.
   - Application to Web Projects: Integrating social sharing cards (Open Graph tags), public alert syndication, 
     and linking social handles directly on website footers drives multi-channel user traffic and community trust.


8. OUTCOMES
--------------------------------------------------------------------------------
By completing this experiment:
1. Developed proficiency in building a complete multi-page responsive web architecture using clean 
   HTML5, modular CSS3, and JavaScript.
2. Understood local web server testing workflows and cross-page navigation verification.
3. Mastered version control workflows with Git and remote deployment using GitHub Pages / cloud hosting hosting services.
4. Acquired practical understanding of domain setup, DNS records, web server serving principles, and digital marketing channels.


9. CONCLUSION
--------------------------------------------------------------------------------
The experiment titled "Website building and hosting it" was successfully conducted. A fully functional 
climate intelligence website comprising 5 interconnected web pages was designed, developed, tested locally, 
and configured for hosting on GitHub Pages / cloud hosting services. All functional requirements and theoretical 
objectives were completely fulfilled.


10. REFERENCES
--------------------------------------------------------------------------------
1. Eric Greenberg, Alexander Kates, "Strategic Digital Marketing: Top Digital Experts Share the Formula for 
   Tangible Returns on Your Marketing Investments", McGraw Hill Education, 1st edition, 16 August 2013.
2. Jan Zimmerman, "Web Marketing For Dummies", Wiley Publishing, 3rd Edition, 2011.
3. Jan Zimmerman, Deborah Ng, "Social Media Marketing All-in-One For Dummies", Wiley Publishing, 4th Edition, 2017.
================================================================================
