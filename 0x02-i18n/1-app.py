#!/usr/bin/env python3
"""Flask Babel basic"""

from flask_babel import Babel, request
from flask import Flask, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def hello():
    """hello function"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run()




