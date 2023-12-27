#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """Displays 'C' followed by the value of <text>."""
    #Replace underscores with spaces in the text variable
  formatted_text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    #start the flask development server
    #Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host="0.0.0.0",  port=5000)

