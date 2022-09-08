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
    logging.basicConfig(filename='LogWebScrapping.log', encoding='utf-8', level=logging.INFO)

    # load parameters
    datalib = load_libel()

    WEBSITE = datalib["Website"]["BookScrap"]
    SAVE_IMAGES = datalib["Directory"]["Images"]
    SAVE_BOOKS = datalib["Directory"]["Books"]

    logging.info("Start of " + argv[0] + " on " + aw.DateNow() + " at " + aw.TimeNow())
    page = rq.get(WEBSITE)
    if page.status_code == 200:
        lst_cat = aw.list_category(WEBSITE)
        if len(argv) == 1:
            print("Please type a category or 'all' ")
        elif argv[1] == "all":
            for Name_Category, Url_Category in lst_cat.items():
                aw.analyze_url_category(Name_Category,Url_Category, WEBSITE, SAVE_BOOKS, SAVE_IMAGES)
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
    # end of the program
    logging.info("End of " + argv[0] + " on " + aw.DateNow() + " at " + aw.TimeNow())
if __name__ == '__main__':
    main(sys.argv)
