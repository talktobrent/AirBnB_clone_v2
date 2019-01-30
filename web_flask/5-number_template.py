#!/usr/bin/python3
""" flask module """

from flask import Flask
from flask import render_template_string


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
    """ returns format string with given text  """
    return ("C " + text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text="is cool"):
    """ returns format string with given text value or default """
    return ('Python ' + text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def test_int(n):
    """ returns format string with n """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def test_int_html(n):
    """ returns template with n """
    return(render_template_string('''<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {{ number }}</H1>
    </BODY>
</HTML>''', number=n))


app.env = 'development'
app.run(host='0.0.0.0', port=5000)
