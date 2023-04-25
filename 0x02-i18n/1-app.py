#!/usr/bin/env python3
"""Flask Babel basic"""

from flask_babel import Babel, request
from flask import Flask, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'



@app.route('/', strict_slashes=False)
def hello():
    """hello function"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run()




