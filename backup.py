#!/usr/bin/env python

import sys

import boto3
import requests
from requests_aws4auth import AWS4Auth

host = sys.argv[1]
snap = sys.argv[2]

host = ("https://%s/" % host) # include https:// and trailing /

region = 'us-east-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# # Take snapshot
#
path = '_snapshot/s3-snapshot/%s' % snap
url = host + path

r = requests.put(url, auth=awsauth, verify=False)

print(r.status_code)
print(r.text)
