from sqlalchemy import desc, asc
def searchFood(searchTerm, brandTerm, Food):
	searchTermList = searchTerm.split()
	q = Food.query
	for each in searchTermList:
		q = q.filter(Food.tag.ilike("% "+each+" %"))
	if brandTerm != "":
		q = q.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=brandTerm)

	foodIDs = [each.id for each in q]
	return foodIDs
	
def searchFoodBrand(brandTerm, Food):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=brandTerm)
	foodIDs = [each.id for each in q]
	return foodIDs