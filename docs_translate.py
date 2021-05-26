import requests, infos

# Endpoint of your translator Service on Azure
endpoint = "https://mdtranslator25.cognitiveservices.azure.com/translator/text/batch/v1.0-preview.1"
subscriptionKey =  infos.subscriptionKey # Add your subscription key here!
path = '/batches'
constructed_url = endpoint + path

payload= {
    "inputs": [
        {
            "source": {
                "sourceUrl": "https://mdsourcedocs.blob.core.windows.net/demo1?sv=2020-04-08&st=2021-05-18T15%3A32%3A05Z&se=2021-05-28T15%3A32%3A00Z&sr=c&sp=rl&sig=6cA7hWg%2F63Jyq6xur8qrySewhV1pSaJ4ds%2Bbj2u3klo%3D",
                    # Storage ource of the document 
                "storageSource": "AzureBlob",
                "language": "en",
                "filter":{
                    #"prefix": "Demo_1/"
                }
            },
            "targets": [
                {
                    "targetUrl": "https://mdtargetdocs.blob.core.windows.net/demo1?sv=2020-04-08&st=2021-05-18T15%3A34%3A57Z&se=2021-05-28T15%3A34%3A00Z&sr=c&sp=wl&sig=RPhBNbnmEM%2BS16cZVwnG3v6t46lZv4wm0%2BlaIeXb%2B60%3D",
                        #Target Storage for the translated document
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": "es"
                }
            ]
        }
    ]
}
headers = {
  'Ocp-Apim-Subscription-Key': subscriptionKey,
  'Content-Type': 'application/json'
}

response = requests.post(constructed_url, headers=headers, json=payload)

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\nresponse headers: {response.headers}')