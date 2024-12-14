# Books To Scrape Web Scraping

# Web Scraper for Books Data

This project is a Python-based web scraper designed to extract information about books from the website "[Books to Scrape](https://books.toscrape.com)". It retrieves the book names, prices, and availability status from multiple pages and stores the data in a CSV file.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [How the Code Works](#how-the-code-works)
  - [Imports](#imports)
  - [Data Containers](#data-containers)
  - [Scraping Logic](#scraping-logic)
  - [Saving Data](#saving-data)

- [Output](#output)

---

## Overview
This script uses Python libraries like `requests` for HTTP requests, `BeautifulSoup` for parsing HTML, and `pandas` for organizing and exporting the extracted data. The scraper navigates through multiple pages of the website to gather information about books.

### Features:
- Extracts book names, prices, and availability statuses.
- Automatically navigates to the next page using the pagination feature.
- Saves the collected data into a CSV file for analysis or further processing.

---

## Prerequisites
Before running the script, ensure you have the following Python libraries installed:
- `pandas`
- `requests`
- `beautifulsoup4`

You can install them using:
```bash
pip install pandas requests beautifulsoup4
```

---

## How the Code Works

### Imports
```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
```
- `pandas`: Used for organizing and exporting data into a CSV file.
- `requests`: Fetches the webpage content using HTTP requests.
- `BeautifulSoup`: Parses the HTML content to extract specific elements.

### Data Containers
```python
Names = []
Price = []
Availability = []
```
These lists store the scraped data for:
- **Names**: Book titles.
- **Price**: Book prices.
- **Availability**: Book availability status.

### Scraping Logic
The scraper starts by fetching the first page of the website:
```python
url = "https://books.toscrape.com/catalogue/page-1.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
```

It iterates through multiple pages using a `for` loop, extracting book details and moving to the next page:
```python
for i in range(1,20):
    np= soup.find("li", class_="next")
    npl = np.find("a")["href"]
    cnp = "https://books.toscrape.com/catalogue/"+npl
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
```
1. **Find Next Page:**
   - The `li` element with class `next` contains the URL for the next page.
   - Construct the full URL for the next page and fetch its content.

2. **Extract Book Data:**
   - **Book Names:**
     ```python
     names = soup.find_all("h3")
     for i in names:
         n = i.find("a")["title"]
         Names.append(n)
     ```
     Each `<h3>` tag contains a book title within an `<a>` tag.
   
   - **Book Prices:**
     ```python
     price = soup.find_all("p", class_="price_color")
     for a in price:
         b = a.text
         Price.append(b)
     ```
     Prices are located in `<p>` tags with the class `price_color`.
   
   - **Availability:**
     ```python
     Available = soup.find_all("p", class_="instock availability")
     for c in Available:
         d = c.text.strip()
         Availability.append(d)
     ```
     Availability status is stored in `<p>` tags with the class `instock availability`.

### Saving Data
The collected data is saved in a CSV file using `pandas`:
```python
df = pd.DataFrame({"Name": Names, "Price": Price, "Availability": Availability})
df.to_csv("Books Data.csv")
```
- A DataFrame is created with columns for **Name**, **Price**, and **Availability**.
- The data is exported to a file named `Books Data.csv`.

---


## Output
The final output is a CSV file containing the scraped data. Example:

| Name                                | Price   | Availability          |
|-------------------------------------|---------|-----------------------|
| A Light in the Attic                | £51.77 | In stock (22 available) |
| Tipping the Velvet                  | £53.74 | In stock (20 available) |
| Soumission                          | £50.10 | In stock (20 available) |






















