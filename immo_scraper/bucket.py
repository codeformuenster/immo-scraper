""" Utils to interact with s3 bucket. """

import os
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
    session = boto3.Session(
        aws_access_key_id=os.environ["BUCKET_ACCESS_KEY"],
        aws_secret_access_key=os.environ["BUCKET_SECRET_KEY"],
        region_name=os.environ["BUCKET_REGION_NAME"],
    )
    s3 = session.resource(
        "s3",
        endpoint_url="https://storage.googleapis.com",
        config=Config(signature_version="s3v4"),
    )
    bucket = s3.Bucket(os.environ["BUCKET_NAME"])
    return bucket


def print_bucket_contents() -> None:
    bucket = get_bucket()
    for obj in bucket.objects.all():
        key = obj.key
        print(f"key: {key}")


def write_to_s3(filename: Text, content: Text) -> None:
    bucket = get_bucket()
    key = BUCKET_FOLDER + filename
    bucket.put_object(Bucket=BUCKET_NAME, Body=content, Key=key)
