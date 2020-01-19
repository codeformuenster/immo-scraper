""" Utils to interact with s3 bucket. """

import re
from typing import Text

import boto3

# s3 bucket
BUCKET_URL = "https://s3.fr-par.scw.cloud"
BUCKET_NAME = "codeformuenster"
BUCKET_KEY_ID = "SCWXCS9VG5RY2DBM8RRQ"
BUCKET_REGION = "fr-par"
BUCKET_FOLDER = "immoscout/"
# path to credentials
CREDENTIALS_PATH = "secret/bucket.txt"


def read_credentials() -> Text:
    with open(CREDENTIALS_PATH, "r") as f:
        secret_key = f.read()
        secret_key_clean = re.sub("[^a-z0-9\\-]", "", secret_key)
    return secret_key_clean


def get_bucket():
    BUCKET_SECRET_KEY = read_credentials()
    session = boto3.Session(region_name=BUCKET_REGION)
    s3 = session.resource(
        service_name="s3",
        endpoint_url=BUCKET_URL,
        aws_access_key_id=BUCKET_KEY_ID,
        aws_secret_access_key=BUCKET_SECRET_KEY,
    )
    bucket = s3.Bucket(BUCKET_NAME)
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
