

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
params = '&to=fr'
constructed_url = endpoint + path + params

# create a function
def translate(en):
    body = [{'text': en}]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    return (response[0]['translations'][0]['text'])

# example of the call
df = pd.DataFrame({'English': ['Hello', 'today', 'goodbye']})
df['French'] = df['English'].apply(translate)
df
