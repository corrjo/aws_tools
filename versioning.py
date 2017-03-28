import boto3
import boto
from boto.s3.connection import S3Connection
from botocore.client import Config

s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))
connect = boto.connect_s3()
buckets = connect.get_all_buckets()

for i in buckets:
    bucket_versioning = s3.BucketVersioning(i.name)
    bucket_versioning.enable()
    print i.name, 'versioning enabled'
