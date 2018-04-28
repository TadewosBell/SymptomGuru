from flask import Flask, jsonify
from flask_pymongo import PyMongo
from Surgeries import PageScrape
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'symptomguru'
app.config['MONGO_URI'] = 'mongodb://hacker1:PussyMoneyWeed@ds261429.mlab.com:61429/symptomguru'

mongo = PyMongo(app)

@app.route('/add')
def add():
	procedures = mongo.db.procedures
	procedures.insert(PageScrape()) 
	return 'Success'

if __name__ == '__main__':
	app.run(debug=True)
