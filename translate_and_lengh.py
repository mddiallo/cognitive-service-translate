import requests, uuid, json, infos

subscription_key = infos.subscription_key
region = infos.region
endpoint = infos.endpoint

# Add your subscription key and endpoint
# subscription_key = "YOUR_SUBSCRIPTION_KEY"
# endpoint structure = "https://api.cognitive.microsofttranslator.com"

subscription_key = infos.subscription_key
region = infos.region
endpoint = infos.endpoint



# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = region #"YOUR_RESOURCE_LOCATION"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': 'es',
    'includeSentenceLength': True
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Can you tell me how to get to Penn Station? Oh, you aren\'t sure? That\'s fine.'
}]
request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))