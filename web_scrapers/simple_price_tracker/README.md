# BikeKings Price Scraper

## Overview

This Python program scrapes the price of an item from the website [BikeKings](https://www.bikekings.co.za). It retrieves and parses the HTML of a specified product page, extracts the item's price, and outputs it.

---

## Features

- **Web scraping:** Uses the `requests` library to fetch the webpage content.
- **HTML parsing:** Utilizes `BeautifulSoup` from the `bs4` package to parse and navigate the webpage's HTML.
- **Regex extraction:** Employs regular expressions to extract the price from the parsed HTML.

---

## Requirements

To run this program, you need:
- Python 3.x
- The following Python libraries:
  - `bs4` (BeautifulSoup)
  - `requests`
  - `re` (built-in)

---

## Installation

1. Clone the repository or download the script file.
2. Install the required libraries using `pip`:
   ```bash
   pip install beautifulsoup4 requests
   ```

---

## How to Use

1. Open the script and set the value of `LINK` to the URL of the product page you want to scrape.
   ```python
   LINK = "https://www.bikekings.co.za/collections/fullface/products/shark-skwal-i3-hellcat-matte-kur?_pos=28&_fid=271f4b3e9&_ss=c"
   ```
2. Run the script:
   ```bash
   python script_name.py
   ```
3. The program will extract and return the price of the item from the given link.

---

## Code Structure

### Variables

- `LINK`: A constant that stores the URL of the product to scrape.

### Functions

1. **`get_data(link)`**
   - Fetches the HTML content of the page from the provided link.
   - Parses the HTML using BeautifulSoup.
   - Locates the price using the `product-page-info__price` and `price` classes.
   - Extracts and returns the price using a regular expression.

2. **`main()`**
   - Calls the `get_data()` function with the predefined `LINK`.

### Example Output

If the product price is displayed as `R 1,499.99`, the output of the script will be:
```plaintext
1,499.99
```

---

## Known Limitations

- **URL Specificity:** The script is tailored for BikeKings product pages with specific HTML structure. If the structure changes, the script will need updates.
- **Locale Dependency:** The script assumes prices follow the format `X,XXX.XX` (e.g., `1,499.99`). It may not work for other locales or formats.
- **Single URL:** Currently, it scrapes only the price of the item at the URL specified in `LINK`. Extending the script for multiple URLs requires additional modifications.

---

## Future Improvements

- **Error Handling:** Add error handling for scenarios like invalid URLs, changes in the HTML structure, or network issues.
- **User Input:** Allow users to specify the URL dynamically via command-line arguments.
- **Output Options:** Save the price to a file or display additional product details.

---

## Disclaimer

This program is intended for educational purposes only. Ensure compliance with the website's terms of service before scraping. Excessive or unauthorized scraping can lead to legal consequences.
