#!flask/bin/python
from app.models import Food, FoodKey
from app import db
from unidecode import unidecode
from fractions import Fraction

def convertUni(word):
	return  unidecode(unicode(word,'utf-8'))
def convertMixedFraction(mixedFrac):
	mixedFrac = mixedFrac.split()
	output = 0
	for i in mixedFrac:
		output += Fraction(i)
	return output
def createFood(food_item_info):
	#create tag

	foodName = food_item_info[2].replace('&amp;','&')
	foodName = convertUni(foodName)
	
	foodDetail = food_item_info[3].replace('&amp;','&')
	foodDetail = convertUni(foodDetail)
	
	foodSource = food_item_info[4].replace('&amp;','&')	
	foodSource = convertUni(foodSource)
	
	tag = foodName + " " + foodDetail
	tagList = tag.split()
	for i in range(len(tagList)):	
		tagList[i] = tagList[i].lower().rstrip(',')
	tagList = list(set(tagList))
	space = " "
	tag = space.join(tagList)
	tag = " "+tag+" "
	
	#size of this list is 25
	food_item = Food(mainType = food_item_info[0]
	,type = food_item_info[1]
	,food = foodName
	,detail = foodDetail
	,source = foodSource
	,amount = float(convertMixedFraction(str(food_item_info[5])))
	,unit = food_item_info[6]
	,gram = float(food_item_info[7])
	,tag = tag
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
	,iron_pct = float(food_item_info[24])
	,t0Water_g= float(food_item_info[25])
	,t0Energy_kcal= float(food_item_info[26])
	,t0Energy_kj= float(food_item_info[27])
	,t0Protein_g= float(food_item_info[28])
	,t0TotalLipidFat_g= float(food_item_info[29])
	,t0Carbohydrate_ByDifference_g= float(food_item_info[30])
	,t0Fiber_TotalDietary_g= float(food_item_info[31])
	,t0Sugars_Total_g= float(food_item_info[32])
	,t0Sucrose_g= float(food_item_info[33])
	,t0GlucoseDextrose_g= float(food_item_info[34])
	,t0Fructose_g= float(food_item_info[35])
	,t0Lactose_g= float(food_item_info[36])
	,t0Maltose_g= float(food_item_info[37])
	,t0Galactose_g= float(food_item_info[38])
	,t0Starch_g= float(food_item_info[39])
	,t0AdjustedProtein_g= float(food_item_info[40])
	,t1Calcium_Ca_mg= float(food_item_info[41])
	,t1Iron_Fe_mg= float(food_item_info[42])
	,t1Magnesium_Mg_mg= float(food_item_info[43])
	,t1Phosphorus_P_mg= float(food_item_info[44])
	,t1Potassium_K_mg= float(food_item_info[45])
	,t1Sodium_Na_mg= float(food_item_info[46])
	,t1Zinc_Zn_mg= float(food_item_info[47])
	,t1Copper_Cu_mg= float(food_item_info[48])
	,t1Manganese_Mn_mg= float(food_item_info[49])
	,t1Selenium_Se_mcg= float(food_item_info[50])
	,t1Fluoride_F_mcg= float(food_item_info[51])
	,t2VitaminC_TotalAscorbicAcid_mg= float(food_item_info[52])
	,t2Thiamin_mg= float(food_item_info[53])
	,t2Riboflavin_mg= float(food_item_info[54])
	,t2Niacin_mg= float(food_item_info[55])
	,t2PantothenicAcid_mg= float(food_item_info[56])
	,t2VitaminB_6_mg= float(food_item_info[57])
	,t2Folate_Total_mcg= float(food_item_info[58])
	,t2FolicAcid_mcg= float(food_item_info[59])
	,t2Folate_Food_mcg= float(food_item_info[60])
	,t2Folate_DFE_mcg_DFE= float(food_item_info[61])
	,t2Choline_Total_mg= float(food_item_info[62])
	,t2Betaine_mg= float(food_item_info[63])
	,t2VitaminB_12_mcg= float(food_item_info[64])
	,t2VitaminB_12_Added_mcg= float(food_item_info[65])
	,t2VitaminA_IU_IU= float(food_item_info[66])
	,t2VitaminA_RAE_mcg_RAE= float(food_item_info[67])
	,t2Retinol_mcg= float(food_item_info[68])
	,t2VitaminE_alpha_tocopherol__mg= float(food_item_info[69])
	,t2VitaminE_Added_mg= float(food_item_info[70])
	,t2Tocopherol_Beta_mg= float(food_item_info[71])
	,t2Tocopherol_Gamma_mg= float(food_item_info[72])
	,t2Tocopherol_Delta_mg= float(food_item_info[73])
	,t2VitaminKPhylloquinone_mcg= float(food_item_info[74])
	,t2Carotene_Beta_mcg= float(food_item_info[75])
	,t2Carotene_Alpha_mcg= float(food_item_info[76])
	,t2Cryptoxanthin_Beta_mcg= float(food_item_info[77])
	,t2Lycopene_mcg= float(food_item_info[78])
	,t2Lutein_Zeaxanthin_mcg= float(food_item_info[79])
	,t2VitaminD_IU= float(food_item_info[80])
	,t3Stigmasterol_mg= float(food_item_info[81])
	,t3Phytosterols_mg= float(food_item_info[82])
	,t3Beta_sitosterol_mg= float(food_item_info[83])
	,t3Campesterol_mg= float(food_item_info[84])
	,t3Cholesterol_mg= float(food_item_info[85])
	,t3FattyAcids_TotalMonounsaturated_g= float(food_item_info[86])
	,t3FattyAcids_TotalPolyunsaturated_g= float(food_item_info[87])
	,t3FattyAcids_TotalSaturated_g= float(food_item_info[88])
	,t3FattyAcids_TotalTrans_monoenoic_g= float(food_item_info[89])
	,t3FattyAcids_TotalTrans_polyenoic_g= float(food_item_info[90])
	,t3FattyAcids_TotalTrans_g= float(food_item_info[91])
	,t3MonounsaturatedFats14_1_g= float(food_item_info[92])
	,t3MonounsaturatedFats15_1_g= float(food_item_info[93])
	,t3MonounsaturatedFats16_1C_g= float(food_item_info[94])
	,t3MonounsaturatedFats16_1T_g= float(food_item_info[95])
	,t3MonounsaturatedFats16_1Undifferentiated_g= float(food_item_info[96])
	,t3MonounsaturatedFats17_1_g= float(food_item_info[97])
	,t3MonounsaturatedFats18_1C_g= float(food_item_info[98])
	,t3MonounsaturatedFats18_1T_g= float(food_item_info[99])
	,t3MonounsaturatedFats18_1Undifferentiated_g= float(food_item_info[100])
	,t3MonounsaturatedFats20_1_g= float(food_item_info[101])
	,t3MonounsaturatedFats22_1C_g= float(food_item_info[102])
	,t3MonounsaturatedFats22_1T_g= float(food_item_info[103])
	,t3MonounsaturatedFats22_1Undifferentiated_g= float(food_item_info[104])
	,t3MonounsaturatedFats24_1C_g= float(food_item_info[105])
	,t3PolyunsaturatedFats18_2CLAs_g= float(food_item_info[106])
	,t3PolyunsaturatedFats18_2I_g= float(food_item_info[107])
	,t3PolyunsaturatedFats18_2N_6C_c_g= float(food_item_info[108])
	,t3PolyunsaturatedFats18_2T_t_g= float(food_item_info[109])
	,t3PolyunsaturatedFats18_2TNotFurtherDefined_g= float(food_item_info[110])
	,t3PolyunsaturatedFats18_2Undifferentiated_g= float(food_item_info[111])
	,t3PolyunsaturatedFats18_3N_3C_c_c_g= float(food_item_info[112])
	,t3PolyunsaturatedFats18_3N_6C_c_c_g= float(food_item_info[113])
	,t3PolyunsaturatedFats18_3Undifferentiated_g= float(food_item_info[114])
	,t3PolyunsaturatedFats18_3i_g= float(food_item_info[115])
	,t3PolyunsaturatedFats18_4_g= float(food_item_info[116])
	,t3PolyunsaturatedFats20_2N_6C_c_g= float(food_item_info[117])
	,t3PolyunsaturatedFats20_3N_3_g= float(food_item_info[118])
	,t3PolyunsaturatedFats20_3N_6_g= float(food_item_info[119])
	,t3PolyunsaturatedFats20_3Undifferentiated_g= float(food_item_info[120])
	,t3PolyunsaturatedFats20_4N_6_g= float(food_item_info[121])
	,t3PolyunsaturatedFats20_4Undifferentiated_g= float(food_item_info[122])
	,t3PolyunsaturatedFats20_5N_3_g= float(food_item_info[123])
	,t3PolyunsaturatedFats21_5_g= float(food_item_info[124])
	,t3PolyunsaturatedFats22_4_g= float(food_item_info[125])
	,t3PolyunsaturatedFats22_5N_3_g= float(food_item_info[126])
	,t3PolyunsaturatedFats22_6N_3_g= float(food_item_info[127])
	,t3SaturatedFats10_0_g= float(food_item_info[128])
	,t3SaturatedFats12_0_g= float(food_item_info[129])
	,t3SaturatedFats13_0_g= float(food_item_info[130])
	,t3SaturatedFats14_0_g= float(food_item_info[131])
	,t3SaturatedFats15_0_g= float(food_item_info[132])
	,t3SaturatedFats16_0_g= float(food_item_info[133])
	,t3SaturatedFats17_0_g= float(food_item_info[134])
	,t3SaturatedFats18_0_g= float(food_item_info[135])
	,t3SaturatedFats20_0_g= float(food_item_info[136])
	,t3SaturatedFats22_0_g= float(food_item_info[137])
	,t3SaturatedFats24_0_g= float(food_item_info[138])
	,t3SaturatedFats4_0_g= float(food_item_info[139])
	,t3SaturatedFats6_0_g= float(food_item_info[140])
	,t3SaturatedFats8_0_g= float(food_item_info[141])
	,t4Alanine_g= float(food_item_info[142])
	,t4Arginine_g= float(food_item_info[143])
	,t4AsparticAcid_g= float(food_item_info[144])
	,t4Cystine_g= float(food_item_info[145])
	,t4GlutamicAcid_g= float(food_item_info[146])
	,t4Glycine_g= float(food_item_info[147])
	,t4Histidine_g= float(food_item_info[148])
	,t4Hydroxyproline_g= float(food_item_info[149])
	,t4Isoleucine_g= float(food_item_info[150])
	,t4Leucine_g= float(food_item_info[151])
	,t4Lysine_g= float(food_item_info[152])
	,t4Methionine_g= float(food_item_info[153])
	,t4Phenylalanine_g= float(food_item_info[154])
	,t4Proline_g= float(food_item_info[155])
	,t4Serine_g= float(food_item_info[156])
	,t4Threonine_g= float(food_item_info[157])
	,t4Tryptophan_g= float(food_item_info[158])
	,t4Tyrosine_g= float(food_item_info[159])
	,t4Valine_g= float(food_item_info[160])
	,t5Ash_g= float(food_item_info[161])
	,t5Alcohol_Ethyl_g= float(food_item_info[162])
	,t5Caffeine_mg= float(food_item_info[163])
	,t5Theobromine_mg= float(food_item_info[164]))

	return food_item

