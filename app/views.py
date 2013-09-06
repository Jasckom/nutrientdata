#2pm friday - start making without dictionary of id

from flask import render_template, flash, redirect, url_for, g, session, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import SearchForm, LoginForm, SignupForm, createMinMaxForm, Profile, createFoodsILike, SelectFilter, ProfileFull
from datetime import datetime
from linearOptimize import *
from sqlalchemy import asc, desc, func
from sqlalchemy.orm import aliased
from searchFood import searchFood, searchFoodBrand
from app.models import Food, Nutri,User,FoodKey
from config import RESULTS_PER_PAGE
SECRET_KEY = 'you-will-never-guess'
from flask.ext.wtf import Form, TextField, SubmitField

full_ext_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
full_ext_nutrient_unit = [ each.split('/')[1] for each in full_ext_nutrient]
full_ext_nutrient = [ each.split('/')[0] for each in full_ext_nutrient]
basic_nutrient = ["Calories/kcal","Calories from Fat/kcal","Total Fat/g","Fat /%","Saturated Fat/g","Polyunsaturated Fat/g","Monounsaturated Fat/g","Cholestorl/mg","Sodium/mg","Total Carbohydrate/g","Fiber/g","Sugar/g","Protein/g","Vitamin A/%","Vitamin C/%","Calcium/%","Iron/%"]
instrumentAttribute = [Food.mainType,Food.type,Food.food,Food.detail,Food.source,Food.amount,Food.unit,Food.gram,Food.cal_kcal,Food.calFat_kcal,Food.fat_g,Food.fat_pct,Food.saturFat_g,Food.polyunFat_g,Food.monounFat_g,Food.chol_mg,Food.sodium_mg,Food.carb_g,Food.fiber_g,Food.sugar_g,Food.protein_g,Food.vitA_pct,Food.vitC_pct,Food.calcium_pct,Food.iron_pct,Food.t0Water_g,Food.t0Energy_kcal,Food.t0Energy_kj,Food.t0Protein_g,Food.t0TotalLipidFat_g,Food.t0Carbohydrate_ByDifference_g,Food.t0Fiber_TotalDietary_g,Food.t0Sugars_Total_g,Food.t0Sucrose_g,Food.t0GlucoseDextrose_g,Food.t0Fructose_g,Food.t0Lactose_g,Food.t0Maltose_g,Food.t0Galactose_g,Food.t0Starch_g,Food.t0AdjustedProtein_g,Food.t1Calcium_Ca_mg,Food.t1Iron_Fe_mg,Food.t1Magnesium_Mg_mg,Food.t1Phosphorus_P_mg,Food.t1Potassium_K_mg,Food.t1Sodium_Na_mg,Food.t1Zinc_Zn_mg,Food.t1Copper_Cu_mg,Food.t1Manganese_Mn_mg,Food.t1Selenium_Se_mcg,Food.t1Fluoride_F_mcg,Food.t2VitaminC_TotalAscorbicAcid_mg,Food.t2Thiamin_mg,Food.t2Riboflavin_mg,Food.t2Niacin_mg,Food.t2PantothenicAcid_mg,Food.t2VitaminB_6_mg,Food.t2Folate_Total_mcg,Food.t2FolicAcid_mcg,Food.t2Folate_Food_mcg,Food.t2Folate_DFE_mcg_DFE,Food.t2Choline_Total_mg,Food.t2Betaine_mg,Food.t2VitaminB_12_mcg,Food.t2VitaminB_12_Added_mcg,Food.t2VitaminA_IU_IU,Food.t2VitaminA_RAE_mcg_RAE,Food.t2Retinol_mcg,Food.t2VitaminE_alpha_tocopherol__mg,Food.t2VitaminE_Added_mg,Food.t2Tocopherol_Beta_mg,Food.t2Tocopherol_Gamma_mg,Food.t2Tocopherol_Delta_mg,Food.t2VitaminKPhylloquinone_mcg,Food.t2Carotene_Beta_mcg,Food.t2Carotene_Alpha_mcg,Food.t2Cryptoxanthin_Beta_mcg,Food.t2Lycopene_mcg,Food.t2Lutein_Zeaxanthin_mcg,Food.t2VitaminD_IU,Food.t3Stigmasterol_mg,Food.t3Phytosterols_mg,Food.t3Beta_sitosterol_mg,Food.t3Campesterol_mg,Food.t3Cholesterol_mg,Food.t3FattyAcids_TotalMonounsaturated_g,Food.t3FattyAcids_TotalPolyunsaturated_g,Food.t3FattyAcids_TotalSaturated_g,Food.t3FattyAcids_TotalTrans_monoenoic_g,Food.t3FattyAcids_TotalTrans_polyenoic_g,Food.t3FattyAcids_TotalTrans_g,Food.t3MonounsaturatedFats14_1_g,Food.t3MonounsaturatedFats15_1_g,Food.t3MonounsaturatedFats16_1C_g,Food.t3MonounsaturatedFats16_1T_g,Food.t3MonounsaturatedFats16_1Undifferentiated_g,Food.t3MonounsaturatedFats17_1_g,Food.t3MonounsaturatedFats18_1C_g,Food.t3MonounsaturatedFats18_1T_g,Food.t3MonounsaturatedFats18_1Undifferentiated_g,Food.t3MonounsaturatedFats20_1_g,Food.t3MonounsaturatedFats22_1C_g,Food.t3MonounsaturatedFats22_1T_g,Food.t3MonounsaturatedFats22_1Undifferentiated_g,Food.t3MonounsaturatedFats24_1C_g,Food.t3PolyunsaturatedFats18_2CLAs_g,Food.t3PolyunsaturatedFats18_2I_g,Food.t3PolyunsaturatedFats18_2N_6C_c_g,Food.t3PolyunsaturatedFats18_2T_t_g,Food.t3PolyunsaturatedFats18_2TNotFurtherDefined_g,Food.t3PolyunsaturatedFats18_2Undifferentiated_g,Food.t3PolyunsaturatedFats18_3N_3C_c_c_g,Food.t3PolyunsaturatedFats18_3N_6C_c_c_g,Food.t3PolyunsaturatedFats18_3Undifferentiated_g,Food.t3PolyunsaturatedFats18_3i_g,Food.t3PolyunsaturatedFats18_4_g,Food.t3PolyunsaturatedFats20_2N_6C_c_g,Food.t3PolyunsaturatedFats20_3N_3_g,Food.t3PolyunsaturatedFats20_3N_6_g,Food.t3PolyunsaturatedFats20_3Undifferentiated_g,Food.t3PolyunsaturatedFats20_4N_6_g,Food.t3PolyunsaturatedFats20_4Undifferentiated_g,Food.t3PolyunsaturatedFats20_5N_3_g,Food.t3PolyunsaturatedFats21_5_g,Food.t3PolyunsaturatedFats22_4_g,Food.t3PolyunsaturatedFats22_5N_3_g,Food.t3PolyunsaturatedFats22_6N_3_g,Food.t3SaturatedFats10_0_g,Food.t3SaturatedFats12_0_g,Food.t3SaturatedFats13_0_g,Food.t3SaturatedFats14_0_g,Food.t3SaturatedFats15_0_g,Food.t3SaturatedFats16_0_g,Food.t3SaturatedFats17_0_g,Food.t3SaturatedFats18_0_g,Food.t3SaturatedFats20_0_g,Food.t3SaturatedFats22_0_g,Food.t3SaturatedFats24_0_g,Food.t3SaturatedFats4_0_g,Food.t3SaturatedFats6_0_g,Food.t3SaturatedFats8_0_g,Food.t4Alanine_g,Food.t4Arginine_g,Food.t4AsparticAcid_g,Food.t4Cystine_g,Food.t4GlutamicAcid_g,Food.t4Glycine_g,Food.t4Histidine_g,Food.t4Hydroxyproline_g,Food.t4Isoleucine_g,Food.t4Leucine_g,Food.t4Lysine_g,Food.t4Methionine_g,Food.t4Phenylalanine_g,Food.t4Proline_g,Food.t4Serine_g,Food.t4Threonine_g,Food.t4Tryptophan_g,Food.t4Tyrosine_g,Food.t4Valine_g,Food.t5Ash_g,Food.t5Alcohol_Ethyl_g,Food.t5Caffeine_mg,Food.t5Theobromine_mg]
toReduce = [29]+ [i for i in range(32,41)] + [46]+[i for i in range(81,142)] + [i for i in range(161,165)]
basicPlan = [26,28,29,30,31,32,41,42,46,52,85,88]

