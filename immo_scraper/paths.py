""" Path variables, shared between functions/scripts of the library. """

from pathlib import Path

BUCKET_RAW_DIR = "nestoria/"  # folder to raw data (inside bucket)

DIR_RAW = Path("data/raw/")  # folder of raw data
DIR_PROCESSED = Path("data/processed/")  # folder of processed data
AGGREGATED_CSV = Path("data/processed/aggregated.csv")  # aggregation of raw data
ALERTS_IDS = Path("data/processed/alerts_ids.txt")  # alerts that were sent out
