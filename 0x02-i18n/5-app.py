#!/usr/bin/env python3
"""
5. Mock logging in

Starting a web application listenting on
0.0.0.0, port 5000
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    This class stores the configuraiton of the web application
    server

    Properties:
    ----------
    LANGUAGES: The list of supported languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    This function determine the lanaguage to be used
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


def get_user():
    """
    This function returns a user dictionary or none if the user ID
    cannot be found
    """
    users = {
            1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
            2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
            3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
            4: {"name": "Teletubby", "locale": None, "timezone":
                "Europe/London"},
        }
    _id = request.args.get('login_as')
    user = users.get(int(_id)) if _id else None
    return user


@app.before_request
def before_request():
    """
    This function runs before each request gets processed
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    This is the entry point to the application
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
