import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('students')

item = {
    'student_id':'4',
    'mail':'geeta@javahome.in',
    'phone':'9999999999'
}
# Put item into dynamodb
table.put_item(Item=item)


# To get Item from dynamodb
item = table.get_item(Key={'student_id':'1'})
print(item['Item'])