import os
import boto3
from boto3.s3.transfer import S3Transfer

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def create_s3_client():
    client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    return client


def create_s3_transfer():
    client = create_s3_client()
    return S3Transfer(client)
