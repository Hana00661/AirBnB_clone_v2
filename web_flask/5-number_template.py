#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """display "HBNB"
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """display "C", followed by the value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """display "Python", followed by the value of the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """display "n is a number" only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template_route(n):
    """display a HTML page only if n is an integer
    """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(debug=True)
