
def searchFood(searchTerm, brandTerm):
	searchTermList = searchTerm.split()
	orTerm = "|"
	searchTerm = orTerm.join(searchTermList)
	searchTerm.rstrip("|")
	
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	
	#to be changed to tags
	q = Food.query.filter("Food.food @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.food) , to_tsquery(:searchTerm))")).params(searchTerm=searchTerm)
	qWithBrands = q.filter("Food.source @@ to_tsquery(:brandTerm)").params(brandTerm=brandTerm)
	if qWithBrands.count == 0:
		qResult = q	
	
	return q
	
def searchFoodBrand(brandTerm):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.source) , to_tsquery(:searchTerm))")).params(searchTerm=searchTerm)

	return resultList