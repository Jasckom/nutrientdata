from app import db
from app import app
#from sqlalchemy_searchable import SearchQueryMixin, Searchable
#from flask.ext.sqlalchemy import BaseQuery
#import flask.ext.whooshalchemy as whooshalchemy


ROLE_USER = 0
ROLE_GUEST = 1
ROLE_ADMIN = 2

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(64), index = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    age = db.Column(db.Float)
    gender = db.Column(db.String(10))
    conditions = db.Column(db.String(64))
    #For calculating calories
    weight = db.Column(db.Float)
    heightFeet = db.Column(db.Float)
    heightInch = db.Column(db.Float)
    activity = db.Column(db.Float)
    nutri = db.relationship('Nutri', backref = 'user', lazy = 'dynamic')
    food = db.relationship('Food')
    checkedFood = db.Column(db.String) #tell which foods from the food selected is given for optimization
    portions = db.Column(db.String) # correspond to the shortlisted food when compared to checkedFood
    optPlans = db.Column(db.String)
    opt_nut = db.Column(db.Integer)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

TYPE_DEFAULT = 0
TYPE_CUSTOMIZE = 1
class Nutri(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.Integer, default = TYPE_DEFAULT)
	ageGroup = db.Column(db.String(15))
	gender = db.Column(db.String(10))
	conditions = db.Column(db.String(64))
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))
	cal_kcal =db.Column(db.String(32)) #6
	calFat_kcal =db.Column(db.String(32))
	fat_g =db.Column(db.String(32))
	fat_pct =db.Column(db.String(32))
	saturFat_g =db.Column(db.String(32))
	polyunFat_g =db.Column(db.String(32))
	monounFat_g =db.Column(db.String(32))
	chol_mg =db.Column(db.String(32))
	sodium_mg =db.Column(db.String(32))
	carb_g =db.Column(db.String(32))
	fiber_g =db.Column(db.String(32))
	sugar_g =db.Column(db.String(32))
	protein_g =db.Column(db.String(32))
	vitA_pct =db.Column(db.String(32))
	vitC_pct =db.Column(db.String(32))
	calcium_pct =db.Column(db.String(32))
	iron_pct =db.Column(db.String(32))
	t0Water_g=db.Column(db.String(32)) #23
	t0Energy_kcal=db.Column(db.String(32))
	t0Energy_kj=db.Column(db.String(32))
	t0Protein_g=db.Column(db.String(32))
	t0TotalLipidFat_g=db.Column(db.String(32))
	t0Carbohydrate_ByDifference_g=db.Column(db.String(32))
	t0Fiber_TotalDietary_g=db.Column(db.String(32))
	t0Sugars_Total_g=db.Column(db.String(32))
	t0Sucrose_g=db.Column(db.String(32))
	t0GlucoseDextrose_g=db.Column(db.String(32))
	t0Fructose_g=db.Column(db.String(32))
	t0Lactose_g=db.Column(db.String(32))
	t0Maltose_g=db.Column(db.String(32))
	t0Galactose_g=db.Column(db.String(32))
	t0Starch_g=db.Column(db.String(32))
	t0AdjustedProtein_g=db.Column(db.String(32))
	t1Calcium_Ca_mg=db.Column(db.String(32))
	t1Iron_Fe_mg=db.Column(db.String(32))
	t1Magnesium_Mg_mg=db.Column(db.String(32))
	t1Phosphorus_P_mg=db.Column(db.String(32))
	t1Potassium_K_mg=db.Column(db.String(32))
	t1Sodium_Na_mg=db.Column(db.String(32))
	t1Zinc_Zn_mg=db.Column(db.String(32))
	t1Copper_Cu_mg=db.Column(db.String(32))
	t1Manganese_Mn_mg=db.Column(db.String(32))
	t1Selenium_Se_mcg=db.Column(db.String(32))
	t1Fluoride_F_mcg=db.Column(db.String(32))
	t2VitaminC_TotalAscorbicAcid_mg=db.Column(db.String(32))
	t2Thiamin_mg=db.Column(db.String(32))
	t2Riboflavin_mg=db.Column(db.String(32))
	t2Niacin_mg=db.Column(db.String(32))
	t2PantothenicAcid_mg=db.Column(db.String(32))
	t2VitaminB_6_mg=db.Column(db.String(32))
	t2Folate_Total_mcg=db.Column(db.String(32))
	t2FolicAcid_mcg=db.Column(db.String(32))
	t2Folate_Food_mcg=db.Column(db.String(32))
	t2Folate_DFE_mcg_DFE=db.Column(db.String(32))
	t2Choline_Total_mg=db.Column(db.String(32))
	t2Betaine_mg=db.Column(db.String(32))
	t2VitaminB_12_mcg=db.Column(db.String(32))
	t2VitaminB_12_Added_mcg=db.Column(db.String(32))
	t2VitaminA_IU_IU=db.Column(db.String(32))
	t2VitaminA_RAE_mcg_RAE=db.Column(db.String(32))
	t2Retinol_mcg=db.Column(db.String(32))
	t2VitaminE_alpha_tocopherol__mg=db.Column(db.String(32))
	t2VitaminE_Added_mg=db.Column(db.String(32))
	t2Tocopherol_Beta_mg=db.Column(db.String(32))
	t2Tocopherol_Gamma_mg=db.Column(db.String(32))
	t2Tocopherol_Delta_mg=db.Column(db.String(32))
	t2VitaminKPhylloquinone_mcg=db.Column(db.String(32))
	t2Carotene_Beta_mcg=db.Column(db.String(32))
	t2Carotene_Alpha_mcg=db.Column(db.String(32))
	t2Cryptoxanthin_Beta_mcg=db.Column(db.String(32))
	t2Lycopene_mcg=db.Column(db.String(32))
	t2Lutein_Zeaxanthin_mcg=db.Column(db.String(32))
	t2VitaminD_IU=db.Column(db.String(32))
	t3Stigmasterol_mg=db.Column(db.String(32))
	t3Phytosterols_mg=db.Column(db.String(32))
	t3Beta_sitosterol_mg=db.Column(db.String(32))
	t3Campesterol_mg=db.Column(db.String(32))
	t3Cholesterol_mg=db.Column(db.String(32))
	t3FattyAcids_TotalMonounsaturated_g=db.Column(db.String(32))
	t3FattyAcids_TotalPolyunsaturated_g=db.Column(db.String(32))
	t3FattyAcids_TotalSaturated_g=db.Column(db.String(32))
	t3FattyAcids_TotalTrans_monoenoic_g=db.Column(db.String(32))
	t3FattyAcids_TotalTrans_polyenoic_g=db.Column(db.String(32))
	t3FattyAcids_TotalTrans_g=db.Column(db.String(32))
	t3MonounsaturatedFats14_1_g=db.Column(db.String(32))
	t3MonounsaturatedFats15_1_g=db.Column(db.String(32))
	t3MonounsaturatedFats16_1C_g=db.Column(db.String(32))
	t3MonounsaturatedFats16_1T_g=db.Column(db.String(32))
	t3MonounsaturatedFats16_1Undifferentiated_g=db.Column(db.String(32))
	t3MonounsaturatedFats17_1_g=db.Column(db.String(32))
	t3MonounsaturatedFats18_1C_g=db.Column(db.String(32))
	t3MonounsaturatedFats18_1T_g=db.Column(db.String(32))
	t3MonounsaturatedFats18_1Undifferentiated_g=db.Column(db.String(32))
	t3MonounsaturatedFats20_1_g=db.Column(db.String(32))
	t3MonounsaturatedFats22_1C_g=db.Column(db.String(32))
	t3MonounsaturatedFats22_1T_g=db.Column(db.String(32))
	t3MonounsaturatedFats22_1Undifferentiated_g=db.Column(db.String(32))
	t3MonounsaturatedFats24_1C_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2CLAs_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2I_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2N_6C_c_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2T_t_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2TNotFurtherDefined_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_2Undifferentiated_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_3N_3C_c_c_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_3N_6C_c_c_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_3Undifferentiated_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_3i_g=db.Column(db.String(32))
	t3PolyunsaturatedFats18_4_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_2N_6C_c_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_3N_3_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_3N_6_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_3Undifferentiated_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_4N_6_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_4Undifferentiated_g=db.Column(db.String(32))
	t3PolyunsaturatedFats20_5N_3_g=db.Column(db.String(32))
	t3PolyunsaturatedFats21_5_g=db.Column(db.String(32))
	t3PolyunsaturatedFats22_4_g=db.Column(db.String(32))
	t3PolyunsaturatedFats22_5N_3_g=db.Column(db.String(32))
	t3PolyunsaturatedFats22_6N_3_g=db.Column(db.String(32))
	t3SaturatedFats10_0_g=db.Column(db.String(32))
	t3SaturatedFats12_0_g=db.Column(db.String(32))
	t3SaturatedFats13_0_g=db.Column(db.String(32))
	t3SaturatedFats14_0_g=db.Column(db.String(32))
	t3SaturatedFats15_0_g=db.Column(db.String(32))
	t3SaturatedFats16_0_g=db.Column(db.String(32))
	t3SaturatedFats17_0_g=db.Column(db.String(32))
	t3SaturatedFats18_0_g=db.Column(db.String(32))
	t3SaturatedFats20_0_g=db.Column(db.String(32))
	t3SaturatedFats22_0_g=db.Column(db.String(32))
	t3SaturatedFats24_0_g=db.Column(db.String(32))
	t3SaturatedFats4_0_g=db.Column(db.String(32))
	t3SaturatedFats6_0_g=db.Column(db.String(32))
	t3SaturatedFats8_0_g=db.Column(db.String(32))
	t4Alanine_g=db.Column(db.String(32))
	t4Arginine_g=db.Column(db.String(32))
	t4AsparticAcid_g=db.Column(db.String(32))
	t4Cystine_g=db.Column(db.String(32))
	t4GlutamicAcid_g=db.Column(db.String(32))
	t4Glycine_g=db.Column(db.String(32))
	t4Histidine_g=db.Column(db.String(32))
	t4Hydroxyproline_g=db.Column(db.String(32))
	t4Isoleucine_g=db.Column(db.String(32))
	t4Leucine_g=db.Column(db.String(32))
	t4Lysine_g=db.Column(db.String(32))
	t4Methionine_g=db.Column(db.String(32))
	t4Phenylalanine_g=db.Column(db.String(32))
	t4Proline_g=db.Column(db.String(32))
	t4Serine_g=db.Column(db.String(32))
	t4Threonine_g=db.Column(db.String(32))
	t4Tryptophan_g=db.Column(db.String(32))
	t4Tyrosine_g=db.Column(db.String(32))
	t4Valine_g=db.Column(db.String(32))
	t5Ash_g=db.Column(db.String(32))
	t5Alcohol_Ethyl_g=db.Column(db.String(32))
	t5Caffeine_mg=db.Column(db.String(32))
	t5Theobromine_mg=db.Column(db.String(32))
	

	def __repr__(self):
		return "<Nutri('%s','%s', '%s', '%s')>" % (self.type , self.ageGroup , self.gender, self.conditions )
		
	def nutCalRatio(self,index):
		values = [0,0]
		for keys in self.__table__.columns.keys():
			values.append( getattr(self,keys))
