# Importations packages
import requests as rq
import AnalizeWeb as aw
import logging
import json
import sys


# Variables
PARAM = "parameters.txt"

def load_libel():
    f = open(PARAM, "r")
    # Reading from file
    dataj = json.loads(f.read())

    return dataj

def main(argv):
    logging.basicConfig(filename='LogWebScrapping.log', encoding='utf-8', level=logging.ERROR)
    # load parameters
    datalib = load_libel()

    WEBSITE = datalib["Website"]["BookScrap"]
    SAVE_IMAGES = datalib["Directory"]["Images"]
    SAVE_BOOKS = datalib["Directory"]["Books"]

    page = rq.get(WEBSITE)
    if page.status_code == 200:
        lst_cat = aw.list_category(WEBSITE)
        if argv[1] == "all":
            for k, v in lst_cat.items():
              aw.analyze_url_category(k,v, WEBSITE, SAVE_BOOKS, SAVE_IMAGES)
            print("all csv files have been created in directory " + SAVE_BOOKS)
        else:
            try:
                if lst_cat[argv[1]]:
                    aw.analyze_url_category(argv[1], lst_cat[argv[1]], WEBSITE, SAVE_BOOKS, SAVE_IMAGES)
                    print("csv file for the category '" + argv[1] + "' has been created in directory " + SAVE_BOOKS)
            except:
                print("category " + argv[1] + " doesn't exist")
    else:
        print("error acces website " + WEBSITE + " : " + str(page.status_code))

if __name__ == '__main__':
    main(sys.argv)
