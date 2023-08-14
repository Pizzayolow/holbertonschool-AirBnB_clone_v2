#!/usr/bin/python3

from flask import Flask
"""open the applicatation"""
app = Flask(__name__)

"""decorator"""
@app.route('/', strict_slashes=False)
def route():
    """return SHello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
