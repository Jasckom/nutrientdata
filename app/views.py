#2pm friday - start making without dictionary of id

from flask import render_template, flash, redirect, url_for, g, session, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import SearchForm, SelectFood, LoginForm, SignupForm, createMinMaxForm, EditPreferredList, Profile, manyButtons, createFoodsILike, SelectFilter, ProfileFull
from datetime import datetime
from linearOptimize import linearOptimize
from filterFood import *
from sqlalchemy import asc, desc
from sqlalchemy.orm import aliased
from searchFood import searchFood, searchFoodBrand
from app.models import Food, Nutri,User
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
mainCategories = ['baked products', 'beans legume products', 'beef products', 'beverages', 'breakfast cereals', 'cereal grains pasta', 'dairy egg products', 'ethnic foods', 'fast foods', 'fats oils', 'fish seafood products', 'fruits fruit juices', 'lamb veal game products', 'meals entrees sidedishes', 'nut seed products', 'pork products', 'poultry products', 'sausages deli meats', 'snacks', 'soups sauces gravies', 'spices herbs', 'sweets', 'vegetables']
foodTypes = [['apple pies', 'bagels', 'banana muffins', 'banana pumpkin breads', 'biscotti', 'biscuit breads', 'blueberry muffins', 'bran muffins', 'bread', 'bread crumbs', 'breadsticks', 'brownies', 'cakes', 'carrot cakes', 'cheese crackers', 'cheesecakes', 'cherry berry pies', 'chocolate cakes', 'chocolate chip cookies', 'chocolate chip muffins', 'cinnamon raisin bread', 'coffee cakes', 'cookies', 'corn muffins', 'cornbread', 'crackers', 'cream custard pies', 'crepes', 'crispbread crackers', 'croissants', 'croutons', 'cupcakes', 'danish pastries', 'dinner rolls', 'doughnuts', 'english muffins crumpets', 'focaccia flat pizza breads', 'french italian bread', 'french toast', 'garlic bread toast', 'ginger cookies', 'graham crackers', 'hamburger buns', 'hot dog buns', 'lemon cakes', 'matzo', 'meat savory pies', 'muffins scones', 'multigrain bread', 'multigrain crackers', 'oatmeal cookies', 'oyster crackers', 'pancakes waffles', 'pastries', 'peanut butter cookies', 'pie pastry crusts', 'pies', 'pita bread', 'pumpkin pies', 'quiches', 'rice crackers cakes', 'rolls buns', 'rye bread', 'saltine crackers', 'sandwich cookies', 'scones', 'shortbread cookies', 'sourdough bread', 'stuffings', 'sugar cookies', 'sweet buns rolls', 'tarts', 'toast', 'toaster pastries', 'tortillas tacos wraps', 'wafer cookies', 'water crackers', 'wheat bread', 'wheat crackers', 'white bread'], ['baked beans', 'bean dishes', 'black beans', 'chickpeas', 'green beans', 'hummus', 'kidney beans', 'lentils', 'lima beans', 'meat substitutes tvps', 'pinto beans', 'refried beans', 'soybeans', 'tofu tempeh', 'tofu tempeh dishes', 'white beans'], ['beef', 'beef broccoli', 'beef cold cuts', 'beef dishes', 'beef meatballs', 'beef patties', 'beef ribs', 'beef stroganoff', 'chuck steak', 'corned beef', 'country fried steak', 'flank steak', 'ground beef', 'hamburgers', 'meatloaf', 'porterhouse', 'pot roast', 'roast beef', 'roast beef sandwiches', 'salisbury steak', 'sirloin steak', 'steak', 'steak sandwiches', 'teriyaki beef'], ['alcoholic drinks', 'americano', 'beer', 'black tea', 'bloody mary', 'cafe mocha', 'cappuccino', 'caramel macchiato', 'carbonated drinks', 'chocolate smoothies', 'coconut water', 'coffee', 'cola', 'cream soda', 'dunkin donuts', 'energy drinks', 'espresso', 'fruit punch', 'fruit smoothies', 'ginger ale', 'green tea', 'herbal tea', 'hot chocolate', 'hot drinks', 'iced coffee', 'iced tea', 'juices', 'latte', 'lemon lime soda', 'lite beer', 'mai tai', 'margarita', 'martini', 'milk', 'milk substitutes', 'mixers cocktails', 'nutritional drinks', 'orange soda', 'pina colada', 'protein body building shakes', 'root beer', 'seltzer sparkling club tonic water', 'smoothies', 'sports drinks', 'starbucks', 'tea', 'vanilla smoothies', 'vodka gin rum whiskey', 'water', 'weight loss meal replacement shakes', 'white tea', 'wine', 'yogurt drinks'], ['bran flakes', 'cold cereals', 'corn flakes', 'cream wheat', 'granola muesli', 'grits', 'hot cereals', 'oats oatmeal', 'rice cereal', 'wheat cereal', 'wheat germ bran'], ['angel hair', 'barley', 'basmati rice', 'breakfast cereals', 'brown rice', 'buckwheat kasha', 'bulgur', 'chicken rice', 'corn meal', 'couscous', 'egg noodles', 'fettucini', 'flour', 'fried rice', 'gnocchi', 'grains', 'lasagna', 'linguini', 'macaroni', 'macaroni beef', 'macaroni cheese', 'noodles', 'pasta', 'pasta casserole', 'pasta dishes', 'penne', 'polenta', 'quinoa', 'ramen noodles', 'ravioli', 'rice', 'rice beans', 'rice dishes', 'rice flour', 'rice pilaf', 'rigatoni', 'risotto', 'rotini', 'soy flour', 'spaghetti', 'spaghetti meatballs', 'tortellini', 'vermicelli', 'wheat flour', 'white rice', 'whole wheat pasta', 'wild rice', 'yellow rice'], ['american cheese', 'apple yogurt', 'banana yogurt', 'blue cheese', 'blueberry yogurt', 'brie cheese', 'butter', 'cheddar cheese', 'cheese', 'chive onion cream cheese', 'chocolate flavored milk', 'coffee yogurt', 'colby cheese', 'colby jack cheese', 'condensed evaporated milk', 'cottage cheese', 'cream', 'cream cheese', 'creamer', 'egg whites substitutes', 'eggs', 'fat free cream', 'fat yogurt', 'feta cheese', 'flavored yogurt', 'fried eggs', 'frozen yogurt', 'goat cheese', 'gouda cheese', 'greek yogurt', 'half', 'hard boiled eggs', 'havarti cheese', 'honey nut cream cheese', 'jack cheese', 'lemon lime yogurt', 'light cream cheese', 'light yogurt', 'low fat milk percent', 'milk shakes', 'mozzarella cheese', 'muenster cheese', 'omelets', 'parmesan cheese', 'peach yogurt', 'poached eggs', 'provolone cheese', 'raisin cream cheese', 'reduced fat milk percent', 'ricotta cheese', 'scrambled eggs', 'skim milk fat free', 'sour cream', 'strawberry cream cheese', 'strawberry yogurt', 'string cheese', 'swiss cheese', 'vanilla yogurt', 'vegetable cream cheese', 'whipped cream', 'whole milk', 'yogurt'], ['afghani food', 'african food', 'american food', 'arabic food', 'australasian food', 'australian food', 'austrian food', 'brazilian food', 'british food', 'canadian food', 'caribbean jamaican', 'chinese food', 'east asian food', 'ethiopian food', 'european food', 'french food', 'german food', 'greek food', 'indian food', 'irish food', 'italian food', 'japanese food', 'korean food', 'kosher israeli', 'latin food', 'mexican food', 'middle eastern food', 'moroccan food', 'new zealand food', 'north american food', 'pakistani food', 'polish food', 'portuguese food', 'russian food', 'scandinavian food', 'south african food', 'south asian food', 'spanish food', 'thai food', 'turkish food', 'vietnamese food'], ['blt sandwiches', 'breakfast sandwiches', 'burger sandwiches', 'burritos', 'calzones', 'cheese pizza', 'cheeseburgers', 'chicken burgers', 'chicken sandwiches', 'chili', 'club sandwiches', 'cold cut sandwiches', 'corn dogs', 'enchiladas', 'fajitas', 'fast food side dishes', 'fish sandwiches', 'french fries potato wedges', 'fried chicken', 'grilled cheese sandwiches', 'ham sandwiches', 'hash browns', 'hawaiian pizza', 'hot dogs', 'italian sandwiches', 'meatball sandwiches', 'nachos', 'onion rings', 'pepperoni pizza', 'pizza calzones', 'pork sandwiches', 'quesadillas', 'roast chicken', 'salads', 'sandwiches wraps', 'sausage pizza', 'sausage sandwiches', 'sausages', 'spring rolls', 'tacos', 'tamales', 'tex mex food', 'tuna sandwiches melts', 'turkey sandwiches', 'veggie burgers', 'veggie pizza', 'veggie sandwiches'], ['blue cheese dressing', 'caesar dressing', 'canola oil', 'cooking spray', 'corn oil', 'fats lard shortening', 'fish oil', 'french dressing', 'grape seed oil', 'greek dressing', 'honey mustard dressing', 'italian dressing', 'margarine', 'mayonnaise aioli', 'oils', 'olive oil', 'onion dressing', 'poppyseed dressing', 'ranch dressing', 'salad dressings', 'sesame dressing', 'sesame oil', 'thousand island dressing', 'vegetable oil', 'vegetable oil spread', 'vinegar vinaigrette dressing'], ['california rolls', 'clams', 'cod', 'crab', 'fish chips', 'fish dishes', 'fish sticks cakes', 'flounder', 'gefilte fish', 'haddock', 'halibut', 'herring', 'lobster', 'manhattan clam chowder', 'new england clam chowder', 'oysters', 'pollocks', 'salmon', 'sardines', 'scallops', 'shrimp', 'sole', 'sushi rolls', 'sushi sashimi', 'tilapia', 'tuna', 'whitefish pike'], ['apple juice', 'apples', 'apricots', 'avocados', 'bananas', 'blueberries', 'cherries', 'coconuts', 'cranberries', 'cranberry juice', 'fruit', 'fruit salads', 'grape juice', 'grapefruit juice', 'grapefruits', 'grapes', 'lemonade limeade', 'mangos', 'melons cantaloupe', 'olives', 'orange juice', 'oranges tangerines mandarins', 'peaches', 'pears', 'pineapple juice', 'pineapples', 'plums', 'pumpkins', 'raisins', 'raspberries', 'strawberries', 'tomato vegetable juice'], ['lamb', 'lamb dishes', 'veal', 'veal dishes'], ['baby food', 'baby food cereal', 'baby food dinners', 'baby food juice', 'baby food meats', 'baby food snacks', 'chicken dishes', 'egg dishes', 'ethnic foods', 'fast foods', 'fruit baby food', 'infant formula', 'pork dishes', 'potato dishes', 'turkey dishes', 'vegetable baby food', 'vegetable dishes'], ['almond other nut butters', 'almonds', 'cashews', 'chestnuts', 'flaxseeds', 'hazelnuts', 'macadamia nuts', 'nut trail mixes', 'peanut butter', 'peanuts', 'pecans', 'pine nuts', 'pistachios', 'pumpkin seeds', 'sesame seeds', 'soy nuts', 'sunflower seeds', 'walnuts'], ['bacon', 'ham', 'ham cold cuts', 'pork chops', 'pork loin', 'pork ribs', 'pork roast', 'pork sausage', 'pork shoulder', 'pork tenderloin', 'pulled pork'], ['bbq chicken', 'chicken', 'chicken breasts', 'chicken cold cuts', 'chicken drumsticks', 'chicken dumplings', 'chicken nuggets tenders', 'chicken parmesan', 'chicken patties', 'chicken salad', 'chicken sausage', 'chicken soups', 'chicken thighs', 'chicken tikka masala', 'chicken wings', 'duck', 'fried chicken', 'grilled chicken', 'ground turkey', 'teriyaki chicken', 'turkey', 'turkey bacon', 'turkey breast', 'turkey chili', 'turkey cold cuts', 'turkey legs', 'turkey patties', 'turkey sausage', 'turkey soups'], ['beef sausage', 'bologna cold cuts', 'bratwurst', 'chorizo', 'italian sausage', 'jerky snack sticks', 'lunch meats', 'pastrami', 'polish sausage', 'salami pepperoni'], ['banana plantain chips', 'candy', 'cereal bars', 'cheese puffs', 'chewing gum mints', 'chips', 'corn tortilla chips', 'cracker sandwiches', 'energy protein bars', 'filled pretzels', 'flavored pretzels', 'fruit nut bars', 'fruit snacks', 'granola bars', 'meal replacement bars', 'multigrain chips', 'nutrition bars', 'oatmeal raisin bars', 'pita bagel chips', 'popcorn', 'pork skins rinds', 'potato chips', 'pretzel sticks rods', 'pretzels', 'puddings', 'puffed rice bars', 'snack bars', 'snack mixes', 'soft pretzels', 'trail mix bars'], ['alfredo sauce', 'barbecue sauce', 'bean soup', 'beef barley soup', 'beef broth stock bouillon', 'beef chili', 'beef noodle soup', 'beef soups', 'beef stew', 'bisques', 'broth stock bouillon', 'bruschetta', 'butternut squash pumpkin soup', 'cheese dip', 'cheese soups', 'chicken broth stock bouillon', 'chicken gravy', 'chicken noodle soup', 'chicken rice soup', 'chowders', 'chutney', 'cocktail sauce', 'condiments', 'corn chowder', 'cream broccoli soup', 'cream chicken soup', 'cream mushroom soup', 'cream potato soup', 'cream soups', 'cream tomato soup', 'curry sauce', 'dips spreads', 'french onion dip', 'garlic sauce', 'gravy', 'guacamole', 'gumbo', 'hot sauce chipotle', 'ketchup', 'lentil soup', 'marinades', 'marinara tomato sauce', 'minestrone soup', 'mushroom gravy', 'mushroom soup', 'mustard', 'onion soup', 'pasta pizza sauces', 'pate', 'pea soup', 'peanut sauce', 'pesto sauce', 'potato soup', 'relish', 'salsa', 'sauces', 'soups', 'soy sauce', 'spinach dip', 'steak sauce', 'stews', 'sugars syrups', 'sweet sour sauce', 'tapenade', 'tartar sauce', 'teriyaki sauce', 'tomato soup', 'tortilla soup', 'turkey gravy', 'vegetable broth bouillon', 'vegetable soups', 'vodka sauce', 'wedding soup'], ['baking soda', 'chili powder', 'coating mixes', 'curry', 'food coloring', 'garlic', 'ginger', 'onion', 'oregano', 'paprika', 'parsley', 'pepper', 'salt', 'seasoning mix', 'steak seasoning', 'vitamins'], ['apple butter', 'apple jams jellies', 'artificial sweeteners', 'brown sugar', 'candy canes christmas', 'caramel candy', 'caramel syrup', 'chocolate', 'chocolate candy', 'chocolate candy bars', 'chocolate chips morsels', 'chocolate covered candy', 'chocolate ice cream', 'chocolate pudding', 'chocolate spreads', 'chocolate syrup', 'coffee ice cream', 'cookies n cream ice', 'crisps cobblers', 'dark chocolate', 'decorating icing', 'dessert toppings', 'desserts', 'easter eggs candy', 'fat free ice cream', 'flavored syrups', 'fruit desserts compotes', 'fruit jams jellies', 'gelatin desserts', 'grape jams jellies', 'gummy snacks', 'hard candy', 'honey', 'ice cream bars', 'ice cream cakes', 'ice cream sandwiches', 'ice cream sorbet', 'ice cream sundaes', 'icing decorations', 'icings frostings', 'jellies jams preserves spreads', 'licorice', 'lite syrup', 'lollipops suckers', 'low fat ice cream', 'maple syrup', 'marmalade', 'marshmallows', 'milk chocolate', 'orange jams jellies', 'pancake syrup', 'parfaits', 'pie cake fillings', 'rice pudding', 'sauces', 'seasonal candy', 'sherbet sorbet', 'soft serve frozen yogurt', 'sour candy', 'sprinkles', 'strawberry ice cream', 'strawberry jams jellies', 'sugar free candy', 'sugar free ice cream', 'sugar free syrup', 'sugars sweeteners', 'toppings', 'valentines candy', 'vanilla', 'vanilla ice cream', 'vanilla pudding', 'whipped toppings'], ['artichokes', 'asparagus', 'au gratin potatoes', 'baked potato', 'beets', 'broccoli', 'cabbage', 'caesar salad', 'carrots', 'cauliflower', 'celery', 'chili peppers', 'coleslaw', 'collards', 'corn', 'cucumber', 'eggplant', 'fruit vegetables', 'garden salad', 'garlic', 'inflorescence vegetables', 'kale', 'leafy vegetables', 'lettuce', 'mashed potatoes', 'mixed vegetables', 'mushrooms', 'onions', 'peas', 'pickles pickled vegetables', 'potato salad', 'potatoes yams', 'pumpkin squash', 'radishes', 'root vegetables', 'scalloped potatoes', 'souffle', 'spinach', 'sprouts', 'stem vegetables', 'stir fried vegetables', 'sweet peppers', 'tomatoes', 'turnips', 'vegetable casseroles', 'zucchini']]

