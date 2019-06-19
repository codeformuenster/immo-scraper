""" Main script that executes all scrapers. """

import logging
import sys
from datetime import datetime

sys.path.append(".")
from immo_scraper import nestoria  # noqa: E402
from immo_scraper.bucket import write_to_s3  # noqa: E402

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
log.info("Writing to s3 bucket...")
timestamp = str(datetime.utcnow()) + ".txt"
write_to_s3(filename=timestamp, content=nestoria_result)
log.info("Writing done.")