# mainCategories = ['baked products', 'beans legume products', 'beef products', 'beverages', 'breakfast cereals', 'cereal grains pasta', 'dairy products', 'egg products', 'ethnic foods', 'fast foods', 'fats oils', 'fish seafood products', 'fruits fruit juices', 'lamb veal game products', 'meals entrees sidedishes', 'nut seed products', 'pork products', 'poultry products', 'sausages deli meats', 'snacks', 'soups sauces gravies', 'spices herbs', 'sweets', 'vegetables']
mainCategories = ['baked products', 'beans, legume products', 'beef products', 'beverages', 'breakfast cereals', 'cereal, grains, pasta', 'dairy products', 'egg products', 'ethnic foods', 'fast foods', 'fats oils', 'fish, seafood products', 'fruits, fruit juices', 'lamb, veal, game products', 'meals, entrees, sidedishes', 'nut seed products', 'pork products', 'poultry products', 'sausages, deli, meats', 'snacks', 'soups, sauces, gravies', 'spices, herbs', 'sweets', 'vegetables']
foodTypes = [['apple pies', 'bagels', 'banana muffins', 'banana pumpkin breads', 'biscotti', 'biscuit breads', 'blueberry muffins', 'bran muffins', 'bread', 'bread crumbs', 'breadsticks', 'brownies', 'cakes', 'carrot cakes', 'cheese crackers', 'cheesecakes', 'cherry berry pies', 'chocolate cakes', 'chocolate chip cookies', 'chocolate chip muffins', 'cinnamon raisin bread', 'coffee cakes', 'cookies', 'corn muffins', 'cornbread', 'crackers', 'cream custard pies', 'crepes', 'crispbread crackers', 'croissants', 'croutons', 'cupcakes', 'danish pastries', 'dinner rolls', 'doughnuts', 'english muffins crumpets', 'focaccia flat pizza breads', 'french italian bread', 'french toast', 'garlic bread toast', 'ginger cookies', 'graham crackers', 'hamburger buns', 'hot dog buns', 'lemon cakes', 'matzo', 'meat savory pies', 'muffins scones', 'multigrain bread', 'multigrain crackers', 'oatmeal cookies', 'oyster crackers', 'pancakes waffles', 'pastries', 'peanut butter cookies', 'pie pastry crusts', 'pies', 'pita bread', 'pumpkin pies', 'quiches', 'rice crackers cakes', 'rolls buns', 'rye bread', 'saltine crackers', 'sandwich cookies', 'scones', 'shortbread cookies', 'sourdough bread', 'stuffings', 'sugar cookies', 'sweet buns rolls', 'tarts', 'toast', 'toaster pastries', 'tortillas tacos wraps', 'wafer cookies', 'water crackers', 'wheat bread', 'wheat crackers', 'white bread'], ['baked beans', 'bean dishes', 'black beans', 'chickpeas', 'green beans', 'hummus', 'kidney beans', 'lentils', 'lima beans', 'meat substitutes tvps', 'pinto beans', 'refried beans', 'soybeans', 'tofu tempeh', 'tofu tempeh dishes', 'white beans'], ['beef', 'beef broccoli', 'beef cold cuts', 'beef dishes', 'beef meatballs', 'beef patties', 'beef ribs', 'beef stroganoff', 'chuck steak', 'corned beef', 'country fried steak', 'flank steak', 'ground beef', 'hamburgers', 'meatloaf', 'porterhouse', 'pot roast', 'roast beef', 'roast beef sandwiches', 'salisbury steak', 'sirloin steak', 'steak', 'steak sandwiches', 'teriyaki beef'], ['alcoholic drinks', 'americano', 'beer', 'black tea', 'bloody mary', 'cafe mocha', 'cappuccino', 'caramel macchiato', 'carbonated drinks', 'chocolate smoothies', 'coconut water', 'coffee', 'cola', 'cream soda', 'dunkin donuts', 'energy drinks', 'espresso', 'fruit punch', 'fruit smoothies', 'ginger ale', 'green tea', 'herbal tea', 'hot chocolate', 'hot drinks', 'iced coffee', 'iced tea', 'juices', 'latte', 'lemon lime soda', 'lite beer', 'mai tai', 'margarita', 'martini', 'milk', 'milk substitutes', 'mixers cocktails', 'nutritional drinks', 'orange soda', 'pina colada', 'protein body building shakes', 'root beer', 'seltzer sparkling club tonic water', 'smoothies', 'sports drinks', 'starbucks', 'tea', 'vanilla smoothies', 'vodka gin rum whiskey', 'water', 'weight loss meal replacement shakes', 'white tea', 'wine', 'yogurt drinks'], ['bran flakes', 'cold cereals', 'corn flakes', 'cream wheat', 'granola muesli', 'grits', 'hot cereals', 'oats oatmeal', 'rice cereal', 'wheat cereal', 'wheat germ bran'], ['angel hair', 'barley', 'basmati rice', 'breakfast cereals', 'brown rice', 'buckwheat kasha', 'bulgur', 'chicken rice', 'corn meal', 'couscous', 'egg noodles', 'fettucini', 'flour', 'fried rice', 'gnocchi', 'grains', 'lasagna', 'linguini', 'macaroni', 'macaroni beef', 'macaroni cheese', 'noodles', 'pasta', 'pasta casserole', 'pasta dishes', 'penne', 'polenta', 'quinoa', 'ramen noodles', 'ravioli', 'rice', 'rice beans', 'rice dishes', 'rice flour', 'rice pilaf', 'rigatoni', 'risotto', 'rotini', 'soy flour', 'spaghetti', 'spaghetti meatballs', 'tortellini', 'vermicelli', 'wheat flour', 'white rice', 'whole wheat pasta', 'wild rice', 'yellow rice'], ['american cheese', 'apple yogurt', 'banana yogurt', 'blue cheese', 'blueberry yogurt', 'brie cheese', 'butter', 'cheddar cheese', 'cheese', 'chive onion cream cheese', 'chocolate flavored milk', 'coffee yogurt', 'colby cheese', 'colby jack cheese', 'condensed evaporated milk', 'cottage cheese', 'cream', 'cream cheese', 'creamer', 'fat free cream', 'fat yogurt', 'feta cheese', 'flavored yogurt', 'frozen yogurt', 'goat cheese', 'gouda cheese', 'greek yogurt', 'half', 'havarti cheese', 'honey nut cream cheese', 'jack cheese', 'lemon lime yogurt', 'light cream cheese', 'light yogurt', 'low fat milk percent', 'milk shakes', 'mozzarella cheese', 'muenster cheese', 'omelets', 'parmesan cheese', 'peach yogurt', 'provolone cheese', 'raisin cream cheese', 'reduced fat milk percent', 'ricotta cheese', 'skim milk fat free', 'sour cream', 'strawberry cream cheese', 'strawberry yogurt', 'string cheese', 'swiss cheese', 'vanilla yogurt', 'vegetable cream cheese', 'whipped cream', 'whole milk', 'yogurt'],['egg whites substitutes', 'eggs', 'fried eggs', 'hard boiled eggs', 'poached eggs', 'scrambled eggs'],['afghani food', 'african food', 'american food', 'arabic food', 'australasian food', 'australian food', 'austrian food', 'brazilian food', 'british food', 'canadian food', 'caribbean jamaican', 'chinese food', 'east asian food', 'ethiopian food', 'european food', 'french food', 'german food', 'greek food', 'indian food', 'irish food', 'italian food', 'japanese food', 'korean food', 'kosher israeli', 'latin food', 'mexican food', 'middle eastern food', 'moroccan food', 'new zealand food', 'north american food', 'pakistani food', 'polish food', 'portuguese food', 'russian food', 'scandinavian food', 'south african food', 'south asian food', 'spanish food', 'thai food', 'turkish food', 'vietnamese food'], ['blt sandwiches', 'breakfast sandwiches', 'burger sandwiches', 'burritos', 'calzones', 'cheese pizza', 'cheeseburgers', 'chicken burgers', 'chicken sandwiches', 'chili', 'club sandwiches', 'cold cut sandwiches', 'corn dogs', 'enchiladas', 'fajitas', 'fast food side dishes', 'fish sandwiches', 'french fries potato wedges', 'fried chicken', 'grilled cheese sandwiches', 'ham sandwiches', 'hash browns', 'hawaiian pizza', 'hot dogs', 'italian sandwiches', 'meatball sandwiches', 'nachos', 'onion rings', 'pepperoni pizza', 'pizza calzones', 'pork sandwiches', 'quesadillas', 'roast chicken', 'salads', 'sandwiches wraps', 'sausage pizza', 'sausage sandwiches', 'sausages', 'spring rolls', 'tacos', 'tamales', 'tex mex food', 'tuna sandwiches melts', 'turkey sandwiches', 'veggie burgers', 'veggie pizza', 'veggie sandwiches'], ['blue cheese dressing', 'caesar dressing', 'canola oil', 'cooking spray', 'corn oil', 'fats lard shortening', 'fish oil', 'french dressing', 'grape seed oil', 'greek dressing', 'honey mustard dressing', 'italian dressing', 'margarine', 'mayonnaise aioli', 'oils', 'olive oil', 'onion dressing', 'poppyseed dressing', 'ranch dressing', 'salad dressings', 'sesame dressing', 'sesame oil', 'thousand island dressing', 'vegetable oil', 'vegetable oil spread', 'vinegar vinaigrette dressing'], ['california rolls', 'clams', 'cod', 'crab', 'fish chips', 'fish dishes', 'fish sticks cakes', 'flounder', 'gefilte fish', 'haddock', 'halibut', 'herring', 'lobster', 'manhattan clam chowder', 'new england clam chowder', 'oysters', 'pollocks', 'salmon', 'sardines', 'scallops', 'shrimp', 'sole', 'sushi rolls', 'sushi sashimi', 'tilapia', 'tuna', 'whitefish pike'], ['apple juice', 'apples', 'apricots', 'avocados', 'bananas', 'blueberries', 'cherries', 'coconuts', 'cranberries', 'cranberry juice', 'fruit', 'fruit salads', 'grape juice', 'grapefruit juice', 'grapefruits', 'grapes', 'lemonade limeade', 'mangos', 'melons cantaloupe', 'olives', 'orange juice', 'oranges tangerines mandarins', 'peaches', 'pears', 'pineapple juice', 'pineapples', 'plums', 'pumpkins', 'raisins', 'raspberries', 'strawberries', 'tomato vegetable juice'], ['lamb', 'lamb dishes', 'veal', 'veal dishes'], ['baby food', 'baby food cereal', 'baby food dinners', 'baby food juice', 'baby food meats', 'baby food snacks', 'chicken dishes', 'egg dishes', 'ethnic foods', 'fast foods', 'fruit baby food', 'infant formula', 'pork dishes', 'potato dishes', 'turkey dishes', 'vegetable baby food', 'vegetable dishes'], ['almond other nut butters', 'almonds', 'cashews', 'chestnuts', 'flaxseeds', 'hazelnuts', 'macadamia nuts', 'nut trail mixes', 'peanut butter', 'peanuts', 'pecans', 'pine nuts', 'pistachios', 'pumpkin seeds', 'sesame seeds', 'soy nuts', 'sunflower seeds', 'walnuts'], ['bacon', 'ham', 'ham cold cuts', 'pork chops', 'pork loin', 'pork ribs', 'pork roast', 'pork sausage', 'pork shoulder', 'pork tenderloin', 'pulled pork'], ['bbq chicken', 'chicken', 'chicken breasts', 'chicken cold cuts', 'chicken drumsticks', 'chicken dumplings', 'chicken nuggets tenders', 'chicken parmesan', 'chicken patties', 'chicken salad', 'chicken sausage', 'chicken soups', 'chicken thighs', 'chicken tikka masala', 'chicken wings', 'duck', 'fried chicken', 'grilled chicken', 'ground turkey', 'teriyaki chicken', 'turkey', 'turkey bacon', 'turkey breast', 'turkey chili', 'turkey cold cuts', 'turkey legs', 'turkey patties', 'turkey sausage', 'turkey soups'], ['beef sausage', 'bologna cold cuts', 'bratwurst', 'chorizo', 'italian sausage', 'jerky snack sticks', 'lunch meats', 'pastrami', 'polish sausage', 'salami pepperoni'], ['banana plantain chips', 'candy', 'cereal bars', 'cheese puffs', 'chewing gum mints', 'chips', 'corn tortilla chips', 'cracker sandwiches', 'energy protein bars', 'filled pretzels', 'flavored pretzels', 'fruit nut bars', 'fruit snacks', 'granola bars', 'meal replacement bars', 'multigrain chips', 'nutrition bars', 'oatmeal raisin bars', 'pita bagel chips', 'popcorn', 'pork skins rinds', 'potato chips', 'pretzel sticks rods', 'pretzels', 'puddings', 'puffed rice bars', 'snack bars', 'snack mixes', 'soft pretzels', 'trail mix bars'], ['alfredo sauce', 'barbecue sauce', 'bean soup', 'beef barley soup', 'beef broth stock bouillon', 'beef chili', 'beef noodle soup', 'beef soups', 'beef stew', 'bisques', 'broth stock bouillon', 'bruschetta', 'butternut squash pumpkin soup', 'cheese dip', 'cheese soups', 'chicken broth stock bouillon', 'chicken gravy', 'chicken noodle soup', 'chicken rice soup', 'chowders', 'chutney', 'cocktail sauce', 'condiments', 'corn chowder', 'cream broccoli soup', 'cream chicken soup', 'cream mushroom soup', 'cream potato soup', 'cream soups', 'cream tomato soup', 'curry sauce', 'dips spreads', 'french onion dip', 'garlic sauce', 'gravy', 'guacamole', 'gumbo', 'hot sauce chipotle', 'ketchup', 'lentil soup', 'marinades', 'marinara tomato sauce', 'minestrone soup', 'mushroom gravy', 'mushroom soup', 'mustard', 'onion soup', 'pasta pizza sauces', 'pate', 'pea soup', 'peanut sauce', 'pesto sauce', 'potato soup', 'relish', 'salsa', 'sauces', 'soups', 'soy sauce', 'spinach dip', 'steak sauce', 'stews', 'sugars syrups', 'sweet sour sauce', 'tapenade', 'tartar sauce', 'teriyaki sauce', 'tomato soup', 'tortilla soup', 'turkey gravy', 'vegetable broth bouillon', 'vegetable soups', 'vodka sauce', 'wedding soup'], ['baking soda', 'chili powder', 'coating mixes', 'curry', 'food coloring', 'garlic', 'ginger', 'onion', 'oregano', 'paprika', 'parsley', 'pepper', 'salt', 'seasoning mix', 'steak seasoning', 'vitamins'], ['apple butter', 'apple jams jellies', 'artificial sweeteners', 'brown sugar', 'candy canes christmas', 'caramel candy', 'caramel syrup', 'chocolate', 'chocolate candy', 'chocolate candy bars', 'chocolate chips morsels', 'chocolate covered candy', 'chocolate ice cream', 'chocolate pudding', 'chocolate spreads', 'chocolate syrup', 'coffee ice cream', 'cookies n cream ice', 'crisps cobblers', 'dark chocolate', 'decorating icing', 'dessert toppings', 'desserts', 'easter eggs candy', 'fat free ice cream', 'flavored syrups', 'fruit desserts compotes', 'fruit jams jellies', 'gelatin desserts', 'grape jams jellies', 'gummy snacks', 'hard candy', 'honey', 'ice cream bars', 'ice cream cakes', 'ice cream sandwiches', 'ice cream sorbet', 'ice cream sundaes', 'icing decorations', 'icings frostings', 'jellies jams preserves spreads', 'licorice', 'lite syrup', 'lollipops suckers', 'low fat ice cream', 'maple syrup', 'marmalade', 'marshmallows', 'milk chocolate', 'orange jams jellies', 'pancake syrup', 'parfaits', 'pie cake fillings', 'rice pudding', 'sauces', 'seasonal candy', 'sherbet sorbet', 'soft serve frozen yogurt', 'sour candy', 'sprinkles', 'strawberry ice cream', 'strawberry jams jellies', 'sugar free candy', 'sugar free ice cream', 'sugar free syrup', 'sugars sweeteners', 'toppings', 'valentines candy', 'vanilla', 'vanilla ice cream', 'vanilla pudding', 'whipped toppings'], ['artichokes', 'asparagus', 'au gratin potatoes', 'baked potato', 'beets', 'broccoli', 'cabbage', 'caesar salad', 'carrots', 'cauliflower', 'celery', 'chili peppers', 'coleslaw', 'collards', 'corn', 'cucumber', 'eggplant', 'fruit vegetables', 'garden salad', 'garlic', 'inflorescence vegetables', 'kale', 'leafy vegetables', 'lettuce', 'mashed potatoes', 'mixed vegetables', 'mushrooms', 'onions', 'peas', 'pickles pickled vegetables', 'potato salad', 'potatoes yams', 'pumpkin squash', 'radishes', 'root vegetables', 'scalloped potatoes', 'souffle', 'spinach', 'sprouts', 'stem vegetables', 'stir fried vegetables', 'sweet peppers', 'tomatoes', 'turnips', 'vegetable casseroles', 'zucchini']]


