#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    data = storage.all(State)
    return render_template('7-states_list.html', data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
