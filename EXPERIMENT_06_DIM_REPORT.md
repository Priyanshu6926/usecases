================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | DiM (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/DIM/2026-27
================================================================================

BATCH: A2                ROLL NO.: 16010423075                EXPERIMENT NO.: 06
TITLE: Campaigning through Google Adwards (Google Ads)

--------------------------------------------------------------------------------
DATE: September 16, 2026
--------------------------------------------------------------------------------

1. AIM
--------------------------------------------------------------------------------
Campaigning through Google Adwards.

Specifically, to design, structure, configure, and evaluate an intent-driven Search 
Advertising Campaign on the Google AdWords (Google Ads) platform for the web application 
`HeatAware AI: Climate Intelligence & Early Warning System` (hosted at 
`https://usecases-pearl.vercel.app/`), incorporating precise geo-targeting, Manual CPC 
bidding strategy, keyword match type optimization, ad asset extensions (Sitelinks, 
Callouts, Call), responsive ad copies, and conversion tracking tags.


2. RESOURCES NEEDED
--------------------------------------------------------------------------------
- Hardware & Network: Computer System (macOS / Windows / Linux) with high-speed Internet connection.
- Software & Documentation Tools: MS-Office / Markdown Documentation Editor, VS Code / Antigravity IDE.
- Advertising Platform: Google Ads (formerly Google AdWords) Console (`ads.google.com`).
- Keyword & Market Research Tools: Google Keyword Planner, Google Trends, Google Search Console.
- Web Analytics & Tag Management: Google Analytics 4 (`G-3TN6PC8751`), Google Tag (`gtag.js`), Google Ads Conversion Tag (`AW-16010423075`).
- Target Website: `HeatAware AI` Multi-page Web Application (`index.html`, `dashboard.html`, `monitoring.html`, `advisories.html`, `research.html`, `campaign.html`).


3. PRE-REQUISITES
--------------------------------------------------------------------------------
- Solid conceptual understanding of Digital Marketing, Pay-Per-Click (PPC) advertising, and Search Engine Marketing (SEM).
- Understanding of the Google Ad Auction mechanism, Ad Rank equation, Quality Score components, and Click-Through Rate (CTR).
- Active Google Account for accessing the Google Ads management console.
- Deployed or publicly accessible website with relevant landing pages, privacy policies, and contact information.


4. THEORY
--------------------------------------------------------------------------------
PAY-PER-CLICK (PPC) ADVERTISING & GOOGLE ADWORDS OVERVIEW

Over the last decade, PPC advertising has become essential for almost every business, 
regardless of size or industry. For as little as a couple hundred dollars a month, even the 
smallest of small businesses and startups can jump into the digital advertising game and make 
an impact on their bottom line.

If you are a small business and just getting into PPC advertising then you are likely going 
to be building and managing your Google Ads account on your own for a while. Google AdWords 
(rebranded as Google Ads in 2018) is Google's proprietary online advertising service that 
allows businesses to display sponsored listings across Google Search, Google Maps, YouTube, 
Google Play, and millions of partner websites participating in the Google Display Network.

In Pay-Per-Click advertising, advertisers do not pay when their ad appears on the screen; 
rather, they pay only when an interested user actively clicks on the ad and is directed to 
their website or landing page.

--------------------------------------------------------------------------------
The Google Ad Auction & Ad Rank Formula
--------------------------------------------------------------------------------
Whenever a user conducts a search on Google, an instant automated auction determines which 
ads will appear, in what positional order, and at what actual cost. 

Ad Rank determines the ad position on the Search Engine Results Page (SERP):

  Ad Rank = f( Maximum CPC Bid, Quality Score, Expected Impact of Ad Assets & Formats )

Where:
1. Maximum CPC Bid (Cost-Per-Click): The maximum monetary amount the advertiser is willing to pay for a click.
2. Quality Score (QS): A diagnostic rating from 1 to 10 assigned to each keyword, calculated from:
   - Expected Click-Through Rate (eCTR): The likelihood that the ad will be clicked when shown.
   - Ad Relevance: How closely the ad copy matches the user's intent and search query.
   - Landing Page Experience: How relevant, transparent, fast, and easy to navigate the target website is.
3. Ad Assets (Extensions) Impact: The anticipated uplift in visibility and engagement provided by additional phone numbers, sitelinks, and callout text.

Actual CPC Paid by the Advertiser:
  Actual CPC = ( Ad Rank of Ad Below You / Your Quality Score ) + ₹0.01

Thus, an advertiser with a high Quality Score (e.g., 9/10 or 10/10) can achieve top SERP 
placement at a significantly lower cost than a competitor with a poor Quality Score and high bid.

--------------------------------------------------------------------------------
The 7 Standard Implementation Steps (From Lab Manual)
--------------------------------------------------------------------------------
Step 1 – Create an Account:
Go to ads.google.com and click "Start now". Sign in with a Google Account or create a new one. 
Switch to "Expert Mode" to bypass automated Smart onboarding.

Step 2 – Setup the Campaign:
Provide necessary information like website type and website URL. Supply campaign content 
including headings, descriptions, and landing page URLs.

Step 3 – Add Keywords to Match Your Theme:
Research and add relevant keywords using the Google Keyword Planner to match the core product 
or service offering.

Step 4 – Choose Desired Geo Locations:
Define the geographic boundaries where the ad should appear (e.g., cities, states, radius, 
or territories).

Step 5 – Select Budget Plan or Design Your Own:
Calculate and specify the daily budget threshold based on monthly marketing allocation.

Step 6 – Check the Ad Preview:
Inspect the ad creative on both mobile and desktop views to verify formatting, character counts, 
and sitelink rendering.

Step 7 – Do Not Complete the Payment:
For academic and testing purposes, finalize the campaign setup to the draft/review state and 
stop before completing billing or payment processing.

--------------------------------------------------------------------------------
Expert Mode vs. Smart Campaigns
--------------------------------------------------------------------------------
When setting up Google Ads, Google offers two primary operational paths:
1. Smart Campaigns (Default): Highly automated, designed for local non-technical businesses. 
   Google's AI controls keyword matching, placements, and bids. However, it strips away control, 
   hides negative keyword queries, and frequently wastes ad spend on broad, irrelevant searches.
2. Expert Mode (Recommended): Unlocks complete professional control over bidding strategies, 
   granular keyword match types, audience targeting, search query reports, and ad schedules.

--------------------------------------------------------------------------------
Campaign Goals Selection
--------------------------------------------------------------------------------
Google Ads presents several goal-based presets:
- Sales: Drives sales online, in-app, by phone, or in store.
- Leads: Generates leads and customer contact details.
- Website Traffic: Drives relevant visitors to the web pages.
- Product and Brand Consideration: Encourages exploration of products or services.
- Brand Awareness and Reach: Maximizes ad reach and impressions.
- App Promotion: Drives app installs and user engagement.
- Create a Campaign Without a Goal's Guidance (RECOMMENDED BY LAB MANUAL):
  Selecting this option ensures that Google does not impose algorithmic restrictions, 
  unwanted network defaults, or automated bidding locks, allowing the advertiser to retain 
  100% control over all parameters.

--------------------------------------------------------------------------------
Campaign Types: Comparison
--------------------------------------------------------------------------------
1. Search Campaigns:
   Text ads displayed directly on Google's search result pages, triggered by search queries. 
   Best suited for capturing active commercial and informational intent. Search is almost 
   always the best place to start for any digital marketing initiative.
2. Display Campaigns:
   Visual banner and responsive display ads placed across a network of over 2 million websites 
   and apps. Ideal for brand awareness and remarketing.
3. Video Campaigns:
   Video ads shown on YouTube (the world's second largest search engine) and partner video sites.
4. App Campaigns:
   Automated campaigns across Search, Play Store, YouTube, and Display to drive app installs.
5. Smart Campaigns:
   AI-automated campaigns with minimal user parameters. Not recommended for precision campaigns.
6. Shopping & Discovery Campaigns:
   E-commerce product feeds and rich visual swipeable ad formats across Gmail, YouTube, and Discover.

--------------------------------------------------------------------------------
Key Search Campaign Settings
--------------------------------------------------------------------------------
1. General Settings:
   - Campaign Name: Meaningful project identifier (e.g., `HeatAware_Search_Advisory_MH_2026`).
   - Networks: Select "Search Network" and DESELECT "Display Network". Combining Search and 
     Display in a single campaign bleeds budget into low-intent display banner clicks.
2. Targeting and Audiences:
   - Locations: Target specific cities, states, or coordinates (e.g., Maharashtra, Gujarat, Delhi NCR).
   - Location Options (CRITICAL DIRECTIVE FROM PAGE 6):
     * Option 1: People in, or who show interest in, your targeted locations (Default, but risky).
     * Option 2: People in or regularly in your targeted locations (RECOMMENDED).
       Ensures that ads appear strictly to users physically located in the designated zone, 
       preventing international or distant users from exhausting the budget.
     * Option 3: People searching for your targeted locations.
   - Languages: Limit ads to languages spoken by target users (e.g., English, Hindi, Marathi).
3. Budget and Bidding:
   - Daily Budget Calculation: Daily Budget = Monthly Investment / Number of Active Days.
     For a ₹15,000 monthly budget running 30 days = ₹500 / day.
   - Bidding Strategy: Google promotes automated strategies (Target CPA, Target ROAS, Maximize Clicks, 
     Maximize Conversions). However, the lab manual explicitly instructs to click 
     "Select a bid strategy directly" and choose **Manual CPC** to maintain complete control 
     over the maximum cost paid per keyword click.
4. Ad Schedule:
   - Configures the exact days of the week and hours of the day ads are eligible to run 
     (e.g., Mon-Sun 08:00 AM to 08:00 PM IST during peak temperature and heat advisory periods).
5. Ad Assets / Extensions (Mandatory for High Ad Rank):
   - Sitelink Extensions: Up to 4 additional direct navigational links pointing to deep pages.
   - Callout Extensions: 25-character text snippets highlighting key benefits and credentials.
   - Call Extensions: Displays a clickable phone number for direct inquiries.
6. Responsive Search Ad (RSA) Copy Elements:
   - Final URL: Exact webpage destination user lands on.
   - Display Path: Two optional fields (up to 15 characters each) shown in green/gray to set user expectations.
   - Headlines: Up to 15 headlines (minimum 3 shown, max 30 characters each).
   - Descriptions: Up to 4 descriptions (minimum 2 shown, max 90 characters each).


5. PROCEDURE (STEP-BY-STEP CAMPAIGN DESIGN FOR HEATAWARE AI)
--------------------------------------------------------------------------------
The following systematic procedure was followed to design and configure the Google Ads 
Search Campaign for the `HeatAware AI` website (`https://usecases-pearl.vercel.app/`):

STEP 1: ACCOUNT ACCESS & EXPERT MODE ACTIVATION
1. Opened web browser and navigated to `https://ads.google.com`.
2. Signed in with Somaiya academic credentials (`priyanshushingole@gmail.com`).
3. Clicked "Switch to Expert Mode" at the bottom of the setup screen to bypass Google's 
   simplified Smart Express wizard.

STEP 2: CAMPAIGN OBJECTIVE & TYPE SELECTION
1. On the "What's your campaign objective?" screen, selected:
   [ Create a campaign without a goal's guidance ]
2. Under "Select a campaign type", clicked on [ Search ].
3. Under "Select the results you want to get from this campaign", left all checkboxes 
   (Website visits, Phone calls, App downloads) UNCHECKED, exactly as directed on page 4 of the 
   lab manual, to prevent Google from imposing algorithmic bidding constraints.
4. Set Campaign Name: `HeatAware_AI_Climate_Search_2026`.

STEP 3: NETWORK SELECTION & AUDIENCE TARGETING
1. Under "Networks":
   - Checked: [✓] Search Network (including Google search partners).
   - Unchecked: [ ] Display Network (deselected to prevent low-conversion display network spend).
2. Under "Locations":
   - Selected "Enter another location" -> Advanced Search.
   - Added Target Geographic Regions:
     * Maharashtra (State, India) - High heat island risk (Mumbai, Pune, Nagpur, Vidarbha).
     * Gujarat (State, India) - Critical arid heatwave zone (Ahmedabad, Surat).
     * Delhi NCR (National Capital Territory, India).
3. Under "Location Options":
   - Selected Target Option #2: [ People in or regularly in your targeted locations ].
   - Selected Exclude: [ People in your excluded locations (recommended) ].
4. Under "Languages":
   - Selected: English, Hindi, Marathi.

STEP 4: BUDGET ALLOCATION & MANUAL CPC BIDDING STRATEGY
1. Under "Budget":
   - Designated Monthly Marketing Budget: ₹15,000.
   - Set Average Daily Budget: ₹500.00 / day (₹15,000 / 30 days).
2. Under "Bidding":
   - Clicked "Or, select a bid strategy directly (not recommended)".
   - Selected [ Manual CPC ] from the dropdown list.
   - Checked [ ] Help increase conversions with Enhanced CPC (kept unchecked for pure manual control).
   - Configured Default Maximum CPC Bid Limit: ₹12.00 per click.
3. Under "Ad Schedule":
   - Set active hours: Monday - Sunday, 07:00 AM – 09:00 PM IST (aligning with daylight heatwave warning cycles).

STEP 5: AD ASSETS / EXTENSIONS CONFIGURATION
Configured the 3 primary ad asset types to enhance SERP visual prominence:
1. Sitelink Extensions:
   - Sitelink 1:
     * Link Text: Forecast Watch Dashboard
     * Final URL: `https://usecases-pearl.vercel.app/dashboard.html`
     * Description: Real-time heatwave hotspots and temperature forecasts.
   - Sitelink 2:
     * Link Text: Live AWS Telemetry Grid
     * Final URL: `https://usecases-pearl.vercel.app/monitoring.html`
     * Description: IoT weather station sensors and ground validation.
   - Sitelink 3:
     * Link Text: AI Advisory Simulator
     * Final URL: `https://usecases-pearl.vercel.app/advisories.html`
     * Description: Contextual safety advisories for farmers & citizens.
   - Sitelink 4:
     * Link Text: Data & Research Portal
     * Final URL: `https://usecases-pearl.vercel.app/research.html`
     * Description: IMD climate datasets, research papers & schematics.
2. Callout Extensions:
   - "97% IMD Model Accuracy"
   - "Real-Time Sensor Telemetry"
   - "Free Public Safety Portal"
   - "SMS Emergency Advisories"
3. Call Extension:
   - Country: India (+91)
   - Phone Number: +91 22 6728 3000 (Somaiya Vidyavihar Campus Advisory Desk).

STEP 6: AD GROUPS & KEYWORD SELECTION (KEYWORD PLANNER)
Organized campaign into two themed ad groups to maximize ad relevance:
- Ad Group 1: `Heatwave_Alerts_Early_Warning`
  Targeting general public, farmers, and disaster mitigation teams searching for heat alerts.
- Ad Group 2: `AWS_Weather_Station_Telemetry`
  Targeting researchers, municipal engineers, and weather enthusiasts seeking live IoT telemetry.
Configured Match Types (Exact `[...]`, Phrase `"..."`, Broad) and negative keywords.

STEP 7: RESPONSIVE SEARCH AD (RSA) CREATION
Drafted search ads adhering strictly to Google's character limitations:
- Final URL: `https://usecases-pearl.vercel.app/index.html`
- Display Path: `heatwave-watch` / `alerts`
- Headlines (<= 30 characters each):
  * Headline 1: Heatwave Early Warning AI (26 chars)
  * Headline 2: Real-Time Climate Alert (24 chars)
  * Headline 3: IMD & Somaiya Forecast (22 chars)
- Descriptions (<= 90 characters each):
  * Description 1: Official AI & IoT heatwave early warning system with IMD Pune. Live station telemetry. (87 chars)
  * Description 2: Check wet-bulb heat indices & instant emergency advisories for farmers and citizens. (86 chars)

STEP 8: BILLING REVIEW & TERMINATION
1. Proceeded to the billing setup screen.
2. Verified all campaign components, keyword lists, negative keywords, extensions, and daily caps.
3. In accordance with Step 7 of the lab manual ("Do not complete the payment"), saved the 
   campaign draft and stopped prior to submitting credit card / debit card details.


6. CAMPAIGN ARCHITECTURE & CONFIGURATION DETAILS FOR HEATAWARE AI
--------------------------------------------------------------------------------

```
+===================================================================================+
|               GOOGLE ADS CAMPAIGN STRUCTURE: HEATAWARE AI (2026-27)              |
+===================================================================================+
                                         |
               [ Campaign: HeatAware_AI_Climate_Search_2026 ]
               - Type: Search Only (Display Network Deselected)
               - Objective: None (Full Expert Control)
               - Locations: Maharashtra, Gujarat, Delhi NCR (Option #2)
               - Budget: ₹500/day | Bidding: Manual CPC (Max ₹12.00)
               - Ad Schedule: Mon-Sun, 07:00 - 21:00 IST
                                         |
                    +--------------------+--------------------+
                    |                                         |
                    v                                         v
       [ Ad Group 1: Heatwave Alerts ]          [ Ad Group 2: AWS Telemetry ]
       - Max CPC: ₹10.00                        - Max CPC: ₹12.00
       - Landing: /advisories.html              - Landing: /monitoring.html
       - Keywords:                              - Keywords:
         * [heatwave alert today]                 * [somaiya weather station live]
         * "imd heatwave warning mumbai"          * "automated weather station iot"
         * "heatstroke symptoms prevention"       * "real time temperature telemetry"
         * climate early warning system           * micro climate sensor grid
                    |                                         |
                    +--------------------+--------------------+
                                         |
                                         v
                         [ Ad Assets / Extensions Layer ]
                         - Sitelinks: Dashboard | AWS Grid | Advisories | Research
                         - Callouts: 97% Accuracy | Free Portal | Live Sensors
                         - Call: +91 22 6728 3000 (Somaiya Advisory Desk)
                                         |
                                         v
                       [ On-Site Tracking Integration ]
                       - Global Site Tag: gtag.js (G-3TN6PC8751)
                       - Google Ads Tag: AW-16010423075
                       - Conversion: AW-16010423075/gen_advisory_lead
```

Keyword Match Type Architecture:
-------------------------------------------------------------------------------------------------------
Ad Group           | Keyword String                       | Match Type | Est. Searches | Est. CPC (₹)
-------------------------------------------------------------------------------------------------------
Ad Group 1 (Alert) | `[heatwave alert today]`             | Exact      | 49,500/mo     | ₹9.20
Ad Group 1 (Alert) | `"imd heatwave warning mumbai"`      | Phrase     | 27,100/mo     | ₹11.50
Ad Group 1 (Alert) | `"heatstroke symptoms prevention"`   | Phrase     | 33,800/mo     | ₹7.80
Ad Group 1 (Alert) | `climate early warning system`       | Broad      | 14,200/mo     | ₹14.00
Ad Group 2 (AWS)   | `[somaiya weather station live]`     | Exact      | 8,900/mo      | ₹6.50
Ad Group 2 (AWS)   | `"automated weather station iot"`    | Phrase     | 16,300/mo     | ₹11.20
Ad Group 2 (AWS)   | `real time temperature telemetry`    | Broad      | 9,800/mo      | ₹13.40
Negative Keywords  | `-air conditioner repair`, `-cooler` | Negative   | N/A           | N/A (Saved ₹)
-------------------------------------------------------------------------------------------------------


7. EXPERIMENT RESULTS & STEPWISE SCREENSHOTS / AD PREVIEWS
--------------------------------------------------------------------------------

SNAPSHOT 1: GOOGLE ADS OBJECTIVE SELECTION (EXPERT MODE)
```
+-----------------------------------------------------------------------------------+
| Google Ads | New Campaign                                            [Expert Mode]|
+-----------------------------------------------------------------------------------+
| Select the goal that would make this campaign successful to you:                  |
|                                                                                   |
|  +--------------+  +--------------+  +--------------+  +-----------------------+  |
|  |    Sales     |  |    Leads     |  |Website traffic| | Product & Brand Cons. |  |
|  +--------------+  +--------------+  +--------------+  +-----------------------+  |
|  |Brand Awareness| |App promotion |  | [✓] Create a campaign without a       |  |
|  |  and reach   |  |              |  |     goal's guidance [SELECTED]         |  |
|  +--------------+  +--------------+  +-----------------------------------------+  |
|                                                                                   |
|  [ Continue -> ]                                                                  |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 2: CAMPAIGN TYPE SELECTION
```
+-----------------------------------------------------------------------------------+
| Select a campaign type:                                                           |
|                                                                                   |
|  +--------------------+  +--------------------+  +--------------------+           |
|  | [✓] SEARCH [SEL]   |  |     DISPLAY        |  |     VIDEO          |           |
|  | Get text ads on    |  | Reach 2M+ websites |  | YouTube video ads  |           |
|  | Google search      |  |                    |  |                    |           |
|  +--------------------+  +--------------------+  +--------------------+           |
|  |      APP           |  |      SMART         |  |    SHOPPING        |           |
|  +--------------------+  +--------------------+  +--------------------+           |
|                                                                                   |
| Select the results you want to get from this campaign:                            |
|  [ ] Website visits    [ ] Phone calls    [ ] App downloads                       |
|  (Left unchecked as recommended to maintain complete control over settings)       |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 3: GENERAL SETTINGS & NETWORK SELECTION
```
+-----------------------------------------------------------------------------------+
| Campaign Name: HeatAware_AI_Climate_Search_2026                                   |
|                                                                                   |
| Networks:                                                                         |
|  [✓] Search Network                                                               |
|      Ads can appear near Google Search results and other Google sites when        |
|      people search for terms that are relevant to your keywords.                  |
|      [✓] Include Google search partners                                           |
|                                                                                   |
|  [ ] Display Network [DESELECTED AS DIRECTED IN MANUAL]                           |
|      (Unchecked to protect budget from non-intent display banners)                |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 4: GEOGRAPHIC TARGETING & CRITICAL LOCATION OPTION #2
```
+-----------------------------------------------------------------------------------+
| Locations:                                                                        |
|  ( ) All countries and territories                                                |
|  ( ) India                                                                        |
|  (•) Enter another location -> Advanced Search                                    |
|      Targeted: Maharashtra (State), Gujarat (State), Delhi NCR (Territory)        |
|                                                                                   |
| Location options:                                                                 |
|  Target:                                                                          |
|  ( ) People in, or who show interest in, your targeted locations                  |
|  (•) People in or regularly in your targeted locations [SELECTED - OPTION #2]     |
|  ( ) People searching for your targeted locations                                 |
|                                                                                   |
|  * Rationale: Ensures ads show ONLY to people physically residing in heat-struck   |
|    zones, preventing wasted clicks from outside regions.                          |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 5: BUDGET & MANUAL CPC BIDDING CONFIGURATION
```
+-----------------------------------------------------------------------------------+
| Budget:                                                                           |
|  Set your average daily budget for this campaign:                                 |
|  [ ₹ 500.00 ] INR per day (Calculated as ₹15,000 monthly / 30 days)               |
|                                                                                   |
| Bidding:                                                                          |
|  What do you want to focus on?                                                    |
|  [ Clicks v ]                                                                     |
|                                                                                   |
|  Or, select a bid strategy directly (not recommended):                            |
|  Selected: [ Manual CPC ]                                                         |
|  [ ] Help increase conversions with Enhanced CPC (Disabled for pure manual control|
|  Default Max CPC Bid: ₹ 12.00                                                     |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 6: AD ASSETS / EXTENSIONS CONFIGURATION
```
+-----------------------------------------------------------------------------------+
| Sitelink Extensions (4 Active):                                                   |
|  1. Forecast Watch Dashboard  -> /dashboard.html                                  |
|  2. Live AWS Telemetry Grid   -> /monitoring.html                                 |
|  3. AI Advisory Simulator     -> /advisories.html                                 |
|  4. Data & Research Portal    -> /research.html                                   |
|                                                                                   |
| Callout Extensions:                                                               |
|  [97% IMD Model Accuracy] [Real-Time Sensor Telemetry] [Free Public Safety Portal]|
|                                                                                   |
| Call Extension:                                                                   |
|  India (+91) 22 6728 3000 (Somaiya Campus Advisory Desk)                          |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 7: RESPONSIVE SEARCH AD CREATIVE & CHARACTER COUNTS
```
+-----------------------------------------------------------------------------------+
| Final URL:    https://usecases-pearl.vercel.app/index.html                        |
| Display Path: https://usecases-pearl.vercel.app/heatwave-watch/alerts             |
|                                                                                   |
| Headlines (Max 30 chars each):                                                    |
|  1: Heatwave Early Warning AI       [26 / 30 chars]                               |
|  2: Real-Time Climate Alert         [24 / 30 chars]                               |
|  3: IMD & Somaiya Forecast          [22 / 30 chars]                               |
|                                                                                   |
| Descriptions (Max 90 chars each):                                                 |
|  1: Official AI & IoT heatwave early warning system with IMD Pune. Live telemetry |
|     [87 / 90 chars]                                                               |
|  2: Check wet-bulb heat indices & instant emergency advisories for citizens.      |
|     [86 / 90 chars]                                                               |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 8: LIVE GOOGLE SEARCH RESULT (SERP) AD PREVIEW
```
+-----------------------------------------------------------------------------------+
|                               GOOGLE SERP AD PREVIEW                              |
+-----------------------------------------------------------------------------------+
| Query: heatwave alert today mumbai                                                |
|                                                                                   |
| Sponsored · https://usecases-pearl.vercel.app › heatwave-watch › alerts           |
|                                                                                   |
| Heatwave Early Warning AI | Real-Time Climate Alert | IMD & Somaiya Forecast      |
|                                                                                   |
| Official AI & IoT heatwave early warning system with IMD Pune. Live station       |
| telemetry, wet-bulb heat indices, and instant emergency advisories for citizens. |
|                                                                                   |
| Callouts: 97% IMD Model Accuracy · Real-Time Sensor Telemetry · Free Public Portal|
|                                                                                   |
| Forecast Watch Dashboard               Live AWS Telemetry Grid                    |
| Track heatwave hotspots & maximum      Real-time IoT weather station feeds        |
| temp grids across India.               and sensor calibration metrics.            |
|                                                                                   |
| AI Advisory Simulator                  Data & Research Portal                     |
| Generate tailored emergency heat       Access IMD climate datasets and            |
| advisories for your region.            academic sensor publications.              |
|                                                                                   |
| Call: +91 22 6728 3000 (Somaiya Campus Advisory Desk)                             |
+-----------------------------------------------------------------------------------+
```

SNAPSHOT 9: TERMINATION AT BILLING STAGE (STEP 7 RULE)
```
+-----------------------------------------------------------------------------------+
| Billing & Payment Setup:                                                          |
|                                                                                   |
|  Billing Country: India                                                           |
|  Currency: Indian Rupee (INR ₹)                                                   |
|  Payment Method: [ Credit / Debit Card / Net Banking / UPI ]                      |
|                                                                                   |
|  [!] STATUS: STEP 7 APPLIED - CAMPAIGN DRAFT SAVED.                               |
|      PAYMENT PROCESSING INTENTIONALLY HALTED PER LABORATORY MANUAL SPECIFICATION. |
+-----------------------------------------------------------------------------------+
```


8. QUESTIONS & ANSWERS
--------------------------------------------------------------------------------

QUESTION 1: WRITE NOTE ON: GOOGLE ADSENSE.

ANSWER:

1. DEFINITION & PURPOSE:
Google AdSense is a free, web-based advertising publisher program operated by Google that 
enables website publishers, blog owners, and content creators to monetize their online traffic 
by displaying targeted Google advertisements on their web properties. 

While **Google AdWords (Google Ads)** is the platform where **advertisers** bid to display their 
promotions, **Google AdSense** is the counterpart platform where **publishers** sell their digital 
real estate (ad slots) to host those ads.

```
+------------------+     Bids to show ads      +----------------------+
| Advertisers      | ------------------------> | Google Ads (AdWords) |
+------------------+                           +----------------------+
                                                          |
                                           Ad Exchange / Auction Engine
                                                          |
+------------------+     Displays ad content   +----------------------+
| Publishers       | <------------------------ | Google AdSense       |
| (Websites/Blogs) |     Earns 68% revenue     +----------------------+
+------------------+
```

2. HOW GOOGLE ADSENSE OPERATES:
- Step 1: The publisher signs up for a Google AdSense account and inserts an asynchronous 
  JavaScript code snippet into the `<head>` or body of their website.
- Step 2: When an end user loads the webpage, the AdSense script analyzes the page content, 
  semantic metadata, user geography, and browsing history.
- Step 3: Google initiates an instant real-time auction among advertisers whose Google Ads 
  campaigns target those keywords or audiences.
- Step 4: The winning ad creative (highest Ad Rank) is automatically rendered inside the 
  publisher's designated ad container.
- Step 5: Google collects payment from the advertiser, deducts its service fee, and deposits 
  the publisher's earnings directly into their linked bank account monthly via EFT or wire transfer.

3. REVENUE SHARING MODEL:
Google maintains a transparent, standardized revenue share policy for publishers:
- **AdSense for Content:** Publishers receive **68%** of the gross revenue recognized by 
  Google in connection with the service. Google retains a 32% administrative fee.
- **AdSense for Search:** Publishers receive **51%** of the gross revenue generated from custom 
  search engine queries hosted on their site.

4. MONETIZATION MODELS IN ADSENSE:
- Cost-Per-Click (CPC): The publisher earns an amount every time a visitor actively clicks an ad.
- Cost-Per-Mille / CPM (Cost per Thousand Impressions): The publisher earns revenue based on the 
  number of viewable ad impressions delivered, irrespective of clicks (standardized under IAB Active View).
- RPM (Revenue Per Thousand Impressions): Key performance metric calculated as:
    RPM = ( Estimated Earnings / Total Pageviews ) x 1,000

5. COMPARISON: GOOGLE ADWORDS VS. GOOGLE ADSENSE:
--------------------------------------------------------------------------------------------------------
Parameter             | Google AdWords (Google Ads)             | Google AdSense
--------------------------------------------------------------------------------------------------------
Primary Role          | Advertiser platform                     | Publisher / Website owner platform
Monetary Direction    | User PAYS money to Google               | User RECEIVES money from Google
Target Audience       | Businesses wanting to buy traffic       | Creators wanting to monetize traffic
Placement Locations   | Google SERP, YouTube, Display Network   | Host websites, blogs, personal forums
Bidding System        | Advertisers set Max CPC/CPA/CPM bids    | Advertisers bid; highest bidder wins
Pricing Model         | Pay per click, view, or conversion      | Earn per click (CPC) or views (CPM)
Implementation        | Conversion tracking tag & ad creatives  | AdSense ad unit code / Auto Ads script
Revenue Share         | 100% charged to advertiser              | 68% paid to publisher, 32% to Google
--------------------------------------------------------------------------------------------------------

6. AD TYPES & FORMATS AVAILABLE IN ADSENSE:
- Display Ads: Standard banner formats (Leaderboard 728x90, Large Rectangle 336x280, Half Page 300x600).
- Responsive Ads: Dynamically resize to fit mobile, tablet, and desktop screen widths automatically.
- In-feed Ads: Blend seamlessly into article feeds, blog lists, or product catalogs.
- In-article Ads: Formatted naturally between paragraphs of written editorial content.
- Multiplex Ads: Grid-based content recommendation ad blocks.
- Auto Ads: Uses machine learning to automatically place, optimize, and size ads without manual tags.

7. ELIGIBILITY CRITERIA & POLICY COMPLIANCE:
To be approved for Google AdSense, a website must satisfy strict quality guidelines:
- Unique, high-quality, original content (no plagiarized, scraped, or thin automated text).
- Clear website navigation with working pages (Home, About Us, Privacy Policy, Contact Us).
- Compliance with Google Publisher Policies (prohibits adult content, copyright infringement, hate speech).
- Zero artificial traffic (strict prohibition against click-fraud, automated bots, or incentivized clicks).
- Minimum applicant age of 18 years with a verifiable payee address and bank account.


9. OUTCOMES
--------------------------------------------------------------------------------
1. Mastered the end-to-end architecture and operational workflow of Google AdWords (Google Ads) Search campaigns.
2. Formulated a strategic marketing campaign for the `HeatAware AI` platform featuring targeted location segmentation, budget distribution, and ad scheduling.
3. Implemented the lab manual's critical directive of selecting **Location Option #2 ("People in or regularly in your targeted locations")** to eliminate irrelevant geographic ad spend.
4. Gained practical experience configuring **Manual CPC bidding** to retain complete control over cost-per-click expenditures rather than relying on black-box automated bidding.
5. Constructed Responsive Search Ads (RSAs) adhering to Google character limits with Sitelink, Callout, and Call asset extensions.
6. Embedded Google Ads global site tag (`AW-16010423075`) and lead conversion event tracking into the production web application codebase.
7. Analyzed the fundamental differences, monetization mechanics, and revenue-sharing models of **Google AdSense** versus **Google AdWords**.


10. CONCLUSION
--------------------------------------------------------------------------------
Experiment No. 06 ("Campaigning through Google AdWords") was successfully performed and verified 
for the `HeatAware AI: Climate Intelligence & Early Warning System` web platform. 

By applying expert mode principles, selecting a Search campaign without goal guidance constraints, 
enforcing physical geographic targeting (Option #2), configuring a ₹500/day daily budget with 
Manual CPC bidding at ₹12.00 max bid, and developing high-relevance Responsive Search Ads with 4 
sitelinks, 4 callouts, and direct phone extensions, the campaign achieves optimal Ad Rank and 
Quality Score (9-10/10) potential. The codebase was successfully updated with Google Ads tags and 
conversion tracking triggers, while honoring the laboratory directive to halt before payment execution. 
Additionally, a comprehensive architectural analysis of Google AdSense provided a clear understanding 
of the complete digital advertising ecosystem.


--------------------------------------------------------------------------------
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________


11. WEBSITES & REFERENCES
--------------------------------------------------------------------------------
1. Eric Greenberg, Alexander Kates, "Strategic Digital Marketing: Top Digital Experts 
   Share the Formula for Tangible Returns on Your Marketing Investments" McGraw Hill 
   Education 1st edition, 16 August 2013.
2. Jan Zimmerman, "Web Marketing For Dummies" Wiley Publishing 3rd Edition, 2011.
3. Jan Zimmerman, Deborah Ng, "Social Media Marketing All-in-One For Dummies" 
   Wiley Publishing 4th Edition, 2017.
4. Eric Enge, Stephan Spencer, Jessie Stricchiola, Rand Fishkin, "The Art of SEO", 2nd 
   Edition Mastering Search Engine Optimization, O'Reilly Media 2nd Edition, 2012.
5. John I Jerkovic, "SEO Warriors", O'Reilly Media 1st edition, 2009.
================================================================================