def createDict():
	#Get the ext_nutrients by the right format (unsorted) - b
	#Get the ext_nutrients by the format - ext_cat (nestedlist)
	a = open('ex_nutrient_cat.txt','r')
	ext_cat = [[] for i in range(6)]
	b = []
	dict = {}
	for i in a:
		i = i.rstrip('\n')
		index = int(i[0])
		i = i.split()
		if len(i) > 1:
			for eachi in i:
				eachi[0].upper()
		new = ""
		for eachi in i:
			new = new+eachi 
		i = new.split('/')
		i = i[0]+"_"+i[1]
		i = i[0].lower() + i[1::]
		ext_cat[index].append(i)
		b.append(i)
	a.close()

	# Sort excat for the fats
	ext_cat[3].sort()
	ext_cat[3].remove("3Phytosterols_mg")
	ext_cat[3].insert(0,"3Phytosterols_mg")
	ext_cat[3].remove("3Stigmasterol_mg")
	ext_cat[3].insert(0,"3Stigmasterol_mg")
	correctOrder = []
	ext_cat[4].sort()
	
	# Unnest the excat into correctOrder
	for each in ext_cat:
		for eachi in each:
			correctOrder.append(eachi)

	#Creating dictionary mapping correctOrder and the unsorted b
	for wrong_index in range(len(b)):
		for right_index in range(len(correctOrder)):
			if b[wrong_index] == correctOrder[right_index]:
				dict[wrong_index] = right_index
	
	#Get the list of nutrients in format and in order
	testOrder = [[] for i in range(len(b))]
	for try_index in range(len(b)):
		right_index = dict[try_index]
		testOrder[right_index] = b[try_index]
	
	for each in testOrder:
		print each
	
	return dict
	
