# coding: utf-8
import boto3
session = boto3.Session
s3 = session.resource('s3')
session = boto3.Session()
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='maurovideolyzervideos')
from pathlib import path
from pathlib import Path
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '/Users/mauricioroda/Downloads/*.mp4')
pathname = '~/Downloads/Man Texting On The Street.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
path
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('recognition')
rekognition_client = session.client('rekognition')
s3
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
job_id
result = rekognition.client.get_label_detection(JobId=job_id)
result = rekognition_client.get_label_detection(JobId=job_id)
result
result
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.key()
result.keys()
resul['JobStatus']
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
