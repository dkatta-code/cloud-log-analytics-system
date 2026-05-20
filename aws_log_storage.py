import boto3

from config import config

s3_client = boto3.client(
    "s3",
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.AWS_REGION
)

def upload_log_archive(
    file_path,
    s3_key
):

    s3_client.upload_file(
        file_path,
        config.S3_BUCKET,
        s3_key
    )

def upload_raw_log_payload(
    payload,
    s3_key
):

    s3_client.put_object(
        Bucket=config.S3_BUCKET,
        Key=s3_key,
        Body=payload
    )

def fetch_bucket_objects():

    response = s3_client.list_objects_v2(
        Bucket=config.S3_BUCKET
    )

    return response.get(
        "Contents",
        []
    )
