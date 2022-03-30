import boto3
s3 = boto3.client('s3', endpoint_url='http://sp22-cs240-001.cs.illinois.edu:9000', aws_access_key_id='minioadmin', aws_secret_access_key='minioadmin')

# Reading data from S3:
obj = s3.get_object(Bucket="cs240", Key="session_data")
f = obj["Body"]

print("== S3 Response ==")
print(obj)
print()

print("== Contents ==")
print(f.read().decode("utf-8"))
print()