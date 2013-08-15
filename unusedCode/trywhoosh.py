#!flask/bin/python

from unidecode import unidecode
import os.path
from whoosh.index import create_in
from whoosh.fields import *
id = 0
def convertUni(word):
	return  unicode(unidecode(unicode(word,'utf-8')),'utf-8')
def convertMixedFraction(mixedFrac):
	mixedFrac = mixedFrac.split()
	output = 0
	for i in mixedFrac:
		output += Fraction(i)
	return output
def createFood(food_item_info,writer):
	global id
	id+=1
	#size of this list is 25
	type = convertUni(food_item_info[1])
	food = convertUni(food_item_info[2])
	detail = convertUni(food_item_info[3])
	source = convertUni(food_item_info[4])
	tag = convertUni(food_item_info[2]+" "+food_item_info[3])

	writer.add_document(id = id, type=type,food=food,detail=detail,source=source,tag=tag)

def addAllFood(ix):
	j_result = -23
	while j_result <= 826:
		print j_result
		writer = ix.writer()
		result = open('result'+str(j_result),'r')
		for eachInfo_list in result:
			eachInfo_list = eachInfo_list.rstrip('\n')
			eachInfo_list = eachInfo_list.split('^')
			eachBasicInfo = eachInfo_list[0]
			eachBasicInfo = eachBasicInfo.split('|')
			eachBasicInfo.remove('')
			for i in range(len(eachBasicInfo)):
				if eachBasicInfo[i] == "NA" and i == 3:
					eachBasicInfo[i] = " "
				elif eachBasicInfo[i] == "NA":
					eachBasicInfo[i] = 0
			createFood(eachBasicInfo,writer)
		writer.commit()
		result.close()
		j_result += 1
			

#CREATE NEW DATABASE
# schema = Schema(id = NUMERIC(stored=True),type=TEXT,food=TEXT(stored=True),detail=TEXT(stored=True),source=TEXT(stored=True),tag=TEXT)
# if not os.path.exists("index"):
# 	os.mkdir("index")
# ix = create_in("index", schema)
# addAllFood(ix)

# LOAD EXISTING
import whoosh.index as index
ix = index.open_dir("index")

from whoosh.query import *
from whoosh.qparser import QueryParser



parser = QueryParser("source", ix.schema)
myquery = parser.parse("dunkin")

#myquery = Or([Term("food", u"seaweed raw"), Term("detail", "seaweed raw")])
searcher = ix.searcher()
results = searcher.search(myquery, limit=10)
resultList = []
for i in results:
	print(i["food"]),
	print(i["detail"]),
	print(i["source"])
	print(i["id"])
searcher.close()

	



