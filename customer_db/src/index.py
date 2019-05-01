from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.sqlite3'

db = SQLAlchemy(app)
class Customer(db.Model):
	id = db.Column('customer_id', db.Integer, primary_key = True)
	name = db.Column(db.String(256))
	city = db.Column(db.String(256))

def __init__(self, name, city):
	self.name = name
	self.city = city

@app.route('/')
def getIndex():
	return render_template('index.html')

@app.route('/create/')
def create():
	return render_template('new.html')

@app.route('/retrieve/')
def showAll():
	customers = Customer.query.all()
	return render_template('list.html', customers = customers)

@app.route('/update/')
def update():
	customers = Customer.query.all()
	return render_template('update.html', customers = customers)

@app.route('/delete/')
def delete():
	customers = Customer.query.all()
	return render_template('delete.html', customers = customers)

@app.route('/new/', methods=['post'])
def new():
	obj = Customer()
	obj.name = request.form['name']
	obj.city = request.form['city']
	db.session.add(obj)
	db.session.commit()
	customers = Customer.query.all()
	return render_template('list.html', customers = customers)

@app.route('/modify/', methods=['post'])
def modify():
	cust_id = request.form['id']
	newname = request.form['name']
	newcity = request.form['city']
	customer = Customer.query.filter_by(id=cust_id).first()
	customer.name = newname
	customer.city = newcity
	db.session.commit()
	customers = Customer.query.all()
	return render_template('list.html', customers = customers)

@app.route('/remove/', methods=['post'])
def remove():
	id = request.form['id']
	name = request.form['name']
	city = request.form['city']
	customer = Customer.query.filter_by(id=id).first()
	db.session.delete(customer)
	db.session.commit()
	customers = Customer.query.all()
	return render_template('list.html', customers = customers)

if __name__ == '__main__':
	app.run(debug = True)