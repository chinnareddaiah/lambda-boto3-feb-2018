import boto3

client = boto3.client('ec2')

instances = client.describe_instances();

for instance in instances['Reservations']:
    for x in  instance['Instances']:
        print('Instance id is {} '.format(x['InstanceId']))
        print('State is {} '.format(x['State']['Name']))
