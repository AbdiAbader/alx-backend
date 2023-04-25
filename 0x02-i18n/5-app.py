#!/usr/bin/env python3
""" Task3 """

from flask_babel import Babel
from flask import Flask, render_template, request, g


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', strict_slashes=False)
def hello():
    """hello function"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """get locale function"""
    if request.args.get('locale') and request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    
# babel.init_app(app, locale_selector=get_locale)

def get_user():
    """get user function"""
    logged = request.args.get("login_as")
    if logged:
        return users.get(int(logged))
    
    
@app.before_request
def handlerequest():
    """handlerequest function"""
    g.user = get_user()
    


if __name__ == "__main__":
    app.run()
