#With objective in mind it helps only for soritng that objective sort fucntion then needs the input of which value
#of the food to sort
#this function would return the query th
#everything must be per calories
#what to have high/ what to have low

#input - objective, what to maximize, minimize -
#look at what to minimize or maximize - the number of the nutrient - map it eg fat wil be low, 
from app.models import Food
from sqlalchemy import asc, desc
def merge(left, right,objNut):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i].value(objNut) <= right[j].value(objNut):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst,objNut):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle],objNut)
    right = mergesort(lst[middle:],objNut)
    return merge(left, right,objNut)

# max is 1 , min is zero
def rankFoodByNutrient(iNut, objNut, query, minMax, ratio, sumCal, sumNut):
	
# 	print "In Ranked Food"
# 	for each in query:
# 		print each, each.value(iNut)

	instrumentAttribute = [Food.mainType,Food.type,Food.food,Food.detail,Food.source,Food.amount,Food.unit,Food.gram,Food.cal_kcal,Food.calFat_kcal,Food.fat_g,Food.fat_pct,Food.saturFat_g,Food.polyunFat_g,Food.monounFat_g,Food.chol_mg,Food.sodium_mg,Food.carb_g,Food.fiber_g,Food.sugar_g,Food.protein_g,Food.vitA_pct,Food.vitC_pct,Food.calcium_pct,Food.iron_pct,Food.t0Water_g,Food.t0Energy_kcal,Food.t0Energy_kj,Food.t0Protein_g,Food.t0TotalLipidFat_g,Food.t0Carbohydrate_ByDifference_g,Food.t0Fiber_TotalDietary_g,Food.t0Sugars_Total_g,Food.t0Sucrose_g,Food.t0GlucoseDextrose_g,Food.t0Fructose_g,Food.t0Lactose_g,Food.t0Maltose_g,Food.t0Galactose_g,Food.t0Starch_g,Food.t0AdjustedProtein_g,Food.t1Calcium_Ca_mg,Food.t1Iron_Fe_mg,Food.t1Magnesium_Mg_mg,Food.t1Phosphorus_P_mg,Food.t1Potassium_K_mg,Food.t1Sodium_Na_mg,Food.t1Zinc_Zn_mg,Food.t1Copper_Cu_mg,Food.t1Manganese_Mn_mg,Food.t1Selenium_Se_mcg,Food.t1Fluoride_F_mcg,Food.t2VitaminC_TotalAscorbicAcid_mg,Food.t2Thiamin_mg,Food.t2Riboflavin_mg,Food.t2Niacin_mg,Food.t2PantothenicAcid_mg,Food.t2VitaminB_6_mg,Food.t2Folate_Total_mcg,Food.t2FolicAcid_mcg,Food.t2Folate_Food_mcg,Food.t2Folate_DFE_mcg_DFE,Food.t2Choline_Total_mg,Food.t2Betaine_mg,Food.t2VitaminB_12_mcg,Food.t2VitaminB_12_Added_mcg,Food.t2VitaminA_IU_IU,Food.t2VitaminA_RAE_mcg_RAE,Food.t2Retinol_mcg,Food.t2VitaminE_alpha_tocopherol__mg,Food.t2VitaminE_Added_mg,Food.t2Tocopherol_Beta_mg,Food.t2Tocopherol_Gamma_mg,Food.t2Tocopherol_Delta_mg,Food.t2VitaminKPhylloquinone_mcg,Food.t2Carotene_Beta_mcg,Food.t2Carotene_Alpha_mcg,Food.t2Cryptoxanthin_Beta_mcg,Food.t2Lycopene_mcg,Food.t2Lutein_Zeaxanthin_mcg,Food.t2VitaminD_IU,Food.t3Stigmasterol_mg,Food.t3Phytosterols_mg,Food.t3Beta_sitosterol_mg,Food.t3Campesterol_mg,Food.t3Cholesterol_mg,Food.t3FattyAcids_TotalMonounsaturated_g,Food.t3FattyAcids_TotalPolyunsaturated_g,Food.t3FattyAcids_TotalSaturated_g,Food.t3FattyAcids_TotalTrans_monoenoic_g,Food.t3FattyAcids_TotalTrans_polyenoic_g,Food.t3FattyAcids_TotalTrans_g,Food.t3MonounsaturatedFats14_1_g,Food.t3MonounsaturatedFats15_1_g,Food.t3MonounsaturatedFats16_1C_g,Food.t3MonounsaturatedFats16_1T_g,Food.t3MonounsaturatedFats16_1Undifferentiated_g,Food.t3MonounsaturatedFats17_1_g,Food.t3MonounsaturatedFats18_1C_g,Food.t3MonounsaturatedFats18_1T_g,Food.t3MonounsaturatedFats18_1Undifferentiated_g,Food.t3MonounsaturatedFats20_1_g,Food.t3MonounsaturatedFats22_1C_g,Food.t3MonounsaturatedFats22_1T_g,Food.t3MonounsaturatedFats22_1Undifferentiated_g,Food.t3MonounsaturatedFats24_1C_g,Food.t3PolyunsaturatedFats18_2CLAs_g,Food.t3PolyunsaturatedFats18_2I_g,Food.t3PolyunsaturatedFats18_2N_6C_c_g,Food.t3PolyunsaturatedFats18_2T_t_g,Food.t3PolyunsaturatedFats18_2TNotFurtherDefined_g,Food.t3PolyunsaturatedFats18_2Undifferentiated_g,Food.t3PolyunsaturatedFats18_3N_3C_c_c_g,Food.t3PolyunsaturatedFats18_3N_6C_c_c_g,Food.t3PolyunsaturatedFats18_3Undifferentiated_g,Food.t3PolyunsaturatedFats18_3i_g,Food.t3PolyunsaturatedFats18_4_g,Food.t3PolyunsaturatedFats20_2N_6C_c_g,Food.t3PolyunsaturatedFats20_3N_3_g,Food.t3PolyunsaturatedFats20_3N_6_g,Food.t3PolyunsaturatedFats20_3Undifferentiated_g,Food.t3PolyunsaturatedFats20_4N_6_g,Food.t3PolyunsaturatedFats20_4Undifferentiated_g,Food.t3PolyunsaturatedFats20_5N_3_g,Food.t3PolyunsaturatedFats21_5_g,Food.t3PolyunsaturatedFats22_4_g,Food.t3PolyunsaturatedFats22_5N_3_g,Food.t3PolyunsaturatedFats22_6N_3_g,Food.t3SaturatedFats10_0_g,Food.t3SaturatedFats12_0_g,Food.t3SaturatedFats13_0_g,Food.t3SaturatedFats14_0_g,Food.t3SaturatedFats15_0_g,Food.t3SaturatedFats16_0_g,Food.t3SaturatedFats17_0_g,Food.t3SaturatedFats18_0_g,Food.t3SaturatedFats20_0_g,Food.t3SaturatedFats22_0_g,Food.t3SaturatedFats24_0_g,Food.t3SaturatedFats4_0_g,Food.t3SaturatedFats6_0_g,Food.t3SaturatedFats8_0_g,Food.t4Alanine_g,Food.t4Arginine_g,Food.t4AsparticAcid_g,Food.t4Cystine_g,Food.t4GlutamicAcid_g,Food.t4Glycine_g,Food.t4Histidine_g,Food.t4Hydroxyproline_g,Food.t4Isoleucine_g,Food.t4Leucine_g,Food.t4Lysine_g,Food.t4Methionine_g,Food.t4Phenylalanine_g,Food.t4Proline_g,Food.t4Serine_g,Food.t4Threonine_g,Food.t4Tryptophan_g,Food.t4Tyrosine_g,Food.t4Valine_g,Food.t5Ash_g,Food.t5Alcohol_Ethyl_g,Food.t5Caffeine_mg,Food.t5Theobromine_mg]
