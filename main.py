import requests
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import SelectionForm, BookForm
import os


API_KEY = 'jb5dgzd8zO_V2ej8YPHl' # os.environ.get("API_KEY")
USERNAME = 'okamiryuku@gmail.com'
BREWERY_ENDPOINT = 'https://api.openbrewerydb.org/v1/breweries'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/city', methods=["GET", "POST"])
def city():
    if request.method == "POST":
        city = request.form.get('name')
        return render_template("city.html", data=data)

    return render_template("index.html")


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selection = request.form.get('selection').lower()
        return redirect(url_for(f"{selection}"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)