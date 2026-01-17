# What is Scrapy? 
An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way. 

# Why Use Scrapy Over Other Python Web Crawling Frameworks 🕷️

Scrapy is a **full-fledged, production-ready web crawling framework** designed specifically for large-scale data extraction. Compared to ad-hoc tools like `requests + BeautifulSoup` or browser automation tools like Selenium/Playwright, Scrapy shines in **performance, scalability, and maintainability**.

Below are the key benefits of using **Scrapy** over other Python web crawling approaches.

---

## 1. Built for High-Performance Crawling 🚀

- **Asynchronous & non-blocking** (built on Twisted)
- Handles **thousands of concurrent requests** efficiently
- No browser overhead → extremely fast for HTML-based websites

**Result:**  
Much faster crawls with lower CPU & memory usage.

---

## 2. Framework, Not Just a Library 🧱

Scrapy gives you an **end-to-end crawling ecosystem**:

- Spider lifecycle management
- Request scheduling & prioritization
- Retry & timeout handling
- Auto throttling & concurrency control
- Middleware & pipeline architecture

👉 With other tools, you have to manually wire all this together.

---

## 3. Automatic Request Scheduling & Deduplication 🔁

- Built-in **request queue**
- Automatic **URL deduplication**
- Depth-based crawling out of the box

No need to track visited URLs manually like in custom crawlers.

---

## 4. Clean Separation of Concerns 🧩

Scrapy enforces a **clean architecture**:

- **Spiders** → what to crawl
- **Middlewares** → how requests/responses are handled
- **Pipelines** → how data is cleaned, validated, stored

This makes:
- Code easier to maintain
- Collaboration easier
- Debugging much simpler

---

## 5. Powerful Data Pipelines 📦

- Built-in support for:
  - Validation
  - Cleaning
  - Deduplication
  - Storing to DB / S3 / Files
- Easily plug into:
  - PostgreSQL / MySQL
  - MongoDB
  - Kafka / Queues

Perfect for **production data ingestion systems**.

---

## 6. Smart Throttling & Politeness Controls 🤝

Scrapy helps you avoid bans:

- AutoThrottle
- Download delays
- Per-domain concurrency
- Respect for `robots.txt`

Much harder to manage correctly in custom scripts.

---

## 7. Middleware System = Superpowers 🛠️

You can intercept and modify:
- Requests
- Responses
- Headers
- Cookies
- Proxies
- User agents

This is ideal for:
- Proxy rotation
- Auth handling
- Header spoofing
- Anti-bot strategies

---

## 8. Robust Error Handling & Retries ⚠️

Built-in handling for:
- Timeouts
- Network errors
- HTTP error codes
- Retry logic
- Backoff strategies

You get **stable crawlers** without writing defensive code everywhere.

---

## 9. CLI, Logging & Monitoring Ready 📊

- Built-in CLI (`scrapy crawl`, `scrapy shell`)
- Structured logging
- Stats collection (requests/sec, errors, retries)

Easy to integrate with:
- Cron
- Docker
- Airflow
- Kubernetes

---

## 10. Scales Well for Production 🏗️

Scrapy is ideal when:
- You have **multiple spiders**
- Crawls run **daily/hourly**
- Data needs to be **clean & consistent**
- Failures must be **recoverable**

This is why Scrapy is widely used in **data engineering & crawling teams**.

---

## Scrapy vs Other Approaches ⚔️

| Tool | Best For | Limitation |
|----|----|----|
| requests + BeautifulSoup | Small scripts | No scale, no retries |
| Selenium / Playwright | JS-heavy sites | Slow, resource-heavy |
| Scrapy | Large-scale crawling | JS rendering not native |
| Scrapy + Playwright | JS sites at scale | Slight complexity |

---

## When Scrapy is the Best Choice ✅

Use Scrapy if:
- Website is **HTML or API based**
- You need **speed & reliability**
- Crawling is **recurring**
- Code needs to be **maintainable**
- Data feeds into **pipelines or dashboards**

# 🕷️ Scrapy Project Guide

A practical guide to getting started with **Scrapy**, testing selectors, building real spiders, and understanding when to choose Scrapy vs Selenium.

---

## 🚀 Creating a New Scrapy Project

```bash
scrapy startproject <project_name>

<project_name>/
├── scrapy.cfg
└── <project_name>/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        └── __init__.py
```

## 🕸️ Creating a Spider
Navigate to the spiders directory and run:
```bash
scrapy genspider <spider_name> <website_url>
```
Example:
```bash
scrapy genspider quotes quotes.toscrape.com
```
This generates a spider inside:
```bash
<project_name>/spiders/quotes.py
```

## ▶️ Running a Spider
From the project root:

```bash
scrapy crawl <spider_name>
```
Save output to a file:

```bash
scrapy crawl <spider_name> -O output.json
```
Supported formats: json, csv, jl, xml

## 🧪 Scrapy Shell (Selector Testing & Debugging)
### 1️⃣ Install IPython
```bash
pip install ipython
```
### 2️⃣ Enable IPython in scrapy.cfg
```
[settings]
shell = ipython
```

### 3️⃣ Start the Shell

```bash
scrapy shell
```
#### 🔍 Using Scrapy Shell
```python
# Fetch a URL
fetch("https://example.com")
# Response Object
response
# 🎯 CSS Selector Examples
response.css("div.quote")
# Get first match:
response.css("div.quote").get()
# Get all matches:
response.css("div.quote").getall()
# Extract text:
response.css("span.text::text").get()
# Extract attribute:
response.css("a::attr(href)").get()

# 🧭 XPath Selector Examples

# Basic XPath:
response.xpath("//div[@class='quote']")
# Get text:
response.xpath("//span[@class='text']/text()").get()
# Get all texts:
response.xpath("//span[@class='text']/text()").getall()
# Get attribute:
response.xpath("//a/@href").get()
# Using contains:
response.xpath("//div[contains(@class,'quote')]")
# Relative XPath:
response.xpath(".//span/text()").get()
```

### 🧑‍💻 Real Scrapy Spider Example

Example spider that crawls quotes.toscrape.com
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # pagination
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```
Run:
```bash
scrapy crawl quotes -O quotes.json
```

```bash
scrapy crawl quotes -O quotes.csv
```
