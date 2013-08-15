from sqlalchemy import desc
def searchFood(searchTerm, brandTerm, Food):
	searchTermList = searchTerm.split()
	andTerm = "&"
	andSearchTerm = andTerm.join(searchTermList)
	andSearchTerm.rstrip("&")
	
	orTerm = "|"
	orSearchTerm = orTerm.join(searchTermList)
	orSearchTerm.rstrip("|")
	
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	
	#to be changed to tags
	q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.tag) , to_tsquery(:searchTerm))")).params(searchTerm=andSearchTerm)
	if q.count() == 0:
		q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.tag) , to_tsquery(:searchTerm))")).params(searchTerm=orSearchTerm)
	
	qWithBrands = q.filter("Food.source @@ to_tsquery(:brandTerm)").params(brandTerm=brandTerm)
	if qWithBrands.count() != 0:
		q = qWithBrands
	
	return q
	
def searchFoodBrand(brandTerm, Food):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.source) , to_tsquery(:searchTerm))")).params(searchTerm=searchTerm)

	return resultList