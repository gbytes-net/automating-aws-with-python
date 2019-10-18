# coding: utf-8
import boto3
session = boto3.Session
ec2 = session.resource('ec2)
ec2 = session.resource('ec2')
session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')
ec2.describe_instances()
ec2.instances
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.image('ami-0b69ea66ff7391e80')
img = ec2.Image('ami-0b69ea66ff7391e80')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20190823.1-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}] 
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-922914f7')
img_aspe2.name
img_apse2.name
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ec2_us2 = session.resource('ec2', region_name='us-east-2')
img_us2 = ec2_apse2.Image('ami-00c03f7f7f2ec15c3')
img.name
img_us2.name
img_us2 = ec2_us2.Image('ami-00c03f7f7f2ec15c3')
img_us2.name
img.name
img
img_us2
key
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_us2.images.filter(Owners=['amazon'], Filters=filters))
img
instances = ec2.create_instances(ImageID=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances
ec2.Instance(id='i-0c10f9276a6420054')
inst = instance[0]
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.reload
inst.reload()
inst.public_dns_name()
inst.public_dns_name
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])

    
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol'='TCP', 'IpRanges': [{'CidrIp': '184.164.163.196/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '184.164.163.196/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
