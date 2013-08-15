noContent = []
file = -23
while file <= 826:
	a = open("result"+str(file),'r')
	content = []
	for i in a:
		content.append(i)
	if not content:
		noContent.append(file)
		print "No content here"
	file +=1

print "Total no content file:"
for i in noContent:
	print i,",",