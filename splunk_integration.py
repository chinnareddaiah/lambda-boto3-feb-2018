import requests
import json
SPLUNK_URL = 'http://52.37.7.77:8088/services/collector/event'

SPLUNK_TOKEN = '26b16c9a-beea-4738-b044-e2b9067e82f3'

headers = {}

headers['Authorization'] = 'Splunk {}'.format(SPLUNK_TOKEN)


payload = {}

payload.update({"index": "devops"})
payload.update({"sourcetype": "ecs_secstack_logs"})
payload.update({"source": "python"})
payload.update({"host": "prod"})
payload.update({"event": 'Dummy event'})


response = requests.post(SPLUNK_URL, data=json.dumps(payload), headers=headers)

print(response)