def addAllFood(session,dict):
	j_result = -23
	dict = createDict()
	while (j_result <= 826) :
		print j_result
		result = open('result'+str(j_result),'r')
		for eachInfo_list in result:
			eachInfo_list = eachInfo_list.rstrip('\n')
			eachInfo_list = eachInfo_list.split('^')
			
			#Basic Nutrients
			eachBasicInfo = eachInfo_list[0]
			eachBasicInfo = eachBasicInfo.split('|')
			eachBasicInfo.remove('')
			for i in range(len(eachBasicInfo)):
				if eachBasicInfo[i] == "NA" and i == 3:
					eachBasicInfo[i] = " "
				elif eachBasicInfo[i] == "NA":
					eachBasicInfo[i] = 0
			
			#Extra Nutrients
			extBasicInfo = eachInfo_list[1]
			extBasicInfo = extBasicInfo.split('|')
			extBasicInfo.remove('')
			new = [[] for i in range(len(extBasicInfo))]
			for i in range(len(extBasicInfo)):
				right_index = dict[i]
				new[right_index] = extBasicInfo[i]
				
			#Combine extInfo with basic info
			eachBasicInfo += new
			
			#Manage NA
			for i in range(len(eachBasicInfo)):
				if eachBasicInfo[i] == "NA" and i == 3:
					eachBasicInfo[i] = " "
				elif eachBasicInfo[i] == 0 and i == 5 and eachBasicInfo[i+1] == "Serving":
					eachBasicInfo[i] = 1
				elif eachBasicInfo[i] == "NA" or eachBasicInfo[i] == '~':
					eachBasicInfo[i] = 0
					
