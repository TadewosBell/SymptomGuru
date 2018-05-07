from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
from Surgeries import allLinks
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'symptomguru'
app.config['MONGO_URI'] = 'mongodb://hacker1:PussyMoneyWeed@ds261429.mlab.com:61429/symptomguru'

mongo = PyMongo(app)

@app.route('/add')
def add():
	procedures = mongo.db.surgeries
	surgeries = allLinks()
	for key,values in surgeries.items():
		procedures.insert({
				'name':(str(key)).strip(),
				'information':str(values)})  
	return 'Success'
@app.route('/search')
def student():
	return render_template('search.html')


@app.route('/procedure')
def retrieve():
	if request.method == 'GET':
		surgeries = mongo.db.surgeries
		name = request.args['search']
		surgery = surgeries.find_one({'name':str(name)})
		return render_template('procedures.html', name=surgery)

if __name__ == '__main__':
	app.run(debug=True)
