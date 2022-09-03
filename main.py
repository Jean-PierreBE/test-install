# Importations packages
import pandas as pd
import requests as rq
#import AnalizeWeb as aw
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
import re

# Variables
WEBSITE = "http://books.toscrape.com/"
# type the book of url book
URLBOOK = ["http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
           "http://books.toscrape.com/catalogue/a-flight-of-arrows-the-pathfinders-2_876/index.html",
           "http://books.toscrape.com/catalogue/the-bachelor-girls-guide-to-murder-herringford-and-watts-mysteries-1_491/index.html",
           "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"]

HEADER_CSV = ["product_page_url","universal_ product_code (upc)","title","price_including_tax (£)","price_excluding_tax (£)",
              "number_available","product_description","category","review_rating","image_url"]

COLUMNS_URL = {"universal_ product_code (upc)" :"UPC",
               "title" : "col-sm-6 product_main",
               "price_including_tax (£)" : "Price (incl. tax)",
               "price_excluding_tax (£)" : "Price (excl. tax)",
               "number_available" : "Availability",
               "product_description" : "Product Description",
               "category" : "books.toscrape.com/catalogue/category/books/",
               "review_rating" : "Number of reviews",
               "image_url" : "image_container"}

# Fonctions
def list_category(url):
    list_cat = {}
    page = rq.get(url)

    soup = bs(page.content, 'html.parser')
    for h in soup.find_all('div', class_="side_categories"):
        for a in h.find_all('a', href=True):
            # looking for anchor tag inside the <li>tag
            if a.text.strip() != "Books":
                list_cat[a.text.strip()] = url + a.get("href").strip()

    return list_cat

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
    #print(soup.find('p', class_="star-rating"))
    #print(soup.find_all('div', 'thumbnail'))
    for div in soup.find_all('div', 'thumbnail'):
        img = div.find('img', alt=True)
    # upc ,price , number available
    th = soup.find_all('th')
    td = soup.find_all('td')
    # add url
    simple_line.append(url)
    # add UPC
    simple_line.append(search_col(th, td, col_url, cols, 1))
    # add title
    simple_line.append(img['alt'])
    # add price_excluding_tax
    simple_line.append(search_col(th, td, col_url, cols, 4).replace("£",''))
    # add price_including_tax
    simple_line.append(search_col(th, td, col_url, cols, 3).replace("£",''))
    # add number_available
    nbr_books = search_col(th, td, col_url, cols, 5)
    simple_line.append(re.sub("[^0-9]", "", nbr_books))
    # add description
    simple_line.append(soup.find("meta",  attrs={'name':'description'}).get('content').strip())
    # add category
    categ = soup.find_all('a', href=True)  # category
    i = 1
    for title in categ:
        if i == 4:
            simple_line.append(title.string)
            break
        else:
            i = i + 1
    # add review rating
    simple_line.append(search_col(th, td, col_url, cols, 8))
    # add url image
    simple_line.append(img['src'].replace("../../",WEBSITE))

    return simple_line

# analyze category
def analyze_url_category(cat,url,col_url,cols):
    df_category = pd.DataFrame(columns=cols)
    page = rq.get(url)

    soup = bs(page.content, 'html.parser')
    for h in soup.find_all('article', class_="product_pod"):
        for h3 in h.find_all('h3'):
            for a in h3.find_all('a', href=True):
                df_category.loc[len(df_category)] = analyze_url_book(a.get("href").replace("../../../",WEBSITE + "catalogue/").strip(), col_url,cols)
    df_category.to_csv(cat + '.csv', index=False, sep=';', encoding='utf-8')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        page = rq.get(WEBSITE)
        page.raise_for_status()
    except HTTPError as hp:
        print(hp)

    # create one csv for one or several books
    df_book = pd.DataFrame(columns=HEADER_CSV)

    for urlbook in URLBOOK:
        df_book.loc[len(df_book)] = analyze_url_book(urlbook,COLUMNS_URL,HEADER_CSV)
    # create csv
    df_book.to_csv('books.csv', index=False,sep=';', encoding='utf-8')

    lst_cat = list_category(WEBSITE)
    #for k, v in lst_cat.items():
    #    print(k, v)
    #analyze_url_category("Mystery",lst_cat["Mystery"], COLUMNS_URL, HEADER_CSV)
    for k, v in lst_cat.items():
        analyze_url_category(k,v, COLUMNS_URL, HEADER_CSV)

