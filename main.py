# Importations packages
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

# Variables
WEBSITE = "http://books.toscrape.com/"

HEADER_CSV = ["product_page_url","universal_ product_code (upc)","title","price_including_tax","price_excluding_tax",
              "number_available","product_description","category","review_rating","image_url"]

COLUMNS_URL = {"universal_ product_code (upc)" :"UPC",
               "title" : "col-sm-6 product_main",
               "price_including_tax" : "Price (incl. tax)",
               "price_excluding_tax" : "Price (excl. tax)",
               "number_available" : "Availability",
               "product_description" : "Product Description",
               "category" : "books.toscrape.com/catalogue/category/books/",
               "review_rating" : "Number of reviews",
               "image_url" : "image_container"}

# Fonctions
def analyze_url_book(url,col_url):
    simple_line = []

    return simple_line

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page = rq.get(WEBSITE)
    if page.ok:
        print("ok")
    soup = bs(page.content, 'html.parser')
    print(soup)

    # create one csv for one book
    df = pd.DataFrame(columns=HEADER_CSV)
    # type the book of url book
    urlbook = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

    df.loc[len(df)] = analyze_url_book(urlbook,COLUMNS_URL)

