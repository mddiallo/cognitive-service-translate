# Example for translating one sentence

import os, requests, uuid, json, infos, ssl
import pandas as pd
subscription_key = infos.subscription_key
region = infos.region
endpoint = infos.endpoint

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

path = '/translate?api-version=3.0'
params = '&to=fr&to=sl'
constructed_url = endpoint + path + params

# create body
body = [{
    'text' : 'Hello Sam, how are you in this sunny friday?'
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))