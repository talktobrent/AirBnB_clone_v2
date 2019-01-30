#!/usr/bin/python3
""" flask module """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns string at root request """
    return ("Hello HBNB!")


app.env = 'development'
app.run(host='0.0.0.0', port=5000)
