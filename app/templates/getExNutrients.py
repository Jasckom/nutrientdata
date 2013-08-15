def convertMixedFraction(mixedFrac):
	mixedFrac = mixedFrac.split()
	output = 0
	for i in mixedFrac:
		output += Fraction(i)
	return output
def createFood(food_item_info):
	#size of this list is 25
	food_item = Food(mainType = food_item_info[0]
	,type = food_item_info[1]
	,food = convertUni(food_item_info[2])
	,detail = convertUni(food_item_info[3])
	,source = food_item_info[4]
	,amount = float(convertMixedFraction(str(food_item_info[5])))
	,unit = food_item_info[6]
	,gram = float(food_item_info[7])
	#nutrients per the stated gram
	,cal_kcal = float(food_item_info[8])
	,calFat_kcal = float(food_item_info[9])
	,fat_g = float(food_item_info[10])
	,fat_pct = float(food_item_info[11])
	,saturFat_g = float(food_item_info[12])
	,polyunFat_g = float(food_item_info[13])
	,monounFat_g = float(food_item_info[14])
	,chol_mg = float(food_item_info[15])
	,sodium_mg = float(food_item_info[16])
	,carb_g = float(food_item_info[17])
	,fiber_g = float(food_item_info[18])
	,sugar_g = float(food_item_info[19])
	,protein_g = float(food_item_info[20])
	,vitA_pct = float(food_item_info[21])
	,vitC_pct = float(food_item_info[22])
	,calcium_pct = float(food_item_info[23])
	,iron_pct = float(food_item_info[24]))
	return food_item

def addAllFood(ex_nutrient):
	j_result = -23
	while j_result <= -23:
		print j_result
		result = open('result'+str(j_result),'r')
		for eachInfo_list in result:
			eachInfo_list = eachInfo_list.rstrip('\n')
			eachInfo_list = eachInfo_list.split('^')
			eachBasicInfo = eachInfo_list[1]
			eachBasicInfo = eachBasicInfo.split('|')
			eachBasicInfo.remove('')
			print eachBasicInfo
			for i in range(len(eachBasicInfo)):
				print i, ex_nutrient[i], eachBasicInfo[i]
		result.close()
		j_result += 1
		
ex_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid (fat)/g","Ash/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose (dextrose)/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K (phylloquinone)/mcg","Fatty acids, total saturated/g","4:0/g","6:0/g","8:0/g","10:0/g","12:0/g","14:0/g","16:0/g","18:0/g","Fatty acids, total monounsaturated/g","16:1 undifferentiated/g","18:1 undifferentiated/g","20:1/g","22:1 undifferentiated/g","Fatty acids, total polyunsaturated/g","18:2 undifferentiated/g","18:3 undifferentiated/g","18:4/g","20:4 undifferentiated/g","20:5 n-3/g","22:5 n-3/g","22:6 n-3/g","Cholesterol/mg","Phytosterols/mg","Tryptophan/g","Threonine/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Cystine/g","Phenylalanine/g","Tyrosine/g","Valine/g","Arginine/g","Histidine/g","Alanine/g","Aspartic acid/g","Glutamic acid/g","Glycine/g","Proline/g","Serine/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Fluoride, F/mcg","Vitamin D/IU","15:0/g","17:0/g","20:0/g","14:1/g","15:1/g","16:1 c/g","17:1/g","18:1 c/g","18:1 t/g","18:2 n-6 c,c/g","18:2 i/g","18:3 n-3 c,c,c/g","Stigmasterol/mg","Campesterol/mg","Beta-sitosterol/mg","Fatty acids, total trans/g","22:0/g","24:0/g","13:0/g","24:1 c/g","18:3 n-6 c,c,c/g","20:2 n-6 c,c/g","20:3 undifferentiated/g","Fatty acids, total trans-monoenoic/g","Hydroxyproline/g","21:5/g","22:4/g","18:2 CLAs/g","16:1 t/g","20:3 n-6/g","20:4 n-6/g","Fatty acids, total trans-polyenoic/g","22:1 c/g","18:2 t,t/g","18:3i/g","22:1 t/g","18:2 t not further defined/g","20:3 n-3/g","Adjusted Protein/g"]
print "Number of ex_nutrients: ", len(ex_nutrient)
addAllFood(ex_nutrient)