# 		print index,
		full_ext_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
		# to make it consistent with accessing values of Food starting with water at 25
		cal = self.t0Energy_kcal.split(":")[1]
		if cal == "ND":
			cal = 5000
		else:
			cal = float(cal)
		val = (values[index].split(":")[0])
		
		if val == "ND":
			val = 0
		else:	
			val = float(val)
		
		if cal == 0:
			return val
# 		print "ratio of ", full_ext_nutrient[index-25], "is", val, "/", cal, "=", val/cal

		return (val/cal)
	

class Food(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	mainType = db.Column(db.String)
	type = db.Column(db.String)
	food = db.Column(db.String)
	detail = db.Column(db.String)
	source = db.Column(db.String)
	amount = db.Column(db.Float)
	unit = db.Column(db.String)
	gram = db.Column(db.Float)
	#for search and for linking to user
	tag =  db.Column(db.String, index = True)
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	cal_kcal = db.Column(db.Float)
	calFat_kcal = db.Column(db.Float)
	fat_g = db.Column(db.Float)
	fat_pct = db.Column(db.Float)
	saturFat_g = db.Column(db.Float)
	polyunFat_g = db.Column(db.Float)
	monounFat_g = db.Column(db.Float)
	chol_mg = db.Column(db.Float)
	sodium_mg = db.Column(db.Float)
	carb_g = db.Column(db.Float)
	fiber_g = db.Column(db.Float)
	sugar_g = db.Column(db.Float)
	protein_g = db.Column(db.Float)
	vitA_pct = db.Column(db.Float)
	vitC_pct = db.Column(db.Float)
	calcium_pct = db.Column(db.Float)
	iron_pct = db.Column(db.Float)
	t0Water_g= db.Column(db.Float)
	t0Energy_kcal= db.Column(db.Float)
	t0Energy_kj= db.Column(db.Float)
	t0Protein_g= db.Column(db.Float)
	t0TotalLipidFat_g= db.Column(db.Float)
	t0Carbohydrate_ByDifference_g= db.Column(db.Float)
	t0Fiber_TotalDietary_g= db.Column(db.Float)
	t0Sugars_Total_g= db.Column(db.Float)
	t0Sucrose_g= db.Column(db.Float)
	t0GlucoseDextrose_g= db.Column(db.Float)
	t0Fructose_g= db.Column(db.Float)
	t0Lactose_g= db.Column(db.Float)
	t0Maltose_g= db.Column(db.Float)
	t0Galactose_g= db.Column(db.Float)
	t0Starch_g= db.Column(db.Float)
	t0AdjustedProtein_g= db.Column(db.Float)
	t1Calcium_Ca_mg= db.Column(db.Float)
	t1Iron_Fe_mg= db.Column(db.Float)
	t1Magnesium_Mg_mg= db.Column(db.Float)
	t1Phosphorus_P_mg= db.Column(db.Float)
	t1Potassium_K_mg= db.Column(db.Float)
	t1Sodium_Na_mg= db.Column(db.Float)
	t1Zinc_Zn_mg= db.Column(db.Float)
	t1Copper_Cu_mg= db.Column(db.Float)
	t1Manganese_Mn_mg= db.Column(db.Float)
	t1Selenium_Se_mcg= db.Column(db.Float)
	t1Fluoride_F_mcg= db.Column(db.Float)
	t2VitaminC_TotalAscorbicAcid_mg= db.Column(db.Float)
	t2Thiamin_mg= db.Column(db.Float)
	t2Riboflavin_mg= db.Column(db.Float)
	t2Niacin_mg= db.Column(db.Float)
	t2PantothenicAcid_mg= db.Column(db.Float)
	t2VitaminB_6_mg= db.Column(db.Float)
	t2Folate_Total_mcg= db.Column(db.Float)
	t2FolicAcid_mcg= db.Column(db.Float)
	t2Folate_Food_mcg= db.Column(db.Float)
	t2Folate_DFE_mcg_DFE= db.Column(db.Float)
	t2Choline_Total_mg= db.Column(db.Float)
	t2Betaine_mg= db.Column(db.Float)
	t2VitaminB_12_mcg= db.Column(db.Float)
	t2VitaminB_12_Added_mcg= db.Column(db.Float)
	t2VitaminA_IU_IU= db.Column(db.Float)
	t2VitaminA_RAE_mcg_RAE= db.Column(db.Float)
	t2Retinol_mcg= db.Column(db.Float)
	t2VitaminE_alpha_tocopherol__mg= db.Column(db.Float)
	t2VitaminE_Added_mg= db.Column(db.Float)
	t2Tocopherol_Beta_mg= db.Column(db.Float)
	t2Tocopherol_Gamma_mg= db.Column(db.Float)
	t2Tocopherol_Delta_mg= db.Column(db.Float)
	t2VitaminKPhylloquinone_mcg= db.Column(db.Float)
	t2Carotene_Beta_mcg= db.Column(db.Float)
	t2Carotene_Alpha_mcg= db.Column(db.Float)
	t2Cryptoxanthin_Beta_mcg= db.Column(db.Float)
	t2Lycopene_mcg= db.Column(db.Float)
	t2Lutein_Zeaxanthin_mcg= db.Column(db.Float)
	t2VitaminD_IU= db.Column(db.Float)
	t3Stigmasterol_mg= db.Column(db.Float)
	t3Phytosterols_mg= db.Column(db.Float)
	t3Beta_sitosterol_mg= db.Column(db.Float)
	t3Campesterol_mg= db.Column(db.Float)
	t3Cholesterol_mg= db.Column(db.Float)
	t3FattyAcids_TotalMonounsaturated_g= db.Column(db.Float)
	t3FattyAcids_TotalPolyunsaturated_g= db.Column(db.Float)
	t3FattyAcids_TotalSaturated_g= db.Column(db.Float)
	t3FattyAcids_TotalTrans_monoenoic_g= db.Column(db.Float)
	t3FattyAcids_TotalTrans_polyenoic_g= db.Column(db.Float)
	t3FattyAcids_TotalTrans_g= db.Column(db.Float)
	t3MonounsaturatedFats14_1_g= db.Column(db.Float)
	t3MonounsaturatedFats15_1_g= db.Column(db.Float)
	t3MonounsaturatedFats16_1C_g= db.Column(db.Float)
	t3MonounsaturatedFats16_1T_g= db.Column(db.Float)
	t3MonounsaturatedFats16_1Undifferentiated_g= db.Column(db.Float)
	t3MonounsaturatedFats17_1_g= db.Column(db.Float)
	t3MonounsaturatedFats18_1C_g= db.Column(db.Float)
	t3MonounsaturatedFats18_1T_g= db.Column(db.Float)
	t3MonounsaturatedFats18_1Undifferentiated_g= db.Column(db.Float)
	t3MonounsaturatedFats20_1_g= db.Column(db.Float)
	t3MonounsaturatedFats22_1C_g= db.Column(db.Float)
	t3MonounsaturatedFats22_1T_g= db.Column(db.Float)
	t3MonounsaturatedFats22_1Undifferentiated_g= db.Column(db.Float)
	t3MonounsaturatedFats24_1C_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2CLAs_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2I_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2N_6C_c_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2T_t_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2TNotFurtherDefined_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_2Undifferentiated_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_3N_3C_c_c_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_3N_6C_c_c_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_3Undifferentiated_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_3i_g= db.Column(db.Float)
	t3PolyunsaturatedFats18_4_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_2N_6C_c_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_3N_3_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_3N_6_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_3Undifferentiated_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_4N_6_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_4Undifferentiated_g= db.Column(db.Float)
	t3PolyunsaturatedFats20_5N_3_g= db.Column(db.Float)
	t3PolyunsaturatedFats21_5_g= db.Column(db.Float)
	t3PolyunsaturatedFats22_4_g= db.Column(db.Float)
	t3PolyunsaturatedFats22_5N_3_g= db.Column(db.Float)
	t3PolyunsaturatedFats22_6N_3_g= db.Column(db.Float)
	t3SaturatedFats10_0_g= db.Column(db.Float)
	t3SaturatedFats12_0_g= db.Column(db.Float)
	t3SaturatedFats13_0_g= db.Column(db.Float)
	t3SaturatedFats14_0_g= db.Column(db.Float)
	t3SaturatedFats15_0_g= db.Column(db.Float)
	t3SaturatedFats16_0_g= db.Column(db.Float)
	t3SaturatedFats17_0_g= db.Column(db.Float)
	t3SaturatedFats18_0_g= db.Column(db.Float)
	t3SaturatedFats20_0_g= db.Column(db.Float)
	t3SaturatedFats22_0_g= db.Column(db.Float)
	t3SaturatedFats24_0_g= db.Column(db.Float)
	t3SaturatedFats4_0_g= db.Column(db.Float)
	t3SaturatedFats6_0_g= db.Column(db.Float)
	t3SaturatedFats8_0_g= db.Column(db.Float)
	t4Alanine_g= db.Column(db.Float)
	t4Arginine_g= db.Column(db.Float)
	t4AsparticAcid_g= db.Column(db.Float)
	t4Cystine_g= db.Column(db.Float)
	t4GlutamicAcid_g= db.Column(db.Float)
	t4Glycine_g= db.Column(db.Float)
	t4Histidine_g= db.Column(db.Float)
	t4Hydroxyproline_g= db.Column(db.Float)
	t4Isoleucine_g= db.Column(db.Float)
	t4Leucine_g= db.Column(db.Float)
	t4Lysine_g= db.Column(db.Float)
	t4Methionine_g= db.Column(db.Float)
	t4Phenylalanine_g= db.Column(db.Float)
	t4Proline_g= db.Column(db.Float)
	t4Serine_g= db.Column(db.Float)
	t4Threonine_g= db.Column(db.Float)
	t4Tryptophan_g= db.Column(db.Float)
	t4Tyrosine_g= db.Column(db.Float)
	t4Valine_g= db.Column(db.Float)
	t5Ash_g= db.Column(db.Float)
	t5Alcohol_Ethyl_g= db.Column(db.Float)
	t5Caffeine_mg= db.Column(db.Float)
	t5Theobromine_mg= db.Column(db.Float)

	def value(self,index):
		values = [self.mainType,self.type,self.food,self.detail,self.source,self.amount,self.unit,self.gram,self.cal_kcal,self.calFat_kcal,self.fat_g,self.fat_pct,self.saturFat_g,self.polyunFat_g,self.monounFat_g,self.chol_mg,self.sodium_mg,self.carb_g,self.fiber_g,self.sugar_g,self.protein_g,self.vitA_pct,self.vitC_pct,self.calcium_pct,self.iron_pct,self.t0Water_g,self.t0Energy_kcal,self.t0Energy_kj,self.t0Protein_g,self.t0TotalLipidFat_g,self.t0Carbohydrate_ByDifference_g,self.t0Fiber_TotalDietary_g,self.t0Sugars_Total_g,self.t0Sucrose_g,self.t0GlucoseDextrose_g,self.t0Fructose_g,self.t0Lactose_g,self.t0Maltose_g,self.t0Galactose_g,self.t0Starch_g,self.t0AdjustedProtein_g,self.t1Calcium_Ca_mg,self.t1Iron_Fe_mg,self.t1Magnesium_Mg_mg,self.t1Phosphorus_P_mg,self.t1Potassium_K_mg,self.t1Sodium_Na_mg,self.t1Zinc_Zn_mg,self.t1Copper_Cu_mg,self.t1Manganese_Mn_mg,self.t1Selenium_Se_mcg,self.t1Fluoride_F_mcg,self.t2VitaminC_TotalAscorbicAcid_mg,self.t2Thiamin_mg,self.t2Riboflavin_mg,self.t2Niacin_mg,self.t2PantothenicAcid_mg,self.t2VitaminB_6_mg,self.t2Folate_Total_mcg,self.t2FolicAcid_mcg,self.t2Folate_Food_mcg,self.t2Folate_DFE_mcg_DFE,self.t2Choline_Total_mg,self.t2Betaine_mg,self.t2VitaminB_12_mcg,self.t2VitaminB_12_Added_mcg,self.t2VitaminA_IU_IU,self.t2VitaminA_RAE_mcg_RAE,self.t2Retinol_mcg,self.t2VitaminE_alpha_tocopherol__mg,self.t2VitaminE_Added_mg,self.t2Tocopherol_Beta_mg,self.t2Tocopherol_Gamma_mg,self.t2Tocopherol_Delta_mg,self.t2VitaminKPhylloquinone_mcg,self.t2Carotene_Beta_mcg,self.t2Carotene_Alpha_mcg,self.t2Cryptoxanthin_Beta_mcg,self.t2Lycopene_mcg,self.t2Lutein_Zeaxanthin_mcg,self.t2VitaminD_IU,self.t3Stigmasterol_mg,self.t3Phytosterols_mg,self.t3Beta_sitosterol_mg,self.t3Campesterol_mg,self.t3Cholesterol_mg,self.t3FattyAcids_TotalMonounsaturated_g,self.t3FattyAcids_TotalPolyunsaturated_g,self.t3FattyAcids_TotalSaturated_g,self.t3FattyAcids_TotalTrans_monoenoic_g,self.t3FattyAcids_TotalTrans_polyenoic_g,self.t3FattyAcids_TotalTrans_g,self.t3MonounsaturatedFats14_1_g,self.t3MonounsaturatedFats15_1_g,self.t3MonounsaturatedFats16_1C_g,self.t3MonounsaturatedFats16_1T_g,self.t3MonounsaturatedFats16_1Undifferentiated_g,self.t3MonounsaturatedFats17_1_g,self.t3MonounsaturatedFats18_1C_g,self.t3MonounsaturatedFats18_1T_g,self.t3MonounsaturatedFats18_1Undifferentiated_g,self.t3MonounsaturatedFats20_1_g,self.t3MonounsaturatedFats22_1C_g,self.t3MonounsaturatedFats22_1T_g,self.t3MonounsaturatedFats22_1Undifferentiated_g,self.t3MonounsaturatedFats24_1C_g,self.t3PolyunsaturatedFats18_2CLAs_g,self.t3PolyunsaturatedFats18_2I_g,self.t3PolyunsaturatedFats18_2N_6C_c_g,self.t3PolyunsaturatedFats18_2T_t_g,self.t3PolyunsaturatedFats18_2TNotFurtherDefined_g,self.t3PolyunsaturatedFats18_2Undifferentiated_g,self.t3PolyunsaturatedFats18_3N_3C_c_c_g,self.t3PolyunsaturatedFats18_3N_6C_c_c_g,self.t3PolyunsaturatedFats18_3Undifferentiated_g,self.t3PolyunsaturatedFats18_3i_g,self.t3PolyunsaturatedFats18_4_g,self.t3PolyunsaturatedFats20_2N_6C_c_g,self.t3PolyunsaturatedFats20_3N_3_g,self.t3PolyunsaturatedFats20_3N_6_g,self.t3PolyunsaturatedFats20_3Undifferentiated_g,self.t3PolyunsaturatedFats20_4N_6_g,self.t3PolyunsaturatedFats20_4Undifferentiated_g,self.t3PolyunsaturatedFats20_5N_3_g,self.t3PolyunsaturatedFats21_5_g,self.t3PolyunsaturatedFats22_4_g,self.t3PolyunsaturatedFats22_5N_3_g,self.t3PolyunsaturatedFats22_6N_3_g,self.t3SaturatedFats10_0_g,self.t3SaturatedFats12_0_g,self.t3SaturatedFats13_0_g,self.t3SaturatedFats14_0_g,self.t3SaturatedFats15_0_g,self.t3SaturatedFats16_0_g,self.t3SaturatedFats17_0_g,self.t3SaturatedFats18_0_g,self.t3SaturatedFats20_0_g,self.t3SaturatedFats22_0_g,self.t3SaturatedFats24_0_g,self.t3SaturatedFats4_0_g,self.t3SaturatedFats6_0_g,self.t3SaturatedFats8_0_g,self.t4Alanine_g,self.t4Arginine_g,self.t4AsparticAcid_g,self.t4Cystine_g,self.t4GlutamicAcid_g,self.t4Glycine_g,self.t4Histidine_g,self.t4Hydroxyproline_g,self.t4Isoleucine_g,self.t4Leucine_g,self.t4Lysine_g,self.t4Methionine_g,self.t4Phenylalanine_g,self.t4Proline_g,self.t4Serine_g,self.t4Threonine_g,self.t4Tryptophan_g,self.t4Tyrosine_g,self.t4Valine_g,self.t5Ash_g,self.t5Alcohol_Ethyl_g,self.t5Caffeine_mg,self.t5Theobromine_mg]
		return (values[index])
	
	def nutCalRatio(self,index):
		if float(self.t0Energy_kcal) == 0:
			return self.values(index)
		return (self.value(index)/self.t0Energy_kcal)

	def __repr__(self):
		return "<Food('%s','%s', '%s', '%s')>" % (self.food , self.detail , self.source, self.id )
	
  