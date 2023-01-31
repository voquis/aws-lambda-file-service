"""
AWS test utils
"""

from tempfile import NamedTemporaryFile
import boto3

def s3_create_bucket(bucket='test_bucket'):
    """
    Create an S3 bucket
    """

    client = boto3.client('s3')
    client.create_bucket(Bucket=bucket)

def s3_put_content(bucket='test_bucket', path='/test/key', content='test content'):
    """
    Create an S3 bucket
    """
    # Create temporary file to be uploaded
    tmp_file = None
    with NamedTemporaryFile(mode="w", delete=False, encoding='utf8') as file:
        tmp_file = file.name
        file.write(content)

    resource = boto3.resource('s3')
    bucket = resource.Bucket(bucket)
    with open(tmp_file, 'rb') as file:
        bucket.upload_fileobj(file, path)
