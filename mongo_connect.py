from flask import Flask, jsonify
from flask_pymongo import PyMongo
from Surgeries import allLinks
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'symptomguru'
app.config['MONGO_URI'] = 'mongodb://hacker1:PussyMoneyWeed@ds261429.mlab.com:61429/symptomguru'

mongo = PyMongo(app)

#@app.route('/add')
#def add():
#	procedures = mongo.db.procedures
#	surgeries = allLinks()
#	for key,values in surgeries.items():
#		procedures.insert({
#				'name':str(key),
#				'conditions':str(values)})  
#	return 'Success'

@app.route('/retrieve')
def retrieve():
	surgeries = mongo.db.procedures
	Tracheotomy = surgeries.find_one({'name':' Tracheotomy '})
	return(str(Tracheotomy))

if __name__ == '__main__':
	app.run(debug=True)

