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


if __name__ == '__main__':
    app.run()
