#!/usr/bin/env python3
"""
6. Use user locale

Starting a web application listenting on
0.0.0.0, port 5000
"""
from flask import Flask, render_template, request, g
from typing import Union, Dict
from flask_babel import Babel
import pytz


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
users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    This function determine the lanaguage to be used
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    header_lang = request.headers.get('locale')
    if header_lang in app.config['LANGUAGES']:
        return header_lang
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> Union[str, None]:
    """
    This method determine the timezone to be used
    """
    tz = request.args.get('timezone')
    user_tz = g.user.get('timezone') if g.user else None
    timezone = tz or user_tz

    if timezone:
        try:
            pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    return timezone


def get_user() -> Union[Dict, None]:
    """
    This function returns a user dictionary or none if the user ID
    cannot be found
    """
    _id = request.args.get('login_as')
    user = users.get(int(_id)) if _id else None
    return user


@app.before_request
def before_request() -> None:
    """
    This function runs before each request gets processed
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    This is the entry point to the application
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
