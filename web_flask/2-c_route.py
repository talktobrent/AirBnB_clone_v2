#!/usr/bin/python3
""" flask module """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns string for location """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns string for location """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """ returns string for location, formatted with variable """
    return ("C " + text.replace('_', ' '))


app.env = 'development'
app.run(host='0.0.0.0', port=5000)