# 			extnutrient = ["t0Water_g","t0Energy_kcal","t0Energy_kj","t0Protein_g","t0TotalLipidFat_g","t0Carbohydrate_ByDifference_g","t0Fiber_TotalDietary_g","t0Sugars_Total_g","t0Sucrose_g","t0GlucoseDextrose_g","t0Fructose_g","t0Lactose_g","t0Maltose_g","t0Galactose_g","t0Starch_g","t0AdjustedProtein_g","t1Calcium_Ca_mg","t1Iron_Fe_mg","t1Magnesium_Mg_mg","t1Phosphorus_P_mg","t1Potassium_K_mg","t1Sodium_Na_mg","t1Zinc_Zn_mg","t1Copper_Cu_mg","t1Manganese_Mn_mg","t1Selenium_Se_mcg","t1Fluoride_F_mcg","t2VitaminC_TotalAscorbicAcid_mg","t2Thiamin_mg","t2Riboflavin_mg","t2Niacin_mg","t2PantothenicAcid_mg","t2VitaminB_6_mg","t2Folate_Total_mcg","t2FolicAcid_mcg","t2Folate_Food_mcg","t2Folate_DFE_mcg_DFE","t2Choline_Total_mg","t2Betaine_mg","t2VitaminB_12_mcg","t2VitaminB_12_Added_mcg","t2VitaminA_IU_IU","t2VitaminA_RAE_mcg_RAE","t2Retinol_mcg","t2VitaminE_alpha_tocopherol__mg","t2VitaminE_Added_mg","t2Tocopherol_Beta_mg","t2Tocopherol_Gamma_mg","t2Tocopherol_Delta_mg","t2VitaminKPhylloquinone_mcg","t2Carotene_Beta_mcg","t2Carotene_Alpha_mcg","t2Cryptoxanthin_Beta_mcg","t2Lycopene_mcg","t2Lutein_Zeaxanthin_mcg","t2VitaminD_IU","t3Stigmasterol_mg","t3Phytosterols_mg","t3Beta_sitosterol_mg","t3Campesterol_mg","t3Cholesterol_mg","t3FattyAcids_TotalMonounsaturated_g","t3FattyAcids_TotalPolyunsaturated_g","t3FattyAcids_TotalSaturated_g","t3FattyAcids_TotalTrans_monoenoic_g","t3FattyAcids_TotalTrans_polyenoic_g","t3FattyAcids_TotalTrans_g","t3MonounsaturatedFats14_1_g","t3MonounsaturatedFats15_1_g","t3MonounsaturatedFats16_1C_g","t3MonounsaturatedFats16_1T_g","t3MonounsaturatedFats16_1Undifferentiated_g","t3MonounsaturatedFats17_1_g","t3MonounsaturatedFats18_1C_g","t3MonounsaturatedFats18_1T_g","t3MonounsaturatedFats18_1Undifferentiated_g","t3MonounsaturatedFats20_1_g","t3MonounsaturatedFats22_1C_g","t3MonounsaturatedFats22_1T_g","t3MonounsaturatedFats22_1Undifferentiated_g","t3MonounsaturatedFats24_1C_g","t3PolyunsaturatedFats18_2CLAs_g","t3PolyunsaturatedFats18_2I_g","t3PolyunsaturatedFats18_2N_6C_c_g","t3PolyunsaturatedFats18_2T_t_g","t3PolyunsaturatedFats18_2TNotFurtherDefined_g","t3PolyunsaturatedFats18_2Undifferentiated_g","t3PolyunsaturatedFats18_3N_3C_c_c_g","t3PolyunsaturatedFats18_3N_6C_c_c_g","t3PolyunsaturatedFats18_3Undifferentiated_g","t3PolyunsaturatedFats18_3i_g","t3PolyunsaturatedFats18_4_g","t3PolyunsaturatedFats20_2N_6C_c_g","t3PolyunsaturatedFats20_3N_3_g","t3PolyunsaturatedFats20_3N_6_g","t3PolyunsaturatedFats20_3Undifferentiated_g","t3PolyunsaturatedFats20_4N_6_g","t3PolyunsaturatedFats20_4Undifferentiated_g","t3PolyunsaturatedFats20_5N_3_g","t3PolyunsaturatedFats21_5_g","t3PolyunsaturatedFats22_4_g","t3PolyunsaturatedFats22_5N_3_g","t3PolyunsaturatedFats22_6N_3_g","t3SaturatedFats10_0_g","t3SaturatedFats12_0_g","t3SaturatedFats13_0_g","t3SaturatedFats14_0_g","t3SaturatedFats15_0_g","t3SaturatedFats16_0_g","t3SaturatedFats17_0_g","t3SaturatedFats18_0_g","t3SaturatedFats20_0_g","t3SaturatedFats22_0_g","t3SaturatedFats24_0_g","t3SaturatedFats4_0_g","t3SaturatedFats6_0_g","t3SaturatedFats8_0_g","t4Alanine_g","t4Arginine_g","t4AsparticAcid_g","t4Cystine_g","t4GlutamicAcid_g","t4Glycine_g","t4Histidine_g","t4Hydroxyproline_g","t4Isoleucine_g","t4Leucine_g","t4Lysine_g","t4Methionine_g","t4Phenylalanine_g","t4Proline_g","t4Serine_g","t4Threonine_g","t4Tryptophan_g","t4Tyrosine_g","t4Valine_g","t5Ash_g","t5Alcohol_Ethyl_g","t5Caffeine_mg","t5Theobromine_mg"]
# 			print "########"
# 			print len(eachBasicInfo)
# 			print len(extnutrient)
# 			for k in range(len(eachBasicInfo)):
# 				if k >= 25:
# 					print extnutrient[k-25],
# 				print eachBasicInfo[k]
			eachBasicInfo[26] = eachBasicInfo[8] #cal_kcal 
			eachBasicInfo[29] = eachBasicInfo[10] # total fat
			eachBasicInfo[88] = eachBasicInfo[12] #saturated fat
			eachBasicInfo[87] = eachBasicInfo[13] #polyun
			eachBasicInfo[86] = eachBasicInfo[14] #mono-un
			eachBasicInfo[85] = eachBasicInfo[15] #choles
			eachBasicInfo[46] = eachBasicInfo[16] #sodium
			eachBasicInfo[30] = eachBasicInfo[17] #carb
			eachBasicInfo[31] = eachBasicInfo[18] #fiber
			eachBasicInfo[32] = eachBasicInfo[19] #sugar
			eachBasicInfo[28] = eachBasicInfo[20] #protein
			if eachBasicInfo[21] != 0:
				eachBasicInfo[66] = float(eachBasicInfo[21])*5000/100 #vita
			if eachBasicInfo[22] != 0:
				eachBasicInfo[52] = float(eachBasicInfo[22])*60/100 # vitc
			if eachBasicInfo[23] != 0:
				eachBasicInfo[41] = float(eachBasicInfo[23])*1000/100 #calcium
			if eachBasicInfo[24] != 0:
				eachBasicInfo[42] = float(eachBasicInfo[24])*18/100 # iron
			
			newFood = createFood(eachBasicInfo)
			session.add(newFood)
			session.commit()
			
			####
			tag = newFood.tag
			tagList = tag.split()
			for eachTag in tagList:
				eachKey = FoodKey(keyid = newFood.id, word = eachTag)
				session.add(eachKey)
			session.commit()
			
		print "Done committing at", j_result
		result.close()
		j_result += 1
			
dict = createDict()
addAllFood(db.session,dict)
db.session.commit()