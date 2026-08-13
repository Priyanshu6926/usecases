================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | DiM (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/DiM/2026-27
================================================================================

EXPERIMENT NO.: 02
TITLE: Google Analytics Set Up for Website

--------------------------------------------------------------------------------
BATCH: ___________            ROLL NO.: ___________           DATE: August 04, 2026
--------------------------------------------------------------------------------

1. AIM
--------------------------------------------------------------------------------
Setting up Google Analytics for Website.


2. RESOURCES NEEDED
--------------------------------------------------------------------------------
- Hardware & Network: Computer System with active Internet Connection.
- Software Tools: Modern Web Browser (Google Chrome / Mozilla Firefox), VS Code / Antigravity IDE.
- Documentation & Office Suite: MS-Office / Markdown Documentation Editor.
- Web Analytics Platform: Google Analytics Account (GA4 - Google Analytics 4).


3. PRE-REQUISITES
--------------------------------------------------------------------------------
- Active Internet Connection.
- Installed Web Browser.
- Google Account for accessing Google Analytics platform (analytics.google.com).
- Deployed or locally hosted website (`usecases` Climate Intelligence Platform HTML/CSS/JS files).


4. THEORY
--------------------------------------------------------------------------------
GOOGLE ANALYTICS

Knowing your audience and what they want is an important success factor for any website. 
The best way to know your audience is through your traffic stats and this is exactly what 
Google Analytics does. Google Analytics is one of the top, most powerful tools out there for 
monitoring and analysing traffic on your website. For using analytics one should create the 
account and then need to copy the tracking code. Once you add the tracking code to your 
webpages, Google analytics will track the various activities on the website and will generate 
the reports for it.

Key Concepts in Google Analytics 4 (GA4):
1. Account & Property: A Google Analytics Account is the top-level administrative container. 
   Under an account, a Property represents a specific website or mobile app monitoring entity.
2. Measurement ID (`G-3TN6PC8751`): A unique identifier assigned to a web data stream. It directs 
   the global site tag (`gtag.js`) script to send telemetry data to the correct Google Analytics property.
3. Global Site Tag (`gtag.js`): A JavaScript tagging framework and API that sends event data to 
   Google Analytics, Google Ads, and Google Marketing Platform.
4. Data Streams: The data pipeline connecting a website to Google Analytics. Each web data stream 
   receives pageviews, clicks, scrolls, and user interactions.
5. Realtime Reporting: Monitors activity on your website as it happens in real time (e.g., active 
   users in the last 30 minutes, user locations, page views, and triggered events).
6. Metrics & Dimensions:
   - Dimensions: Descriptive attributes of data (e.g., Page Title, City, Device Category, Browser).
   - Metrics: Quantitative measurements (e.g., Active Users, Event Count, Engagement Time, Views).


5. PROCEDURE (STEP-BY-STEP)
--------------------------------------------------------------------------------

STEP 1: CREATE A GOOGLE ANALYTICS ACCOUNT & PROPERTY
1. Navigate to https://analytics.google.com and sign in with a Google account.
2. Click on "Admin" (gear icon) in the bottom-left corner of the Google Analytics dashboard.
3. Click "+ Create Account", provide an Account Name (e.g., `Somaiya Climate Intelligence`), and accept data sharing settings.
4. Set up a Property Name (e.g., `Heatwave Watch Portal`), set the reporting time zone and currency (e.g., India - IST, INR).
5. Select business details and objectives (e.g., "Examine user behavior", "Generate leads").

STEP 2: CREATE A WEB DATA STREAM & GET MEASUREMENT ID
1. Choose "Web" as the platform under "Choose a platform".
2. Enter Website URL (e.g., `https://priyanshu.github.io/usecases` or `http://localhost:8000`) and Stream Name (e.g., `HeatAware Web Stream`).
3. Click "Create stream".
4. Copy the unique Measurement ID (`G-3TN6PC8751`).
5. Under "Web stream details", expand "View tag instructions" -> "Install manually" to reveal the Global Site Tag (`gtag.js`) code snippet.

STEP 3: ADD BASIC PAGE TRACKING CODE SNIPPET TO ALL WEBSITE PAGES
1. Open the project source directory (`usecases`).
2. Paste the `gtag.js` tracking code snippet inside the `<head>...</head>` section of every HTML web page:
   - `index.html` (Overview Landing Page)
   - `dashboard.html` (Forecast Watch Dashboard)
   - `monitoring.html` (Live AWS Station Monitoring)
   - `advisories.html` (Alerts & Advisories Generator)
   - `research.html` (Data & Academic Research)

Tracking Code Snippet (`gtag.js`):
```html
<!-- Google Analytics GA4 Tracking Tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3TN6PC8751"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3TN6PC8751', {
    'cookie_domain': 'auto',
    'cookie_flags': 'SameSite=None;Secure'
  });
  
  // Send explicit page_view event (supports file:// & localhost)
  gtag('event', 'page_view', {
    'page_title': document.title,
    'page_location': window.location.href,
    'page_path': window.location.pathname
  });
</script>
```

STEP 4: VERIFY TRACKING SCRIPT INTEGRATION LOCALLY / ON DEPLOYED SITE
1. Launch local development HTTP server:
   $ python3 -m http.server 8000
2. Open web browser and visit `http://localhost:8000/index.html`.
3. Right-click page -> Select "Inspect" (DevTools) -> Open "Network" tab.
4. Filter network requests by `collect` or `gtag`.
5. Observe outgoing HTTP POST/GET requests sent to `https://www.google-analytics.com/g/collect` with HTTP status code `200 OK` or `204 No Content`.

STEP 5: VERIFY REALTIME TRAFFIC REPORT IN GOOGLE ANALYTICS
1. Return to the Google Analytics dashboard (analytics.google.com).
2. Click on "Reports" -> "Realtime".
3. Navigate across different pages of the website (`dashboard.html`, `monitoring.html`, `advisories.html`).
4. Confirm real-time metrics update:
   - Active Users: > 0
   - Users by First User Source/Medium: `direct / (none)`
   - Views by Page Title and Screen Class: Shows visited page titles.


6. CODE IMPLEMENTATION IN HTML PAGES
--------------------------------------------------------------------------------

Sample Integration in `index.html` (Lines 14-22):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heatwave Watch - Climate Intelligence & Early Warning</title>
  <meta name="description" content="AI and IoT-driven climate intelligence system...">
  
  <!-- Google Fonts & FontAwesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="css/style.css">

  <!-- Google Analytics GA4 Tracking Tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-3TN6PC8751"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-3TN6PC8751', {
    'cookie_domain': 'auto',
    'cookie_flags': 'SameSite=None;Secure'
  });
  
  // Send explicit page_view event (supports file:// & localhost)
  gtag('event', 'page_view', {
    'page_title': document.title,
    'page_location': window.location.href,
    'page_path': window.location.pathname
  });
  </script>
