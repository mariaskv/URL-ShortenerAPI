from typing import final
from urllib import request
from flask import Blueprint, jsonify, render_template
from shorty.providers.provider import *
import re
import flask
import json
import cgi


# regex implements a regular expression that checks if a url is correct or not
regex = re.compile(
        r'^(?:http)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

api = Blueprint('api', __name__)


# Root endpoint that opens the homepage of the server(index.html)
@api.route("/")
def short():
    return render_template("index.html")

# POST endpoint. Takes a string in json format and looks for a url inside of it.
# Validates this url or returns an error. Also look for a provider and check if it is correct
# Lastly returns the given string transformed by the provider

@api.route('/shortlinks/', methods=['POST'])
def create_shortlink():
    
    # Get the data from the html form
    form = dict(flask.request.form)
    
    if form is None:
        return "Error. Please provide data."

    # Take the first value from the dict
    data1 = form['name']

    if data1 is None:
        return "Error. Please provide data."

    # Turn this data to json format
    data = json.loads(data1)

    print(data)

    if data is None:
        return "Error. Please provide data."

    if 'url' not in data:
        return "Error. This data does not contain an url"

    url_new = Provider(data)

    url = url_new.url

    # get the provider given in the input
    provider = url_new.provider

    # short() function returns the initial url after it has been shortened
    new = url_new.short()

    if new == None:
        return "Error. Please provide a provider between bitly or tinyurl." 

    if re.match(regex, url) is None:
        return "Error. Please provide a correct url."

    if provider not in ["bitly", "tinyurl"]:
        return "Error. Please provide a provider between bitly or tinyurl." 

    final = "{url:" +  url + ", link:" + new + "}"

    return jsonify(final), 200

# GET endpoint that returns an error when the user tries to shorten an url through GET 
@api.route('/shortlinks', methods=['GET'])
def create_shortlink_get():
    return "Error. Please try through POST"
