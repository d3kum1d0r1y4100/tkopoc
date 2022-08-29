from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "D3ku Tko poc! "