# def getCat():
# 	toSkip = [38 , 123 , 124 , 126 , 137 , 138 , 142 , 163 , 178 , 179 , 184 , 186 , 188 , 189 , 190 , 191 , 193 , 194 , 196 , 197 , 199 , 302 , 316 , 317 , 359 , 371 , 400 , 709 , 710 , 711 , 712 , 738 , 740 , 744 ]
# 	categories = []
# 	foodTypes = []
# 	foodTypesinCat = []
# 	categoryFile = open('IndexCategories','r')
# 	for eachCat in categoryFile:
# 		eachCatList = eachCat.split('^')
# 		cat = int(eachCatList[0])
# 		food = eachCatList[1]
# 		if cat in toSkip:
# 			continue
# 		if cat < 0:
# 			categories.append(food)
# 			foodTypesinCat.sort()
# 			foodTypes.append(foodTypesinCat)
# 			foodTypesinCat = []
# 		else:
# 			foodTypesinCat.append(food)
# 	foodTypesinCat.sort()
# 	foodTypes.append(foodTypesinCat)
# 	foodTypes.remove([])
# 	return (categories, foodTypes)
# 	
# (mainCategories, foodTypes) = getCat()

def getSearchEntry(brandEntry,searchEntry):
	##print "in search, brand is: ", brandEntry, searchEntry, 
	if len(brandEntry) != 0:
		if len(searchEntry) != 0:
			if not searchEntry.isspace():
				searchEntry += ":"+brandEntry				
			else:
				searchEntry = "brandOnly:"+brandEntry
		else:
			searchEntry = "brandOnly:"+brandEntry
	return searchEntry


