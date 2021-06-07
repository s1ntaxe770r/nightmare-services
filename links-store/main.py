from os import link
from flask import Flask, jsonify, Response
from flask.globals import request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)





import redis 
from os import getenv
from typing import List


host:str =  getenv("REDIS_HOST")
port:str =  getenv("REDIS_PORT")




class Link:
    """
    Link class represents an image link 
    """
    def __init__(self,url:str) -> None:
        self.url = url
        



def add_link(link:Link) -> Link:
    """
    insert a new link into the cache 
    Input : Link
    Returns: Link
    """
    client = redis.Redis(host,port,0)
    client.rpush('links',link.url)
    return link.url


def get_links() -> List[bytes]:
    """
    Retrive all the links from the cache
    Returns: List
    """
    client = redis.Redis(host,port,0)
    links = client.lrange('links',0,-1)
    return links 


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


