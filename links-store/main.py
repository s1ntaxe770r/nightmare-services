from os import link
from flask import Flask, jsonify, Response
from flask.globals import request
from flask_cors import CORS
from .utils import get_links, add_link, Link
import json

app = Flask(__name__)
CORS(app)

@app.route("/links/get", methods=["GET"])
def retrive_links():
    response = Response()
    bytelist = get_links()
    results = []
    for link in bytelist:
        string = link.decode()
        results.append(string)
    response = {"images": results}
    return jsonify(response),200


@app.route("/links/store",methods=["POST"])
def insert_link():
    response = Response()
    request_data = request.json
    image_name = request_data['image_name']
    link = Link(image_name)
    return_val = add_link(link)
    return jsonify({'stored': return_val})


