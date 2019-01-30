#!/usr/bin/python3
""" flask module """

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)

state_list = [value for key, value in storage.all("State").items()]
amenity_list = [value for key, value in storage.all("Amenity").items()]


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_html():
    """ displays dynamic html foir hbnb """
    return(render_template('10-hbnb_filters.html',
           state_list=state_list, amenity_list=amenity_list))


@app.teardown_appcontext
def closer():
    """ closes storage """
    storage.close()


if __name__ == '__main__':
    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
