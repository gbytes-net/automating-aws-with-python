# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-11-30T16:00:11.473Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAIKRAZZLCVSHZERBMY'}, 'requestParameters': {'sourceIPAddress': '184.164.163.196'}, 'responseElements': {'x-amz-request-id': '799B1164C61462B4', 'x-amz-id-2': 'q2JCYzGOegqpuaRDPrgdh2QoS0mhXVWzXE3/mcbt00IkOI4dUl6HZ6hGnOtY9QBxx8d/Zen8/F0='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '6a300d66-2470-4348-88c9-742598675028', 'bucket': {'name': 'maurovideolyzervideos123', 'ownerIdentity': {'principalId': 'ABUZSBA2DCT6Q'}, 'arn': 'arn:aws:s3:::maurovideolyzervideos123'}, 'object': {'key': 'Pexels+Videos+2880.mp4', 'size': 8123504, 'eTag': 'a705c560565ea3aae621383a33362f2e', 'sequencer': '005DE291FF62C6CE30'}}}]}
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
get_ipython().run_line_magic('save', 's3-event-example.py 1-7')
