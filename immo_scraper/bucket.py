import boto3

BUCKET_NAME = "codeformuenster"


def read_credentials():
    with open("secret/bucket.txt", "r") as f:
        creds = f.read().split("\n")
        BUCKET_URL = creds[0]
        BUCKET_SECRET = creds[1]
        BUCKET_ID = creds[2]
    return BUCKET_URL, BUCKET_SECRET, BUCKET_ID


def get_bucket():
    BUCKET_URL, BUCKET_SECRET, BUCKET_ID = read_credentials()
    session = boto3.Session(region_name="fr-par")
    s3 = session.resource(
        service_name="s3",
        endpoint_url=BUCKET_URL,
        aws_access_key_id=BUCKET_ID,
        aws_secret_access_key=BUCKET_SECRET,
    )
    bucket = s3.Bucket(BUCKET_NAME)
    return bucket


def print_bucket_files():
    bucket = get_bucket()
    for obj in bucket.objects.all():
        key = obj.key
        print(f"key: {key}")


def write_to_s3(filename, content):
    bucket = get_bucket()
    key = "immoscout/" + filename
    bucket.put_object(Bucket=BUCKET_NAME, Body=content, Key=key)
