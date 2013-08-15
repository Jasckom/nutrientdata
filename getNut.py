#!flask/bin/python
from app.models import Nutri
from app import db

#upper 1 bound nutrient
def upper1(correctOrder):
	b = ["t2VitaminA_RAE_mcg_RAE","t2VitaminC_TotalAscorbicAcid_mg","t2VitaminD_IU","t2VitaminE_alpha_tocopherol__mg","t2VitaminKPhylloquinone_mcg","t2Thiamin_mg","t2Riboflavin_mg","t2Niacin_mg","t2VitaminB_6_mg","t2Folate_Total_mcg","t2VitaminB_12_mcg","t2PantothenicAcid_mg","[] Biotin","t2Choline_Total_mg","[]"]
	newnut = []
	doc = open('constraintUpper1.txt','r')
	for i in doc:
		if i[0].isalpha():
			continue
		else:
			#print i
			newnut.append(i)

	total = []
	for i in range(0,2):
		ij = newnut[i].split("mo")
		#print "INFANT", ij[1]
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					each_nut[eachc] = j[eachj]
					break
		#for eachc in range(len(each_nut)):
		#	print eachc, each_nut[eachc]
		total.append(each_nut)
	for i in range(2,len(newnut)):
		ij = newnut[i].split("y")
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					each_nut[eachc] = j[eachj]
					break
		#for eachc in range(len(each_nut)):
			#print eachc, each_nut[eachc]
		total.append(each_nut)
	for k in total:
		for j in range(len(k)):
			k[j] = str(k[j])
		print k[55], "vit D"
		if k[55] != "[]":
			k[55] = str(float(k[55])/0.025) # convert vitd to IU unit
	print "length total: ", len(total)
	return total
#Lower bound nutrient	
def EARfirst(correctOrder):
	b = ["t1Calcium_Ca_mg","t0Carbohydrate_ByDifference_g","t0Protein_g","t2VitaminA_RAE_mcg_RAE","t2VitaminC_TotalAscorbicAcid_mg","t2VitaminD_IU","t2VitaminE_alpha_tocopherol__mg","t2Thiamin_mg","t2Riboflavin_mg","t2Niacin_mg","t2VitaminB_6_mg","t2Folate_Total_mcg","t2VitaminB_12_mcg","t1Copper_Cu_mg","[]Iodine","t1Iron_Fe_mg","t1Magnesium_Mg_m","[]Molybdenum","t1Phosphorus_P_mg","t1Selenium_Se_mcg","t1Zinc_Zn_mg"]
	newnut = []
	doc = open('constraintLower1.txt','r')
	for i in doc:
		if i[0].isalpha():
			continue
		else:
			#print i
			newnut.append(i)

	total = []
	two_to_six = [[] for i in range(len(correctOrder))]
	six_to_twelve = [[] for i in range(len(correctOrder))]
	six_to_twelve[3] = 1.0
	six_to_twelve[17] = 6.9
	six_to_twelve[22] = 2.5
	total.append(two_to_six)
	total.append(six_to_twelve) 
	for i in range(2,len(newnut)):
		ij = newnut[i].split("y")
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					each_nut[eachc] = j[eachj]
					break
		#for eachc in range(len(each_nut)):
		#	print eachc, each_nut[eachc]
		total.append(each_nut)
	#print "EAR: "
	#for i in range(len(total[5])):
	#	print i, total[5][i]
	#print "DONE"
	print "length total: ", len(total)
	for k in total:
		for j in range(len(k)):
			k[j] = str(k[j])
		if k[55] != "[]":
			print "VitaD before:", k[55]
			k[55] = str(float(k[55])/0.025) #convert vitamin D to IU unit
			print "VitaD After", k[55]
	return total
#upper2
def upper2(correctOrder):
	b = ["[]Arsenic","[]boron","t1Calcium_Ca_mg","[] Chromium","t1Copper_Cu_mg","t1Fluoride_F_mcg","[] Iodine","t1Iron_Fe_mg","t1Magnesium_Mg_m","[] Manganese","[] Molybdenum","[] Nickel","t1Phosphorus_P_mg","t1Selenium_Se_mcg","[]silicon","[] vanadium","t1Zinc_Zn_mg","t1Sodium_Na_mg","[] chloride",]
	newnut = []
	doc = open('constraintUpper2.txt','r')
	for i in doc:
		if i[0].isalpha():
			continue
		else:
			#print i
			newnut.append(i)

	total = []
	for i in range(0,2):
		ij = newnut[i].split("mo")
		#print "INFANT", ij[1]
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					each_nut[eachc] = j[eachj]
					break
		#for eachc in range(len(each_nut)):
		#	print eachc, each_nut[eachc]
		total.append(each_nut)
	for i in range(2,len(newnut)):
		ij = newnut[i].split("y")
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					each_nut[eachc] = j[eachj]
					break
		#for eachc in range(len(each_nut)):
		#	print eachc, each_nut[eachc]
		total.append(each_nut)
	#print "upper2: "
	#for i in range(len(total[5])):
	#	print i, total[5][i]
	#print "DONE"
	for k in total:
		print "new"
		for j in range(len(k)):
			if (j == 19 or j ==21) and (k[j] != "ND") :
				k[j] = float(k[j])*1000
			k[j] = str(k[j])
			
	print "length total: ", len(total)
	return total

def remove(x):
	if not x[-1].isdigit() and not x[-1].isalpha():
		return(remove(x[:-1]))
	else:
		return x