#Determine if the entry from search box is with brand or 
def getSearchEntry(brandEntry,searchEntry):
	if len(brandEntry) != 0:
		if len(searchEntry) != 0:
			if not searchEntry.isspace():
				searchEntry += ":"+brandEntry				
			else:
				searchEntry = "brandOnly:"+brandEntry
		else:
			searchEntry = "brandOnly:"+brandEntry
	return searchEntry

#Get search term from the concatenate form - this is for remembering the search term
#Instead of putting in the session a two separate terms 
def getSearchTerms(searchTerms):
	#The form is of the format food:brand
	#If only brand is searched then in food "brandOnly"
	searchTermsList = searchTerms.split(":")
	if len(searchTermsList) > 1:
		food = searchTermsList[0]
		brand = searchTermsList[1]
	else:
		food = searchTermsList[0]
		brand = None
	if food == "brandOnly":
		food = None
	return food, brand

#Save food to the current user
def saveFood():
    userFood = Food.query.filter(Food.id.in_(session[g.user.get_id()])).all()
    if userFood:
		g.user.food = userFood
		db.session.commit()

#Get Matching Categories from search
def getMatchingCat(searchEntry,foodTypes):
	matchingCat = []
	eachTermList = searchEntry.split()
	for eachTerm in eachTermList:
		for eFdTp in foodTypes:
			for eFd in eFdTp:
				eFdLst = eFd.split()
				for eeFdLst in eFdLst:
					if eachTerm == eeFdLst or eachTerm+'s' == eeFdLst or eeFdLst+'s' == eachTerm:
						matchingCat.append(eFd)
	matchingCat = list(set(matchingCat))
	matchingCat.sort()
	return matchingCat

#Get diet plan which has the most number of food items
def findMaxFood(listFoodObject, constraints, defaultGenlowerBound, openUpperBound):
	#This is just running the functions through the common diet plans
	# cal, protein , fat ,carb, vitC
	listOptNut = [26,28,29,30,52]
	minAndMax = [0,1]
	maxNonZeros = 0
	for opt_nut in listOptNut:
		for opt_maxormin in minAndMax:
			(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, openUpperBound, opt_maxormin, opt_nut)
			countNonZeros = 0
			for eachVal in outputFoodAmount:
				if eachVal != 0:
					countNonZeros += 1
			if  countNonZeros >= maxNonZeros:
				maxNonZeros = countNonZeros
				BestResult = (outputFood, outputFoodAmount, stat, valobj, nullNut)
				status = "Max variety from" + str(opt_nut) + " " + str(opt_maxormin)
				print "Number of foods: " + str(maxNonZeros)
				print status

# 	for opt_maxormin in minAndMax:
# 		(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimizeMaxMinPortions(listFoodObject, constraints, defaultGenlowerBound, openUpperBound, opt_maxormin, opt_nut)
# 		countNonZeros = 0
# 		for eachVal in outputFoodAmount:
# 			if eachVal != 0:
# 				countNonZeros += 1
# 		if  countNonZeros >= maxNonZeros:
# 			maxNonZeros = countNonZeros
# 			BestResult = (outputFood, outputFoodAmount, stat, valobj, nullNut)
# 			status = "Max variety from min max potions"
# 			print "Number of foods: " + str(maxNonZeros)
# 			print status
			
	print "Total non zeroes: ", str(maxNonZeros)
	return BestResult	

@login_required
@app.route('/mainCat/<mainCatChosen>')
def mainCat(mainCatChosen):
	global mainCategories
	global foodTypes
	mainCatChosen = int(mainCatChosen)
	
	#Store the headings
	session["box1Head"] = mainCategories[mainCatChosen]
	session["box1Cat"] = foodTypes[mainCatChosen]

	#if filter is applied, but now new category is chosen, filter is removed from the session dictionary
	if "filter" in session.keys():
		session.pop("filter")
	
	return redirect(url_for('resultCategory', categoryChosen =mainCategories[mainCatChosen]+":General"))
	
@app.route('/resultSearch', methods = ['GET', 'POST'])
@app.route('/resultSearch/<int:page>', methods = ['GET', 'POST'])
def resultSearch(page = 1):
	
	if not g.user.is_authenticated():
		flash('Please first sign in as a guest')
		return redirect(url_for('login'))

	global mainCategories
	global foodTypes
	global full_ext_nutrient
	
	#Get the previous search term to put in the search form	
	if "resultNew" in session.keys():
		(defaultFood, defaultBrand) = getSearchTerms(session["resultNew"])
	
	# Create search form
	form = SearchForm(defaultFood,defaultBrand)
	
	# If search form is submitted, and at lest one of the search box is filled
	if form.validate_on_submit() and ( (len(form.searchEntry.data) != 0) or (len(form.brandEntry.data) != 0) ):
		# get entries from the form
		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		searchEntry = getSearchEntry(brandEntry,searchEntry)
		
		#Get the new search terms from the search form
		session["resultNew"] = searchEntry
		#Clear the filter when new search takes place
		if "filter" in session.keys():
			session.pop("filter")
		#Redirect back to the function 
		return redirect(url_for('resultSearch'))
	
	# Create foods I like form
	foodIdsArg = session[g.user.get_id()]
	foodNamesArg = session["foodItem"]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)
	
	#If the user has chosen some foods - foodIdsArg is not empty then get all the foods
	#This is to create nutritional labels for all the foods from query in that pagination
	if foodIdsArg:
		foodsItemsILike = Food.query.filter(Food.id.in_(foodIdsArg)).all()
	else:
		foodsItemsILike = []

	#Validate form of foods I like
	if foodsILike.validate_on_submit() and (foodsILike.submit.data or  foodsILike.remove.data or foodsILike.toggle.data):
		check = []
		checkedFood = []
		fieldIndex = 0
		# The first 4 fields are not selected items
		for field in foodsILike:
			if fieldIndex >= 4:
				check.append(field.data)
				# Get ids of the checked food for submitting or for removing
				if field.data: 
					checkedFood.append(field.name)
			fieldIndex +=1
		
		# Submit the food for linear programming
		if foodsILike.submit.data == 1:
			# If some foods are actually chosen, foods can be submitted
			if sum(check) >=1:
				session["optimize"] = [i for i in checkedFood]
				return redirect(url_for('optimize'))
			else:
				flash('Please select the foods you like')
		
		# Remove the foods
		elif foodsILike.remove.data == 1:
			for i in checkedFood:
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('resultSearch'))
	

	# If filter is applied, keep the filter else give default to first one
	if "filter" in session.keys():
		selectFilter = SelectFilter(session["filter"])
	else:
		selectFilter = SelectFilter(22)
	if request.method == 'POST':
		if selectFilter.filter.data and request.form['filter'] == 'Go!':
			filterNut = selectFilter.filterNut.data
			session["filter"] = filterNut
		
	#Store search term
	#If the search term is still the same, the same list of result is given
	#If the search term is different, emit query to the database
	if session["result"] != session["resultNew"]:
		
		#Hard copy of search term letter by letter
		resultNew = ""
		for each in session["resultNew"]:
			resultNew += each
		session["result"] = resultNew
		searchEntry = session["resultNew"]
		
		#operate on this new search term
		searchEntryList = searchEntry.split(":")
		brandEntry = ""
		if len(searchEntryList) > 1:
			brandEntry = searchEntryList[1]		
		searchEntry = searchEntryList[0]
		
		#intercept empty search because the query takes unnecessarily long to return empty query
		if searchEntry == "" and brandEntry == "":
			results= []
		else:
			if searchEntry == "brandOnly":
				results = searchFoodBrand(brandEntry, Food)
			else:
				results = searchFood(searchEntry, brandEntry, Food,FoodKey)
			#store current food ids found after querying the database
			session["resultID"] = results
	else:
		#Just to get potential categories
		searchEntry = session["result"]
		searchEntryList = searchEntry.split(":")
		brandEntry = ""
		if len(searchEntryList) > 1:
			brandEntry = searchEntryList[1]		
		searchEntry = searchEntryList[0]
		#get the food ids from the previous querying (same search terms)
		results = session["resultID"]
	
	#Create standard query before storing them in any order
	if results:
		results = Food.query.filter(Food.id.in_(results))
	else:
		results = Food.query.filter(Food.id==0)

	box2Head = "Search Results - Foods"

	# if filter is applied and not the default value
	if "filter" in session.keys():
		filterNut = session["filter"]
		if filterNut != 22:
			if filterNut == 23:
				print "by food source"
				results = results.order_by(Food.source)
				box2Head += " by Brands"
			elif filterNut == 24:
				box2Head += " by Alphabetical Order"
				results = results.order_by(Food.food)
			# Differentiate which type of nutrients to rank by highest or lowest
			# instrumentAttribute is the list of nutrients for ordering
			elif filterNut in toReduce:
				results = results.order_by(asc(instrumentAttribute[filterNut]))
				box2Head += " with Lowest " + full_ext_nutrient[filterNut-25]
			else:
				results = results.order_by(desc(instrumentAttribute[filterNut]))
				box2Head += " with Highest " + full_ext_nutrient[filterNut-25]
		else:
			results = results.order_by(asc(func.char_length(Food.tag)))

	# if no filter is applied, relevant search is made by ranking according to lengths of the tag
	# This is because all the foods here strictly have all the keywords in the search.
	else:
		results = results.order_by(asc(func.char_length(Food.tag)))
	
	# Paginate the result
	resultSearch = results.paginate(page, 20, False)
	
	#Get potential 
	matchingCat = getMatchingCat(searchEntry,foodTypes)
	session["box1Head"] = "Search Results - Categories"
	session["box1Cat"] = matchingCat
	
	saveFood()
	
	return render_template('resultSearch.html',
		title = 'Search your food',
		form = form,
		selectFilter =selectFilter,
		foodsILike = foodsILike,
		mainCat = mainCategories,
		box1Head = session["box1Head"],
		box1Cat = session["box1Cat"],
		box2Head = box2Head,
		resultSearch = resultSearch,
		foodNamesArg = foodNamesArg,
		userProfile=session["userProfile"],
		foodsItemsILike = foodsItemsILike)

