""" Utils to interact with s3 bucket. """

import re
from typing import Text

import boto3
from botocore.client import Config


# s3 bucket
BUCKET_URL = "https://s3.fr-par.scw.cloud"
BUCKET_NAME = "immo-scraper"
BUCKET_KEY_ID = "SCWXCS9VG5RY2DBM8RRQ"
BUCKET_REGION = "fr-par"
BUCKET_FOLDER = "nestoria/"
# path to credentials
CREDENTIALS_PATH = "secret/bucket.txt"


def get_bucket():
    """Connect to S3 bucket"""
    ACCESS_KEY = "GOOGCUKVXASYVZCKAANOB4OR"
    SECRET_KEY = open("secret/gs_secret_key.txt", "r").read()

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name="US-CENTRAL1",
    )

    s3 = session.resource(
        "s3",
        endpoint_url="https://storage.googleapis.com",
        config=Config(signature_version="s3v4"),
    )

    bucket = s3.Bucket("immo-scraper")
    return bucket


def read_credentials() -> Text:
    with open(CREDENTIALS_PATH, "r") as f:
        secret_key = f.read()
        secret_key_clean = re.sub("[^a-z0-9\\-]", "", secret_key)
    return secret_key_clean


def print_bucket_contents() -> None:
    bucket = get_bucket()
    for obj in bucket.objects.all():
        key = obj.key
        print(f"key: {key}")


def write_to_s3(filename: Text, content: Text) -> None:
    bucket = get_bucket()
    key = BUCKET_FOLDER + filename
    bucket.put_object(Bucket=BUCKET_NAME, Body=content, Key=key)
