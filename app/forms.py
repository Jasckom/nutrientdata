from flask.ext.wtf import Form, TextField, PasswordField, DecimalField, RadioField, SelectMultipleField,SubmitField, BooleanField, Field, TextInput,validators, IntegerField
from flask.ext.wtf import Required, widgets

class SearchForm(Form):
    searchEntry = TextField('searchEntry')
    brandEntry = TextField('brandEntry')
    
from flask.ext.wtf import SelectField
class SelectFood(Form):
	foodOptions = SelectField('foodOptions', coerce=int)

def SelectFilter(filter):
	class selectFilter(Form):
		full_total_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
		choices = []
		choices.append((24, 'Nutrients'))
		for i in range(len(full_total_nutrient)):
			if i != 2 and i != 0:
				choices.append((i+25, (full_total_nutrient[i].split('/'))[0]) ) 
	selectFilter.filterNut = SelectField('Filter by',coerce=int,choices = selectFilter.choices, validators = [Required()], default = filter)
	selectFilter.filter = SubmitField("Go!")
	form = selectFilter()
	return form

class LoginForm(Form):
	usernameLog = TextField('usernameLog', validators = [Required()])
	passwordLog = PasswordField('passwordLog', validators = [Required()])

class SignupForm(Form):
	usernameSign = TextField('usernameLog', validators = [Required()])
	passwordSign = PasswordField('passwordLog', validators = [Required()])
	

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class EditPreferredList(Form):
	foodOptions = MultiCheckboxField('foodOptions', coerce=int)
	submit = SubmitField("Checkout: Create My Diet Plan")
	remove = SubmitField("Remove")
	checkAll = BooleanField("Check All")
	
def createFoodsILike(foodIdsArg, foodNamesArg):
#foodDict has key as ID and value as foodnames - This helps the quick reflection of the current status of the session
	class FoodsILike(Form):
		foodIds = foodIdsArg
		foodNames = foodNamesArg
	FoodsILike.submit = SubmitField('Generate My Diet')
	FoodsILike.remove = SubmitField("Remove")
	FoodsILike.toggle = SubmitField("Select/Deselect All")
	for i in range(len(FoodsILike.foodIds)):
		setattr(FoodsILike, FoodsILike.foodIds[i] , BooleanField(FoodsILike.foodNames[i], [validators.Optional()]))
	form = FoodsILike()
	return form

		
	
class MultiInputField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = TextInput()

