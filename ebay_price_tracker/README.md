# eBay Price Tracker

## Overview
The eBay Price Tracker is a Python application that scrapes eBay search results for specific products, processes the prices to remove outliers, calculates the average price, and saves the data to a CSV file. This project demonstrates web scraping, data cleaning, and basic file handling.

## Features
- **Web Scraping**: Extracts prices of items from eBay search results.
- **Outlier Removal**: Filters out prices that deviate significantly from the average.
- **Data Storage**: Saves average prices to a CSV file with timestamps.
- **Data Analysis**: Displays average prices in the console.

## Installation
### Prerequisites
- Python 3.x
- Required libraries:
  - `beautifulsoup4`
  - `requests`
  - `numpy`
  - `csv`

### Setup
1. Clone the repository or download the project files.
2. Install the required libraries using pip:
   ```bash
   pip install beautifulsoup4 requests numpy
   ```
3. Ensure that the script has internet access to scrape eBay.

## Usage
1. Update the `LINK` variable in the script with your desired eBay search URL.
2. Run the script:
   ```bash
   python ebay_price_tracker.py
   ```
3. Check the console output for the average price.
4. View saved price data in `prices.csv`.

## How It Works
1. **Data Collection**: The script sends a GET request to the specified eBay search URL and parses the page using BeautifulSoup.
2. **Price Extraction**: Extracts item prices while skipping price ranges.
3. **Outlier Removal**: Filters out prices beyond two standard deviations from the mean.
4. **Data Storage**: Saves the average price with the current date to `prices.csv`.

## Example Output
```
[849.99, 859.00, 870.00, 890.50]
Average price: £867.37
```

## Notes
- Ensure the eBay search URL is correctly formatted.
- Be aware of potential changes in the eBay website structure that could affect scraping.

## License
This project is licensed under the MIT License.

## Acknowledgments
- eBay for providing the data.
- The developers of BeautifulSoup, Requests, and NumPy for their great libraries.
- Internet Made Coder: [Video](https://youtu.be/ZRlbf5P2iMA?si=BAa_5NoPUCN5D6c1)

## Disclaimer
This project is for educational purposes only. Scraping websites without permission may violate terms of service. Use responsibly.

