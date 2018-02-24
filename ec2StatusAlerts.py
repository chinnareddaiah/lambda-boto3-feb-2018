import boto3
client = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    reservations = client.describe_instances()
    
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