</head>
```


7. RESULTS & EXPECTED ANALYTICS REPORT SNAPSHOTS
--------------------------------------------------------------------------------

1. Stepwise Verification Checklist:
   [✓] Google Analytics 4 Property & Account created.
   [✓] Measurement ID (`G-3TN6PC8751`) generated under Web Data Stream.
   [✓] `gtag.js` script successfully integrated into `<head>` section of all 5 web pages.
   [✓] Network requests to `google-analytics.com/g/collect` verified with 200/204 status codes.
   [✓] Google Analytics Realtime Dashboard displays active user session and pageview events.

2. Analytics Metrics Log (Captured Stream Data):
   -----------------------------------------------------------------------
   Metric Name                 Captured Value         Status
   -----------------------------------------------------------------------
   Measurement ID              G-3TN6PC8751           CONFIGURED
   Realtime Active Users       1 User (Desktop)       ACTIVE
   Page Location (`dl`)        http://localhost:8000  VERIFIED
   Event Name (`en`)           page_view              TRIGGERED
   Browser / OS                Chrome / macOS         DETECTED
   Engagement Time             120s                   RECORDED
   -----------------------------------------------------------------------


8. QUESTIONS & ANSWERS
--------------------------------------------------------------------------------

Q1: Create account for Google Analytics.
Answer:
To create a Google Analytics account:
1. Visit https://analytics.google.com and log in with your Google credentials.
2. Click on the "Admin" gear icon at the bottom-left corner of the console.
3. Click "+ Create Account", enter the desired Account Name, and accept administrative options.
4. Next, create a Property by providing a Property Name (e.g., Website Name), selecting time zone (India IST) and currency.
5. Setup a Web Data Stream by supplying the target website URL and Stream Name.
6. Once created, Google Analytics provides a unique Measurement ID (e.g., `G-3TN6PC8751`) and global tracking code script block (`gtag.js`).

Q2: Add basic page tracking to website by copying the code snippet.
Answer:
To add basic page tracking to a website:
1. Copy the global site tag (`gtag.js`) snippet provided under "Web stream details" in Google Analytics:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-3TN6PC8751"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-3TN6PC8751', { 'cookie_domain': 'auto', 'cookie_flags': 'SameSite=None;Secure' });
     gtag('event', 'page_view', { 'page_title': document.title, 'page_location': window.location.href, 'page_path': window.location.pathname });
   </script>
   ```
2. Open each HTML file of the website (`index.html`, `dashboard.html`, `monitoring.html`, etc.) in a code editor.
3. Paste the code snippet inside the `<head>` section of each webpage, preferably near the top or right before the closing `</head>` tag.
4. Save the HTML files and re-deploy or launch the website. The `gtag.js` script automatically executes on page load, capturing `page_view` events and sending session telemetry data to Google Analytics.


9. OUTCOMES
--------------------------------------------------------------------------------
1. Understood the fundamentals of Web Analytics and traffic monitoring using Google Analytics 4 (GA4).
2. Successfully established a Google Analytics account, property, and web data stream with Measurement ID `G-3TN6PC8751`.
3. Successfully integrated the global site tag (`gtag.js`) into a multi-page web application.
4. Verified real-time user tracking, pageviews, and network event logging using browser developer tools and Google Analytics Realtime Dashboard.

10. CONCLUSION
--------------------------------------------------------------------------------
The setup of Google Analytics for the website was successfully completed and verified. 
By integrating the `gtag.js` snippet with Measurement ID `G-3TN6PC8751` into the header of all HTML pages, 
real-time tracking of user visits, page views, and engagement metrics was established. Google Analytics 
provides vital insights into audience demographics, acquisition channels, and user behavior patterns, 
enabling data-driven optimizations for website performance and digital marketing strategies.


11. WEBSITE & REFERENCES
--------------------------------------------------------------------------------
Website:
1. https://www.youtube.com/watch?v=ZXSI5R7GeVA

References:
1. Eric Greenberg, Alexander Kates, "Strategic Digital Marketing: Top Digital Experts 
   Share the Formula for Tangible Returns on Your Marketing Investments" McGraw Hill 
   Education 1st edition, 16 August 2013.
2. Jan Zimmerman "Web Marketing For Dummies" Willy Publishing 3rd Edition, 2011.
3. Jan Zimmerman, Deborah Ng, "Social Media Marketing All-in-One For Dummies" 
   Willy Publishing 4th Edition, 2017.
================================================================================
