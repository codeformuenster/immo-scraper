""" Utils to interact with s3 bucket. """

import os
import logging
from typing import Text, List

import boto3
from botocore.client import Config
from pathlib import Path

from immo_scraper import config
from immo_scraper.paths import BUCKET_RAW_DIR, DIR_RAW

CONFIG = config.read_config()


def get_bucket():
    """Get bucket object, e.g. to write data.
    Returns:
        boto3.resources.factory.s3.Bucket -- Bucket object.
    """
    session = boto3.Session(
        aws_access_key_id=CONFIG["bucket"]["access_key"],
        aws_secret_access_key=CONFIG["bucket"]["secret_key"],
        region_name=CONFIG["bucket"]["region_name"],
    )
    s3 = session.resource(
        "s3",
        endpoint_url="https://storage.googleapis.com",
        config=Config(signature_version="s3v4"),
    )
    bucket = s3.Bucket(CONFIG["bucket"]["name"])
    return bucket


def list_bucket_keys() -> List[Text]:
    """Listing keys/filenames in bucket.
    Returns:
        List[Text] -- List of keys/filenames.
    """
    bucket = get_bucket()
    bucket_keys = [obj.key.replace("+", " ") for obj in bucket.objects.all()]
    return bucket_keys


def write_to_bucket(filename: Text, content: Text) -> Text:
    """Write data to 'BUCKET_RAW_DIR' within bucket.
    Arguments:
        filename {Text} -- Name of file to write to.
        content {Text} -- Content of file (e.g. UTF-8 text).
    Returns:
        Text -- Path of file to which data was written.
    """
    bucket = get_bucket()
    key = BUCKET_RAW_DIR + filename
    bucket.put_object(Bucket=CONFIG["bucket"]["name"], Body=content, Key=key)
    return key.replace("+", " ")


def download_raw_data_from_bucket():
    """Download scraped raw JSON data from bucket."""
    DIR_RAW.mkdir(parents=True, exist_ok=True)  # create target directory, if not exists
    bucket = get_bucket()
    keys_bucket = [
        key
        for key in list_bucket_keys()
        if (key.startswith(BUCKET_RAW_DIR) and key.endswith(".txt"))
    ]
    # filter downloadable files by what is downloaded already
    files_local = [
        filename for filename in os.listdir(str(DIR_RAW)) if filename != ".gitkeep"
    ]
    keys_download = [key for key in keys_bucket if Path(key).name not in files_local]
    # download files
    for key in keys_download:
        logging.info(f"Downloading from bucket: {key}")
        filename = str(DIR_RAW / Path(key).name)
        bucket.download_file(key, filename)
    if not keys_download:
        logging.info("Local raw data was up to date.")
