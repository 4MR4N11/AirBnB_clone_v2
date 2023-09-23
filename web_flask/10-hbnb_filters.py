#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the storage"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def list_states():
    """ Returns data from storage and renders an html template """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)
