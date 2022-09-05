# Importations packages
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
import urllib.request as rql
import logging
import re

# Variables
WEBSITE = "http://books.toscrape.com/"
SAVE_IMAGES = "C:/openclassroom/Python/P2/Images/"
SAVE_BOOKS = "C:/openclassroom/Python/P2/Books/"

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
# download image and save it on the disk jps
def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpeg'
    rql.urlretrieve(url, full_path)

# creation dictionnary with title of category and url
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

# find number of pages
def det_nbr_pages(soup):
    nb_page = 1
    data1 = soup.find('ul', class_="pager")

    if data1:
        for li in data1.find_all("li"):
            return int(re.sub("[^2-9]", "", li.text.strip()))
    else:
        return nb_page

# Analize webpage of one book
def analyze_url_book(url,col_url,cols):
    simple_line = []
    page = rq.get(url)

    soup = bs(page.content, 'html.parser')
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
    url_image = img['src'].replace("../../",WEBSITE)
    simple_line.append(url_image)
    # download image on the disk
    #try:
        #download_image(url_image, SAVE_IMAGES, img['alt'])
        #sk.setdefaulttimeout(time=10)
        #print(url_image)
    #except :
        #logging.error('Unable to write image of ' + img['alt'])
        #pass
    return simple_line

# Analize webpage for one category
def analyze_url_category(cat,url,col_url,cols):
    df_category = pd.DataFrame(columns=cols)
    page = rq.get(url)

    soup = bs(page.content, 'html.parser')

    nb_page = det_nbr_pages(soup)
    # only one page , we keep the url
    if nb_page == 1:
        for h in soup.find_all('article', class_="product_pod"):
            for h3 in h.find_all('h3'):
                for a in h3.find_all('a', href=True):
                    df_category.loc[len(df_category)] = analyze_url_book(a.get("href").replace("../../../",WEBSITE + "catalogue/").strip(), col_url,cols)
    else:
        nmax = nb_page + 1
        for n in range(1,nmax):
            new_url = url.replace("index","page-" + str(n))
            page = rq.get(new_url)
            soup = bs(page.content, 'html.parser')
            for h in soup.find_all('article', class_="product_pod"):
                for h3 in h.find_all('h3'):
                    for a in h3.find_all('a', href=True):
                        df_category.loc[len(df_category)] = analyze_url_book(a.get("href").replace("../../../", WEBSITE + "catalogue/").strip(), col_url, cols)
    df_category.to_csv(SAVE_BOOKS+ cat + '.csv', index=False, sep=';', encoding='utf-8')