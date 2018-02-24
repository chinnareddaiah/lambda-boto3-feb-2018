import boto3
client =  boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=[
        'i-0774bc0e744476671',
        'i-0a58f7aea982565ea'
    ])