#Copy the previous task to a new script that starts a Flask web application
'''Importing Flask form flask'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format((text).replace("_", " "))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text ='is cool'):
    return 'Python {}'.format((text).replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")