@login_required
@app.route('/resultCategory/<categoryChosen>', methods = ['GET', 'POST'])
@app.route('/resultCategory/<categoryChosen>/<int:page>', methods = ['GET', 'POST'])
def resultCategory(categoryChosen, page = 1):
	#print session[("foodItem")]
	
	global mainCategories
	global foodTypes
	global full_ext_nutrient
		
	#Search Function same snippet as in resultSearch
	
	# Create search form
	defaultFood = None
	defaultBrand = None
	form = SearchForm(defaultFood,defaultBrand)
	if form.validate_on_submit() and ( (len(form.searchEntry.data) != 0) or (len(form.brandEntry.data) != 0) ):
		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		searchEntry = getSearchEntry(brandEntry,searchEntry)		
		session["resultNew"] = searchEntry
		print "in search box: ", session["resultNew"]
		if "filter" in session.keys():
			session.pop("filter")
		return redirect(url_for('resultSearch'))
	
	#Store category term
	session["resultCategory"] = categoryChosen
	
	# Create foods I like form
	# The snippet is the same as the resultSearch
	foodIdsArg = session[g.user.get_id()]
	foodNamesArg = session["foodItem"]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)
	
	if foodIdsArg:
		foodsItemsILike = Food.query.filter(Food.id.in_(foodIdsArg)).all()
	else:
		foodsItemsILike = []

	if foodsILike.validate_on_submit() and (foodsILike.submit.data or  foodsILike.remove.data or foodsILike.toggle.data):
		check = []
		checkedFood = []
		fieldIndex = 0
		for field in foodsILike:
			if fieldIndex >= 4:
				check.append(field.data)
				if field.data:
					checkedFood.append(field.name)
			fieldIndex +=1
		if foodsILike.submit.data == 1:
			if sum(check) >=1:
				session["optimize"] = [i for i in checkedFood]
				return redirect(url_for('optimize'))
			else:
				flash('Please select the foods you like')
		elif foodsILike.remove.data == 1:
			for i in checkedFood:
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('resultCategory', categoryChosen=categoryChosen))

	# Filter form
	if "filter" in session.keys():
		selectFilter = SelectFilter(session["filter"])
	else:
		selectFilter = SelectFilter(22)
	if request.method == 'POST':
		if selectFilter.filter.data and request.form['filter'] == 'Go!':
			filterNut = selectFilter.filterNut.data
			session["filter"] = filterNut
	
	#Get resultsCategory as a standard result before sorting in any order
	categoryChosen = categoryChosen.split(':')
	if categoryChosen[1] == "General":
		mainType = categoryChosen[0]
		categoryChosen = categoryChosen[1]
		query = Food.query.filter_by(mainType=mainType).filter_by(type=categoryChosen)
	else:
		mainType = categoryChosen[0]
		categoryChosen = categoryChosen[1]
		query = Food.query.filter_by(type=categoryChosen)
		
	if "filter" in session.keys():
		filterNut = session["filter"]
		#print "filterrr: ", filterNut
		if filterNut != 22:
			if filterNut == 23:
				print "by food source"
				resultCategory = query.order_by(Food.source)
				box2Head = categoryChosen + " by Brands"
			elif filterNut == 24:
				print "alphabetical"
				resultCategory = query.order_by(Food.food)
				box2Head = categoryChosen + " by Alphabetical Order"
						
			elif filterNut in toReduce:
				resultCategory = query.order_by(asc(instrumentAttribute[filterNut]))
 				box2Head = categoryChosen + " with Lowest " + full_ext_nutrient[filterNut-25]

			else:
				resultCategory = query.order_by(desc(instrumentAttribute[filterNut]))
 				box2Head = categoryChosen + " with Highest " + full_ext_nutrient[filterNut-25]
 		else:
 			resultCategory = query.order_by(asc(Food.food))
			box2Head = categoryChosen
	else:
		resultCategory = query.order_by(asc(Food.food))
		box2Head = categoryChosen
	
	resultCategory = resultCategory.paginate(page, RESULTS_PER_PAGE, False)
	
	saveFood()
	return render_template('resultCategory.html',
			title = 'Search your food',
			form = form,
			selectFilter = selectFilter,
			foodsILike = foodsILike,
			mainCat = mainCategories,
			box1Head = session["box1Head"],
			box1Cat = session["box1Cat"],
			resultCategory = resultCategory,
			foodNamesArg = foodNamesArg,
			box2Head= box2Head,
			categoryChosen = categoryChosen,
			userProfile = session["userProfile"],
			foodsItemsILike = foodsItemsILike)

@login_required
@app.route('/selectFood/<foodChosen>')
def selectFood(foodChosen):
	#This is from the link of each food when users click on it
	#Only new food item is added
	if not foodChosen in session[g.user.get_id()]:
		session[g.user.get_id()].insert(0,foodChosen)
		food = Food.query.filter(Food.id==foodChosen).first()
		session[("foodItem")].insert(0,food.food+ " "+ food.detail+ " (" +  food.source+")")
	
	categoryChosen = session["resultCategory"]
	#Maintain the query string for url to redirect to resultCategory
	return redirect(url_for('resultCategory',categoryChosen =categoryChosen ))

@login_required
@app.route('/selectFoodFromSearch/<foodIDFromSearch>')
def selectFoodFromSearch(foodIDFromSearch):
	#Only new food item is added
	if not foodIDFromSearch in session[g.user.get_id()]:
		session[g.user.get_id()].insert(0,foodIDFromSearch)
		food = Food.query.filter(Food.id==foodIDFromSearch).first()
		session[("foodItem")].insert(0,food.food+ " "+ food.detail+ " (" +  food.source+")")
	return redirect(url_for('resultSearch'))

@login_required
@app.route('/selectFoodFromSuggest/<foodIDFromSuggest>')
def selectFoodFromSuggest(foodIDFromSuggest):
	#In selectFoodFromSuggest - foods are added to 2 places - in session["optimize"] and in session[g.user.get_id()]
	#This is because only food submitted appears in result suggest it is separated from the whole list of foods
	#All the calculations to dynamically satisfy the lacking nutrients are based on foods submitted session["optimize"]
	#If the food is removed - the nutrients lacking should be recalculated
	
	#Two main parts - when foods are added tand when they are removed
	#First when it is removed
	if foodIDFromSuggest == "updateAfterRemove":
		# Get check here is used to find the current constraints 
		(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(g.user.nutri[0],1)
		constraints = []
		for i in range(len(check)):
			if check[i]:
				constraints.append(i+25)
		# only take the ones in basic plan if it is chosen
		if "basicPlan" in session.keys():
			if session["basicPlan"] == 1:
				global basicPlan
				newConstrainsts = []
				for each in constraints:
					if each in basicPlan:
						newConstrainsts.append(each)
				constraints = newConstrainsts
		
		
		foodItems = Food.query.filter(Food.id.in_(session["optimize"])).all()
		
		#Get ratioUnmet from the foods submitted	
		(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio(constraints, foodItems, g.user.nutri[0])
						
		if nutRatioMin:
			session["sumCal"] = sumCal
			session["sumNutUnmet"] = sumNutUnmet
			session["nutRatioMin"] = nutRatioMin
			session["nutRatioUnmet"] = nutRatioUnmet
			session[("chosenNut")] = 0
			return redirect(url_for('resultSuggest'))
		
		else:
			return redirect(url_for('resultSuggest'))
	
	# When food is added - have to check if it's already in the foods submitted
	# Also check if it is in the foods i like
	if not foodIDFromSuggest in session["optimize"]:
		session["optimize"].insert(0,foodIDFromSuggest)
		if not foodIDFromSuggest in session[g.user.get_id()]:
			session[g.user.get_id()].insert(0,foodIDFromSuggest)
			food = Food.query.filter(Food.id==foodIDFromSuggest).first()
			session[("foodItem")].insert(0,food.food+ " "+ food.detail+ " (" +  food.source+")")
	
		(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(g.user.nutri[0],1)
		constraints = []
		for i in range(len(check)):
			if check[i]:
				constraints.append(i+25)
		
		if "basicPlan" in session.keys():
			if session["basicPlan"] == 1:
				global basicPlan
				newConstrainsts = []
				for each in constraints:
					if each in basicPlan:
						newConstrainsts.append(each)
				constraints = newConstrainsts
		
		foodItems = Food.query.filter(Food.id.in_(session["optimize"])).all()
			
		(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio(constraints, foodItems, g.user.nutri[0])
		
				
		if nutRatioMin:
			session["sumCal"] = sumCal
			session["sumNutUnmet"] = sumNutUnmet
			session["nutRatioMin"] = nutRatioMin
			session["nutRatioUnmet"] = nutRatioUnmet
			session[("chosenNut")] = 0
			return redirect(url_for('resultSuggest'))
		else:
			session["sumCal"] = sumCal
			session["sumNutUnmet"] = sumNutUnmet
			session["nutRatioMin"] = nutRatioMin
			session["nutRatioUnmet"] = nutRatioUnmet
			return redirect(url_for('resultSuggest'))
		
	else:
		return redirect(url_for('resultSuggest'))



@login_required
@app.route('/foodsILike', methods = ['GET', 'POST'])
def foodsILike():
	#Manage foods I like
	
	global mainCategories
	global foodTypes
	global full_ext_nutrient
	
	# If filter is applied, keep the filter else give default to first one
	if "filterFoodsILike" in session.keys():
		selectFilter = SelectFilter(session["filterFoodsILike"])
	else:
		selectFilter = SelectFilter(22)
	if request.method == 'POST':
		if selectFilter.filter.data and request.form['filter'] == 'Go!':
			filterNut = selectFilter.filterNut.data
			session["filterFoodsILike"] = filterNut
	
	#If filter is applied and not the default value
	#byCat will be passed to the html page so that the look is different from sorting by other criteria
	foodsItemsILike = Food.query.filter(Food.id.in_(session[g.user.get_id()]))
	byCat = True
	if "filterFoodsILike" in session.keys():
		filterNut = session["filterFoodsILike"]
		if filterNut != 22:
			byCat = False
			if filterNut == 23:
				foodsItemsILike = foodsItemsILike.order_by(Food.source)
			elif filterNut == 24:
				foodsItemsILike = foodsItemsILike.order_by(Food.food)
			# Differentiate which type of nutrients to rank by highest or lowest
			# instrumentAttribute is the list of nutrients for ordering
			elif filterNut in toReduce:
				foodsItemsILike = foodsItemsILike.order_by(asc(instrumentAttribute[filterNut]))
			else:
				foodsItemsILike = foodsItemsILike.order_by(desc(instrumentAttribute[filterNut]))
		else:
			foodsItemsILike = foodsItemsILike.order_by(Food.mainType)

	# if no filter is applied, relevant search is made by ranking according to lengths of the tag
	# This is because all the foods here strictly have all the keywords in the search.
	else:
		foodsItemsILike = foodsItemsILike.order_by(Food.mainType)
	
	# Create foods I like form
	foodIdsArg = [str(food.id) for food in foodsItemsILike]
	foodNamesArg = [food.food+ " "+ food.detail+ " (" +  food.source+")" for food in foodsItemsILike]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)
	
	#Validate form of foods I like
	if foodsILike.validate_on_submit() and (foodsILike.submit.data or  foodsILike.remove.data or foodsILike.toggle.data):
		check = []
		checkedFood = []
		fieldIndex = 0
		# The first 4 fields are not selected items
		for field in foodsILike:
			if fieldIndex >= 4:
				check.append(field.data)
				# Get ids of the checked food for submitting or for removing
				if field.data: 
					checkedFood.append(field.name)
			fieldIndex +=1
		
		# Submit the food for linear programming
		if foodsILike.submit.data == 1:
			# If some foods are actually chosen, foods can be submitted
			if sum(check) >=1:
				session["optimize"] = [i for i in checkedFood]
				return redirect(url_for('optimize'))
			else:
				flash('Please select the foods you like')
		
		# Remove the foods
		elif foodsILike.remove.data == 1:
			for i in checkedFood:
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('foodsILike'))
	
	
	return render_template('foodsILike.html',
		selectFilterFoodsILike =selectFilter,
		manageFoodsILike = foodsILike,
		foodNamesArg = foodNamesArg,
		userProfile=session["userProfile"],
		foodsItemsILike = foodsItemsILike,
		byCat = byCat)
		
		
# get bounds from Nutri and decide whether to follow the recommended or follow the user's new constrainst
# the default ones are unchecked when lower bounds are zeros and upper bounds are ND
def getKeysBounds(nutriObject,override):
	nutriField = []
	check = []

	for eachkey in nutriObject.__table__.columns.keys():
			nutriField.append(eachkey)
	bounds = [getattr(nutriObject,nutriField[i]) for i in range(23,len(nutriField))]
	defaultGenlowerBound = []
	defautGenupperBound = []
	i = 23
	
	for each in bounds:
		each = each.split(":")
		defaultGenlowerBound.append(each[0])
		defautGenupperBound.append(each[1])
		if override:
			#get all the constraints 0 or 1 just as they are -
			if len(each) >= 3:
				check.append(int(each[2]))
		else:
			#check only those that has zero as lower bound as undefined upper bound (only meaningful ones)
			if (each[0] == "0" and each[1] == "ND"):
				check.append(0)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":0")
			else:
				check.append(1)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":1")
		i += 1

	db.session.commit()
	check[0] = 0
	
	return 	check, nutriField, defaultGenlowerBound, defautGenupperBound

