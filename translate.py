import os, requests, uuid, json

def translate(text):
    # Add your subscription key and endpoint
    endpoint = os.getenv("TRANSLATOR_ENDPOINT")

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = os.getenv("TRANSLATOR_LOCATION")

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': 'pt'
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': os.getenv('TRANSLATOR_SUBSCRIPTION_KEY'),
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]['translations'][0]['text']
