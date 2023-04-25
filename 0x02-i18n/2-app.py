#!/usr/bin/env python3
"""Flask Babel basic"""

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')

@babel.localeselector
def get_locale():
    """get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def hello():
    """hello function"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
