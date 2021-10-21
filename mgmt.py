from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

screens = [
    {"name": "Screen 1", "ip": "10.0.196.210"}, 
    {"name": "Screen 2", "ip": "10.0.196.211"}, 
    {"name": "Screen 3", "ip": "10.0.196.212"}, 
    {"name": "Screen 4", "ip": "10.0.196.213"}, 
    {"name": "Screen 5", "ip": "10.0.196.214"}, 
    {"name": "Screen 6", "ip": "10.0.196.215"}
    ]
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', screens=screens)

