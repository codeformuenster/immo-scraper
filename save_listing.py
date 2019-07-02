
import hashlib
import json
import datetime

from kafka import KafkaConsumer
from kafka import TopicPartition

import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

KAFKA_URI = "kafka:9092"
NESTORIA_TOPIC = "nestoria_event"

print("Making connection.")
consumer = KafkaConsumer(
    bootstrap_servers=KAFKA_URI,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
consumer.assign([TopicPartition(NESTORIA_TOPIC, 0)])


def hash_listing(listing):
    return hashlib.md5(str(listing).encode("utf-8")).hexdigest()


def get_listing_id(listing):
    return listing["lister_url"].split("/")[4]


def get_today():
    return str(datetime.datetime.now().date())


def generate_filename(listing):
    # today =  get_today()
    listing_id = get_listing_id(listing)
    listing_hash = hash_listing(listing)

    # return today + '_' + listing_id + '_' + listing_hash + '.json'
    return listing_id + "_" + listing_hash + ".json"


def write_listings_to_disk(listings):
    for listing in listings:
        print(listing)
        filename = generate_filename(listing)
        with open(filename, "w") as f:
            print("writing " + filename)
            json.dump(listing, f, indent=4)


if __name__ == "__main__":
    for message in consumer:
        listings = message.value
        # add_timestamp_to_listings(listings)
        write_listings_to_disk(listings)
