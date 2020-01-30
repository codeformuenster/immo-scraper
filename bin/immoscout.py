""" Scraping Immoscout24. """

import os
from typing import Dict

from immo_scraper.scraper.immoscout24 import immoscout24parser


immos: Dict[str, Dict] = {}
b = os.environ["STATE"]  # Bundesland
s = os.environ["CITY"]  # Stadt
k = os.environ["ESTATE_TYPE"]  # Wohnung oder Haus
w = os.environ["RENT_TYPE"]  # Miete oder Kauf

page = 0
print("Suche %s / %s" % (k, w))

while True:
    page += 1
    url = (
        "http://www.immobilienscout24.de/Suche/S-T/P-%s/%s-%s/%s/%s?pagerReporting=true"
        % (page, k, w, b, s)
    )

    # Because of some timeout or immoscout24.de errors,
    # we try until it works \o/
    resultlist_json = None
    while resultlist_json is None:
        try:
            resultlist_json = immoscout24parser(url)
            numberOfPages = int(resultlist_json[u"paging"][u"numberOfPages"])
            pageNumber = int(resultlist_json[u"paging"][u"pageNumber"])
        except Exception:
            pass

    if page > numberOfPages:
        break

    # Get the data
    for resultlistEntry in resultlist_json["resultlistEntries"][0][
        u"resultlistEntry"
    ]:
        realEstate_json = resultlistEntry[u"resultlist.realEstate"]

        realEstate = {}

        realEstate[u"Miete/Kauf"] = w
        realEstate[u"Haus/Wohnung"] = k

        realEstate["address"] = realEstate_json["address"]["description"]["text"]
        realEstate["city"] = realEstate_json["address"]["city"]
        realEstate["postcode"] = realEstate_json["address"]["postcode"]
        realEstate["quarter"] = realEstate_json["address"]["quarter"]
        try:
            realEstate["lat"] = realEstate_json["address"][u"wgs84Coordinate"][
                "latitude"
            ]
            realEstate["lon"] = realEstate_json["address"][u"wgs84Coordinate"][
                "longitude"
            ]
        except Exception:
            realEstate["lat"] = None
            realEstate["lon"] = None

        realEstate["title"] = realEstate_json["title"]

        realEstate["numberOfRooms"] = realEstate_json["numberOfRooms"]
        realEstate["livingSpace"] = realEstate_json["livingSpace"]

        if k == "Wohnung":
            realEstate["balcony"] = realEstate_json["balcony"]
            realEstate["builtInKitchen"] = realEstate_json["builtInKitchen"]
            realEstate["garden"] = realEstate_json["garden"]
            realEstate["price"] = realEstate_json["price"]["value"]
            realEstate["privateOffer"] = realEstate_json["privateOffer"]
        elif k == "Haus":
            realEstate["isBarrierFree"] = realEstate_json["isBarrierFree"]
            realEstate["cellar"] = realEstate_json["cellar"]
            realEstate["plotArea"] = realEstate_json["plotArea"]
            realEstate["price"] = realEstate_json["price"]["value"]
            realEstate["privateOffer"] = realEstate_json["privateOffer"]

        realEstate["floorplan"] = realEstate_json["floorplan"]
        realEstate["from"] = realEstate_json["companyWideCustomerId"]
        realEstate["ID"] = realEstate_json[u"@id"]
        realEstate["url"] = (
            u"https://www.immobilienscout24.de/expose/%s" % realEstate["ID"]
        )

        immos[realEstate["ID"]] = realEstate

    print(
        "Scrape Page %i/%i (%i Immobilien %s %s gefunden)"
        % (page, numberOfPages, len(immos), k, w)
    )
