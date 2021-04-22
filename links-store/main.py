from os import link
from flask import Flask, jsonify
from flask.globals import request
from utils import get_links, add_link, Link
import json

app = Flask(__name__)


@app.route("/links/get", methods=["GET"])
def retrive_links():
    bytelist = get_links()
    results = []
    for link in bytelist:
        string = link.decode()
        results.append(string)
    response = {"images": results}
    return jsonify(response),200


@app.route("/links/store",methods=["POST"])
def insert_link():
    request_data = request.json
    image_name = request_data['image_name']
    link = Link(image_name)
    return_val = add_link(link)
    return jsonify({'sotored': return_val})




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)