@login_required
@app.route('/index', methods = ['GET', 'POST'])
def index():
	##print session
	#If first page they decided to search - give anonymous user
	first = True
	form = SearchForm()
	if form.validate_on_submit():
		if not g.user.is_authenticated():
			guestID = (datetime.utcnow()-datetime(1970,1,1)).total_seconds()
			guestID = (str(guestID)).split('.')
			guestID = int((guestID[0]+guestID[1]))
			guestUser = User(username = str(guestID), role = 2)
			db.session.add(guestUser)
			db.session.commit()
			login_user(guestUser)
			##print guestUser
		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		#print "in search, brand is: ", brandEntry
		if not brandEntry is None:
			searchEntry += ":"+brandEntry
		session["result"] = searchEntry
		#print session
		#print "sending to result"
		return redirect(url_for('resultSearch'))
	return render_template('search.html',
		title = 'Search your food',
		form = form,
		first = first)
    
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

@login_required
@app.route('/search', methods = ['GET', 'POST'])
@login_required
def search():
	form = SearchForm()
	
	if form.validate_on_submit() and ( (len(form.searchEntry.data) != 0) or (len(form.brandEntry.data) != 0) ):
		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		searchEntry = getSearchEntry(brandEntry,searchEntry)		
		session["result"] = searchEntry
		if "filter" in session.keys():
			session.pop("filter")
		return redirect(url_for('resultSearch'))
	
	(categories,foodTypes) = getCat()
	return render_template('search.html',
		title = 'Search your food',
		form = form,
		myPreferedFood = [Food.query.filter(Food.id == i).first() for i in session[g.user.get_id()]],
		categories = categories,
		foodTypes = foodTypes)

@login_required
@app.route('/mainCatFromSearch/<mainCatChosen>/<foodChosen>')
def mainCatFromSearch(mainCatChosen,foodChosen):
	global mainCategories
	global foodTypes
	
	session["box1Head"] = mainCatChosen
	session["box1Cat"] = foodTypes[mainCategories.index(mainCatChosen)]

	return redirect(url_for('resultCategory', categoryChosen =mainCatChosen+":"+foodChosen))

@login_required
@app.route('/mainCat/<mainCatChosen>')
def mainCat(mainCatChosen):
	global mainCategories
	global foodTypes
	mainCatChosen = int(mainCatChosen)
	#print "in MainCat: ", mainCatChosen
	#print "box1Head"
	#print id(session["box1Head"])
	session["box1Head"] = mainCategories[mainCatChosen]
	session["box1Cat"] = foodTypes[mainCatChosen]
	#print session["box1Head"]
	#print session["box1Cat"] 
	if "filter" in session.keys():
		session.pop("filter")
	
	return redirect(url_for('resultCategory', categoryChosen =mainCategories[mainCatChosen]+":General"))

def getInfo():
	global basic_nutrient
	global full_ext_nutrient
	if session["foodInfo"] == None:
		return [],[]
	food = Food.query.filter(Food.id==session["foodInfo"]).first()
	info = []
	extraInfo = []
	for i in range(8,25):
		info.append( (basic_nutrient[i-8],   food.value(i)) )
	for i in range(25,165):
		extraInfo.append((full_ext_nutrient[i-25],   food.value(i)))
		
	return info, food
	
