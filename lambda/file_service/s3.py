"""
S3 module
"""

import boto3
import botocore

def file_exists(bucket:str, path: str):
    """
    Example function
    """

    client = boto3.client("s3")

    try:
        return client.head_object(Bucket=bucket, Key=path)
    except botocore.exceptions.ClientError as exception:
        print(exception)
        return False
    except (
        client.exceptions.NoSuchBucket,
        client.exceptions.NoSuchKey
    ) as exception:
        print(exception)
        return False
