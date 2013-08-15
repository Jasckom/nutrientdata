a = open('IndexCategories','r')
types =[]
for each in a:
	eachList = each.split('^')
	num = int(eachList[0])
	if num < 0:
		type = eachList[1]
		types.append(type)

i = 0
for each in types:
	if i != 0:
		print "\'"+ each+"\',",
	i = 1