@app.route('/resultSearch', methods = ['GET', 'POST'])
@app.route('/resultSearch/<int:page>', methods = ['GET', 'POST'])
def resultSearch(page = 1):
	if not g.user.is_authenticated():
		flash('Please First Sign in as a Guest')
		return redirect(url_for('login'))
	#get categories for the side
	global mainCategories
	global foodTypes
	global full_ext_nutrient
	#Search Function
	form = SearchForm()
	if form.validate_on_submit() and ( (len(form.searchEntry.data) != 0) or (len(form.brandEntry.data) != 0) ):

		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		searchEntry = getSearchEntry(brandEntry,searchEntry)		
		session["result"] = searchEntry
		if "filter" in session.keys():
			session.pop("filter")
		return redirect(url_for('resultSearch'))
	
	foodIdsArg = session[g.user.get_id()]
	foodNamesArg = session["foodItem"]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)
	if foodIdsArg:
		foodsItemsILike = Food.query.filter(Food.id.in_(foodIdsArg)).all()
	else:
		foodsItemsILike = []

	#Validate form
	if foodsILike.validate_on_submit() and (foodsILike.submit.data or  foodsILike.remove.data or foodsILike.toggle.data):
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
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('resultSearch'))
	
	# Filter form
	if "filter" in session.keys():
		selectFilter = SelectFilter(session["filter"])
	else:
		selectFilter = SelectFilter(24)
	if request.method == 'POST':
		if selectFilter.filter.data and request.form['filter'] == 'Go!':
			filterNut = selectFilter.filterNut.data
			session["filter"] = filterNut
	
	#Store search term
	searchEntry = session["result"]
	searchEntryList = searchEntry.split(":")
	brandEntry = ""
	if len(searchEntryList) > 1:
		brandEntry = searchEntryList[1]		
	searchEntry = searchEntryList[0]
	
	#Get potential 
	matchingCat = getMatchingCat(searchEntry,foodTypes)
	print "Search Term:", searchEntry, type(searchEntry), len(searchEntry)
	print  "brand term:", brandEntry, type(brandEntry), len(brandEntry)
	
	box2Head = "Search Results - Foods"	
	if searchEntry == "" and brandEntry == "":
		resultSearch = []
	else:
		if "filter" in session.keys():
			filterNut = session["filter"]
			if filterNut != 24:
				if searchEntry == "brandOnly":
					results = searchFoodBrand(brandEntry, Food, "unordered")
				else:
					results = searchFood(searchEntry, brandEntry, Food, "unordered")
				
				if filterNut in toReduce:
					results = results.order_by(asc(instrumentAttribute[filterNut]))
					box2Head += " with Lowest " + full_ext_nutrient[filterNut-25]
				else:
					results = results.order_by(desc(instrumentAttribute[filterNut]))
					box2Head += " with Highest " + full_ext_nutrient[filterNut-25]
			else:
				if searchEntry == "brandOnly":
					results = searchFoodBrand(brandEntry, Food, "ordered")
				else:
					results = searchFood(searchEntry, brandEntry, Food, "ordered")
		else:
			if searchEntry == "brandOnly":
				results = searchFoodBrand(brandEntry, Food, "ordered")
			else:
				results = searchFood(searchEntry, brandEntry, Food, "ordered")
		
		resultSearch = results.paginate(page, RESULTS_PER_PAGE, False)
	


	session["box1Head"] = "Search Results - Categories"
	session["box1Cat"] = matchingCat
	
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
	
	#print "Test catchosen: ",categoryChosen
	
	# filterNut is the index of nutRatioUnmet
	#Search Function
	form = SearchForm()
	if form.validate_on_submit() and ( (len(form.searchEntry.data) != 0) or (len(form.brandEntry.data) != 0) ):
		searchEntry = form.searchEntry.data
		brandEntry = form.brandEntry.data
		searchEntry = getSearchEntry(brandEntry,searchEntry)		
		session["result"] = searchEntry
		if "filter" in session.keys():
			session.pop("filter")
		return redirect(url_for('resultSearch'))
	
	#Store search term
	session["result"] = categoryChosen
	
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
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('resultCategory', categoryChosen=categoryChosen))

	# Filter form
	if "filter" in session.keys():
		selectFilter = SelectFilter(session["filter"])
	else:
		selectFilter = SelectFilter(24)
	if request.method == 'POST':
		if selectFilter.filter.data and request.form['filter'] == 'Go!':
			filterNut = selectFilter.filterNut.data
			session["filter"] = filterNut
	
	#Get results/cat
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
		if filterNut != 24:			
			if filterNut in toReduce:
				resultCategory = query.order_by(asc(instrumentAttribute[filterNut])).paginate(page, RESULTS_PER_PAGE, False)
 				box2Head = categoryChosen + " with Lowest " + full_ext_nutrient[filterNut-25]

			else:
				resultCategory = query.order_by(desc(instrumentAttribute[filterNut])).paginate(page, RESULTS_PER_PAGE, False)
 				box2Head = categoryChosen + " with Highest " + full_ext_nutrient[filterNut-25]
 		else:
 			resultCategory = query.order_by(asc(Food.food)).paginate(page, RESULTS_PER_PAGE, False)
			box2Head = categoryChosen
	else:
		resultCategory = query.order_by(asc(Food.food)).paginate(page, RESULTS_PER_PAGE, False)
		box2Head = categoryChosen
	
	(info, food) = getInfo()
# 	for each in foodsILike:
		#print each.label
	
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


# redirecting functions Get Info
@login_required
@app.route('/selectFoodInfo/<foodIDInfo>')
def selectFoodInfo(foodIDInfo):
	session["foodInfo"] = foodIDInfo
	return redirect(url_for('resultSearch'))

@login_required
@app.route('/selectFoodInfoCat/<foodIDInfo>')
def selectFoodInfoCat(foodIDInfo):
	session["foodInfo"] = foodIDInfo
	categoryChosen = session["result"]
	return redirect(url_for('resultCategory',categoryChosen =categoryChosen ))

@login_required
@app.route('/selectFoodInfoSuggest/<foodIDInfo>')
def selectFoodInfoSuggest(foodIDInfo):
	#print "lala"
	session["foodInfo"] = foodIDInfo
	return redirect(url_for('resultSuggest'))


# redirecting functions Select Food
@login_required
@app.route('/selectFood/<foodChosen>')
def selectFood(foodChosen):
	if not foodChosen in session[g.user.get_id()]:
		#print "IN SELECT FOOD"
		session[g.user.get_id()].insert(0,foodChosen)
		food = Food.query.filter(Food.id==foodChosen).first()
		session[("foodItem")].insert(0,food.food+ " "+ food.detail+ " (" +  food.source+")")
	categoryChosen = session["result"]
	return redirect(url_for('resultCategory',categoryChosen =categoryChosen ))

@login_required
@app.route('/selectFoodFromSearch/<foodIDFromSearch>')
def selectFoodFromSearch(foodIDFromSearch):
	if not foodIDFromSearch in session[g.user.get_id()]:
		#print "IN SELECT FOOD FROM SEARCH"
		session[g.user.get_id()].insert(0,foodIDFromSearch)
		food = Food.query.filter(Food.id==foodIDFromSearch).first()
		session[("foodItem")].insert(0,food.food+ " "+ food.detail+ " (" +  food.source+")")
	return redirect(url_for('resultSearch'))