# 	query = query.filter(instrumentAttribute[iNut] >=ratio* (sumCal + Food.t0Energy_kcal) -sumNut).limit(20)
	query = query.filter(instrumentAttribute[iNut]/sumCal >= ratio)

	result = [each for each in query]
	checkResult = []
	for each in result:
		if each.value(iNut) != 0:
			checkResult.append(each)
 			print "Food: ", each, each.value(iNut)

	return checkResult


def rankFoodByNutrientAb(query, iNut):
	instrumentAttribute = [Food.mainType,Food.type,Food.food,Food.detail,Food.source,Food.amount,Food.unit,Food.gram,Food.cal_kcal,Food.calFat_kcal,Food.fat_g,Food.fat_pct,Food.saturFat_g,Food.polyunFat_g,Food.monounFat_g,Food.chol_mg,Food.sodium_mg,Food.carb_g,Food.fiber_g,Food.sugar_g,Food.protein_g,Food.vitA_pct,Food.vitC_pct,Food.calcium_pct,Food.iron_pct,Food.t0Water_g,Food.t0Energy_kcal,Food.t0Energy_kj,Food.t0Protein_g,Food.t0TotalLipidFat_g,Food.t0Carbohydrate_ByDifference_g,Food.t0Fiber_TotalDietary_g,Food.t0Sugars_Total_g,Food.t0Sucrose_g,Food.t0GlucoseDextrose_g,Food.t0Fructose_g,Food.t0Lactose_g,Food.t0Maltose_g,Food.t0Galactose_g,Food.t0Starch_g,Food.t0AdjustedProtein_g,Food.t1Calcium_Ca_mg,Food.t1Iron_Fe_mg,Food.t1Magnesium_Mg_mg,Food.t1Phosphorus_P_mg,Food.t1Potassium_K_mg,Food.t1Sodium_Na_mg,Food.t1Zinc_Zn_mg,Food.t1Copper_Cu_mg,Food.t1Manganese_Mn_mg,Food.t1Selenium_Se_mcg,Food.t1Fluoride_F_mcg,Food.t2VitaminC_TotalAscorbicAcid_mg,Food.t2Thiamin_mg,Food.t2Riboflavin_mg,Food.t2Niacin_mg,Food.t2PantothenicAcid_mg,Food.t2VitaminB_6_mg,Food.t2Folate_Total_mcg,Food.t2FolicAcid_mcg,Food.t2Folate_Food_mcg,Food.t2Folate_DFE_mcg_DFE,Food.t2Choline_Total_mg,Food.t2Betaine_mg,Food.t2VitaminB_12_mcg,Food.t2VitaminB_12_Added_mcg,Food.t2VitaminA_IU_IU,Food.t2VitaminA_RAE_mcg_RAE,Food.t2Retinol_mcg,Food.t2VitaminE_alpha_tocopherol__mg,Food.t2VitaminE_Added_mg,Food.t2Tocopherol_Beta_mg,Food.t2Tocopherol_Gamma_mg,Food.t2Tocopherol_Delta_mg,Food.t2VitaminKPhylloquinone_mcg,Food.t2Carotene_Beta_mcg,Food.t2Carotene_Alpha_mcg,Food.t2Cryptoxanthin_Beta_mcg,Food.t2Lycopene_mcg,Food.t2Lutein_Zeaxanthin_mcg,Food.t2VitaminD_IU,Food.t3Stigmasterol_mg,Food.t3Phytosterols_mg,Food.t3Beta_sitosterol_mg,Food.t3Campesterol_mg,Food.t3Cholesterol_mg,Food.t3FattyAcids_TotalMonounsaturated_g,Food.t3FattyAcids_TotalPolyunsaturated_g,Food.t3FattyAcids_TotalSaturated_g,Food.t3FattyAcids_TotalTrans_monoenoic_g,Food.t3FattyAcids_TotalTrans_polyenoic_g,Food.t3FattyAcids_TotalTrans_g,Food.t3MonounsaturatedFats14_1_g,Food.t3MonounsaturatedFats15_1_g,Food.t3MonounsaturatedFats16_1C_g,Food.t3MonounsaturatedFats16_1T_g,Food.t3MonounsaturatedFats16_1Undifferentiated_g,Food.t3MonounsaturatedFats17_1_g,Food.t3MonounsaturatedFats18_1C_g,Food.t3MonounsaturatedFats18_1T_g,Food.t3MonounsaturatedFats18_1Undifferentiated_g,Food.t3MonounsaturatedFats20_1_g,Food.t3MonounsaturatedFats22_1C_g,Food.t3MonounsaturatedFats22_1T_g,Food.t3MonounsaturatedFats22_1Undifferentiated_g,Food.t3MonounsaturatedFats24_1C_g,Food.t3PolyunsaturatedFats18_2CLAs_g,Food.t3PolyunsaturatedFats18_2I_g,Food.t3PolyunsaturatedFats18_2N_6C_c_g,Food.t3PolyunsaturatedFats18_2T_t_g,Food.t3PolyunsaturatedFats18_2TNotFurtherDefined_g,Food.t3PolyunsaturatedFats18_2Undifferentiated_g,Food.t3PolyunsaturatedFats18_3N_3C_c_c_g,Food.t3PolyunsaturatedFats18_3N_6C_c_c_g,Food.t3PolyunsaturatedFats18_3Undifferentiated_g,Food.t3PolyunsaturatedFats18_3i_g,Food.t3PolyunsaturatedFats18_4_g,Food.t3PolyunsaturatedFats20_2N_6C_c_g,Food.t3PolyunsaturatedFats20_3N_3_g,Food.t3PolyunsaturatedFats20_3N_6_g,Food.t3PolyunsaturatedFats20_3Undifferentiated_g,Food.t3PolyunsaturatedFats20_4N_6_g,Food.t3PolyunsaturatedFats20_4Undifferentiated_g,Food.t3PolyunsaturatedFats20_5N_3_g,Food.t3PolyunsaturatedFats21_5_g,Food.t3PolyunsaturatedFats22_4_g,Food.t3PolyunsaturatedFats22_5N_3_g,Food.t3PolyunsaturatedFats22_6N_3_g,Food.t3SaturatedFats10_0_g,Food.t3SaturatedFats12_0_g,Food.t3SaturatedFats13_0_g,Food.t3SaturatedFats14_0_g,Food.t3SaturatedFats15_0_g,Food.t3SaturatedFats16_0_g,Food.t3SaturatedFats17_0_g,Food.t3SaturatedFats18_0_g,Food.t3SaturatedFats20_0_g,Food.t3SaturatedFats22_0_g,Food.t3SaturatedFats24_0_g,Food.t3SaturatedFats4_0_g,Food.t3SaturatedFats6_0_g,Food.t3SaturatedFats8_0_g,Food.t4Alanine_g,Food.t4Arginine_g,Food.t4AsparticAcid_g,Food.t4Cystine_g,Food.t4GlutamicAcid_g,Food.t4Glycine_g,Food.t4Histidine_g,Food.t4Hydroxyproline_g,Food.t4Isoleucine_g,Food.t4Leucine_g,Food.t4Lysine_g,Food.t4Methionine_g,Food.t4Phenylalanine_g,Food.t4Proline_g,Food.t4Serine_g,Food.t4Threonine_g,Food.t4Tryptophan_g,Food.t4Tyrosine_g,Food.t4Valine_g,Food.t5Ash_g,Food.t5Alcohol_Ethyl_g,Food.t5Caffeine_mg,Food.t5Theobromine_mg]
	field = [each for each in Food.__table__.columns.keys()]
	
	query = query.all()
	result = mergesortRatio(query,iNut)
	result.reverse()
	
# 	print "In rank Ab"
# 	for i in result:
# 		print i, "has this much", i.value(iNut)
	
	return result

def mergeRatio(left, right,objNut):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
    	if objNut == 26:
    		leftValue = left[i].value(objNut)
    		rightValue = right[j].value(objNut)
    	else:
    		leftValue = left[i].value(objNut)/(left[i].value(26)+0.1)
    		rightValue = right[j].value(objNut)/(right[j].value(26)+0.1)
    	if leftValue <= rightValue:
    		result.append(left[i])
    		i += 1
    	else:
    		result.append(right[j])
    		j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesortRatio(lst,objNut):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesortRatio(lst[:middle],objNut)
    right = mergesortRatio(lst[middle:],objNut)
    return mergeRatio(left, right,objNut)
    