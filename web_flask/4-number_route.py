#!/usr/bin/python3
""" Program that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
In Route /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display a custom String on main Route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def second_task():
    """ This function returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def third_task(text):
    """ This function returns a string.
    It also takes a variable
    """
    return 'C %s' % text.replace('_', ' ')

@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def fourth_task(text):
    """ This function returns a string.
    It also takes a variable
    """
    return 'Python %s' % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def fifth_task(n):
    """ This function returns a string.
    It also takes a variable
    """
    return '%i is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0')
