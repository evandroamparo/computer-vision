from flask import Flask, request
from image_describer import describe_image
from flask import jsonify

app = Flask(__name__)

@app.route("/describe")
def describe_api():
    url = request.args.get('url')
    description = describe_image(url)
    api_response = {}
    api_response["description"] = description[0]
    api_response["confidence"] = round(description[1])
    return jsonify(api_response)