@login_required
@app.route('/selectFoodFromSuggest/<foodIDFromSuggest>')
def selectFoodFromSuggest(foodIDFromSuggest):

	if foodIDFromSuggest == "updateAfterRemove":
		(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(g.user.nutri[0],1)
		constraints = []
		for i in range(len(check)):
			if check[i]:
				constraints.append(i+25)
	
		foodItems = []
		for i in range(len(session[g.user.get_id()])):
			foodItems.append(Food.query.filter(Food.id ==session[g.user.get_id()][i]).first())
		
		if "basicPlan" in session.keys():
			if session["basicPlan"] == 1:
				global basicPlan
				newConstrainsts = []
				for each in constraints:
					if each in basicPlan:
						newConstrainsts.append(each)
				constraints = newConstrainsts
			
		
		(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio2(constraints, foodItems, g.user.nutri[0])
						
		if nutRatioMin:
			session["sumCal"] = sumCal
			session["sumNutUnmet"] = sumNutUnmet
			session["nutRatioMin"] = nutRatioMin
			session["nutRatioUnmet"] = nutRatioUnmet
			session[("chosenNut")] = 0
			return redirect(url_for('resultSuggest'))
		
		else:
			#print "Here" ,nutRatioUnmet
			return redirect(url_for('resultSuggest'))
	
	if not foodIDFromSuggest in session[g.user.get_id()]:
		#print "i'm heree3" , foodIDFromSuggest	
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
		
		foodItems = []
		for i in range(len(session[g.user.get_id()])):
			foodItems.append(Food.query.filter(Food.id ==session[g.user.get_id()][i]).first())
			
		(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio2(constraints, foodItems, g.user.nutri[0])
		
		#print "In selectFood", nutRatioMin, nutRatioUnmet
				
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
	
# get bounds from Nutri and decide whether to follow the recommended or follow the user's new constrainst
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
		##print "each in getkeys", each
		each = each.split(":")
		defaultGenlowerBound.append(each[0])
		defautGenupperBound.append(each[1])
		if override:
			if len(each) >= 3:
				check.append(int(each[2]))
		else:
			if (each[0] == "0" and each[1] == "ND"):
				check.append(0)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":0")
			else:
				check.append(1)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":1")
			##print "In setting", nutriField[i], getattr(nutriObject, nutriField[i])
		i += 1

	db.session.commit()
# 	#print "In f(getKeybounds) end: "
# 	for eachkey in nutriObject.__table__.columns.keys():
# 		nutriField.append(eachkey)
#		#print eachkey, getattr(nutriObject, eachkey)
	check[0] = 0
	
	return 	check, nutriField, defaultGenlowerBound, defautGenupperBound

# tell ratios and indicate which nutrient is not satisfied
def reportRatio2(constraints, foodItems, nutri):

	if (not constraints) and (not foodItems):
		return None, [],[],[]	
	nutRatioUnmet = []
	nutRatioMin = []
	nullNut = []
	failedBestFood = []

	givenCal = nutri.t0Energy_kcal.split(":")[1]
	if givenCal == "ND":
		givenCal = 5000
	else:
		givenCal = float(givenCal)
	bestFoods = []
	bestFoodsVals = []

	if not foodItems:
		for eachCon in constraints:
			nutRatioMin.append(nutri.nutCalRatio(eachCon))
		return givenCal, [], nutRatioMin, constraints
	
	global full_ext_nutrient
	
	for i in range(len(constraints)):
		eachCon = constraints[i]
		maxNut = 0
		for j in range(len(foodItems)):
			if foodItems[j].value(eachCon) >= maxNut:
				maxNut = foodItems[j].value(eachCon)
				bestFood = foodItems[j]
		bestFoods.append(bestFood)
		bestFoodsVals.append(maxNut)
	

	for i in range(len(constraints)):
		eachCon = constraints[i]
		bestFoodVal = bestFoodsVals[i]
		nutRatio = bestFoodVal/givenCal
		minRatio= nutri.nutCalRatio(eachCon)
		if nutRatio <= minRatio:
			nutRatioUnmet.append(eachCon)
			nutRatioMin.append(minRatio)
			failedBestFood.append(nutRatio)
			#print eachCon, nutRatio, "<=", minRatio
	
	return givenCal, failedBestFood, nutRatioMin, nutRatioUnmet


# XX return dictionary of each lacking nutrient and how much
def reportTotal(constraints, outputFoodAmount, foodItems):
	#print outputFoodAmount
	TotalNut = []
	full_ext_nutrient = ["Water/g","Energy/kcal","Energy/kj","Protein/g","Total lipid fat/g","Carbohydrate, by difference/g","Fiber, total dietary/g","Sugars, total/g","Sucrose/g","Glucose dextrose/g","Fructose/g","Lactose/g","Maltose/g","Galactose/g","Starch/g","Adjusted Protein/g","Calcium, Ca/mg","Iron, Fe/mg","Magnesium, Mg/mg","Phosphorus, P/mg","Potassium, K/mg","Sodium, Na/mg","Zinc, Zn/mg","Copper, Cu/mg","Manganese, Mn/mg","Selenium, Se/mcg","Fluoride, F/mcg","Vitamin C, total ascorbic acid/mg","Thiamin/mg","Riboflavin/mg","Niacin/mg","Pantothenic acid/mg","Vitamin B-6/mg","Folate, total/mcg","Folic acid/mcg","Folate, food/mcg","Folate, DFE/mcg_DFE","Choline, total/mg","Betaine/mg","Vitamin B-12/mcg","Vitamin B-12, added/mcg","Vitamin A, IU/IU","Vitamin A, RAE/mcg_RAE","Retinol/mcg","Vitamin E (alpha-tocopherol)/mg","Vitamin E, added/mg","Tocopherol, beta/mg","Tocopherol, gamma/mg","Tocopherol, delta/mg","Vitamin K phylloquinone/mcg","Carotene, beta/mcg","Carotene, alpha/mcg","Cryptoxanthin, beta/mcg","Lycopene/mcg","Lutein + zeaxanthin/mcg","Vitamin D/IU","Stigmasterol/mg","Phytosterols/mg","Beta-sitosterol/mg","Campesterol/mg","Cholesterol/mg","Fatty acids, total monounsaturated/g","Fatty acids, total polyunsaturated/g","Fatty acids, total saturated/g","Fatty acids, total trans-monoenoic/g","Fatty acids, total trans-polyenoic/g","Fatty acids, total trans/g","Monounsaturated fats14:1/g","Monounsaturated fats15:1/g","Monounsaturated fats16:1 c/g","Monounsaturated fats16:1 t/g","Monounsaturated fats16:1 undifferentiated/g","Monounsaturated fats17:1/g","Monounsaturated fats18:1 c/g","Monounsaturated fats18:1 t/g","Monounsaturated fats18:1 undifferentiated/g","Monounsaturated fats20:1/g","Monounsaturated fats22:1 c/g","Monounsaturated fats22:1 t/g","Monounsaturated fats22:1 undifferentiated/g","Monounsaturated fats24:1 c/g","Polyunsaturated fats18:2 CLAs/g","Polyunsaturated fats18:2 i/g","Polyunsaturated fats18:2 n-6 c,c/g","Polyunsaturated fats18:2 t not further defined/g","Polyunsaturated fats18:2 t,t/g","Polyunsaturated fats18:2 undifferentiated/g","Polyunsaturated fats18:3 n-3 c,c,c/g","Polyunsaturated fats18:3 n-6 c,c,c/g","Polyunsaturated fats18:3 undifferentiated/g","Polyunsaturated fats18:3i/g","Polyunsaturated fats18:4/g","Polyunsaturated fats20:2 n-6 c,c/g","Polyunsaturated fats20:3 n-3/g","Polyunsaturated fats20:3 n-6/g","Polyunsaturated fats20:3 undifferentiated/g","Polyunsaturated fats20:4 n-6/g","Polyunsaturated fats20:4 undifferentiated/g","Polyunsaturated fats20:5 n-3/g","Polyunsaturated fats21:5/g","Polyunsaturated fats22:4/g","Polyunsaturated fats22:5 n-3/g","Polyunsaturated fats22:6 n-3/g","Saturated fats10:0/g","Saturated fats12:0/g","Saturated fats13:0/g","Saturated fats14:0/g","Saturated fats15:0/g","Saturated fats16:0/g","Saturated fats17:0/g","Saturated fats18:0/g","Saturated fats20:0/g","Saturated fats22:0/g","Saturated fats24:0/g","Saturated fats4:0/g","Saturated fats6:0/g","Saturated fats8:0/g","Alanine/g","Arginine/g","Aspartic acid/g","Cystine/g","Glutamic acid/g","Glycine/g","Histidine/g","Hydroxyproline/g","Isoleucine/g","Leucine/g","Lysine/g","Methionine/g","Phenylalanine/g","Proline/g","Serine/g","Threonine/g","Tryptophan/g","Tyrosine/g","Valine/g","Ash/g","Alcohol, ethyl/g","Caffeine/mg","Theobromine/mg"]
	for i in range(len(constraints)):
		eachCon = constraints[i]
		totalEachNut = []
		for j in range(len(foodItems)):
			eachFood = foodItems[j]
			eachFoodNut = float(eachFood.value(eachCon))
			totalEachNut.append(outputFoodAmount[j]*eachFoodNut)
		TotalNut.append(sum(totalEachNut))			
# 	for i in range(len(TotalNut)):
		#print full_ext_nutrient[constraints[i]-25], TotalNut[i]
	return TotalNut

# XXreturn dictionary of each lacking nutrient and how much
def addHealthy(check, lowerbound, foodItems, multiple):
	lackingNut = []
	amountMoreNut = []
	global full_ext_nutrient
	for i in range(len(check)):
		if check[i]: # if it is one of the constraints
			totalEachNut = []
			for eachFood in foodItems:
				eachFoodNut = float(eachFood.value(i+25))
				totalEachNut.append(eachFoodNut)
			if lowerbound[i] == "ND":
				bound = 0
			else:
				bound = float(lowerbound[i])
			#print "Total each ", full_ext_nutrient[i], bound, sum(totalEachNut)
			if sum(totalEachNut) <= multiple*bound:
				sumEachNut = sum(totalEachNut)
				lackingNut.append(i)
				amountMoreNut.append(multiple*bound-sum(totalEachNut))
			
#  	#print "Add healthy"
#  	for i in range(len(lackingNut)):
#  		#print full_ext_nutrient[lackingNut[i]], amountMoreNut[i]
	return lackingNut, amountMoreNut

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
	return cal*float(activity)

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

def showExceed(xNut, totalNut, foodAmount, foodItems):
# 	foodItems = [Food.query.filter(Food.id==each) for each in session["optimize"] ]
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

def getUserProfileDisplay(user):
	# Show profile of the user - this should be done for all pages as well
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
	
	if "basicPlan" not in session.keys():
		firstDefault = 1
	else:
		firstDefault = session["basicPlan"]
	
	
	# Get lower/upper bounds from the curent user - this is not overriding but based on what is recommended	
	currentNutri = g.user.nutri[0]
	(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,1)
	minMaxForm = createMinMaxForm(check,firstDefault)
	minMaxForm.lowerBound = defaultGenlowerBound
	minMaxForm.upperBound = defautGenupperBound	
	
	# Form is submitted
	if minMaxForm.is_submitted() and request.form['submit'] == 'Proceed to Select Foods' and (u'y' in request.form.values()):
		#print "Imhere 1"
		if ((minMaxForm.opt_maxormin.data == 0) or (minMaxForm.opt_maxormin.data == 1)):
			#print "Im here2"
			if minMaxForm.opt_nut.data is None:
				#print "Ime here 3"
				return redirect(url_for('manage'))
			else:
				opt_maxormin = minMaxForm.opt_maxormin.data
				opt_nut = minMaxForm.opt_nut.data
		
		elif minMaxForm.opt_maxormin.data == 2:
			opt_maxormin = 0
			opt_nut = 26
			minMaxForm.opt_nut.data = None
		elif minMaxForm.opt_maxormin.data == 3:
			opt_maxormin = 0
			opt_nut = 28
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
		#print ("Form taken")
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

		#session["currentCheck"] = currentCheck		
		#Save the nutritional constraints
		#print "Save nutritional"
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
		
		return redirect(url_for('resultSearch'))
		
	return render_template("manage.html",
		minMaxForm = minMaxForm,
		check = check,
		userProfile = session['userProfile'])

@login_required
@app.route('/optimize', methods = ['GET', 'POST'])
def optimize():
	if not g.user.is_authenticated():
		flash('Please First Sign in as a Guest or Sign up')
		return redirect(url_for('login'))

	if "opt_maxormin" not in session.keys():
		flash ('You have not chosen the diet plan')
		return redirect(url_for('manage'))
	
	if "optimize" not in session.keys():
		if session[g.user.get_id()]:
			session["optimize"] = session[g.user.get_id()]
		else:
			flash('You have not selected any foods')
			return redirect(url_for('resultSearch'))
			
	# Get save food that user select into Database
	userFood = [Food.query.filter(Food.id==int(each)).first() for each in session[g.user.get_id()]]
	if userFood:
		g.user.food = userFood
		db.session.commit()

	listFoodObject = [Food.query.filter(Food.id == i).first() for i in session["optimize"] ]	
	(check, nutriField, defaultGenlowerBound, defaultGenupperBound) = getKeysBounds(g.user.nutri[0],1)
	constraints = []
	for i in range(len(check)):
		if check[i]:
			constraints.append(i+25)
	opt_maxormin = session["opt_maxormin"]
	opt_nut = session["opt_nut"]
	
	if session["basicPlan"] == 1: # Chosen basic
		global basicPlan 
		newConstrainsts = []
		for each in constraints:
			if each in basicPlan:
				newConstrainsts.append(each)
		constraints = newConstrainsts

	result = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, defaultGenupperBound, opt_maxormin, opt_nut)
	(outputFood , outputFoodAmount , status ,objective, nullNut) = result
	
	#get upperbound of constraints
	upperBoundConst = []
	for each in constraints:
		upperBoundConst.append(defaultGenupperBound[each-25])
	
	if status == "Undefined":
		#print "LEAVE BOUND OPEN \n\n\n"
		if opt_maxormin:
			stat = "Optimal"
			pace = 5000
			while stat == "Optimal":
				(outputFoodPre, outputFoodAmountPre, statPre, objective, nullNut) = (outputFood, outputFoodAmount, stat, objective, nullNut)
				pace -= 100
				for each in upperBoundConst:
					if each > pace:
						stat == "Undefined"
				openUpperBound = [pace for i in range(len(defaultGenupperBound))]
				(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, openUpperBound, opt_maxormin, opt_nut)
				reportTotal(constraints, outputFoodAmount, listFoodObject)
			#print "Open Bounded Solution"
			(outputFood , outputFoodAmount , status ,objective, nullNut) = (outputFoodPre, outputFoodAmountPre, statPre, valobj, nullNut)
		else:
			#print "Open Bounded Solution"
			openUpperBound = [5000 for i in range(len(defaultGenupperBound))]
			(outputFood , outputFoodAmount , status ,objective, nullNut) = linearOptimize(listFoodObject, constraints, defaultGenlowerBound, openUpperBound, opt_maxormin, opt_nut)
			#reportTotal(constraints, outputFoodAmount, listFoodObject)
	

	global full_ext_nutrient
	#Find items that have too much
	#Get total of the food to be compared with upperbound
	totalNut = reportTotal(constraints, outputFoodAmount, listFoodObject)
	
	nutExceed = []
	nutExceedVal = []
	nutExceedStatement = []
	global full_ext_nutrient_unit
	for i in range(len(totalNut)):
		if (totalNut[i]- float(upperBoundConst[i])) >= 1:
			#print full_ext_nutrient[constraints[i]-25], "Upper Bound: ", upperBoundConst[i], "Total recommended", totalNut[i]
			nutExceed.append(constraints[i])
			nutExceedVal.append(totalNut[i])
			upper = (upperBoundConst[i].split('.'))[0]
		
			nutExceedStatement.append("Too Much "+full_ext_nutrient[constraints[i]-25] +" " +str(int(round(totalNut[i])))+"/"+ upper + " "+full_ext_nutrient_unit[constraints[i]-25])
	
	# nested list - inside is a tuple with percent value and the food by decreasing order
	nutExceedWhichFood = []
	for i in range(len(nutExceed)):
		exceedPercent = showExceed(nutExceed[i], nutExceedVal[i], outputFoodAmount, listFoodObject)
		nutExceedWhichFood.append(exceedPercent)
	
	(sumCal, sumNutUnmet, nutRatioMin, nutRatioUnmet) = reportRatio2(constraints, listFoodObject, g.user.nutri[0])
