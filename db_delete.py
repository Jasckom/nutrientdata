#!flask/bin/python
from app.models import Food
from app import db
for food in Food.query.all():
	db.session.delete(food)
db.session.commit()