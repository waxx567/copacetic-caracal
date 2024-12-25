from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=m1+macbook+air&_sacat=0"


def get_data(link):
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
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def save_prices(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


def get_average(prices):
    return np.mean(prices)


def main():
    prices = get_data(LINK)
    adjusted_prices = remove_outliers(prices)
    average_price = get_average(adjusted_prices)
    save_prices(adjusted_prices)
    print(f"{adjusted_prices}")

    print(f"Average price: £{average_price:.2f}")


if __name__ == "__main__":    
    main()