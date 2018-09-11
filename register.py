#!/usr/bin/env python

import sys

import boto3
import requests
from requests_aws4auth import AWS4Auth

host = sys.argv[1]
bucket = sys.argv[2]

host = ("https://%s/" % host)
region = 'us-east-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


# Register repository

path = '_snapshot/s3-snapshot' # the Elasticsearch API endpoint
url = host + path

print ("%s%s" % (host,path))
payload = {
  "type": "s3",
  "settings": {
    "bucket": "%s" % (bucket),
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::005956675899:role/es-snapshot-access"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers, verify=False)

print(r.status_code)
print(r.text)

