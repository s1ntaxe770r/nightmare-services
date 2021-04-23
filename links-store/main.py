from os import link
from flask import Flask, jsonify,make_response
from flask.globals import request
from utils import get_links, add_link, Link
import json

app = Flask(__name__)


@app.route("/links/get", methods=["GET"])
def retrive_links():
    response = make_response()
    bytelist = get_links()
    results = []
    for link in bytelist:
        string = link.decode()
        results.append(string)
    response = {"images": results}
    # CORS
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return jsonify(response),200


@app.route("/links/store",methods=["POST"])
def insert_link():
    response = make_response()
    request_data = request.json
    image_name = request_data['image_name']
    link = Link(image_name)
    return_val = add_link(link)
    # CORS
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return jsonify({'sotored': return_val})




if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)