from flask import Flask
from flask.templating import render_template
from flask_cors import CORS
from os import getenv
import requests 



app = Flask(__name__)
CORS(app)


links_api = getenv("LINKS_SERVER")
image_server = getenv("IMAGE_SERVER")




@app.route("/")
def index():
    links = requests.get(links_api+"/links/get").json()
    image_urls = []
    for link in links["images"]:
        url = image_server+"/images/"+link
        image_urls.append(url)
    return render_template("index.html",image_urls=image_urls)


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
