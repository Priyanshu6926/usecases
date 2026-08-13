================================================================================
K J SOMAIYA SCHOOL OF ENGINEERING
SOMAIYA VIDYAVIHAR UNIVERSITY
Department of Information Technology | SEM-VII | DiM (2026-27)
Course Code: KJSSE/IT/LYBTECH /SEM-VII/DiM/2026-27
================================================================================

EXPERIMENT NO.: 04
TITLE: Robot.txt and sitemap creation

--------------------------------------------------------------------------------
BATCH: ___________            ROLL NO.: ___________           DATE: August 13, 2026
--------------------------------------------------------------------------------

1. AIM
--------------------------------------------------------------------------------
To generate, configure, and validate XML Sitemap (`sitemap.xml`) and Robots Exclusion 
Protocol (`robots.txt`) files for a multi-page web application (`usecases` HeatAware AI 
Climate Intelligence Platform) to optimize search engine crawlability, control indexation, 
and prevent access to private system directories.


2. RESOURCES NEEDED
--------------------------------------------------------------------------------
- Hardware & Network: Computer System with active Internet Connection.
- Software Tools: Modern Web Browser (Google Chrome / Mozilla Firefox), VS Code / Antigravity IDE.
- SEO Tools: XML-Sitemaps Generator (xml-sitemaps.com), Screaming Frog SEO Spider, SEO Book Robots.txt Generator tool.
- Documentation & Office Suite: MS-Office / Markdown Documentation Editor.
- Target Web Application: `usecases` Climate Intelligence & Early Warning System (`index.html`, `dashboard.html`, `monitoring.html`, `advisories.html`, `research.html`).


3. PRE-REQUISITES
--------------------------------------------------------------------------------
- Understanding of HTML5 markup structure, CSS, and web application architecture.
- Understanding of Web Crawling, Search Engine Indexing mechanisms, and HTTP request flows.
- Knowledge of the Robots Exclusion Protocol (REP) and XML Schema definitions for Sitemaps.
- Basic knowledge of URL structure, HTTP status codes, canonicalization, and web hosting server paths.


4. THEORY
--------------------------------------------------------------------------------
SITEMAP

In simple terms, a Sitemap is an XML file that is full of your individual webpage's URLs. It's 
like an archive of every webpage in your website. This file should be easily discoverable in 
your site in order for search engine crawlers to stumble upon it.

What is a Sitemap for?
A Sitemap is usually used for the purpose of letting the search engine crawlers follow the 
links to all your individual webpages so that it won't miss out on anything.
Sometimes we leave out URLs or hide them from all visible pages because we don't exactly 
want some of the users to go there. As a result, some of these URLs are uncrawlable to search 
engine spiders.
We can still leave those URLs hidden from some users without having to lose out on those 
pages not being crawled by search engine spiders through including them in an XML Sitemap.

Key XML Sitemap Elements & Tags:
1. `<urlset>`: Encapsulates the file and references the current XML schema standard (sitemaps.org).
2. `<url>`: Parent XML container entry for each individual web page URL.
3. `<loc>`: Absolute URL of the webpage (e.g., `https://priyanshu.github.io/usecases/index.html`).
4. `<lastmod>`: ISO 8601 formatted date indicating when the page content was last updated.
5. `<changefreq>`: Hint to crawlers regarding update frequency (`always`, `hourly`, `daily`, `weekly`, `monthly`, `yearly`, `never`).
6. `<priority>`: Relative priority ranking of the URL compared to other pages on the site (ranges from `0.0` to `1.0`).


ROBOTS.TXT

Robots.txt is a text file webmasters create to instruct web robots (typically search engine 
robots) how to crawl pages on their website. The robots.txt file is part of the robots 
exclusion protocol (REP), a group of web standards that regulate how robots crawl the web, 
access and index content, and serve that content up to users. The REP also includes directives 
like meta robots, as well as page-, subdirectory-, or site-wide instructions for how search 
engines should treat links (such as "follow" or "nofollow").

In practice, robots.txt files indicate whether certain user agents (web-crawling software) can 
or cannot crawl parts of a website. These crawl instructions are specified by "disallowing" or 
"allowing" the behavior of certain (or all) user agents.

Basic Format:
```text
User-agent: [user-agent name]
Disallow: [URL string not to be crawled]
```

Robots.txt Syntax Examples:

