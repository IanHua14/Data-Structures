from pathlib import Path

import requests
from flask import Flask, render_template, request

from flask import Blueprint

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/N&A')
def NaA():
    return render_template("N%A.html")

@app.route('/CT')
def CT():
    return render_template("CT.html")

@app.route('/DOP')
def DOP():
    return render_template("DOP.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
