""" Utils to interact with s3 bucket. """

import os
from typing import Text, List

import boto3
from botocore.client import Config

from immo_scraper.io.paths import BUCKET_FOLDER


def get_bucket():
    """Get bucket object, e.g. to write data.
    Returns:
        boto3.resources.factory.s3.Bucket -- Bucket object.
    """
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


def list_bucket_keys() -> List[Text]:
    """Listing keys/filenames in bucket.
    Returns:
        List[Text] -- List of keys/filenames.
    """
    bucket = get_bucket()
    bucket_keys = [obj.key for obj in bucket.objects.all()]
    return bucket_keys


def write_to_bucket(filename: Text, content: Text) -> Text:
    """Write data to 'BUCKET_FOLDER' within bucket.
    Arguments:
        filename {Text} -- Name of file to write to.
        content {Text} -- Content of file (e.g. UTF-8 text).
    Returns:
        Text -- Path of file to which data was written.
    """
    bucket = get_bucket()
    key = BUCKET_FOLDER + filename
    bucket.put_object(Bucket=os.environ["BUCKET_NAME"], Body=content, Key=key)
    return key.replace(" ", "+")