1. Blocking all web crawlers from all content:
```text
User-agent: *
Disallow: /
```
Using this syntax in a robots.txt file would tell all web crawlers not to crawl any pages 
on www.example.com, including the homepage.

2. Allowing all web crawlers access to all content:
```text
User-agent: *
Disallow: 
```
Using this syntax in a robots.txt file tells web crawlers to crawl all pages 
on www.example.com, including the homepage.

3. Blocking a specific web crawler from a specific folder:
```text
User-agent: Googlebot
Disallow: /example-subfolder/
```
This syntax tells only Google's crawler (user-agent name Googlebot) not to crawl any pages 
that contain the URL string www.example.com/example-subfolder/.

4. Blocking a specific web crawler from a specific web page:
```text
User-agent: Bingbot
Disallow: /example-subfolder/blocked-page.html
```
This syntax tells only Bing's crawler (user-agent name Bing) to avoid crawling the specific 
page at www.example.com/example-subfolder/blocked-page.html.


5. PROCEDURE (STEP-BY-STEP)
--------------------------------------------------------------------------------

1. Create site map for your website:

+-----------------------------------+-----------------------------------------------------------------------------------+
| Name Of the Tool                  | XML-Sitemaps Generator / Screaming Frog SEO Spider                               |
| (Include Company Name, website)   | Website: https://www.xml-sitemaps.com / https://www.screamingfrog.co.uk           |
|                                   | Provider: XML-Sitemaps Inc. & Screaming Frog Ltd.                                 |
+-----------------------------------+-----------------------------------------------------------------------------------+
| License / Open Source             | Freemium / Proprietary Web Utility & Desktop Software                             |
+-----------------------------------+-----------------------------------------------------------------------------------+
| Explanation of Tool               | An automated SEO tool that recursively crawls web pages starting from a domain   |
|                                   | root, extracts hyperlinked HTML documents, validates canonical links, computes     |
|                                   | change frequencies and last modified timestamps, and structures them into a       |
|                                   | standard W3C-compliant XML sitemap protocol format.                               |
+-----------------------------------+-----------------------------------------------------------------------------------+
| Procedure                         | 1. How tool accepts the input?                                                    |
|                                   |    - Input target URL (e.g., `https://priyanshu.github.io/usecases/`) or local site   |
|                                   |      root directory path into the crawler configuration interface.                   |
|                                   |    - Set crawl parameters: Max Depth = 3, Include HTML pages, Exclude CSS/JS assets.  |
|                                   |                                                                                   |
|                                   | 2. How tool processes the data?                                                   |
|                                   |    - Parses HTML tags (`<a href="...">`, `<link rel="canonical">`).               |
|                                   |    - Filters out duplicate URLs, fragment anchors (`#`), and non-200 HTTP responses. |
|                                   |    - Assigns priority ratings (`1.0` for index, `0.9` for core dashboards, `0.7` for  |
|                                   |      research archives) and formats output according to XML sitemap schema.        |
|                                   |                                                                                   |
|                                   | 3. How tool displays the output/result?                                           |
|                                   |    - Generates downloadable `sitemap.xml` file.                                   |
|                                   |    - Uploaded to the web root folder: `usecases/sitemap.xml`.                    |
|                                   |    - Displayed and validated directly in browser at `/sitemap.xml`.              |
+-----------------------------------+-----------------------------------------------------------------------------------+

