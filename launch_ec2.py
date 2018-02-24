import boto3

client = boto3.client('ec2',region_name='us-west-2')

client.run_instances(ImageId='ami-f2d3638a',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=2)