def macroLower(correctOrder):
	b = ["t0Water_g","t0Carbohydrate_ByDifference_g","t0Fiber_TotalDietary_g","t0TotalLipidFat_g","[]Linoleic Acid","[]alpha-Linolenic acid","t0Protein_g",]
	newnut = []
	doc = open('constraintLower2macro.txt','r')
	for i in doc:
		if i[0].isalpha():
			continue
		else:
			#print i
			newnut.append(i)

	total = []
	for i in range(0,2):
		ij = newnut[i].split("mo")
		#print "INFANT", ij[1]
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					value = j[eachj]
					if (not value[-1].isdigit()) and (not value[-1].isalpha()):
						value = remove(value)
					each_nut[eachc] = value
					break
		#for eachc in range(len(each_nut)):
			#print eachc, each_nut[eachc]
		total.append(each_nut)
	for i in range(2,len(newnut)):
		ij = newnut[i].split("y")
		j = ij[1].split()
		each_nut = [[] for i in range(len(correctOrder))]
		for eachj in range(len(j)):
			for eachc in range(len(correctOrder)):
				#print "each pair: ", b[eachj], len(b[eachj]), correctOrder[eachc], len(correctOrder[eachc])
				if b[eachj] == correctOrder[eachc]:
					value = j[eachj]
					if (not value[-1].isdigit()) and (not value[-1].isalpha()):
						value = remove(value)
					each_nut[eachc] = value
					break
		#for eachc in range(len(each_nut)):
			#print eachc, each_nut[eachc]
		total.append(each_nut)
	for k in total:
		for j in range(len(k)):
			k[j] = str(k[j])
	print "length total: ", len(total)
	return total

def getbounds():
	#Creating correct order for all to compare
	ordered = open('ex_nutrient_order','r')
	correctOrder = []
	j = 0
	for i in ordered:
		i = i.rstrip('\n')
		print j, i
		correctOrder.append(i)
		j+=1
	ordered.close()	
	#print "microlower"
	microlower = EARfirst(correctOrder)
	#print "microupper1"
	microupper1 = upper1(correctOrder)
	#print "microupper2"
	microupper2 = upper2(correctOrder)
	#print "macro"
	macrolower = macroLower(correctOrder)
	masterNut = []	
	emptstring = ""
	# j loops for each age group
	for j in range(len(microlower)):
		ageNut = [[] for i in range(len(microlower[0]))]
		print "AGE GROUP: ", j
		# k loops for each element
		for k in range(len(microlower[0])):
			print k,": ",
			microlower[j][k] = emptstring.join(microlower[j][k].split(','))
			macrolower[j][k] = emptstring.join(macrolower[j][k].split(','))
			microupper1[j][k] = emptstring.join(microupper1[j][k].split(','))
			microupper2[j][k] = emptstring.join(microupper2[j][k].split(','))
			lower = 0
			if microlower[j][k] != "[]":
				ageNut[k] = microlower[j][k]
				lower += 1
				#print i, "lower"
			if macrolower[j][k] != "[]":
				ageNut[k] =  macrolower[j][k]
				lower += 1
			if lower >= 1:
				print "lower", 
				ageNut[k] += ":"
			else:
				ageNut[k] = "0:"
				
			upper = 0

			if microupper1[j][k] != "[]":
				ageNut[k] += microupper1[j][k]
				upper +=1
				#print i, "upper1"
			if microupper2[j][k] != "[]":
				ageNut[k] += microupper2[j][k]
				upper +=1
			if upper >= 1:
				print "upper",
			else:
				ageNut[k] += "ND"
			print ageNut[k], (lower,upper)

		masterNut.append(ageNut)
	print "Final", len(masterNut)
	return masterNut

def inputNutri():
	# 22 items in this list
	masterNut = getbounds()
	#lifeStageGroup = ["Infants","Infants","Children","Children","Males","Males","Males","Males","Males","Males","Females","Females","Females","Females","Females","Females","Pregnancy","Pregnancy","Pregnancy","Lactation","Lactation","Lactation"]
	#age = [0,1,2,3,4,5,6,7,8,9,4,5,6,7,8,9, 5,6,7,5,6,7]
	ageGroup =["0-6 mo"]*2 + ["6-12 mo"]*2 + ["1-3 y"]*2 + ["4-8 y"]*2 + ["9-13 y","14-18 y","19-30 y","31-50 y","51-70 y",">70 y"] *2 + ["14-18 y","19-30 y","31-50 y"]*2
	gender = ["Males","Females"]*4 + ["Males"]*6 + ["Females"]*12
	conditions = ["None"]*20 + ["Pregnancy"]*3 + ["Lactation"]*3
	runthru = [0,0, 1,1, 2,2, 3, 3 ] + [i for i in range(4,22)]
	print "lenght: ", len(ageGroup), len(gender), len(conditions), len(runthru)
	fatup = [None]*4 + [40]*2+ [35]*20
	carbup = [None]*4 + [65]*22
	protup = [None]*4+[20]*2 + [30]* 4 +[35]*4 + [30]*2 + [35]*4 + [30,35,35]*2
	
	j = 0
	for index in runthru:
		print
		print
		print "EACH GROUP", j
		eachNut = masterNut[index]
		q = Nutri()
		q_keys = q.__table__.columns.keys()
		i = 0
		for eachkey in q_keys:
			if i>= 23:
				#print "iter:",i, eachkey
				setattr(q,eachkey,eachNut[i-23])
				#print eachkey, getattr(q,eachkey)
			i+= 1
		q.ageGroup = ageGroup[j]
		q.gender = gender[j]
		q.conditions = conditions[j]
		q.fat_g = fatup[j]
		q.protein_g = protup[j]
		q.carb_g = carbup[j]
		j+= 1
			
		for eachkey in q_keys:
			print eachkey, getattr(q,eachkey)
		db.session.add(q)
		db.session.commit()
	
inputNutri()
	
	