#		givenCal, failedBestFood, nutRatioMin, nutRatioUnmet

	session["sumCal"] = sumCal
	session["sumNutUnmet"] = sumNutUnmet
	session["nutRatioMin"] = nutRatioMin
	session["nutRatioUnmet"] = nutRatioUnmet
	session["opt_maxormin"] = opt_maxormin
	session["opt_nut"] = opt_nut
	session[("chosenNut")] = 0
	
	lackNut = []
	zeroNut = []
	for i in range(len(nutRatioUnmet)):
		#print i
		if sumNutUnmet[i] == 0:
			zeroNut.append("Zero Amount of "+ full_ext_nutrient[nutRatioUnmet[i]-25].split("/")[0])
		else:
			percent = 100*(nutRatioMin[i]-sumNutUnmet[i])/(nutRatioMin[i])
			if percent == 0:
				continue
			lackNut.append("Lacking "+ full_ext_nutrient[nutRatioUnmet[i]-25].split("/")[0]) 
# 				lackNut.append("Lacking about " +"%0.2f" %percent+ "% of Required " + full_ext_nutrient[nutRatioUnmet[i]-25].split("/")[0]) 
	
	nullNut = lackNut+zeroNut
	
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
	
	return render_template("optimize.html",
		outputFood = outputFood,
		outputFoodAmount = outputFoodAmount,
		status = status,
		objective = objective,
		nullNut = nullNut,
		check = check,
		nutExceedStatement = nutExceedStatement,
		nutExceedWhichFood =nutExceedWhichFood,
		userProfile = session['userProfile'])
				
