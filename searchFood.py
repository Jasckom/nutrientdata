from sqlalchemy import desc
def searchFood(searchTerm, brandTerm, Food, toOrder):
	searchTermList = searchTerm.split()
	andTerm = "&"
	andSearchTerm = andTerm.join(searchTermList)
	andSearchTerm.rstrip("&")
	
# 	orTerm = "|"
# 	orSearchTerm = orTerm.join(searchTermList)
# 	orSearchTerm.rstrip("|")
	
# 	brandTermList = brandTerm.split()
# 	orTerm = "|"
# 	brandTerm = orTerm.join(brandTermList)
# 	brandTerm.rstrip("|")
	
	#to be changed to tags
	if andSearchTerm == "":
		andSearchTerm = " "
	
	if toOrder == "ordered":
		print "in ordered"
		q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").order_by(desc("ts_rank_cd(to_tsvector(Food.tag) , to_tsquery(:searchTerm))")).params(searchTerm=andSearchTerm)
		if brandTerm != "":
			q = q.filter("Food.source @@ to_tsquery(:brandTerm)").params(brandTerm=brandTerm)
	else:
		print "not ordered"
		q = Food.query.filter("Food.tag @@ to_tsquery(:searchTerm)").params(searchTerm=andSearchTerm)
		if brandTerm != "":
			q = q.filter("Food.source @@ to_tsquery(:brandTerm)").params(brandTerm=brandTerm)

	print "done in searchFood" 
	
	return q
	
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