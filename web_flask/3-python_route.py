from flask import Flask
from markupsafe import escape
""" Flask web application"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Returns a string at the root route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Returns a string at the /hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ Returns a string at the /c route with a variable """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Returns a string at the /python route with a variable """
    return "Python {}".format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)
