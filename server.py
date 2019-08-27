from flask import Flask, request
from modules import netflix, location
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


## Home

@app.route("/", methods=['GET', 'POST'])
def home():
    return "Welcome to my API."


## Netflix

@app.route("/new", methods=['GET', 'POST'])
def new():
    req = request.json
    location = req['code']
    return netflix.getNewContent(location, "get")


@app.route("/expire", methods=['GET', 'POST'])
def expire():
    req = request.json
    location = req['code']
    return netflix.getExpiringContent(location, "get")


## Location

@app.route("/location", methods=['GET', 'POST'])
def loc():
    req = request.json
    place = req['location']
    return location.findCountry(place)

    
if __name__ == "__main__":
    app.run(debug=True)
