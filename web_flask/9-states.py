#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the storage"""
    storage.close()


@app.route("/states", strict_slashes=False)
def list_states():
    """ Returns data from storage and renders an html template """
    data = storage.all(State).values()
    return render_template('7-states_list.html', states=data)


@app.route("/states/<id>", strict_slashes=False)
def show_state_by_id(id):
    """ Returns data from storage and renders an html template """
    data = storage.all(State).values()
    state = None
    for item in data:
        if item.id == id:
            state = item
            break
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)
