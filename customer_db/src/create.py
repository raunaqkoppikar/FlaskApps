from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

db.create_all()