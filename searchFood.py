from sqlalchemy import desc, asc
def searchFood(searchTerm, brandTerm, Food, toOrder):
	searchTermList = searchTerm.split()
	
	q = Food.query
	for each in searchTermList:
		q = q.filter(Food.tag.ilike("% "+each+" %"))

	foodIDs = [each.id for each in q]
	return foodIDs
	
def searchFoodBrand(brandTerm, Food, toOrder):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	if toOrder == "ordered":
		q =  Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.source) , to_tsquery(:searchTerm))")).params(searchTerm=brandTerm)
	else:
		q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=brandTerm)
	
	return q