#!/usr/bin/env python3
"""
A basic flask app

Starting a web application listenting on
0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    This is the entry point to the application
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