XML Sitemap Code (`sitemap.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
                            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <!-- Homepage / Climate Intelligence Platform Overview -->
    <url>
        <loc>https://priyanshu.github.io/usecases/index.html</loc>
        <lastmod>2026-08-13</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    
    <!-- Forecast Watch Dashboard -->
    <url>
        <loc>https://priyanshu.github.io/usecases/dashboard.html</loc>
        <lastmod>2026-08-13</lastmod>
        <changefreq>hourly</changefreq>
        <priority>0.9</priority>
    </url>
    
    <!-- Live AWS Weather Station Monitoring -->
    <url>
        <loc>https://priyanshu.github.io/usecases/monitoring.html</loc>
        <lastmod>2026-08-13</lastmod>
        <changefreq>always</changefreq>
        <priority>0.9</priority>
    </url>
    
    <!-- Early Warning Alerts & AI Advisories -->
    <url>
        <loc>https://priyanshu.github.io/usecases/advisories.html</loc>
        <lastmod>2026-08-13</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
    
    <!-- Data & Research Portal -->
    <url>
        <loc>https://priyanshu.github.io/usecases/research.html</loc>
        <lastmod>2026-08-13</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.7</priority>
    </url>
</urlset>
```

Location of File:
- Web Server / Root Directory: `https://priyanshu.github.io/usecases/sitemap.xml`
- Workspace Root Path: `file:///Users/priyanshu/Desktop/Projects/usecases/sitemap.xml`


2. Create robot.txt having reference of sitemap.xml:

+-----------------------------------+-----------------------------------------------------------------------------------+
| Name Of the Tool                  | SEO Book Robots.txt Generator / Ryte Robots Exclusion Tool                        |
| (Include Company Name, website)   | Website: https://tools.seobook.com/robots-txt/ / https://www.ryte.com            |
|                                   | Provider: SEO Book & Ryte GmbH                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------+
| License / Open Source             | Free Web Utility / Open Source SEO Tool                                           |
+-----------------------------------+-----------------------------------------------------------------------------------+
| Explanation of Tool               | A webmaster generator tool that configures Robots Exclusion Protocol (REP) rules |
|                                   | by specifying crawl permissions (`Allow`/`Disallow`) per User-agent, defining    |
|                                   | crawl-delay parameters, and linking the absolute XML Sitemap path.                |
+-----------------------------------+-----------------------------------------------------------------------------------+
| Procedure                         | 1. How tool accepts the input?                                                    |
|                                   |    - User selects target User-Agents (`*`, `Googlebot`, `Bingbot`, `AhrefsBot`).  |
|                                   |    - User inputs directory exclusion rules (`/tests/`, `/mutants/`, `__pycache__`).|
|                                   |    - User specifies absolute Sitemap location (`sitemap.xml`).                    |
|                                   |                                                                                   |
|                                   | 2. How tool processes the data?                                                   |
|                                   |    - Validates syntax formatting against standard REP specification RFC requirements. |
|                                   |    - Concatenates User-agent blocks, Allow/Disallow tokens, and Sitemap directive.|
|                                   |                                                                                   |
|                                   | 3. How tool displays the output/result?                                           |
|                                   |    - Renders text editor preview and provides downloadable `robots.txt` file.      |
|                                   |    - Uploaded to website root: `usecases/robots.txt`.                            |
|                                   |    - Verified via Google Search Console Robots Testing Tool.                       |
+-----------------------------------+-----------------------------------------------------------------------------------+

Robots.txt Code (`robots.txt`):
```text
# ================================================================================
# ROBOTS.TXT FOR HEATAWARE AI - CLIMATE INTELLIGENCE PLATFORM
# Somaiya Vidyavihar University & IMD Pune Project
# ================================================================================

# Global Crawler Rules (Googlebot, Bingbot, Slurp, DuckDuckBot, etc.)
User-agent: *
Allow: /
Allow: /index.html
Allow: /dashboard.html
Allow: /monitoring.html
Allow: /advisories.html
Allow: /research.html
Allow: /css/
Allow: /js/

# Disallow Internal Directories, Build Artifacts, and Test Suites
Disallow: /mutants/
Disallow: /tests/
Disallow: /.pytest_cache/
Disallow: /__pycache__/
Disallow: /.git/
Disallow: /mutation_runner.py
Disallow: /weather_analytics.py
Disallow: /conftest.py
Disallow: /pytest.ini
Disallow: /setup.cfg

# Specific Crawler Directives & Rate Limiting
User-agent: BadBot
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10

# XML Sitemap Specification
Sitemap: https://priyanshu.github.io/usecases/sitemap.xml
```

Location of File:
- Web Server / Root Directory: `https://priyanshu.github.io/usecases/robots.txt`
- Workspace Root Path: `file:///Users/priyanshu/Desktop/Projects/usecases/robots.txt`


6. RESULTS (DESCRIPTION OF SELECTED TOOL IN PRESCRIBED FORMAT)
--------------------------------------------------------------------------------
The XML Sitemap (`sitemap.xml`) and Robots Exclusion file (`robots.txt`) were created 
and deployed to the root of the HeatAware AI web application. 

Key Results Achieved:
1. **XML Sitemap Verification**: All 5 core web portals (`index.html`, `dashboard.html`, 
   `monitoring.html`, `advisories.html`, `research.html`) were mapped with correct HTTP 
   locations, metadata attributes, update frequencies, and relative priority levels.
2. **Robots.txt Protocol Enforcement**: Universal crawlers (`User-agent: *`) are granted 
   full access to client-facing assets (`/css/`, `/js/`, `.html` files) while restricting 
   indexing of non-production folders (`/tests/`, `/mutants/`, `__pycache__`).
3. **Sitemap Discovery**: The `robots.txt` file contains an explicit `Sitemap:` directive 
   pointing search engine crawlers directly to `https://priyanshu.github.io/usecases/sitemap.xml`.


7. QUESTIONS & ANSWERS
--------------------------------------------------------------------------------
Question 1: Explain the content duplication issues from SEO point of view.

Answer:
Content duplication occurs when identical or substantially similar web content appears at 
multiple distinct URLs across the web or within the same website domain. From a Search 
Engine Optimization (SEO) perspective, duplicate content creates severe structural and 
ranking challenges for search engine crawlers.

1. Causes and Sources of Content Duplication:
   - **URL Variations & Protocol Differences**: Accessing pages via `http://` vs `https://`, 
     or `www.example.com` vs `example.com`.
   - **Trailing Slashes**: Search engines treat `example.com/page` and `example.com/page/` as 
     two separate URLs.
   - **Session IDs & Tracking Parameters**: Query strings like `?utm_source=twitter` or 
     `?sessionid=123` lead to identical content being indexed under hundreds of distinct URLs.
   - **Printer-Friendly / Mobile Pages**: Offering print version URLs (`example.com/page?print=1`) 
     without canonical tagging.
   - **Staging / Mirror Environments**: Leaving development or staging mirrors accessible to 
     crawlers without authentication or `robots.txt` protection.

2. SEO Impacts of Content Duplication:
   - **Crawl Budget Wastage**: Search engine spiders spend finite crawling time and resources 
     re-indexing duplicate pages instead of discovering new or updated content.
   - **Dilution of Link Equity (PageRank)**: Inbound links, social shares, and authority 
     scores are split across multiple duplicate URLs instead of being concentrated into a single 
     authoritative page.
   - **Indexation Confusion**: Search algorithms struggle to determine which version of the 
     URL to index and display in Search Engine Results Pages (SERPs).
   - **Ranking Drop / Algorithmic Filtering**: Search engines like Google actively suppress 
     duplicate search results, causing ranking penalties or drops in organic visibility.

3. Solutions & Mitigation Strategies for Content Duplication:
   - **Canonical Tag (`<link rel="canonical" href="...">`)**: Instructs search engines which 
     URL is the master/authoritative version.
   - **301 Permanent Redirects**: Automatically redirects duplicate URL variations (e.g., HTTP 
     to HTTPS, non-www to www) to the single canonical location.
   - **Robots.txt & Meta Robots**: Use `robots.txt` to block parameter variations or use 
     `<meta name="robots" content="noindex, follow">` on printable/staging pages.
   - **XML Sitemap Optimization**: Include ONLY canonical, 200 OK status URLs inside `sitemap.xml`.
   - **URL Parameter Tool**: Configure parameter handling in Google Search Console to ignore 
     tracking parameters.


8. OUTCOMES
--------------------------------------------------------------------------------
1. Successfully generated and validated a structured XML Sitemap (`sitemap.xml`) indexing all 
   five core pages of the HeatAware AI platform.
2. Formatted and deployed a compliant `robots.txt` file incorporating `User-agent`, `Allow`, 
   `Disallow`, and `Sitemap` directives.
3. Protected sensitive development directories (`/mutants/`, `/tests/`, `__pycache__`) from 
   unwanted search engine crawler indexation.
4. Gained an in-depth understanding of search engine crawling, indexing mechanics, and SEO 
   content duplication mitigation strategies.


9. CONCLUSION
--------------------------------------------------------------------------------
In this experiment, `sitemap.xml` and `robots.txt` files were successfully created and 
configured for the HeatAware AI web platform. XML sitemaps serve as an essential roadmap 
for search engine spiders, ensuring fast, efficient, and complete coverage of all website 
pages. Concurrently, `robots.txt` establishes explicit rules for crawler behavior under the 
Robots Exclusion Protocol, protecting internal scripts and test artifacts while routing 
crawlers directly to the primary sitemap. Implementing both SEO controls guarantees optimal 
search engine indexation, prevents content duplication issues, and preserves crawl budget.


--------------------------------------------------------------------------------
Grade: AA / AB / BB / BC / CC / CD / DD

Signature of faculty in-charge with date: ___________________________
