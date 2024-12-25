"""
Scrapes the price of an item on bikekings.co.za
"""

from bs4 import BeautifulSoup
import requests 
import re

# link to scrape
LINK = "https://www.bikekings.co.za/collections/fullface/products/shark-skwal-i3-hellcat-matte-kur?_pos=28&_fid=271f4b3e9&_ss=c"


"""
Gets the price of the item at the given link
"""
def get_data(link):
    # get data
    response = requests.get(link)
    # parse data    
    soup = BeautifulSoup(response.text, "html.parser")
    # get price string
    price_string = soup.find("div",{"class":"product-page-info__price"}).find_all("span",{"class":"price"})
    # get price by regex
    price = re.search(r"\d+\,\d+\.\d+", price_string[0].text).group()
    # print(price, end="")  # print price                                              
    return price


def main():
    get_data(LINK)


if __name__ == "__main__":
    main()