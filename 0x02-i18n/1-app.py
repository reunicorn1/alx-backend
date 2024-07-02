#!/usr/bin/env python3
"""
1. Basic Babel setup

Starting a web application listenting on
0.0.0.0, port 5000
"""
from flask import Flask, render_template
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


@app.route('/', strict_slashes=False)
def index():
    """
    This is the entry point to the application
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