def createMinMaxForm(checkArg, basicPlan, optMaxMin, optNut, nextButton):
 	total_nutrient = ["t0Water_g","t0Energy_kcal","t0Energy_kj","t0Protein_g","t0TotalLipidFat_g","t0Carbohydrate_ByDifference_g","t0Fiber_TotalDietary_g","t0Sugars_Total_g","t0Sucrose_g","t0GlucoseDextrose_g","t0Fructose_g","t0Lactose_g","t0Maltose_g","t0Galactose_g","t0Starch_g","t0AdjustedProtein_g","t1Calcium_Ca_mg","t1Iron_Fe_mg","t1Magnesium_Mg_mg","t1Phosphorus_P_mg","t1Potassium_K_mg","t1Sodium_Na_mg","t1Zinc_Zn_mg","t1Copper_Cu_mg","t1Manganese_Mn_mg","t1Selenium_Se_mcg","t1Fluoride_F_mcg","t2VitaminC_TotalAscorbicAcid_mg","t2Thiamin_mg","t2Riboflavin_mg","t2Niacin_mg","t2PantothenicAcid_mg","t2VitaminB_6_mg","t2Folate_Total_mcg","t2FolicAcid_mcg","t2Folate_Food_mcg","t2Folate_DFE_mcg_DFE","t2Choline_Total_mg","t2Betaine_mg","t2VitaminB_12_mcg","t2VitaminB_12_Added_mcg","t2VitaminA_IU_IU","t2VitaminA_RAE_mcg_RAE","t2Retinol_mcg","t2VitaminE_alpha_tocopherol__mg","t2VitaminE_Added_mg","t2Tocopherol_Beta_mg","t2Tocopherol_Gamma_mg","t2Tocopherol_Delta_mg","t2VitaminKPhylloquinone_mcg","t2Carotene_Beta_mcg","t2Carotene_Alpha_mcg","t2Cryptoxanthin_Beta_mcg","t2Lycopene_mcg","t2Lutein_Zeaxanthin_mcg","t2VitaminD_IU","t3Stigmasterol_mg","t3Phytosterols_mg","t3Beta_sitosterol_mg","t3Campesterol_mg","t3Cholesterol_mg","t3FattyAcids_TotalMonounsaturated_g","t3FattyAcids_TotalPolyunsaturated_g","t3FattyAcids_TotalSaturated_g","t3FattyAcids_TotalTrans_monoenoic_g","t3FattyAcids_TotalTrans_polyenoic_g","t3FattyAcids_TotalTrans_g","t3MonounsaturatedFats14_1_g","t3MonounsaturatedFats15_1_g","t3MonounsaturatedFats16_1C_g","t3MonounsaturatedFats16_1T_g","t3MonounsaturatedFats16_1Undifferentiated_g","t3MonounsaturatedFats17_1_g","t3MonounsaturatedFats18_1C_g","t3MonounsaturatedFats18_1T_g","t3MonounsaturatedFats18_1Undifferentiated_g","t3MonounsaturatedFats20_1_g","t3MonounsaturatedFats22_1C_g","t3MonounsaturatedFats22_1T_g","t3MonounsaturatedFats22_1Undifferentiated_g","t3MonounsaturatedFats24_1C_g","t3PolyunsaturatedFats18_2CLAs_g","t3PolyunsaturatedFats18_2I_g","t3PolyunsaturatedFats18_2N_6C_c_g","t3PolyunsaturatedFats18_2T_t_g","t3PolyunsaturatedFats18_2TNotFurtherDefined_g","t3PolyunsaturatedFats18_2Undifferentiated_g","t3PolyunsaturatedFats18_3N_3C_c_c_g","t3PolyunsaturatedFats18_3N_6C_c_c_g","t3PolyunsaturatedFats18_3Undifferentiated_g","t3PolyunsaturatedFats18_3i_g","t3PolyunsaturatedFats18_4_g","t3PolyunsaturatedFats20_2N_6C_c_g","t3PolyunsaturatedFats20_3N_3_g","t3PolyunsaturatedFats20_3N_6_g","t3PolyunsaturatedFats20_3Undifferentiated_g","t3PolyunsaturatedFats20_4N_6_g","t3PolyunsaturatedFats20_4Undifferentiated_g","t3PolyunsaturatedFats20_5N_3_g","t3PolyunsaturatedFats21_5_g","t3PolyunsaturatedFats22_4_g","t3PolyunsaturatedFats22_5N_3_g","t3PolyunsaturatedFats22_6N_3_g","t3SaturatedFats10_0_g","t3SaturatedFats12_0_g","t3SaturatedFats13_0_g","t3SaturatedFats14_0_g","t3SaturatedFats15_0_g","t3SaturatedFats16_0_g","t3SaturatedFats17_0_g","t3SaturatedFats18_0_g","t3SaturatedFats20_0_g","t3SaturatedFats22_0_g","t3SaturatedFats24_0_g","t3SaturatedFats4_0_g","t3SaturatedFats6_0_g","t3SaturatedFats8_0_g","t4Alanine_g","t4Arginine_g","t4AsparticAcid_g","t4Cystine_g","t4GlutamicAcid_g","t4Glycine_g","t4Histidine_g","t4Hydroxyproline_g","t4Isoleucine_g","t4Leucine_g","t4Lysine_g","t4Methionine_g","t4Phenylalanine_g","t4Proline_g","t4Serine_g","t4Threonine_g","t4Tryptophan_g","t4Tyrosine_g","t4Valine_g","t5Ash_g","t5Alcohol_Ethyl_g","t5Caffeine_mg","t5Theobromine_mg"]
# 	basic_nutrient = ["cal_kcal","calFat_kcal","fat_g","fat_pct","saturFat_g","polyunFat_g","monounFat_g","chol_mg","sodium_mg","carb_g","fiber_g","sugar_g","protein_g","vitA_pct","vitC_pct","calcium_pct","iron_pct"]
# 	total_nutrient = basic_nutrient+ext_nutrient
# 	full_basic_nutrient = ["Calories/kcal","Calories from Fat/kcal","Total Fat/g","Fat /%","Saturated Fat/g","Polyunsaturated Fat/g","Monounsaturated Fat/g","Cholestorl/mg","Sodium/mg","Total Carbohydrate/g","Fiber/g","Sugar/g","Protein/g","Vitamin A/%","Vitamin C/%","Calcium/%","Iron/%"]
# 	full_ext_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
	full_total_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
	print "Total nutrient", len(full_total_nutrient)
	print "CheckArg", len(checkArg)
	class MinMaxForm(Form):
		heading = full_total_nutrient
		upperBound = [100 for i in range(len(total_nutrient))]
		lowerBound = [1 for i in range(len(total_nutrient))]
		check = checkArg
		basicPlan = [26,28,29,30,31,32,41,42,46,52,85,88]

	for i in range(len(total_nutrient)):
		basic = ""
		if i+25 not in MinMaxForm.basicPlan:
			basic = "Full"
		#print "eachChek: ",MinMaxForm.check[i]
		setattr(MinMaxForm, basic+total_nutrient[i]+"check", BooleanField(basic+total_nutrient[i]+"check",[validators.Optional()], default=MinMaxForm.check[i]))
		setattr(MinMaxForm, basic+total_nutrient[i]+"min", TextField(basic+total_nutrient[i]+"min", [validators.Optional()]))
		setattr(MinMaxForm, basic+total_nutrient[i]+"max", TextField(basic+total_nutrient[i]+"max", [validators.Optional()]))
	
	
	MinMaxForm.opt_maxormin = RadioField('opt_maxormin', coerce = int, choices=[(1, 'Maxmimize'), (0, 'Minimize'),(2, 'Low Calorie'), (3, 'Low Protein'), (4, 'High Protein')], default = optMaxMin)
	
	radioList= []
	for i in range(len(total_nutrient)):
		if i != 2 and i != 0:
			radioList.append((i+25, (full_total_nutrient[i].split('/'))[0]))
	MinMaxForm.opt_nut = RadioField('opt_nut', [validators.Optional()],coerce=int, choices = radioList, default = optNut  )
	MinMaxForm.nutrientPlan = RadioField('nutrientPlan',validators = [Required()], coerce = int, choices=[(1, 'Basic Nutrient'), (0, 'With Minerals and Vitamins')], default= basicPlan)
	MinMaxForm.submit = SubmitField(nextButton, validators = [Required()])

	minMaxForm = MinMaxForm()
	return minMaxForm


