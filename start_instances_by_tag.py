import boto3

ec2 = boto3.resource('ec2')

'''
Filter by tags
  Key = Scheduled
  Values = yes
'''

instances_filter = [
        {
            'Name': 'tag:Scheduled',
            'Values': [
                'yes'
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped'
            ]
        }
    ]
# instances = [EC2.Instance]

instances = ec2.instances.filter(Filters=instances_filter)

for instance in instances:
    print(instance)
    instance.start()