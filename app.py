from flask import Flask, request
from image_describer import describe_image
from flask import jsonify

app = Flask(__name__)

@app.route("/describe")
def describe_api():
    url = request.args.get('url')
    return jsonify(describe_image(url))