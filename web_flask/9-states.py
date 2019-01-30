#!/usr/bin/python3
""" flask module """

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)

st_list = [value for key, value in storage.all("State").items()]


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_html(id=None):
    """ gets one state and cities, or all states and outputs in html """
    if id:
        for x in st_list:
            if x.id == id:
                return(render_template('9-states.html', state=x))
    return(render_template('7-states_list.html', states_list=st_list))


@app.route('/cities_by_states', strict_slashes=False)
def all_states_with_cities_html():
    """ gets all states and cities and outputs in html """
    return(render_template('8-cities_by_states.html', states_list=st_list))


@app.teardown_appcontext
def closer(self):
    """ closes storage """
    storage.close()


if __name__ == '__main__':
    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
