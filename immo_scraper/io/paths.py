""" Path variables, shared between functions/scripts of the library. """

from pathlib import Path

BUCKET_FOLDER = "nestoria/"  # folder to raw data (inside bucket)
BUCKET_NESTORIA = Path("bucket/nestoria/")  # folder of raw data

AGGREGATED_CSV = Path("bucket/processed/aggregated.csv")  # aggregation of raw data
ALERTS_IDS = Path("bucket/processed/alerts_ids.txt")  # alerts that were sent out
