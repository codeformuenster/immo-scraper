"""Scraping real estate API."""

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


def scrape():
    response = requests.get(URL)
    assert response.status_code == 200, "Status is not 200!"

    listings = response.json()['response']['listings']
    assert len(listings) > 0, "No listings in reponse!"

    return listings


if __name__ == "__main__":
    response = scrape()
    pipe(response,
         map(str),
         list,
         print)
