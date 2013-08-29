from sqlalchemy import desc, asc, func, distinct
def searchFood(searchTerm, brandTerm, Food,FoodKey):
	searchTermList = searchTerm.split()
	keywords = []
	for each in searchTermList:
		keywords.append(each.lower())
	a = FoodKey.query.filter(FoodKey.word.in_(keywords)).subquery()
	q = Food.query.filter(Food.id==a.c.keyid).group_by(Food.id).having(func.count(distinct(a.c.word)) == len(keywords))	
	
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	if brandTerm != "":
		q = q.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=brandTerm)

	if len(keywords) == 1:
		q = q.order_by(asc(func.char_length(Food.tag))).limit(40)

	foodIDs = [each.id for each in q]
	return foodIDs
	
def searchFoodBrand(brandTerm, Food):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	print brandTerm
	q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=brandTerm)
	foodIDs = [each.id for each in q]
	return foodIDs