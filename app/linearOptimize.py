def linearOptimize(listFoodObject,constraints, constraintsGivenmin, constraintsGivenmax, opt_maxormin, opt_nut, suggestedFood):
	
	print "constraints:"
	for each in constraints:
		print each,
	#listFoodObject is actual foodobject
	#constraints starting from 25 = Water - this is so that can access attribute of the food object
	#constraintsGivenmin - all values from the table starting from Water/g - it is in string and mayhave None object
	#constraintsGivenmax - all values from the table starting from Water/g - it is in string and mayhave None object
	#opt_nut starts from 8 because it access from full_total_nutreint which the first 8 elements are the basic ones
	
	full_basic_nutrient = ["Calories/kcal","Calories from Fat/kcal","Total Fat/g","Fat /%","Saturated Fat/g","Polyunsaturated Fat/g","Monounsaturated Fat/g","Cholestorl/mg","Sodium/mg","Total Carbohydrate/g","Fiber/g","Sugar/g","Protein/g","Vitamin A/%","Vitamin C/%","Calcium/%","Iron/%"]
	full_ext_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
	full_total_nutrient = full_basic_nutrient+full_ext_nutrient
	
	#Get rid of Nones
	print "ConstraintUpp", len(constraintsGivenmax)
	for i in range(len(constraintsGivenmax)):
		if constraintsGivenmax[i] == "ND":
			constraintsGivenmax[i] = 10000.00
#		print constraintsGivenmax[i]
	print "ConstraintLower", len(constraintsGivenmin)
	for i in range(len(constraintsGivenmin)):
		if constraintsGivenmin[i] == "ND":
			constraintsGivenmin[i] = 0.00
#		print constraintsGivenmin[i]
	print "Food Submitted: "
	for i in listFoodObject:
		print i
		
	#Create a list of dictionaries
	#Each nutrient dict(sub dict) has different food items as keys and the nutritional values as the values
	basic_Nutrients = [i for i in range(165)]

	#large_dict stores all the nutrients of the selected food
	large_dict = {}
	for each_nut in basic_Nutrients:
		small_dict = {}
		large_dict[each_nut] = small_dict

	#contraints is from checkbox starting at 25 this is because it goes to the foodobject
	#get nutritional values of each type of food
	constVal = []
	for const in constraints:
		eachConstVal = [i.value(const) for i in listFoodObject]
		constVal.append(eachConstVal)

	objectiveNu = [opt_nut]
	obVal = []
	for objnu in objectiveNu:
		eachobj = [i.value(objnu) for i in listFoodObject]
		obVal.append(eachobj)

	#foodNut stores food info of each
	foodNut = {}
	for each_nut in range(len(constraints)):
		foodNut[constraints[each_nut]] = constVal[each_nut]
	for each_nut in range(len(objectiveNu)):
		foodNut[objectiveNu[each_nut]] = obVal[each_nut]
	
# 	print "Food Nutrients: "
# 	print foodNut
# 	print "type: ", type(foodNut)

	nullNut = []
	for eachCon in constraints:
		eachNutDiffFood = foodNut[eachCon]
		if sum(eachNutDiffFood) == 0:
			eachCon = (full_ext_nutrient[eachCon-25].split("/"))[0]
			print "There is no", eachCon
			nullNut.append(eachCon)
	
# 	totalNut = []
# 	for tryEachCon in constraints:
# 		totalNut.append(sum(foodNut[tryEachCon]))
# 	
# 	for eachtotalNut in totalNut:
# 		print eachtotalNut

	listFood = [str(i) for i in range(len(listFoodObject))]
	print "listFood: ", listFood
	
	listSuggested = [str(each) for each in suggestedFood]
	
	#Put the different food selected into respective nutrients dictionary
	for each_constr in constraints:
		for each_food in range(len(listFood)):
			large_dict[each_constr][listFood[each_food]] = foodNut[each_constr][each_food]

	for each_constr in objectiveNu:
		for each_food in range(len(listFood)):
			large_dict[each_constr][listFood[each_food]] = foodNut[each_constr][each_food]


	############################## LP Problem ####################################
	from pulp import *

	# Create the 'prob' variable to contain the problem data
	if opt_maxormin == 1:
		prob = LpProblem("FoodLP", LpMaximize)
	else:
		prob = LpProblem("FoodLP", LpMinimize)

	# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
	food_vars = LpVariable.dicts("Food",listFood,0)
	for j in range(len(objectiveNu)):
		nutriObjective = objectiveNu[j]
		prob += lpSum([(large_dict[nutriObjective])[i]*food_vars[i] for i in listFood])
	
#  	for i in listSuggested:
#  		prob += (food_vars[i]) <= 1

	# Adding constraints to the problem
	for j in range(len(constraints)):
		#limit = constraintsGiven[j]
		#print "Limit:", limit
		nutriConst = constraints[j]
		k = [large_dict[nutriConst][i]*food_vars[i] for i in listFood]
		print "constraints: ", full_ext_nutrient[nutriConst-25],
		# using sign as differentiator
		
		print "upperbound:", constraintsGivenmax[nutriConst-25],
		print "lowerbound:", constraintsGivenmin[nutriConst-25]
	
		prob += lpSum([large_dict[nutriConst][i]*food_vars[i] for i in listFood]) <= float(constraintsGivenmax[nutriConst-25])
		prob += lpSum([large_dict[nutriConst][i]*food_vars[i] for i in listFood]) >= float(constraintsGivenmin[nutriConst-25])
			
		#if limit > 0: #Should consume less than
		#	prob += lpSum([large_dict[nutriConst][i]*food_vars[i] for i in listFood]) <= limit
		#else: # Should consume more than
		#	prob += lpSum([large_dict[nutriConst][i]*food_vars[i] for i in listFood]) >= limit
	print "done assigning bounds"
	prob.solve()
	
	outputFood = [0 for i in range(len(listFoodObject))]
	outputFoodAmount = [0 for i in range(len(listFoodObject))]
	blank = " "
	for v in prob.variables():
		print v.name, "=", v.varValue,
		if v.name == "__dummy":
			continue
		foodindex = v.name.split("_")
		foodindex = int(foodindex[1])
		fooditem = listFoodObject[foodindex]
		outputFood[foodindex] = (fooditem.unit +' ' +fooditem.food + " "+ fooditem.detail+ " (" +  fooditem.source+")")
		print outputFood[foodindex]
		outputFoodAmount[foodindex] = (v.varValue)
	
	print "Status:", LpStatus[prob.status],
	
	print "Total "+full_total_nutrient[opt_nut-8], value(prob.objective) # -8 because there are 8 basic nutrients in full_total 
	
	return (outputFood, outputFoodAmount, LpStatus[prob.status], value(prob.objective), nullNut)
	