def reportRatio(constraints, foodItems, nutri):
	# tell ratios and indicate which nutrient is not satisfied

	# If there are no constraints and food items given
	if (not constraints) and (not foodItems):
		return None, [],[],[]	
	nutRatioUnmet = []
	nutRatioMin = []
	nullNut = []
	failedBestFood = []
	
	#get the calorie value that comes in nutri
	givenCal = nutri.t0Energy_kcal.split(":")[1]
	if givenCal == "ND":
		givenCal = 5000
	else:
		givenCal = float(givenCal)
		
	bestFoods = []
	bestFoodsVals = []
	
	# if food item is not given - then return only ratios and constraints
	if not foodItems:
		for eachCon in constraints:
			nutRatioMin.append(nutri.nutCalRatio(eachCon))
		return givenCal, [], nutRatioMin, constraints
	
	#check the best foods in each nutrient
	for i in range(len(constraints)):
		eachCon = constraints[i]
		maxNut = 0
		for j in range(len(foodItems)):
			if foodItems[j].value(eachCon) >= maxNut:
				maxNut = foodItems[j].value(eachCon)
				bestFood = foodItems[j]
		bestFoods.append(bestFood)
		bestFoodsVals.append(maxNut)
	
	#compare the best food if it passes the ratio
	for i in range(len(constraints)):
		eachCon = constraints[i]
		bestFoodVal = bestFoodsVals[i]
		nutRatio = bestFoodVal/givenCal
		minRatio= nutri.nutCalRatio(eachCon)
		if nutRatio <= minRatio:
			nutRatioUnmet.append(eachCon)
			nutRatioMin.append(minRatio)
			failedBestFood.append(nutRatio)
	
	#After failing the following nutrients which is quite strict, 
	#only consider the ones that the infeasible solution cannot meet the lower bounds
	nutRatioMinNew = []
	nutRatioUnmetNew = []
	for each in session["nutLack"]:
		if each in nutRatioUnmet:
			indexNut = nutRatioUnmet.index(each)
			nutRatioMinNew.append(nutRatioMin[indexNut])
			nutRatioUnmetNew.append(nutRatioUnmet[indexNut])
			
	return givenCal, failedBestFood, nutRatioMinNew, nutRatioUnmetNew

#get the nutritional content (according to constraints) from the given food items and the amount of the foods 
def reportTotal(constraints, outputFoodAmount, foodItems):
	TotalNut = []
	for i in range(len(constraints)):
		eachCon = constraints[i]
		totalEachNut = []
		for j in range(len(foodItems)):
			eachFood = foodItems[j]
			eachFoodNut = float(eachFood.value(eachCon))
			totalEachNut.append(outputFoodAmount[j]*eachFoodNut)
		TotalNut.append(sum(totalEachNut))			
	return TotalNut

# get calories based on nutri given	
def getCal(height, height2, weight, USorMetric, gender, activity,age):

	if USorMetric == "US":
		heightCvt = (float(height)*12 + float(height2))*2.54
		weightCvt = float(weight) * 0.453592
	else:
		heightCvt = float(height)
		weightCvt = float(weight)
	if gender == "Males":
		constants = [13.75,5,-6.76,66]
	elif gender == "Females":
		constants = [9.56,1.85,-4.68,655]
	cal = constants[0]*weightCvt + constants[1]* heightCvt + constants[2]*float(age) + constants[3]
	cal = cal*float(activity)
	return cal

# get age group because this is used for calculations of nutrients
def getageGroup(age):
	age = float(age)
	ageGroup =["0-6 mo", "6-12 mo","1-3 y","4-8 y","9-13 y","14-18 y","19-30 y","31-50 y","51-70 y",">70 y"]
	if age <= 0.5:
		result = ageGroup[0]
	elif age <= 1:
		result = ageGroup[1]
	elif age <= 3:
		result = ageGroup[2]
	elif age <= 8:
		result = ageGroup[3]
	elif age <= 13:
		result = ageGroup[4]
	elif age <= 18:
		result = ageGroup[5]
	elif age <= 30:
		result = ageGroup[6]
	elif age <= 50:
		result = ageGroup[7]
	elif age <= 70:
		result = ageGroup[8]
	elif age >= 71:
		result = ageGroup[9]
	return result

#Show the composition of foods that contribute to exceeded nutrients
def showExceed(xNut, totalNut, foodAmount, foodItems):
	nutrientPercent = []
	for i in range(len(foodItems)):
		xVal = foodItems[i].value(xNut)
		nutrientPercent.append(  (foodItems[i], 100*(   (foodAmount[i]*xVal)/totalNut  ) ))
	allPercent = sorted(nutrientPercent, key=lambda percent: percent[1], reverse = True)
	majorPercent = []
	for each in allPercent:
		if each[1] != 0:
			majorPercent.append(("%.1f" %each[1],each[0]))
		
	return majorPercent
	
# Show profile of the user - this should be done for all pages as well
def getUserProfileDisplay(user):
	dictActivity = {1.2:"Sedentary",1.375:"Lightly Active",1.55:"Moderately Active",1.725:"Very active",1.9:"Extremely Active"}
	if user.heightInch is None:
		userProfile = user.gender.rstrip('s') +" " + str(int(user.age)) +", Weight: "+  str(int(user.weight)) + " kg, Height: "+ str(int(user.heightFeet)) + " cm, " + dictActivity[user.activity]
	else:
		userProfile = user.gender.rstrip('s') +" " + str(int(user.age)) +", Weight: "+  str(int(user.weight)) + " lb, Height: "+ str(int(user.heightFeet)) + " ft "+ str( int(user.heightInch)) + " in, " + dictActivity[user.activity]
	if user.username is not None:
		userProfile = user.username+" - "+ userProfile 
	else:
		userProfile = "Guest - "+userProfile 
	return userProfile


