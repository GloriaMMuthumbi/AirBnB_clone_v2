#!/usr/bin/python3
"""Flask framework"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """return text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def dsiplay(text):
    """displays "Python ", followed by text value"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
