#!flask/bin/python
from app.models import Food
from app import db
i = 0
for food in Food.query.all():
	i += 1
	db.session.delete(food)
	if i %500 == 0:
		print i
		db.session.commit()