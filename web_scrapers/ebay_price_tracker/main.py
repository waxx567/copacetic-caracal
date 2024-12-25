from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=m1+macbook+air&_sacat=0"


def get_data(link):
    """
    Given a link to an ebay.co.uk search page, this function will scrape the prices of all
        items on the page and return them as a list of floats.
    """
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    list_items = soup.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

    prices = []

    for item in list_items:
        text_price = item.find("span", {"class": "s-item__price"}).text
        if "to" in text_price:
            continue
        price = float(text_price[1:].replace(",", "")) 
        prices.append(price)

    return prices


def remove_outliers(prices, m=2):
    """
    Removes outliers from a list of prices by removing all values that are more than m standard
        deviations away from the mean.
    """
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def save_prices(prices):
    """
    Saves the average of a list of prices to a CSV file named "prices.csv" in the same
        directory as this script. The CSV file will have two columns: the date and the
        average price, rounded to two decimal places.
    """
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


def get_average(prices):
    """
    Calculates the mean average of a list of prices.
    """
    return np.mean(prices)


def main():
    """
    The main function. Gets a list of prices from the link at the top of the file, removes
        outliers, gets the average price, saves the prices to a CSV file, and prints the
        average price to the console.
    """
    prices = get_data(LINK)
    adjusted_prices = remove_outliers(prices)
    average_price = get_average(adjusted_prices)
    save_prices(adjusted_prices)
    print(f"{adjusted_prices}")

    print(f"Average price: £{average_price:.2f}")


if __name__ == "__main__":    
    main()