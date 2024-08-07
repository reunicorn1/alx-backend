#!/usr/bin/env python3
"""
2. Get locale from request

Starting a web application listenting on
0.0.0.0, port 5000
"""
from flask import Flask, render_template, request
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

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    This function determine the lanaguage to be used
    """
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    This is the entry point to the application
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
