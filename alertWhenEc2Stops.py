import boto3
sns = boto3.client('sns')
def lambda_handler(event, context):
    
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']
    message = 'Instance with Id {} is {}'.format(instance_id,state)
    
    sns.publish(TopicArn='arn:aws:sns:us-west-2:915530126681:weekend-alerts',
    Message=message,
    Subject='EC2 Status')

