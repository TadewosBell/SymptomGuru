from flask import Flask, jsonify
from flask_pymongo import PyMongo
from mongo_connect import mongo 

from Surgeries import PageScrape

app = Flask(__name__)

@app.route('/')

def index():
	return jsonify(Procedures = PageScrape())

if __name__ == "__main__":
	app.run(debug =True, host='0.0.0.0', port=5000)

