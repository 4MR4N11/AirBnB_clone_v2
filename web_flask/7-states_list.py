#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """ Returns a string at the /states_list route with a variable as an
    int and renders an html template """
    data = storage.all(State).values()
    return render_template('7-states_list.html', states=data)


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)
