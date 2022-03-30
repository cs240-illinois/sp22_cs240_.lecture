import boto3
s3 = boto3.client('s3', endpoint_url='http://sp22-cs240-001.cs.illinois.edu:9000', aws_access_key_id='minioadmin', aws_secret_access_key='minioadmin')

# Create bucket if it does not exit:
try:
  s3.create_bucket(Bucket="cs240")
  print("Created `cs240` bucket!")
except:
  # bucket already exists
  print("Bucket `cs240` already exists!")

import json

# Add an object as a string:
s3.put_object(Bucket="cs240", Key="session_data", Body=json.dumps({"hello": "world"}))

# Upload a file:
s3.upload_file("cs240.png", Bucket="cs240", Key="profile-picture.png")
