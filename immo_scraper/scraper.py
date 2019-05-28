"""Scraping real estate API."""

from typing import Dict, List

import requests
from toolz import pipe
from toolz.curried import map

URL = "https://api.nestoria.de/api?" \
      "encoding=json&" \
      "pretty=1&" \
      "action=search_listings&" \
      "listing_type=buy&" \
      "place_name=muenster&" \
      "sort=newest"


def scrape() -> List[Dict]:
    """
    Scrapt nestoria API.
    :return: List of dicts. Each dict is a found listing.
    """
    r = requests.get(URL)
    assert r.status_code == 200, "Status is not 200!"

    listings = r.json()['response']['listings']
    assert len(listings) > 0, "No listings in reponse!"

    return listings


if __name__ == "__main__":
    # scrape listings
    response = scrape()
    # print results
    pipe(response,
         map(str),
         list,
         print)
