# Database structure 
# Source for inheritance: https://hmajid2301.medium.com/implementing-model-class-inheritance-in-sqlalchemy-ad4f388a31fc
# Source for many-to-many relationships: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# helper table for User-Category relationship
# not a model; rather, an actual table
categories = db.Table('categories',
	db.Column('category_id', db.Integer, db.ForeignKey('organization.id'), primary_key=True),
	db.Column('organization_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)


class Organization(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(70), index=True, unique=True)
	purpose = db.Column(db.String(500))
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	is_start_up = db.Column(db.Boolean, index=True) 
	location = db.Column(db.String(70), index=True) # city for start up, school for student group
	verified = db.Column(db.Boolean)
	categories = db.relationship(
		'Category', secondary=categories, lazy='joined',
		backref=db.backref('organization', lazy='joined'))


	def __repr__(self):
		if self.is_start_up:
			return "<StartUp {} in {}>".format(self.name, self.location)
		else:
			return "<StudentGroup {} at {}".format(self.name, self.location)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def add_category(self, category):
		if not category in self.categories:
			self.categories.append(category)

	def remove_category(self, category):
		if category in self.categories:
			self.categories.remove(category)


@login.user_loader
def load_user(id):
	return Organization.query.get(int(id))


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(70), index=True)

	def __repr__(self):
		return "<Category {}>".format(self.name)


