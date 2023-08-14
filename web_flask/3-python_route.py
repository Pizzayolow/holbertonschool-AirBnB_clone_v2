#!/usr/bin/python3
"""import flask and use it"""
from flask import Flask
"""open the applicatation"""
app = Flask(__name__)

"""decorator"""


@app.route('/', strict_slashes=False)
def route():
    """return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def routehbnb():
    """return hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def route_c(text):
    """return a value"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def route_python(text):
    text = text.replace('_', ' ')
    return f"python {text}"


if __name__ == '__main__':
    app.run()
