#!flask/bin/python

from app.models import Food, FoodKey
from app import db

j_result = -23
while (j_result <= 826) :
	print j_result
	result = open('result'+str(j_result),'r')
	for eachInfo_list in result:
		eachInfo_list = eachInfo_list.rstrip('\n')
		eachInfo_list = eachInfo_list.split('^')
		
		#Basic Nutrients
		eachBasicInfo = eachInfo_list[0]
		eachBasicInfo = eachBasicInfo.split('|')
		eachBasicInfo.remove('')
		break
	mainType = eachBasicInfo[0]
	type = eachBasicInfo[1]
	foodInCat = Food.query.filter(Food.mainType == mainType).filter(Food.type == type)
	for eachFood in foodInCat:
		tag = eachFood.tag
		tagList = tag.split()
		for eachTag in tagList:
			eachKey = FoodKey(keyid = eachFood.id, word = eachTag)
 	 		db.session.add(eachKey)
 	 	db.session.commit()
 	 	print eachKey
 	db.session.commit()
 	
	print "Done committing at", j_result
	result.close()
	j_result += 1
		