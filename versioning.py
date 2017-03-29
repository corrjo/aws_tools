import boto3
from botocore.client import Config

s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))
bucketList = s3.buckets.all()

for bucket in bucketList:
    bucket_versioning = s3.BucketVersioning(bucket.name)
    bucket_versioning.enable()
    print bucket.name, 'versioning enabled'
