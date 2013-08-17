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
	if andSearchTerm == "":
		andSearchTerm = "banana"
	
	print "searchTerm", andSearchTerm
	q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").params(searchTerm=andSearchTerm)
	qOrdered = q.order_by(desc("ts_rank_cd(to_tsvector(Food.tag) , to_tsquery(:searchTerm))"))
	if q.count() == 0:
		print "No results from food name"
		q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").params(searchTerm=orSearchTerm)
		qOrdered = q.order_by(desc("ts_rank_cd(to_tsvector(Food.tag) , to_tsquery(:searchTerm))"))
		
	if brandTerm != "":
		print "brand Term is:", brandTerm
		qWithBrands = q.filter("Food.source @@ to_tsquery(:brandTerm)").params(brandTerm=brandTerm)
		qWithBrandsOrdered = qOrdered.filter("Food.source @@ to_tsquery(:brandTerm)")
		print "Filter with the brand"

		if qWithBrands.count() != 0:
			q = qWithBrands
			qOrdered = qWithBrandsOrdered
	print "done in searchFood" 
	
	return q, qOrdered
	
def searchFoodBrand(brandTerm, Food):
	brandTermList = brandTerm.split()
	orTerm = "|"
	brandTerm = orTerm.join(brandTermList)
	brandTerm.rstrip("|")
	q = Food.query.filter("Food.source @@ to_tsquery(:searchTerm)").params(searchTerm=searchTerm)
	qOrdered =  q.order_by(desc("ts_rank_cd(to_tsvector(Food.source) , to_tsquery(:searchTerm))")).params(searchTerm=searchTerm)
	
	return q, qOrdered