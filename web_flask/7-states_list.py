#!/usr/bin/python3
""" flask module """

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def all_states_html():
    """ gets all states and outputs in html """
    st_list = [value for key, value in storage.all("State").items()]

    return(render_template('7-states_list.html', states_list=st_list))


@app.teardown_appcontext
def closer():
    """ closes storage """
    storage.close()


if __name__ == '__main__':
    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
