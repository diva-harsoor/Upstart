# Database structure 
# Source for inheritance: https://hmajid2301.medium.com/implementing-model-class-inheritance-in-sqlalchemy-ad4f388a31fc
# Source for many-to-many relationships: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from app import db
from enum import Enum


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	org_name = db.Column(db.String(70), index=True, unique=True)
	org_purpose = db.Column(db.String(500))
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	is_start_up = db.Column(db.Boolean, index=True) 
	location = db.Column(db.String(70), index=True) # city for start up, school for student group
	claimed = db.Column(db.Boolean)


	def __repr__(self):
		if self.is_start_up:
			return "<StartUp {} in {}>".format(self.org_name, self.location)
		else:
			return "<StudentGroup {} at {}".format(self.org_name, self.location)

# helper table for User-Category relationship
# not a model; rather, an actual table
categories = db.Table('categories',
	db.Column('category_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('user_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)


