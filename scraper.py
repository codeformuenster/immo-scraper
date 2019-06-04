""" Main script that executes all scrapers. """

import logging
import sys

sys.path.append(".")
from immo_scraper import nestoria  # noqa: E402

# set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger("info_logger")
log.setLevel(logging.INFO)
log.info("Logger set up.")

# scrape
log.info("Scraping...")
nestoria_result = nestoria.scrape()
log.info("Scraping done.")

# save to S3 bucket
# TODO
