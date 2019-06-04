""" Main script that executes all scrapers. """

import sys

sys.path.append(".")
from immo_scraper import nestoria  # noqa: E402

# scrape
nestoria_result = nestoria.scrape()

# save to S3 bucket
# TODO
