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


if __name__ == '__main__':
    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
