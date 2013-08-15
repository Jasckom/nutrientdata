#for whoosh
import os.path
from whoosh.index import create_in
from whoosh.fields import *
import whoosh.index as index
from whoosh.query import *
from whoosh.qparser import QueryParser


def whooshSearch(searchTerm, brandTerm):
	brandTerm = brandTerm.lower()
	
	#Open index
	ix = index.open_dir("index")
	
	#Identify which field
	parserFood = QueryParser("tag", ix.schema)
	queryFood = parserFood.parse(searchTerm)
	
	
	searcher = ix.searcher()
	#Create filter
	if brandTerm == "":
		brandTerm = "general"
		allow_q = Term("source", brandTerm)
		resultFoodGen = searcher.search(queryFood,filter = allow_q, limit = 7)
		resultFoodNoGen = searcher.search(queryFood,mask = allow_q, limit = 1000)
		resultFood = [each for each in resultFoodGen] + [each for each in resultFoodNoGen]
	
	else:
		allow_q = Term("source", brandTerm)
		resultFood = searcher.search(queryFood,filter = allow_q, limit = 1000)

	resultList = []	
	for i in resultFood:
		resultList.append(i["id"])
	searcher.close()
	return resultList
	
def whooshSearchBrand(brandTerm):
	ix = index.open_dir("index")
	
	parserBrand = QueryParser("source", ix.schema)
	queryBrand = parserBrand.parse(brandTerm)	
	searcher = ix.searcher()
	
	resultList = []
	resultBrand = searcher.search(queryBrand, limit = 1000)

	for i in resultBrand:
		resultList.append(i["id"])
	searcher.close()
	return resultList