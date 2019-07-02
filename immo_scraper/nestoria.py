"""Scraping Nestoria API."""

import datetime
import json
import logging
from time import sleep
from typing import Dict, List

import requests
from kafka import KafkaProducer
from toolz.curried import map

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

KAFKA_URI = "kafka:9092"
NESTORIA_TOPIC = "nestoria_event"


URL = (
    "https://api.nestoria.de/api?"
    "encoding=json&"
    "pretty=1&"
    "number_of_results=50&"
    "action=search_listings&"
    "listing_type=rent&"
    "property_type=house&"
    "centre_point=52.1762719,7.7579568,50km&"
    "sort=newest"
)


def scrape() -> List[Dict]:
    """
    Scrapt nestoria API.
    :return: List of dicts. Each dict is a found listing.
    """
    r = requests.get(URL)
    assert r.status_code == 200, "Status is not 200!"

    listings = r.json()["response"]["listings"]
    assert len(listings) > 0, "No listings in reponse!"

    return listings


def transform_listing(listing):
    listing["date_of_listing"] = add_date_of_listing(listing)
    listing = remove_unwanted_keys(listing)

    return listing


def remove_unwanted_keys(listing):
    unwanted_keys = ["updated_in_days", "updated_in_days_formatted"]
    return {key: value for key, value in listing.items() if key not in unwanted_keys}


def add_date_of_listing(listing):
    day = listing["updated_in_days"]
    date_today = datetime.datetime.now().date()
    delta = datetime.timedelta(day)
    date_of_listing = (date_today - delta).isoformat()

    return date_of_listing


# TODO: move to serparate place
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_URI],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)


# TODO: move to serparate place
def send_event(event):
    print("sending " + str(len(event)) + " listings")
    producer.send(topic=NESTORIA_TOPIC, value=event, partition=0)


# TODO: move to serparate place
if __name__ == "__main__":
    while True:
        response = scrape()
        cleansed_response = list(map(transform_listing, response))
        send_event(cleansed_response)
        sleep(60)
