# Importations packages
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
import re

# Variables
WEBSITE = "http://books.toscrape.com/"
# type the book of url book
urlbook = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
#urlbook = "http://books.toscrape.com/catalogue/a-flight-of-arrows-the-pathfinders-2_876/index.html"

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
def search_col(th,td,col_url,cols,ind):
    str = ""
    i = 0
    for t in th:
        if col_url[cols[ind]] == t.string:
            break
        else:
            i = i + 1

    j = 0
    for t1 in td:
        if j == i:
            str = t1.string
            break
        else:
            j = j + 1
    return str

def analyze_url_book(url,col_url,cols):
    simple_line = []
    page = rq.get(url)

    soup = bs(page.content, 'html.parser')
   # print(soup.find_all('ul',class_="breadcrumb"))
    #print(soup.find_all('p', class_="star-rating"))
    print(soup.find("meta",  attrs={'name':'description'}).get('content'))

    # upc ,price , number available
    th = soup.find_all('th')
    td = soup.find_all('td')
    # add url
    simple_line.append(url)
    # add UPC
    simple_line.append(search_col(th, td, col_url, cols, 1))
    # add title
    #h1 = soup.find_all('h1')
    h1 = soup.find_all('li', class_="active")
    for title in h1:
        simple_line.append(title.string)
    # add price_excluding_tax
    simple_line.append(search_col(th, td, col_url, cols, 4))
    # add price_including_tax
    simple_line.append(search_col(th, td, col_url, cols, 3))
    # add number_available
    nbr_books = search_col(th, td, col_url, cols, 5)
    simple_line.append(re.sub("[^0-9]", "", nbr_books))
    # add description
    simple_line.append(soup.find("meta",  attrs={'name':'description'}).get('content'))
    # add category
    categ = soup.find_all('a', href=True)  # category
    i = 1
    for title in categ:
        if i == 4:
            simple_line.append(title.string)
            break
        else:
            i = i + 1

    return simple_line

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        page = rq.get(WEBSITE)
        page.raise_for_status()
    except HTTPError as hp:
        print(hp)

    # create one csv for one book
    df = pd.DataFrame(columns=HEADER_CSV)

    #df.loc[len(df)] = analyze_url_book(urlbook,COLUMNS_URL)
    sl = analyze_url_book(urlbook,COLUMNS_URL,HEADER_CSV)
    print(sl)
    #print(df)