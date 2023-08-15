#!/usr/bin/python3
"""import flask and use it"""
from flask import Flask, render_template
from models import storage
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
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """verify if n is a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_body(n):
    """change a variable inside a thml body"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """check if the number is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a list of states"""
    states_list = storage.all("State")
    return render_template('7-states_list.html', states=states_list)

@app.teardown_appcontext
def teardown_db(err):
    storage.close()

if __name__ == '__main__':
    app.run()
