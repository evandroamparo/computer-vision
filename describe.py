from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

def describe(image_path):
    endpoint = os.getenv("COMPUTER_VISION_ENDPOINT")
    subscription_key = os.getenv("COMPUTER_VISION_SUBSCRIPTION_KEY")

    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(subscription_key))

    if (not os.path.isfile(image_path)):
        description_results = computervision_client.describe_image(
            image_path)
    else:
        with open(image_path, "rb") as image:
            description_results = computervision_client.describe_image_in_stream(
                image)

    if (len(description_results.captions) == 0):
        return ("", 0)
    else:
        return (description_results.captions[0].text, description_results.captions[0].confidence * 100)

