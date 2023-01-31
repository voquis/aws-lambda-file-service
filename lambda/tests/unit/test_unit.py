"""
File service unit tests
"""

from moto import mock_s3
from file_service import __version__
from file_service import s3
from .aws_utils import s3_create_bucket, s3_put_content


def test_version():
    """
    Test package version
    """
    assert __version__ == '0.1.0'


@mock_s3
def test_s3_no_such_bucket():
    """
    Test an S3 client error is captured
    """

    assert not s3.file_exists('non_existent_bucket', 'non_existent_key')

@mock_s3
def test_s3_no_such_key():
    """
    Test an S3 client error is captured
    """

    bucket = 'bucket_that_exists'
    path = '/path/that/does/not/exist'

    s3_create_bucket(bucket)
    assert not s3.file_exists(bucket, path)


@mock_s3
def test_file_exists_success():
    """
    Test file exists with success
    """

    # Create an S3 bucket

    bucket = 'test_bucket_for_file_exists_success'
    content = 'Content that exists'
    path = '/path/that/exists'

    s3_create_bucket(bucket)
    s3_put_content(bucket, path, content)

    assert s3.file_exists(bucket, path)
