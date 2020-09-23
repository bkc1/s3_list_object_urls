#!/usr/bin/env python3

import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b','--bucket', help='S3 bucket name', required=True)
parser.add_argument('-p','--path_style', help='Enable Legacy Path formatting', action='store_true')

args = parser.parse_args()

bucket_name = (args.bucket)

s3 = boto3.client('s3')
location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']

response = s3.list_objects(
    Bucket=bucket_name
)

#print(response)

for obj in response['Contents']:
#us-east-1 will have a null location 
  if args.path_style and location is None:
    key = obj['Key']
    path_style_url = "https://s3.amazonaws.com/%s/%s" % (bucket_name, key)
    print(path_style_url)
  elif args.path_style and location is not None:
    key = obj['Key']
    path_style_url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
    print(path_style_url)
  else:
    key = obj['Key']
    virtual_hosted_style_url = "https://%s.s3.amazonaws.com/%s" % (bucket_name, key)
    print(virtual_hosted_style_url)
