# Importations packages
import requests as rq
import AnalizeWeb as aw
from urllib.error import HTTPError
import logging


# Variables
WEBSITE = "http://books.toscrape.com/"
SAVE_IMAGES = "C:/openclassroom/Python/P2/Images/"
SAVE_BOOKS = "C:/openclassroom/Python/P2/Books/"

if __name__ == '__main__':
    logging.basicConfig(filename='LogWebScrapping.log', encoding='utf-8', level=logging.ERROR)
    try:
        page = rq.get(WEBSITE)
        page.raise_for_status()
    except HTTPError as hp:
        print(hp)

    lst_cat = aw.list_category(WEBSITE)
    aw.analyze_url_category("Fiction", lst_cat["Fiction"], aw.COLUMNS_URL, aw.HEADER_CSV)
    #for k, v in lst_cat.items():
        #aw.analyze_url_category(k,v, aw.COLUMNS_URL, aw.HEADER_CSV)
