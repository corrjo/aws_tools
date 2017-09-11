from __future__ import print_function
import boto3

ec2 = boto3.resource('ec2', region_name='us-west-2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:sleep', 'Values': ['true']}])
for instance in instances:
    print ('shutting down', instance.id, instance.instance_type)
    instance.stop()