def SelectFilter(filter):
	class selectFilter(Form):
		full_total_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
		choices = []
		choices.append((24, 'Nutrients'))
		for i in range(len(full_total_nutrient)):
			if i != 2 and i != 0:
				choices.append((i+25, (full_total_nutrient[i].split('/'))[0]) ) 
	selectFilter.filterNut = SelectField('Filter by',coerce=int,choices = selectFilter.choices, validators = [Required()], default = filter)
	selectFilter.filter = SubmitField("Go!")
	form = selectFilter()
	return form



def Profile(user):
	class profile(Form):
		pass

	if user.heightInch is None: #metric
		defaultSystem = "Metric"
		defaultHeight = [int(user.heightFeet), None, None, None]
		defaultWeight = [int(user.weight), None]
		
	else:
		defaultSystem = "US"
		defaultHeight = [None, None,int(user.heightFeet), int(user.heightInch) ]
		defaultWeight = [None, int(user.weight)]


	profile.age = IntegerField('age',validators = [Required()], default = int(user.age))
	profile.gender = RadioField('gender', validators = [Required()], choices =[("Males","Male"),("Females","Female")], default = user.gender)
	profile.conditions = SelectField('condition', choices=[("None","None"),("Pregnancy","Pregnancy"),("Lactation","Lactation")],validators = [Required()],default = user.conditions)
	
	profile.unitSystem = RadioField('gender', validators = [Required()], choices =[("US","US"),("Metric","Metric")], default = defaultSystem)
	profile.weight = IntegerField('weight(lb)',[validators.Optional()], default = defaultWeight[1])
	profile.weightKg = IntegerField('weight(kg)',[validators.Optional()], default = defaultWeight[0])
	profile.heightFeet = IntegerField('height(ft)',[validators.Optional()], default = defaultHeight[2])
	profile.heightInch = IntegerField('height(in)',[validators.Optional()], default = defaultHeight[3])
	profile.heightCm = IntegerField('height(cm)',[validators.Optional()], default = defaultHeight[0])
	profile.activity = SelectField('activity', coerce = float ,choices=[(1.2,"Sedentary"),(1.375,"Lightly Active"),(1.55,"Moderately Active"),(1.725,"Very active"),(1.9,"Extremely Active")],validators = [Required()], default = user.activity)
	profile.saveChange = SubmitField("Save Changes")
	form = profile()
	return form

class ProfileFull(Form):
    age = DecimalField('age',validators = [Required()])
    conditions = SelectField('condition', choices=[("None","None"),("Pregnancy","Pregnancy"),("Lactation","Lactation")],validators = [Required()])
    weight = DecimalField('weight(lb)',[validators.Optional()])
    weightKg = DecimalField('weight(kg)',[validators.Optional()])
    heightFeet = DecimalField('height(ft)',[validators.Optional()])
    heightInch = DecimalField('height(in)',[validators.Optional()])
    heightCm = DecimalField('height(cm)',[validators.Optional()])
    activity = SelectField('activity', coerce = float ,choices=[(1.2,"Sedentary"),(1.375,"Lightly Active"),(1.55,"Moderately Active"),(1.725,"Very active"),(1.9,"Extremely Active")],validators = [Required()])
    submitGuest = SubmitField("Guest")
    submitSignUp = SubmitField("Sign Up")


class manyButtons(Form):
	text = DecimalField('text', validators = [Required()])
	submit1 = SubmitField('Submit1')
	submit2 = SubmitField('Submit2')

class Button(Form):
	submit = SubmitField('button')