import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import os


API_KEY = os.environ.get("API_KEY")
BREWERY_ENDPOINT = 'https://api.openbrewerydb.org/v1/breweries'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/brewery')
def brewery():
    response = requests.get(url=BREWERY_ENDPOINT)
    data = response.json()
    return render_template("index.html", brewery=data)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)