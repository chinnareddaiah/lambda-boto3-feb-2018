import boto3

'''
 Print all instance ids and their associated volumes
'''

ec2 = boto3.client('ec2')
sns = boto3.client('sns')
reservations = ec2.describe_instances()

instance_status = []
for reservation in reservations['Reservations']:
    for instance in reservation['Instances']:
        state = instance['State']['Name']
        id = instance['InstanceId']
        instance_status.append('Instance Id is {} and State is {}'.format(id,state))

print(instance_status)
# Send email
sns.publish(TopicArn='arn:aws:sns:us-west-2:915530126681:weekend-alerts',
    Message=str(instance_status),
    Subject='EC2 Status')