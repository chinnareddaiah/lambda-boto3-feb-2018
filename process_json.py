import json

file = open('employee.json').read()

# Convert json file as as dict
json_dict = json.loads(file)

name = json_dict['Name']
state = json_dict['Address']['State']

print('Name is {}'.format(name))
print('State is {}'.format(state))
