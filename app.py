from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

@app.route("/")
def index():
    tanggal = request.args.get("tanggal", "")

    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": API_KEY}

    if tanggal:
        params["date"] = tanggal

    response = requests.get(url, params=params)
    data = response.json()

    return render_template("index.html", data=data, tanggal=tanggal)

if __name__ == "__main__":
    app.run(debug=True)