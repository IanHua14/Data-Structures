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


@app.route('/NaA')
def NaA():
    return render_template("NaA.html")

@app.route('/CT')
def CT():
    return render_template("CT.html")

@app.route('/DOP')
def DOP():
    return render_template("DOP.html")

@app.route('/5.1.2')
def five1():
    return render_template("5.1.2.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