@app.route('/resultSuggest', methods=['GET', 'POST'])
@app.route('/resultSuggest/<int:page>', methods = ['GET', 'POST'])
def resultSuggest(page = 1):
	#get categories for the side
	global mainCategories
	global foodTypes
	
	foodIdsArg = session[g.user.get_id()]
	foodNamesArg = session["foodItem"]
	foodsILike = createFoodsILike(foodIdsArg, foodNamesArg)
	
	if foodIdsArg:
		foodsItemsILike = Food.query.filter(Food.id.in_(foodIdsArg)).all()
	else:
		foodsItemsILike = []
	
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
				indexToDelete = session[g.user.get_id()].index(i)
				session[g.user.get_id()].pop(indexToDelete)
				session["foodItem"].pop(indexToDelete)
		return redirect(url_for('selectFoodFromSuggest', foodIDFromSuggest = "updateAfterRemove"))
		
	
	# Box 1 is all the food types that i like
	# Box 2 - chose same mechanism - therefore categry is better
	# Main cat becomes the nutrietns that are lacking
	
	typesMainTypesILike = []
	for eachFoodID in session[g.user.get_id()]:
		eachFood = Food.query.filter(Food.id==eachFoodID).first()
		typesMainTypesILike.append(eachFood.mainType +' -> '+eachFood.type )
	
	typesMainTypesILike = list(set(typesMainTypesILike))
	
	typesILike = []
	MainTypeILike = []
	for each in typesMainTypesILike:
		each = each.split(' -> ')
		typesILike.append(each[1])
		MainTypeILike.append(each[0])
	
	session["box1CatSuggest"] = typesMainTypesILike

	# To get the chosen type and main type from web
	
	global full_ext_nutrient
	
# 	#print ("chosenType") in session.keys()
	if ("chosenType") in session.keys():
		typeFood = session["chosenType"].split(' -> ')
		MainTypeILike = typeFood[0]
		typesILike = typeFood[1]
		heading2List = session["chosenType"].title()
	else:
		heading2List = "Suggested Food Types"

	sumCal = session["sumCal"] 
	sumNutUnmet = session["sumNutUnmet"] 
	nutRatioMin = session["nutRatioMin"] 
	nutRatioUnmet = session["nutRatioUnmet"] 

	# To get which nutrient to look for to get from session because we want it to stay
	# whenever client click which type of food this nutrient will be selected
	# sample is calcium
	lackingNut = [full_ext_nutrient[i-25].split('/')[0] for i in nutRatioUnmet]
	(info, food) = getInfo()
	#print "Test2: ",nutRatioUnmet, sumNutUnmet, nutRatioMin
	if not nutRatioUnmet:
		titleFindFood = "Your Food Items Are More Balanced"
		return render_template('resultBalanced.html',
		foodsILike = foodsILike,
		heading2List = heading2List,
		box1Head = "Food Types I Like",
		box1Cat = session["box1CatSuggest"],
		titleFindFood = titleFindFood,
		info = info,
		food = food,
		foodNamesArg= foodNamesArg,
		foodsItemsILike= foodsItemsILike)
	
	
	indexRatio = int(session[("chosenNut")])
	ratio = nutRatioMin[indexRatio]
# 	sumNut = sumNutUnmet[indexRatio]
	nutChosen = nutRatioUnmet[indexRatio]
	opt_maxormin =  session["opt_maxormin"]
	opt_nut = session["opt_nut"]
	
	
	looseUpperSodium = 2600.0 #2400
	looseUpperFat = 75.0 #65
	
	#Names of the two nutrients
	currentNutName = full_ext_nutrient[nutChosen-25].split('/')[0]
	objNutName = full_ext_nutrient[opt_nut-25].split('/')[0]
	
	global instrumentAttribute
	global toReduce

	#Find all the types except beverages
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
		
		if nutChosen in toReduce:
			result = result.order_by(asc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)
		else:
			result = result.order_by(desc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)

	else:
		#print typesILike, MainTypeILike
		#print "In my type"
		result = Food.query.filter(Food.type == typesILike).filter(Food.mainType == MainTypeILike).\
					filter(instrumentAttribute[nutChosen]/sumCal>=ratio)
		if result.count() == 0:
			result = Food.query.filter(Food.mainType == MainTypeILike[0]).\
						filter(instrumentAttribute[nutChosen]/sumCal>=ratio)
			if result.count() == 0:
				#result None
				heading2List = "Please See Suggested Food Types. "+heading2List+":"

		if nutChosen in toReduce:
			result = result.order_by(asc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)
		else:
			result = result.order_by(desc(instrumentAttribute[nutChosen]/sumCal)).paginate(page, RESULTS_PER_PAGE, False)
	box2Head = heading2List
	#print "box2Head" , box2Head 