@app.route('/manage', methods = ['GET', 'POST'])
def manage():
	if not g.user.is_authenticated():
		flash('Please First Sign in as a Guest')
		return redirect(url_for('login'))
	saveFood()
	if "basicPlan" not in session.keys():
		firstDefault = 1
	else:
		firstDefault = session["basicPlan"]
	
	# Get lower/upper bounds from the curent user - this is not overriding but based on what is recommended	
	currentNutri = g.user.nutri[0]
	
	(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,1)
	
	# Default is to stay healthy unless the the nutrient options are chosen before then remember it
	optMaxMin = 2
	optNut = None
	if "opt_maxormin" in session.keys():
		opt_maxormin = session["opt_maxormin"]
		opt_nut = session["opt_nut"]
		if opt_maxormin ==  -1 and opt_nut== -1:
			optMaxMin = 2
		elif opt_maxormin == 0 and opt_nut== 26:
			optMaxMin = 3
		elif opt_maxormin == 1 and opt_nut== 28:
			optMaxMin = 4
		else:
			optMaxMin = opt_maxormin
			optNut = opt_nut
	
	# Create the form
	minMaxForm = createMinMaxForm(check,firstDefault,optMaxMin,optNut,'Proceed to Select Foods')
	minMaxForm.lowerBound = defaultGenlowerBound
	minMaxForm.upperBound = defautGenupperBound	
	
	# Form is submitted
	# at least one of the nutritional constraints is pressed (u'y' in request.form.values())
	if minMaxForm.is_submitted() and request.form['submit'] == 'Proceed to Select Foods' and (u'y' in request.form.values()):
		if ((minMaxForm.opt_maxormin.data == 0) or (minMaxForm.opt_maxormin.data == 1)):
			if minMaxForm.opt_nut.data is None:
				return redirect(url_for('manage'))
			else:
				opt_maxormin = minMaxForm.opt_maxormin.data
				opt_nut = minMaxForm.opt_nut.data
		
		elif minMaxForm.opt_maxormin.data == 2:
			opt_maxormin = -1
			opt_nut = -1
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data == 3:
			opt_maxormin = 0
			opt_nut = 26
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data == 4:
			opt_maxormin = 1
			opt_nut = 28
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data is None:
			return redirect(url_for('manage'))
		constraints = []
		constraintslowerBound = []
		constraintsupperBound = []
		
		#getting the values from the form - beyond 421 are no longer nutritional constraints
		#according to the table format - checkbox ,lower bound, upperbound
		i = 0
		for field in minMaxForm:
			if i >= 421:
				break
			elif i != 0:
				
				if (i-1) %3 == 0:
					# check box - take the index of the nutrients
					#print (i-1)//3, field.name, field.data, type(field.data)
					if field.data == True:
						constraints.append(25+(i-1)//3)
				elif (i-2)%3 == 0:
					# lower bound
					#print (i-2)//3, field.name, field.data, type(field.data)
					constraintslowerBound.append(field.data)
				elif (i-3)%3 == 0:
					#upperbound
					#print (i-3)//3, field.name, field.data, type(field.data)
					constraintsupperBound.append(field.data)
			i += 1

		#convert index of nutrients to 0 and 1 tobe stored in Nutri of the user
		#this is so that user's constraints are saved
		currentCheck = [0 for i in range(len(constraintsupperBound))]
		for eachCon in constraints:
			currentCheck[eachCon-25] = 1
			
		#Modifying user's nutri
		modifyNut = g.user.nutri[0]
		newCon = [field for field in modifyNut.__table__.columns.keys()]
		for ic in range(len(constraintslowerBound)):
			if constraintslowerBound[ic] is None:
				lower = "ND"
			else:
				lower = str(constraintslowerBound[ic])
			if constraintsupperBound[ic] is None:
				upper = "ND"
			else:
				upper = str(constraintsupperBound[ic])
			val = lower+":"+upper+":"+str(currentCheck[ic])
			setattr(modifyNut,newCon[ic+23],val)
			
		session["basicPlan"] = 	minMaxForm.nutrientPlan.data
		session["opt_maxormin"] = opt_maxormin
		session["opt_nut"] = opt_nut
		db.session.commit()
		
		return redirect(url_for('resultSearch'))
		
	return render_template("manage.html",
		minMaxForm = minMaxForm,
		check = check,
		userProfile = session['userProfile'])

@login_required
@app.route('/optimize', methods = ['GET', 'POST'])
def optimize():
	
	#Verify all the states of user before optimizing
	#1. User has be to signed in
	#2. The objective is chosen - (nutrient plan is set default at basic)
	#3. User has clicked checkout in one of the result
	if not g.user.is_authenticated():
		flash('Please First Sign in as a Guest')
		return redirect(url_for('login'))

	if "opt_maxormin" not in session.keys():
		flash ('You have not chosen the diet plan')
		return redirect(url_for('manage'))
	
	if "optimize" not in session.keys():
		if session[g.user.get_id()]:
			print "Sent back to choose Food"
			session["optimize"] = session[g.user.get_id()]
		else:
			flash('You have not selected any foods')
			return redirect(url_for('resultSearch'))
			
	# Save food that user select into Database
	saveFood()

	# Get food items from the ids to pass to LP function
	listFoodObject = Food.query.filter(Food.id.in_(session["optimize"])).all()
	# Get contraints to pass to LP function	
	(check, nutriField, defaultGenlowerBound, defaultGenupperBound) = getKeysBounds(g.user.nutri[0],1)
	# Modify the constraints - if it is basic plan removed all that have been checked
	constraints = []
	for i in range(len(check)):
		if check[i]:
			constraints.append(i+25)
	
	# Get max/min and which objective from sessions 
	# However, if it is just to stay healthy -negative numbers are used to signify this chosen plan
	opt_maxormin = session["opt_maxormin"]
	opt_nut = session["opt_nut"]
	maxVariety = 0 
	if opt_maxormin == -1 and opt_nut == -1:
		opt_maxormin = 1
		opt_nut = 28
		maxVariety = 1
	
	# If basic plan is chosen over full nutrient plan
	if session["basicPlan"] == 1: 
		global basicPlan 
		newConstrainsts = []
		for each in constraints:
			if each in basicPlan:
				newConstrainsts.append(each)
		constraints = newConstrainsts
	
	#Start Linear programming
	# Step 1 - normal LP
	result = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, defaultGenupperBound, opt_maxormin, opt_nut )
	(outputFood , outputFoodAmount , status ,objective, nullNut) = result
	
	# Step 2 - If infeasible - see what's the current situation like to see which food is lacking
	if status == "Infeasible":
		print "minimizing - changed to max"
		if opt_maxormin == 0:
			#When infeasible solution - make objective maximize will make it better
			result = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, defaultGenupperBound, 1, opt_nut)
			(outputFood , outputFoodAmount , status ,objective, nullNut) = result

	finalUpper = defaultGenupperBound 
	finalLower = defaultGenlowerBound
	
	#Get lower bounds and upper bounds convert string from Nutri to float for calculations
	upperBoundConst = []
	lowerBoundConst = []
	for each in constraints:
		if defaultGenupperBound[each-25] == "ND":
			upperBoundConst.append(10000)
		else:
			upperBoundConst.append(float(defaultGenupperBound[each-25]))
		if defaultGenlowerBound[each-25] == "ND":
			lowerBoundConst.append(0)
		else:
			lowerBoundConst.append(float(defaultGenlowerBound[each-25]))
	
	# Get results of all the nutrients and see what are lacking
	totalNut = reportTotal(constraints, outputFoodAmount, listFoodObject)
	nutLack = []		
	for i in range(len(totalNut)):
		if (lowerBoundConst[i]-totalNut[i]) > 0.1:
			nutLack.append(constraints[i])
	
	# Nutlack is only empty when optimal or all the lower constraints are satisfied
	# Meaning if it gives infeasible the problem lies only with the upper bounds.
	session["nutLack"] = nutLack
	(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio(constraints, listFoodObject, g.user.nutri[0])	
	
	stepDecrease = 100
	# Step 3 - when the problem is upper bound 	
	if not nutRatioMin and status == "Infeasible":
		stat = "Optimal"
		pace = 5000
		while stat == "Optimal":
			(outputFoodPre, outputFoodAmountPre, statPre, objective, nullNut) = (outputFood, outputFoodAmount, stat, objective, nullNut)
			pace -= stepDecrease
			for each in upperBoundConst:
				if each > pace:
					stat == "Infeasible"
			openUpperBound = [pace for i in range(len(defaultGenupperBound))]
			(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, openUpperBound, opt_maxormin, opt_nut)
			finalUpper = [each+stepDecrease for each in openUpperBound]
			
		#print "Open Bounded Solution"
		(outputFood , outputFoodAmount , status ,objective, nullNut) = (outputFoodPre, outputFoodAmountPre, statPre, valobj, nullNut)
		#reportTotal(constraints, outputFoodAmount, listFoodObject)
	
	# At the end here, we should get a desirable output as feasible region is found
	
	# Once found if the user wants to maximize variety just to stay healthy
	if maxVariety:
		(outputFood, outputFoodAmount, stat, valobj, nullNut) = findMaxFood(listFoodObject, constraints, finalLower, finalUpper)
		#for remembering of the form below
		opt_maxormin = -1 
		opt_nut = -1
	
	#Report details
	
	#Get total of the food to be compared with upperbound
	totalNut = reportTotal(constraints, outputFoodAmount, listFoodObject)
	
	eachTotalStatement = []		
	nutLack = []
	nutLackVal = []
	nutLackStatement = []	
	nutExceed = []
	nutExceedVal = []
	nutExceedStatement = []
	global full_ext_nutrient_unit
	global full_ext_nutrient

	for i in range(len(totalNut)):
		if (totalNut[i]- upperBoundConst[i]) > 0.1:
			nutExceed.append(constraints[i])
			nutExceedVal.append(totalNut[i])
			upper = str(int(upperBoundConst[i]))
			nutExceedStatement.append("Too Much "+full_ext_nutrient[constraints[i]-25] +" " +str(int(round(totalNut[i])))+"/"+ upper + " "+full_ext_nutrient_unit[constraints[i]-25])
		elif (lowerBoundConst[i]-totalNut[i]) > 0.1:
			nutLack.append(constraints[i])
			nutLackVal.append(totalNut[i])
			lower = str(int(lowerBoundConst[i]))
			nutLackStatement.append("Low on "+full_ext_nutrient[constraints[i]-25] +" " +str(int(round(totalNut[i])))+"/"+ lower + " "+full_ext_nutrient_unit[constraints[i]-25])
			
		lower = lowerBoundConst[i]
		upper = upperBoundConst[i]
		if lower == 10000:
			lower = "ND"
		if upper == 10000:
			upper = "ND"
		if opt_nut != constraints[i]:
			eachTotalStatement.append(full_ext_nutrient[constraints[i]-25])
			eachTotalStatement.append("("+str(lower)+":"+str(upper)+ ")")
			eachTotalStatement.append(str(int(round(totalNut[i]))) + " "+full_ext_nutrient_unit[constraints[i]-25])

	if defaultGenupperBound[opt_nut-25] == "ND":
		upperOptNut = 10000
	else:
		upperOptNut = (float(defaultGenupperBound[opt_nut-25]))
	if defaultGenlowerBound[opt_nut-25] == "ND":
		lowerOptNut = 0
	else:
		lowerOptNut = (float(defaultGenlowerBound[opt_nut-25]))

	if objective == None:
		eachTotalStatement.append(full_ext_nutrient[opt_nut-25])
		eachTotalStatement.append("("+str(lowerOptNut)+":"+str(upperOptNut)+ ")")
		eachTotalStatement.append("0 "+full_ext_nutrient_unit[opt_nut-25])
		eachTotalStatement.append("None of the food items contain "+ full_ext_nutrient[opt_nut-25] + " to be optimized.")
	else:
		objective = int(objective)
		eachTotalStatement.append(full_ext_nutrient[opt_nut-25])
		eachTotalStatement.append("("+str(lowerOptNut)+":"+str(upperOptNut)+ ")")
		eachTotalStatement.append(str(objective) +" "+full_ext_nutrient_unit[opt_nut-25])

	
	
	# nested list - inside is a tuple with percent value and the food by decreasing order	
	nutExceedWhichFood = []
	for i in range(len(nutExceed)):
		exceedPercent = showExceed(nutExceed[i], nutExceedVal[i], outputFoodAmount, listFoodObject)
		nutExceedWhichFood.append(exceedPercent)
	
	session["nutLack"] = nutLack
	session["nutLackVal"] = nutLackVal
	(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio(constraints, listFoodObject, g.user.nutri[0])
	#givenCal, failedBestFood, nutRatioMin, nutRatioUnmet
	

	session["sumCal"] = sumCal
	session["sumNutUnmet"] = sumNutUnmet
	session["nutRatioMin"] = nutRatioMin
	session["nutRatioUnmet"] = nutRatioUnmet
	session["opt_maxormin"] = opt_maxormin
	session["opt_nut"] = opt_nut
	session[("chosenNut")] = 0
		
	yesFood = []
	yesFoodAmount = []
	noFood = []
	noFoodAmount = []
	for i in range(len(outputFood)):
		if outputFoodAmount[i] != 0:
			yesFoodAmount.append("%0.2f"%(outputFoodAmount[i]*listFoodObject[i].amount))
			yesFood.append(outputFood[i])
		else:
			noFoodAmount.append("%0.2f"%(outputFoodAmount[i]*listFoodObject[i].amount))
			noFood.append(outputFood[i])
	outputFood = yesFood+noFood
	outputFoodAmount = yesFoodAmount+noFoodAmount
	print nutLackStatement
	
	#same snippet as that in manage
	
	if "basicPlan" not in session.keys():
		firstDefault = 1
	else:
		firstDefault = session["basicPlan"]
	
	# Get lower/upper bounds from the curent user - this is not overriding but based on what is recommended	
	currentNutri = g.user.nutri[0]
	
	(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,1)
	
	optMaxMin = 2
	optNut = None
	if "opt_maxormin" in session.keys():
		opt_maxormin = session["opt_maxormin"]
		opt_nut = session["opt_nut"]
		if opt_maxormin ==  -1 and opt_nut== -1:
			optMaxMin = 2
		elif opt_maxormin == 0 and opt_nut== 26:
			optMaxMin = 3
		elif opt_maxormin == 1and opt_nut== 28:
			optMaxMin = 4
		else:
			optMaxMin = opt_maxormin
			optNut = opt_nut
		
	minMaxForm = createMinMaxForm(check,firstDefault,optMaxMin,optNut,'Generate My Diet')
	minMaxForm.lowerBound = defaultGenlowerBound
	minMaxForm.upperBound = defautGenupperBound	
	
	# Form is submitted
	if minMaxForm.is_submitted() and request.form['submit'] == 'Generate My Diet' and (u'y' in request.form.values()):
		if ((minMaxForm.opt_maxormin.data == 0) or (minMaxForm.opt_maxormin.data == 1)):
			if minMaxForm.opt_nut.data is None:
				return redirect(url_for('manage'))
			else:
				opt_maxormin = minMaxForm.opt_maxormin.data
				opt_nut = minMaxForm.opt_nut.data
		
		elif minMaxForm.opt_maxormin.data == 2:
			opt_maxormin = -1
			opt_nut = -1
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data == 3:
			opt_maxormin = 0
			opt_nut = 26
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data == 4:
			opt_maxormin = 1
			opt_nut = 28
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data is None:
			return redirect(url_for('manage'))
		constraints = []
		constraintslowerBound = []
		constraintsupperBound = []

		i = 0
		for field in minMaxForm:
			if i >= 421:
				break
			elif i != 0:
				if (i-1) %3 == 0:
#					#print (i-1)//3, field.name, field.data, type(field.data)
					if field.data == True:
						constraints.append(25+(i-1)//3)
				elif (i-2)%3 == 0:
#					#print (i-2)//3, field.name, field.data, type(field.data)
					constraintslowerBound.append(field.data)
				elif (i-3)%3 == 0:
#					#print (i-3)//3, field.name, field.data, type(field.data)
					constraintsupperBound.append(field.data)
			i += 1


		currentCheck = [0 for i in range(len(constraintsupperBound))]
		for eachCon in constraints:
			currentCheck[eachCon-25] = 1
		modifyNut = g.user.nutri[0]
		newCon = [field for field in modifyNut.__table__.columns.keys()]
		for ic in range(len(constraintslowerBound)):
			if constraintslowerBound[ic] is None:
				lower = "ND"
			else:
				lower = str(constraintslowerBound[ic])
			if constraintsupperBound[ic] is None:
				upper = "ND"
			else:
				upper = str(constraintsupperBound[ic])
			val = lower+":"+upper+":"+str(currentCheck[ic])
			setattr(modifyNut,newCon[ic+23],val)
			
		session["basicPlan"] = 	minMaxForm.nutrientPlan.data
		session["opt_maxormin"] = opt_maxormin
		session["opt_nut"] = opt_nut
		db.session.commit()
		
		return redirect(url_for('optimize'))
		
	
	return render_template("optimize.html",
		outputFood = outputFood,
		outputFoodAmount = outputFoodAmount,
		status = status,
		objective = objective,
		nullNut = nullNut,
		check = check,
		nutExceedStatement = nutExceedStatement,
		nutExceedWhichFood =nutExceedWhichFood,
		userProfile = session['userProfile'],
		eachTotalStatement = eachTotalStatement,
		nutLackStatement = nutLackStatement,
		minMaxForm = minMaxForm)

@login_required
@app.route('/resultSuggest', methods=['GET', 'POST'])
@app.route('/resultSuggest/<int:page>', methods = ['GET', 'POST'])
def resultSuggest(page = 1):

	#resultSuggest works only with foods submitted - not the whole list of preferred foods

	global mainCategories
	global foodTypes
	global full_ext_nutrient
	global instrumentAttribute
	
	# If the food diet has not been optimized - this will not work
	# It relies on the information from infeasible solution (in reportRatio in selectFoodFromSuggest)
	if "optimize" not in session.keys():
		flash('Please generate a diet plan first')
		return redirect(url_for('optimize'))
	
	# Create the form - very similar to foods I like form but this is submitted foods I like
	# Therefore it is from session["optimize"] i	
	foodIdsArg = session["optimize"]
	if foodIdsArg:
		# it is necessary that the food in this list appears in this order
		foodsItemsILike = [Food.query.filter(Food.id == each).first() for each in foodIdsArg]
	else:
		foodsItemsILike = []
	for each in foodsItemsILike:
		print each
	foodNamesArg = [food.food+ " "+ food.detail+ " (" +  food.source+")" for food in foodsItemsILike]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)	
	
	#same snippet of code as in resultSearch
	#Validate form
	if foodsILike.validate_on_submit():
		check = []
		checkedFood = []
		fieldIndex = 0
		for field in foodsILike:
			if fieldIndex >= 4:
				check.append(field.data)
				if field.data: # if it is checked - get the ID of the food
					checkedFood.append(field.name)
			fieldIndex +=1
		if foodsILike.submit.data == 1:
			if sum(check) >=1:
				session["optimize"] = [i for i in checkedFood]
				return redirect(url_for('optimize'))
			else:
				flash('Please select the foods you like')
		elif foodsILike.remove.data == 1:
			for i in checkedFood:
				indexToDelete = session["optimize"].index(i)
				session["optimize"].pop(indexToDelete)

		return redirect(url_for('selectFoodFromSuggest', foodIDFromSuggest = "updateAfterRemove"))
		
	# Compared to structure with resultSearch
	# Box 1 - all the food types that i like
	# Box 2 - food items that are hight in that nutrient chosen
	# Main cat - the nutrietns that are lacking
	
	# get the unique mainType and type of foods that I like
	typesMainTypesILike = []
	for eachFoodID in session[g.user.get_id()]:
		eachFood = Food.query.filter(Food.id==eachFoodID).first()
		typesMainTypesILike.append(eachFood.mainType +' -> '+eachFood.type )
	typesMainTypesILike = list(set(typesMainTypesILike))
	session["box1CatSuggest"] = typesMainTypesILike
	
	# ge
	typesILike = []
	MainTypeILike = []
	for each in typesMainTypesILike:
		each = each.split(' -> ')
		typesILike.append(each[1])
		MainTypeILike.append(each[0])
	
 	#get chosenType 
	if ("chosenType") in session.keys():
		typeFood = session["chosenType"].split(' -> ')
		MainTypeILike = typeFood[0]
		typesILike = typeFood[1]
		heading2List = session["chosenType"].title()
	# if not it is a general suggested Foods
	else:
		heading2List = "Suggested Food Types"

	sumCal = session["sumCal"] 
	sumNutUnmet = session["sumNutUnmet"] 
	nutRatioMin = session["nutRatioMin"] 
	nutRatioUnmet = session["nutRatioUnmet"] 

	# get which nutrient to look for to get from session because we want it to stay
	# whenever client click which type of food this nutrient will be selected
	lackingNut = [full_ext_nutrient[i-25].split('/')[0] for i in nutRatioUnmet]
	
	# if all lower nutrients are satisfied - ratio unmet is empty
	# this could be that all the lower nutritional constraints are satisfied given the infeasible solution
	if not nutRatioUnmet:
		titleFindFood = "Your Food Items Are More Balanced"
		return render_template('resultBalanced.html',
		foodsILike = foodsILike,
		heading2List = heading2List,
		box1Head = "Food Types I Like",
		box1Cat = session["box1CatSuggest"],
		titleFindFood = titleFindFood,
		foodNamesArg= foodNamesArg,
		foodsItemsILike= foodsItemsILike)
	
	
	indexRatio = int(session[("chosenNut")])
	ratio = nutRatioMin[indexRatio]
	# make the ratio slightly stricter
	ratio = ratio*1.005
	nutChosen = nutRatioUnmet[indexRatio]
	opt_maxormin =  session["opt_maxormin"]
	opt_nut = session["opt_nut"]
	
	#Make suggested foods healthy - it has limits of sodium and fats
	looseUpperSodium = 2600.0 
	looseUpperFat = 75.0 
	
	#Names of the two nutrients
	currentNutName = full_ext_nutrient[nutChosen-25].split('/')[0]
	objNutName = full_ext_nutrient[opt_nut-25].split('/')[0]
	
	#Find all the types 
	#except beverages (because beveages has a lot of nutrition/energy drinks)
	#except vitamins
	
	if heading2List == "Suggested Food Types":
		result = Food.query.\
					filter(Food.source=="General").\
					filter(Food.mainType!="beverages").\
					filter(Food.type!="vitamins").\
					filter(instrumentAttribute[nutChosen]/sumCal>=ratio).\
					filter(Food.t1Sodium_Na_mg/sumCal<= looseUpperSodium/1800).\
					filter(Food.t0TotalLipidFat_g/sumCal<= looseUpperFat/1800)
		if result.count() == 0:
			result = Food.query.filter(Food.mainType!="beverages").\
								filter(Food.type!="vitamins").\
								filter(instrumentAttribute[nutChosen]/sumCal>=ratio)
			if result.count() == 0:
				result = Food.query.filter(Food.mainType!="beverages").\
								filter(Food.type!="vitamins")
			else:
				heading2List = "In the Database:"
		result = result.order_by(desc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)

	else:
		result = Food.query.filter(Food.type == typesILike).filter(Food.mainType == MainTypeILike).\
					filter(instrumentAttribute[nutChosen]/sumCal>=ratio)
		if result.count() == 0:
			result = Food.query.filter(Food.mainType == MainTypeILike[0]).\
						filter(instrumentAttribute[nutChosen]/sumCal>=ratio)
			if result.count() == 0:
				#result None
				heading2List = "Please See Suggested Food Types. "+heading2List+":"
		result = result.order_by(desc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)
	box2Head = heading2List


	titleFindFood = "Foods High in "+ currentNutName

	
	saveFood()
	return render_template('resultSuggest.html',
		foodsILike = foodsILike,
		lackingNut = lackingNut,
		chosenNut = full_ext_nutrient[nutChosen-25].split('/')[0],
		heading2List = heading2List,
		optimizeNut = full_ext_nutrient[opt_nut-25].split('/')[0],
		box1Head = "Food Types I Like",
		box1Cat = session["box1CatSuggest"],
		box2Head = box2Head,
		resultSearch = result,
		titleFindFood = titleFindFood,
		foodNamesArg = foodNamesArg,
		userProfile = session['userProfile'],
		foodsItemsILike= foodsItemsILike)
	
@app.route('/selectNut/<chosenNut>/')
def selectNut(chosenNut):
	#store nutrient chosen to be satisfied in resultSuggest
	session[("chosenNut")] = chosenNut
	return redirect(url_for('resultSuggest'))
	
@app.route('/selectTypeILike/<chosenType>/')
def selectTypeILike(chosenType):
	#store food type chosen in resultSuggest
	if chosenType == "Suggested Food Types":
		if ("chosenType") in session.keys():
			session.pop(("chosenType"))
	else:
		session[("chosenType")] = chosenType
	return redirect(url_for('resultSuggest'))

@app.before_request
def before_request():
    g.user = current_user
    
	# if it is fresh login
    if g.user.is_authenticated() and not g.user.get_id() in session:
    	session[g.user.get_id()] = [str(each.id) for each in g.user.food]
    	session["foodItem"] = [each.food+ " "+ each.detail+ " (" +  each.source+")" for each in g.user.food]
    	session["foodInfo"] = None
    	session["result"] = ""
    	session["resultNew"] = ""
    	session["resultID"] = []
 
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
    
@login_required
@app.route("/profile", methods=["GET", "POST"])
def profile():
	print "profile 1"
	if not g.user.is_authenticated():
		print "profile 2"
		return redirect(url_for('login'))
	#given the user
	currentUser = g.user
	#create the form for editing the profile
	editProfile = Profile(currentUser)
	formVal =  request.form.values()
	valid = 0
	print "profile 3"
	# manually validate the profile form - to allow for two possible unit types (wtform is not used here)
	if ("Save Changes" in formVal) and ("unitSystem" in request.form.keys()) and editProfile.is_submitted():
		if editProfile.age.data is not None:
			print "profile 4"
			age = editProfile.age.data
			gender = editProfile.gender.data
			condition = editProfile.conditions.data
			unitSystem = request.form["unitSystem"]
			activity = editProfile.activity.data
			if gender == "Males" and condition != "None":
				flash ("Males only have 'None' condition.")
				return redirect(url_for('profile'))
			if unitSystem == "Metric":
				if (editProfile.weightKg.data is not None) and (editProfile.heightCm.data is not None):
					weight = editProfile.weightKg.data
					height = editProfile.heightCm.data
					#getCal(height, height2, weight, USorMetric, gender, editProfile.activity.data, age)
					cal = getCal(height, 0, weight, unitSystem, gender,activity, age)
					valid = 1
			else:
				if (editProfile.weight.data is not None) and (editProfile.heightFeet.data is not None):
					weightLb = editProfile.weight.data
					heightFeet = editProfile.heightFeet.data
					if editProfile.heightInch.data is not None:
						heightInch = editProfile.heightInch.data
					else:
						heightInch = 0
					cal = getCal(heightFeet, heightInch, weightLb, unitSystem, gender, activity ,age)
					valid = 1
		print "profile 5"		
		if valid == 0:
			return redirect(url_for('profile'))
		else:
			print "profile 6"
			# Save new profile of the user
			currentUser = g.user
			currentUser.age = age
			currentUser.gender = gender
			currentUser.conditions = condition
			currentUser.activity = activity 
			if unitSystem == "US":
				currentUser.heightFeet =	heightFeet
				currentUser.heightInch = heightInch
				currentUser.weight = weightLb
			else:
				currentUser.weight = weight
				currentUser.heightFeet = height
				currentUser.heightInch = None
				
			# Update nutri object
			currentNutri = currentUser.nutri[0]
			ageGroup = getageGroup(age)
			currentNutri.ageGroup = ageGroup
			currentNutri.gender = gender
			currentNutri.conditions = condition
				 
			# Get the default from "look-up table" from the database/ generate default lower and upper
			recNut = Nutri.query.filter(Nutri.type==0).filter(Nutri.ageGroup==ageGroup).filter(Nutri.gender==gender).filter(Nutri.conditions==condition).first()
			protup = recNut.protein_g
			fatup = recNut.fat_g
			carbup = recNut.carb_g
			
			print "profile 7"
			# Copy this default into the current's user nutri
			i = 0
			for eachKey in recNut.__table__.columns.keys():
				if i >= 23:
					setattr(currentNutri, eachKey, getattr(recNut, eachKey))
				i += 1
				
			#Adjust calories
			currentNutri.t0Energy_kcal = "0:"+str(int(round(cal)))
			
			#Adjust upperbound of macro according to calories values
			currentNutri.t0Protein_g=  currentNutri.t0Protein_g.replace("ND",str(int(round(cal*int(protup)/400))))
			currentNutri.t0TotalLipidFat_g=currentNutri.t0TotalLipidFat_g.replace(":ND",":"+str(int(round(cal*int(fatup)/900))))
			currentNutri.t0Carbohydrate_ByDifference_g=currentNutri.t0Carbohydrate_ByDifference_g.replace("ND",str(int(round(cal*int(carbup)/400 ))))	
			(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,0)
			db.session.commit()
			
			session['userProfile'] = getUserProfileDisplay(currentUser)
			flash ("My Profile is updated! " +session['userProfile'])
			print "profile 8"
	username = "Guest"
	if currentUser.username is not None:
		username = g.user.username
	print "profile 9"
	return render_template("profile.html", 
		username = username, editProfile = editProfile,
    	userProfile = getUserProfileDisplay(g.user))

@app.route('/', methods = ['GET', 'POST'])
def index():	
	keys = session.keys()
	for each in keys:
		session.pop(each, None)
	logout_user()
	return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
	# check if user is logged in
	if current_user is not None and current_user.is_authenticated():
		return redirect(url_for('resultSearch'))
	
	# profile form
	profileFull = ProfileFull()
	formVal =  request.form.values()
	valid = 0
	print "time out"
	
	# similar snippet as profile to validate form
	if ("Sign Up" in formVal or "Guest" in formVal) and ("unitSystem" in request.form.keys()) and ("gender" in request.form.keys()):
		print "time out1"
		if profileFull.age.data is not None:
			age = profileFull.age.data
			gender = request.form["gender"]
			condition = profileFull.conditions.data
			unitSystem = request.form["unitSystem"]
			activity = profileFull.activity.data
			if gender == "Males" and condition != "None":
				flash ("Males only have 'None' condition.")
				return redirect(url_for('login'))
			if unitSystem == "Metric":
				if (profileFull.weightKg.data is not None) and (profileFull.heightCm.data is not None):
					weight = profileFull.weightKg.data
					height = profileFull.heightCm.data
					#getCal(height, height2, weight, USorMetric, gender, profileFull.activity.data, age)
					cal = getCal(height, 0, weight, unitSystem, gender,activity, age)
					valid = 1
			else:
				if (profileFull.weight.data is not None) and (profileFull.heightFeet.data is not None):
					weightLb = profileFull.weight.data
					heightFeet = profileFull.heightFeet.data
					if profileFull.heightInch.data is not None:
						heightInch = profileFull.heightInch.data
					else:
						heightInch = 0
					cal = getCal(heightFeet, heightInch, weightLb, unitSystem, gender, activity ,age)
					valid = 1
					
		if valid == 0:
			flash ("Please fill in all the information")
			return redirect(url_for('login'))
		else:
			print "time out2"
			# Save profile of the user
			if "Sign Up" in formVal:
				newUser = User()
			elif "Guest" in formVal:
				newUser = User(role = 1)
			newUser.age = age
			newUser.gender = gender
			newUser.conditions = condition
			newUser.activity = activity 
			if unitSystem == "US":
				newUser.heightFeet =	heightFeet
				newUser.heightInch = heightInch
				newUser.weight = weightLb
			else:
				newUser.weight = weight
				newUser.heightFeet = height
				newUser.heightInch = None
				
			# Create nutri object
			print "time out3"
			newNutri = Nutri(type=1)
			newUser.nutri.append(newNutri)
			db.session.add(newUser)
			db.session.add(newNutri)
			db.session.commit()
			currentNutri = newUser.nutri[0]
			ageGroup = getageGroup(age)
			currentNutri.ageGroup = ageGroup
			currentNutri.gender = gender
			currentNutri.conditions = condition
			print "time out4"	 
			# Get the default from "look-up table" from the database/ generate default lower and upper
			recNut = Nutri.query.filter(Nutri.type==0).filter(Nutri.ageGroup==ageGroup).filter(Nutri.gender==gender).filter(Nutri.conditions==condition).first()
			protup = recNut.protein_g
			fatup = recNut.fat_g
			carbup = recNut.carb_g
		
			# Copy this default into the current's user nutri
			i = 0
			for eachKey in recNut.__table__.columns.keys():
				if i >= 23:
					setattr(currentNutri, eachKey, getattr(recNut, eachKey))
				i += 1
			print "time out5"	
		
			currentNutri.t0Energy_kcal = "0:"+str(int(round(cal)))
			#Adjust upperbound of macro according to calories values
		
			currentNutri.t0Protein_g=  currentNutri.t0Protein_g.replace("ND",str(int(round(cal*int(protup)/400))))
			currentNutri.t0TotalLipidFat_g=currentNutri.t0TotalLipidFat_g.replace(":ND",":"+str(int(round(cal*int(fatup)/900))))
			currentNutri.t0Carbohydrate_ByDifference_g=currentNutri.t0Carbohydrate_ByDifference_g.replace("ND",str(int(round(cal*int(carbup)/400 ))))	
			(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,0)
			db.session.commit()
			
			print "time out6"
			if "Sign Up" in formVal:
				login_user(newUser)
				return redirect(url_for('signup'))
			elif "Guest" in formVal:
				print "time out7"
				login_user(newUser)
				session['userProfile'] = getUserProfileDisplay(newUser)
				flash("Welcome, Guest!")
				print "time out8"
				return redirect(url_for("manage"))
	
	print "time out9"		
	formLogin = LoginForm()
	if formLogin.validate_on_submit():
		#print "get login form"
		user = User.query.filter(User.username == formLogin.usernameLog.data).filter(User.password == formLogin.passwordLog.data).first()
		if user is None:
			print "time out10"
			flash("Wrong username or password. Please try again")
			return render_template("login.html", formLogin=formLogin, head_1 = "Log In", profileFull= profileFull)
		login_user(user)
		session['userProfile'] = getUserProfileDisplay(g.user)
		flash("Logged in successfully.")
		print "time out11"
		return redirect(url_for("profile"))
	print "time out12"	
	return render_template("login.html", formLogin=formLogin, profileFull= profileFull)
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupform = SignupForm()
    if signupform.validate_on_submit():
    	user = User.query.filter(User.username == signupform.usernameSign.data).first()
    	if user is None:
    		g.user.username = signupform.usernameSign.data
    		g.user.password = signupform.passwordSign.data
    		g.user.role = 0
        	db.session.commit()
        	flash("Signed in successfully.")
        	session['userProfile'] = getUserProfileDisplay(g.user)
        	return redirect(url_for("manage"))	
    	flash("The username already exists Please try again.")
    return render_template("signup.html", 
    		signupform=signupform,
    		userProfile = getUserProfileDisplay(g.user))

@app.route("/logout")
@login_required
def logout():
	saveFood()
	flash("You have logged out. Thank you")
	#print "g_user is :", g.user
	#print "current user is:", current_user
	if (g.user.role == 2):
		session.pop(g.user.get_id(), None)
		db.session.delete(g.user.nutri[0])
		db.session.delete(g.user)
		db.session.commit()
	keys = session.keys()
	for each in keys:
		session.pop(each, None)
	logout_user()
	return redirect(url_for('login'))

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
	

    