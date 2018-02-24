import boto3

ec2 = boto3.resource('ec2')

# Create a filter with stopped state

stopped_instances = [
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        }
    ]

# instances = [EC2.Instance]

instances = ec2.instances.filter(Filters=stopped_instances)

for instance in instances:
    print(instance)
    instance.start()