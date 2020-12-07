from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import sys, os, requests, uuid, json

try:
    image_path = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <image path or URL>")

# Best practice is to read this key from secure storage, 
# for this example we'll embed it in the code.
endpoint = os.getenv("COMPUTER_VISION_ENDPOINT")

# Create the computer vision client
computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(os.getenv("COMPUTER_VISION_SUBSCRIPTION_KEY")))

if (not os.path.isfile(image_path)):
    # Get caption for a remote image, change to your own image URL as appropriate
    # remote_image_url = "https://preview.redd.it/6eiz82hakfy51.png?width=640&crop=smart&auto=webp&s=03ec43167d2dacb7c1963a2e3da9adc4d2d9eeef"
    description_results = computervision_client.describe_image(
        image_path)
else:
    # Get caption for a local image, change to your own local image path as appropriate
    # local_image_path = "<replace with local image path>"
    with open(image_path, "rb") as image:
        description_results = computervision_client.describe_image_in_stream(
            image)

# Get the first caption (description) from the response
if (len(description_results.captions) == 0):
    image_caption = "No description detected."
else:
    image_caption = description_results.captions[0].text
    print("{:.0f}% de certeza que é...".format(description_results.captions[0].confidence * 100))


# print("Description of image:", image_caption)

# ####################################

import requests, uuid, json

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
    'text': image_caption
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(response[0]['translations'][0]['text'])