# 	for each in result.items:
		#print each.food, each.type, each.mainType
		#print each.value(nutChosen)
 
 	if nutChosen in toReduce:
		titleFindFood = "Foods Low in "+ currentNutName
	else:
		titleFindFood = "Foods High in "+ currentNutName

	lackingNut = [full_ext_nutrient[i-25].split('/')[0] for i in nutRatioUnmet]
	(info, food) = getInfo()
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
		info= info,
		food = food,
		userProfile = session['userProfile'],
		foodsItemsILike= foodsItemsILike)
	
@app.route('/selectNut/<chosenNut>/')
def selectNut(chosenNut):
	session[("chosenNut")] = chosenNut
	return redirect(url_for('resultSuggest'))
	
@app.route('/selectTypeILike/<chosenType>/')
def selectTypeILike(chosenType):
	if chosenType == "Suggested Food Types":
		if ("chosenType") in session.keys():
			session.pop(("chosenType"))
	else:
		session[("chosenType")] = chosenType
	return redirect(url_for('resultSuggest'))



@app.before_request
def before_request():
    g.user = current_user

    if g.user.is_authenticated() and not g.user.get_id() in session:
    	#print "SESSION NOT IN"
    	session[g.user.get_id()] = [str(each.id) for each in g.user.food]
    	session["foodItem"] = [each.food+ " "+ each.detail+ " (" +  each.source+")" for each in g.user.food]
    	session["foodInfo"] = None
    	session["result"] = ""
 
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
    

@app.route("/profile", methods=["GET", "POST"])
def profile():
	currentUser = g.user
	
	editProfile = Profile(currentUser)
	formVal =  request.form.values()
	valid = 0
	if ("Save Changes" in formVal) and ("unitSystem" in request.form.keys()) and editProfile.is_submitted():
		if editProfile.age.data is not None:
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
					#print "Cal",cal
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
					#print "Cal ",cal
					
		if valid == 0:
			return redirect(url_for('profile'))
		else:
			# Save profile of the user
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
				
			# Get calories value
			
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
		
			# Copy this default into the current's user nutri
			i = 0
			for eachKey in recNut.__table__.columns.keys():
				if i >= 23:
					setattr(currentNutri, eachKey, getattr(recNut, eachKey))
				i += 1
		
			currentNutri.t0Energy_kcal = "0:"+str(int(round(cal)))
			#Adjust upperbound of macro according to calories values
		
			currentNutri.t0Protein_g=  currentNutri.t0Protein_g.replace("ND",str(int(round(cal*int(protup)/400))))
			currentNutri.t0TotalLipidFat_g=currentNutri.t0TotalLipidFat_g.replace(":ND",":"+str(int(round(cal*int(fatup)/900))))
			currentNutri.t0Carbohydrate_ByDifference_g=currentNutri.t0Carbohydrate_ByDifference_g.replace("ND",str(int(round(cal*int(carbup)/400 ))))	
			(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,0)
			db.session.commit()
			
			session['userProfile'] = getUserProfileDisplay(currentUser)
			flash ("My Profile is updated! " +session['userProfile'])
			
	username = "Guest"
	if currentUser.username is not None:
		username = g.user.username

	return render_template("profile.html", username = username, editProfile = editProfile)

@app.route('/', methods = ['GET', 'POST'])
@app.route("/login", methods=["GET", "POST"])
def login():
	# check if user is logged in
	if current_user is not None and current_user.is_authenticated():
		return redirect(url_for('resultSearch'))
	
	# profile form
	profileFull = ProfileFull()
	formVal =  request.form.values()
	valid = 0
	if ("Sign Up" in formVal or "Guest" in formVal) and ("unitSystem" in request.form.keys()) and ("gender" in request.form.keys()):
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
					#print "Cal",cal
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
					#print "Cal ",cal
					
		if valid == 0:
			return redirect(url_for('login'))
		else:
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
				
			# Get calories value
			
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
		
			currentNutri.t0Energy_kcal = "0:"+str(int(round(cal)))
			#Adjust upperbound of macro according to calories values
		
			currentNutri.t0Protein_g=  currentNutri.t0Protein_g.replace("ND",str(int(round(cal*int(protup)/400))))
			currentNutri.t0TotalLipidFat_g=currentNutri.t0TotalLipidFat_g.replace(":ND",":"+str(int(round(cal*int(fatup)/900))))
			currentNutri.t0Carbohydrate_ByDifference_g=currentNutri.t0Carbohydrate_ByDifference_g.replace("ND",str(int(round(cal*int(carbup)/400 ))))	
			(check, nutriField, defaultGenlowerBound, defautGenupperBound) = getKeysBounds(currentNutri,0)
			db.session.commit()
			

			if "Sign Up" in formVal:
				login_user(newUser)
				return redirect(url_for('signup'))
			elif "Guest" in formVal:
				login_user(newUser)
				session['userProfile'] = getUserProfileDisplay(newUser)
				flash("Welcome, Guest!")
				return redirect(request.args.get("next") or url_for("manage"))
			
	formLogin = LoginForm()
	if formLogin.validate_on_submit():
		#print "get login form"
		user = User.query.filter(User.username == formLogin.usernameLog.data).filter(User.password == formLogin.passwordLog.data).first()
		if user is None:
			flash("Wrong Username or Password. Please try again")
			#print "No user"
			return render_template("login.html", formLogin=formLogin, head_1 = "Log In", profileFull= profileFull)
		login_user(user)
		session['userProfile'] = getUserProfileDisplay(g.user)
		#print "logged user"
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("profile"))
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
    return render_template("signup.html", signupform=signupform)

@app.route("/logout")
@login_required
def logout():
	flash("You have logged out. Thank you")
	#print "g_user is :", g.user
	#print "current user is:", current_user
	if (g.user.role == 2):
		session.pop(g.user.get_id(), None)
		db.session.delete(g.user)
		db.session.commit()
	keys = session.keys()
	for each in keys:
		session.pop(each, None)
	logout_user()
	return redirect(url_for('login'))


# TESTING Create dynamic form
def create_form():
	class F(Form):
		pass
	F.submit = SubmitField('username')
	list_nut = ['protein','fat','sugar']
	for name in list_nut:
		setattr(F, name, TextField(name))
	k = F()
	return k	
@app.route('/test', methods=['GET', 'POST'])
def test():
	form = manyButtons()
	form2 = manyButtons()
	a = session.keys()
	#print "currentUser: ", g.user.get_id()
	for each in a:
		session.pop(each)
# 		#print "eachID: ", each , id(session[each])
# 		#print session[each]
# 		#print "\n\n"
	
# 	session.pop(each)
	if request.method == 'POST':
		if form.validate_on_submit() and request.form['submit1'] == u'Submit1':
			#print "Reqest.form1111", request.form
# 			for field in form:
				#print field.label, field.data
			return redirect(url_for('test', form = form, form2=form2))
		elif form2.validate_on_submit():
			#print "Reqest.form2222", request.form2['text']
# 			for field in form2:
				#print field.label, field.data
			return redirect(url_for('test', form = form, form2=form2))
	elif request.method == 'GET':
		
		#print "Form GET"
		return render_template('test.html', form1=form, form2=form2)
	return render_template('test.html', form1=form, form2=form2)
    