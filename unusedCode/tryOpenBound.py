#!flask/bin/python
#constraints = [26, 28, 29, 30, 31, 41, 42, 44, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 62, 64, 67, 69, 80]

#[246554 , 30503 , 148898 , 82265 , 50136 , 180796 , 220669 , 56106 , 117036 , 256457 , 213503 , 178355 , 57882 , 76566 , 184412 , 94037 , 163676 , 54391 , 201864 , 91418 , 206392 , 180127 , 78173]
#[226867 , 168586 , 146941 , 134588 , 150224 , 207908 , 221611 , 184531 , 223875 , 206392 , 204599 , 265355 , 181127 , 21913 , 215782 , 146578 , 111542 , 257333 , 181302 , 104275 , 56980 , 39604 , 113620 ]
constraints = [ 26,28, 29, 30, 31, 41, 42, 44, 46,47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 62, 64, 67, 80]
foodTypes = ['bread', 'bagels', 'biscuit breads', 'bread crumbs', 'breadsticks', 'cinnamon raisin bread', 'cornbread', 'croutons', 'english muffins crumpets', 'focaccia flat pizza breads', 'french italian bread', 'french toast', 'garlic bread toast', 'multigrain bread', 'pita bread', 'rolls buns', 'dinner rolls', 'hamburger buns', 'hot dog buns', 'rye bread', 'sourdough bread', 'toast', 'tortillas tacos wraps', 'wheat bread', 'white bread', 'brownies', 'cakes', 'banana pumpkin breads', 'carrot cakes', 'cheesecakes', 'chocolate cakes', 'coffee cakes', 'cupcakes', 'lemon cakes', 'cookies', 'biscotti', 'chocolate chip cookies', 'ginger cookies', 'girl scout cookies nutrition', 'oatmeal cookies', 'peanut butter cookies', 'sandwich cookies', 'shortbread cookies', 'sugar cookies', 'wafer cookies', 'crackers', 'cheese crackers', 'crispbread crackers', 'graham crackers', 'matzo', 'multigrain crackers', 'oyster crackers', 'rice crackers cakes', 'saltine crackers', 'water crackers', 'wheat crackers', 'doughnuts', 'muffins scones', 'banana muffins', 'blueberry muffins', 'bran muffins', 'chocolate chip muffins', 'corn muffins', 'scones', 'pancakes waffles', 'crepes', 'pastries', 'croissants', 'danish pastries', 'pie pastry crusts', 'sweet buns rolls', 'toaster pastries', 'pies', 'apple pies', 'cherry berry pies', 'cream custard pies', 'meat savory pies', 'pumpkin pies', 'quiches', 'tarts', 'stuffings', 'stuffings', 'baked beans', 'bean dishes', 'black beans', 'chickpeas', 'green beans', 'hummus', 'kidney beans', 'lentils', 'lima beans', 'meat substitutes tvps', 'pinto beans', 'refried beans', 'soybeans', 'tofu tempeh', 'tofu tempeh dishes', 'white beans', 'white beans', 'beef', 'beef cold cuts', 'beef patties', 'ground beef', 'beef dishes', 'beef broccoli', 'beef meatballs', 'beef stroganoff', 'country fried steak', 'hamburgers', 'meatloaf', 'pot roast', 'roast beef', 'roast beef sandwiches', 'salisbury steak', 'steak sandwiches', 'teriyaki beef', 'beef ribs', 'corned beef', 'steak', 'chuck steak', 'flank steak', 'porterhouse', 'sirloin steak', 'sirloin steak', 'alcoholic drinks', 'beer', 'budweiser nutrition', 'coors nutrition', 'lite beer', 'miller brewing nutrition', 'mixers cocktails', 'bloody mary', 'mai tai', 'margarita', 'martini', 'pina colada', 'vodka gin rum whiskey', 'wine', 'carbonated drinks', 'cola', 'coke nutrition', 'pepsi nutrition', 'cream soda', 'ginger ale', 'lemon lime soda', 'mountain dew nutrition', 'orange soda', 'root beer', 'seltzer sparkling club tonic water', 'energy drinks', 'fruit punch', 'hot drinks', 'coffee', 'americano', 'cafe mocha', 'cappuccino', 'caramel macchiato', 'dunkin donuts', 'espresso', 'latte', 'starbucks', 'hot chocolate', 'tea', 'black tea', 'green tea', 'herbal tea', 'lipton nutrition', 'white tea', 'iced coffee', 'iced tea', 'juices', 'milk', 'milk substitutes', 'nutritional drinks', 'protein body building shakes', 'weight loss meal replacement shakes', 'smoothies', 'chocolate smoothies', 'fruit smoothies', 'vanilla smoothies', 'sports drinks', 'gatorade nutrition', 'powerade nutrition', 'water', 'coconut water', 'yogurt drinks', 'yogurt drinks', 'cold cereals', 'apple jacks nutrition', 'bran flakes', 'cheerios nutrition', 'corn flakes', 'fiber one nutrition', 'frosted flakes nutrition', 'froot loops nutrition', 'golden grahams nutrition', 'granola muesli', 'kashi nutrition', 'raisin bran nutrition', 'rice cereal', 'rice krispies nutrition', 'special k nutrition', 'wheat cereal', 'wheaties nutrition', 'hot cereals', 'cream wheat', 'grits', 'oats oatmeal', 'wheat germ bran', 'wheat germ bran', 'breakfast cereals', 'flour', 'corn meal', 'rice flour', 'soy flour', 'wheat flour', 'grains', 'barley', 'buckwheat kasha', 'bulgur', 'polenta', 'quinoa', 'noodles', 'egg noodles', 'ramen noodles', 'pasta', 'angel hair', 'couscous', 'fettucini', 'gnocchi', 'lasagna', 'linguini', 'macaroni', 'penne', 'ravioli', 'rigatoni', 'rotini', 'spaghetti', 'tortellini', 'vermicelli', 'whole wheat pasta', 'pasta dishes', 'macaroni beef', 'macaroni cheese', 'pasta casserole', 'spaghetti meatballs', 'rice', 'basmati rice', 'brown rice', 'white rice', 'wild rice', 'yellow rice', 'rice dishes', 'chicken rice', 'fried rice', 'rice beans', 'rice pilaf', 'risotto', 'risotto', 'butter', 'cheese', 'american cheese', 'blue cheese', 'brie cheese', 'cheddar cheese', 'colby cheese', 'colby jack cheese', 'cottage cheese', 'cream cheese', 'chive onion cream cheese', 'honey nut cream cheese', 'light cream cheese', 'raisin cream cheese', 'strawberry cream cheese', 'vegetable cream cheese', 'feta cheese', 'goat cheese', 'gouda cheese', 'havarti cheese', 'jack cheese', 'mozzarella cheese', 'muenster cheese', 'parmesan cheese', 'provolone cheese', 'ricotta cheese', 'string cheese', 'swiss cheese', 'cream', 'creamer', 'fat free cream', 'half', 'sour cream', 'whipped cream', 'eggs', 'egg whites substitutes', 'fried eggs', 'hard boiled eggs', 'omelets', 'poached eggs', 'scrambled eggs', 'chocolate flavored milk', 'condensed evaporated milk', 'low fat milk percent', 'milk shakes', 'reduced fat milk percent', 'skim milk fat free', 'whole milk', 'yogurt', 'danone nutrition', 'flavored yogurt', 'apple yogurt', 'banana yogurt', 'blueberry yogurt', 'coffee yogurt', 'lemon lime yogurt', 'peach yogurt', 'strawberry yogurt', 'vanilla yogurt', 'frozen yogurt', 'greek yogurt', 'light yogurt', 'fat yogurt', 'stonyfield farm nutrition', 'yoplait nutrition', 'yoplait nutrition', 'african food', 'ethiopian food', 'moroccan food', 'south african food', 'australasian food', 'australian food', 'new zealand food', 'east asian food', 'chinese food', 'japanese food', 'korean food', 'thai food', 'vietnamese food', 'european food', 'austrian food', 'british food', 'french food', 'german food', 'greek food', 'irish food', 'italian food', 'polish food', 'portuguese food', 'russian food', 'scandinavian food', 'spanish food', 'latin food', 'brazilian food', 'mexican food', 'middle eastern food', 'arabic food', 'kosher israeli', 'turkish food', 'north american food', 'american food', 'canadian food', 'caribbean jamaican', 'south asian food', 'afghani food', 'indian food', 'pakistani food', 'pakistani food', 'burger king nutrition', 'burger sandwiches', 'cheeseburgers', 'chicken burgers', 'veggie burgers', 'corn dogs', 'fast food side dishes', 'french fries potato wedges', 'hash browns', 'onion rings', 'fried chicken', 'hot dogs', 'mcdonalds nutrition', 'pizza calzones', 'calzones', 'cheese pizza', 'hawaiian pizza', 'pepperoni pizza', 'sausage pizza', 'veggie pizza', 'quesadillas', 'roast chicken', 'salads', 'sandwiches wraps', 'blt sandwiches', 'breakfast sandwiches', 'chicken sandwiches', 'club sandwiches', 'cold cut sandwiches', 'fish sandwiches', 'grilled cheese sandwiches', 'ham sandwiches', 'italian sandwiches', 'meatball sandwiches', 'pork sandwiches', 'sausage sandwiches', 'tuna sandwiches melts', 'turkey sandwiches', 'veggie sandwiches', 'sausages', 'spring rolls', 'subway nutrition', 'tex mex food', 'burritos', 'chili', 'enchiladas', 'fajitas', 'nachos', 'tacos', 'tamales', 'tamales', 'fats lard shortening', 'margarine', 'oils', 'canola oil', 'cooking spray', 'corn oil', 'fish oil', 'grape seed oil', 'olive oil', 'sesame oil', 'vegetable oil', 'salad dressings', 'blue cheese dressing', 'caesar dressing', 'french dressing', 'greek dressing', 'honey mustard dressing', 'italian dressing', 'mayonnaise aioli', 'onion dressing', 'poppyseed dressing', 'ranch dressing', 'sesame dressing', 'thousand island dressing', 'vinegar vinaigrette dressing', 'vegetable oil spread', 'vegetable oil spread', 'clams', 'cod', 'crab', 'fish dishes', 'fish chips', 'fish sticks cakes', 'gefilte fish', 'manhattan clam chowder', 'new england clam chowder', 'whitefish pike', 'flounder', 'haddock', 'halibut', 'herring', 'lobster', 'oysters', 'pollocks', 'salmon', 'sardines', 'scallops', 'shrimp', 'sole', 'sushi sashimi', 'california rolls', 'sushi rolls', 'tilapia', 'tuna', 'tuna', 'fruit', 'apples', 'apricots', 'avocados', 'bananas', 'blueberries', 'cherries', 'coconuts', 'cranberries', 'grapefruits', 'grapes', 'mangos', 'melons cantaloupe', 'olives', 'oranges tangerines mandarins', 'peaches', 'pears', 'pineapples', 'plums', 'pumpkins', 'raisins', 'raspberries', 'strawberries', 'fruit salads', 'apple juice', 'cranberry juice', 'grape juice', 'grapefruit juice', 'lemonade limeade', 'orange juice', 'pineapple juice', 'tomato vegetable juice', 'tomato vegetable juice', 'lamb', 'lamb dishes', 'veal', 'veal dishes', 'veal dishes', 'baby food', 'baby food cereal', 'baby food dinners', 'baby food juice', 'baby food meats', 'baby food snacks', 'fruit baby food', 'infant formula', 'vegetable baby food', 'chicken dishes', 'egg dishes', 'ethnic foods', 'fast foods', 'pork dishes', 'potato dishes', 'turkey dishes', 'vegetable dishes', 'vegetable dishes', 'almond other nut butters', 'almonds', 'cashews', 'chestnuts', 'flaxseeds', 'hazelnuts', 'macadamia nuts', 'nut trail mixes', 'peanut butter', 'peanuts', 'pecans', 'pine nuts', 'pistachios', 'pumpkin seeds', 'sesame seeds', 'soy nuts', 'sunflower seeds', 'walnuts', 'walnuts', 'bacon', 'ham', 'ham cold cuts', 'pork chops', 'pork sausage', 'pulled pork', 'pork loin', 'pork ribs', 'pork roast', 'pork shoulder', 'pork tenderloin', 'pork tenderloin', 'chicken', 'chicken breasts', 'chicken cold cuts', 'chicken drumsticks', 'chicken patties', 'chicken thighs', 'chicken wings', 'bbq chicken', 'chicken dumplings', 'chicken nuggets tenders', 'chicken parmesan', 'chicken salad', 'chicken sausage', 'chicken soups', 'chicken tikka masala', 'fried chicken', 'grilled chicken', 'teriyaki chicken', 'duck', 'turkey', 'ground turkey', 'turkey bacon', 'turkey breast', 'turkey cold cuts', 'turkey legs', 'turkey patties', 'turkey chili', 'turkey sausage', 'turkey soups', 'turkey soups', 'lunch meats', 'bologna cold cuts', 'pastrami', 'salami pepperoni', 'beef sausage', 'bratwurst', 'chorizo', 'italian sausage', 'polish sausage', 'jerky snack sticks', 'jerky snack sticks', 'candy', 'cheese puffs', 'chewing gum mints', 'chips', 'banana plantain chips', 'corn tortilla chips', 'multigrain chips', 'pita bagel chips', 'potato chips', 'cracker sandwiches', 'fruit snacks', 'popcorn', 'pork skins rinds', 'pretzels', 'filled pretzels', 'flavored pretzels', 'pretzel sticks rods', 'soft pretzels', 'puddings', 'snack bars', 'cereal bars', 'energy protein bars', 'fruit nut bars', 'granola bars', 'meal replacement bars', 'nutrition bars', 'oatmeal raisin bars', 'puffed rice bars', 'trail mix bars', 'snack mixes', 'snack mixes', 'beef chili', 'condiments', 'cocktail sauce', 'garlic sauce', 'hot sauce chipotle', 'ketchup', 'mustard', 'relish', 'soy sauce', 'steak sauce', 'sugars syrups', 'tartar sauce', 'dips spreads', 'bruschetta', 'cheese dip', 'chutney', 'french onion dip', 'guacamole', 'pate', 'peanut sauce', 'salsa', 'spinach dip', 'tapenade', 'gravy', 'chicken gravy', 'mushroom gravy', 'turkey gravy', 'sauces', 'barbecue sauce', 'curry sauce', 'marinades', 'pasta pizza sauces', 'alfredo sauce', 'marinara tomato sauce', 'pesto sauce', 'vodka sauce', 'sweet sour sauce', 'teriyaki sauce', 'soups', 'beef soups', 'beef barley soup', 'beef noodle soup', 'bisques', 'broth stock bouillon', 'beef broth stock bouillon', 'chicken broth stock bouillon', 'vegetable broth bouillon', 'cheese soups', 'chicken noodle soup', 'chicken rice soup', 'chowders', 'corn chowder', 'cream soups', 'cream broccoli soup', 'cream chicken soup', 'cream mushroom soup', 'cream potato soup', 'cream tomato soup', 'minestrone soup', 'tortilla soup', 'vegetable soups', 'bean soup', 'butternut squash pumpkin soup', 'lentil soup', 'mushroom soup', 'onion soup', 'pea soup', 'potato soup', 'tomato soup', 'wedding soup', 'stews', 'beef stew', 'gumbo', 'gumbo', 'baking soda', 'chili powder', 'coating mixes', 'curry', 'food coloring', 'garlic', 'ginger', 'onion', 'oregano', 'paprika', 'parsley', 'pepper', 'salt', 'seasoning mix', 'steak seasoning', 'vitamins', 'vitamins', 'apple butter', 'caramel candy', 'chocolate candy', 'chocolate candy bars', 'chocolate chips morsels', 'chocolate covered candy', 'dark chocolate', 'e guittard nutrition', 'godiva nutrition', 'hersheys nutrition', 'lindt nutrition', 'milk chocolate', 'gummy snacks', 'hard candy', 'licorice', 'lollipops suckers', 'marshmallows', 'seasonal candy', 'candy canes christmas', 'easter eggs candy', 'valentines candy', 'sour candy', 'sugar free candy', 'dessert toppings', 'sauces', 'sprinkles', 'toppings', 'whipped toppings', 'desserts', 'crisps cobblers', 'fruit desserts compotes', 'gelatin desserts', 'chocolate pudding', 'rice pudding', 'vanilla pudding', 'soft serve frozen yogurt', 'tcby nutrition', 'ice cream sorbet', 'breyers nutrition', 'chocolate ice cream', 'coffee ice cream', 'cookies n cream ice', 'edys nutrition', 'fat free ice cream', 'ice cream bars', 'ice cream cakes', 'ice cream sandwiches', 'ice cream sundaes', 'low fat ice cream', 'parfaits', 'sherbet sorbet', 'strawberry ice cream', 'sugar free ice cream', 'vanilla ice cream', 'icings frostings', 'chocolate', 'decorating icing', 'icing decorations', 'vanilla', 'jellies jams preserves spreads', 'chocolate spreads', 'fruit jams jellies', 'apple jams jellies', 'grape jams jellies', 'orange jams jellies', 'strawberry jams jellies', 'marmalade', 'pie cake fillings', 'caramel syrup', 'chocolate syrup', 'flavored syrups', 'honey', 'maple syrup', 'pancake syrup', 'lite syrup', 'sugar free syrup', 'sugars sweeteners', 'artificial sweeteners', 'brown sugar', 'brown sugar', 'beets', 'cabbage', 'fruit vegetables', 'chili peppers', 'corn', 'cucumber', 'eggplant', 'peas', 'pumpkin squash', 'sweet peppers', 'tomatoes', 'zucchini', 'inflorescence vegetables', 'artichokes', 'broccoli', 'cauliflower', 'sprouts', 'leafy vegetables', 'collards', 'kale', 'lettuce', 'spinach', 'mixed vegetables', 'mushrooms', 'pickles pickled vegetables', 'root vegetables', 'carrots', 'garlic', 'onions', 'potatoes yams', 'au gratin potatoes', 'baked potato', 'mashed potatoes', 'scalloped potatoes', 'potato salad', 'radishes', 'turnips', 'souffle', 'stem vegetables', 'asparagus', 'celery', 'caesar salad', 'coleslaw', 'garden salad', 'stir fried vegetables', 'vegetable casseroles']

from random import randint, choice
from app.models import Nutri, Food

def reportTotal(constraints, outputFoodAmount, foodItems):
	
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
	
	for i in range(len(constraints)):
		print full_ext_nutrient[constraints[i]-25], TotalNut[i]


def linearOptimize(listFoodObject,constraints, constraintsGivenmin, constraintsGivenmax, opt_maxormin, opt_nut):
	
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
	
	print "Food Nutrients: "
	print foodNut
	print "type: ", type(foodNut)

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
	
	for i in listFood:
		prob += (food_vars[i]) <= 30
	#for i in listFood:
	#	prob += food_vars[i] >= 0.3

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
		#print "each in getkeys", each
		each = each.split(":")
		defaultGenlowerBound.append(each[0])
		defautGenupperBound.append(each[1])
		if override:
			if len(each) >= 3:
				check.append(int(each[2]))
			else:
				print "override when the check is not appended each nutri value eg. 0:ND:??"
		else:
			if (each[0] == "0" and each[1] == "ND"):
				check.append(0)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":0")
			else:
				check.append(1)
				setattr(nutriObject, nutriField[i], str(each[0])+":"+str(each[1])+":1")
			#print "In setting", nutriField[i], getattr(nutriObject, nutriField[i])
		i += 1

# 	print "In f(getKeybounds) end: "
# 	for eachkey in nutriObject.__table__.columns.keys():
# 		nutriField.append(eachkey)
#		print eachkey, getattr(nutriObject, eachkey)

	
	return 	check, nutriField, defaultGenlowerBound, defautGenupperBound

def reportRatio2(constraints, foodItems, nutri):
	nutRatioUnmet = []
	nutRatioMin = []
	nullNut = []
	failedBestFood = []

	givenCal = float(nutri.t0Energy_kcal.split(":")[1])
	bestFoods = []
	bestFoodsVals = []
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
	
	sumCal = [each.value(26) for each in bestFoods]
	sumCal = sum(sumCal)

	for i in range(len(constraints)):
		eachCon = constraints[i]
		bestFoodVal = bestFoodsVals[i]
		nutRatio = bestFoodVal/givenCal
		minRatio= nutri.nutCalRatio(eachCon)
		if nutRatio <= minRatio:
			nutRatioUnmet.append(eachCon)
			nutRatioMin.append(minRatio)
			failedBestFood.append(nutRatio)
			print eachCon, nutRatio, "<=", minRatio

	print "Report Ratio"
	for i in range(len(nutRatioUnmet)):
		print nutRatioUnmet[i], full_ext_nutrient[nutRatioUnmet[i]-25],  "minRatios: ", nutRatioMin[i], "BestFood: ", failedBestFood[i]
	
	return givenCal, failedBestFood, nutRatioMin, nutRatioUnmet
			
# age = randint(2,100)
# age = getageGroup(age)
# gender = randint(0,1)
# if gender = 0:
# 	gender = "Males"
# 	condition = "None"
# else:
# 	gender = "Females"
# 	condition = choice(["Pregnancy","Lactation"])
# weight = randint(110,220)
# heightFeet = randint(4,6)
# heightInch = randint(1,6)
# g.user.activity = float(profileForm.activity.data)

stat = "status"
while stat != "Undefined":
	calUpper = randint(1800,3000)
	allNutris = Nutri.query.filter(Nutri.type==0).all()
	currentNutri = choice(allNutris)
	currentNutri.t0Energy_kcal = "0:"+str(calUpper)
	protup = currentNutri.protein_g
	fatup = currentNutri.fat_g
	carbup = currentNutri.carb_g
	if protup is None:
		protup = 20
		fatup = 40
		carbup = 60

	currentNutri.t0Protein_g=  currentNutri.t0Protein_g.replace("ND",str(calUpper*int(protup)/400))
	currentNutri.t0TotalLipidFat_g=currentNutri.t0TotalLipidFat_g.replace(":ND",":"+str(calUpper*int(fatup)/900))
	currentNutri.t0Carbohydrate_ByDifference_g=currentNutri.t0Carbohydrate_ByDifference_g.replace("ND",str(calUpper*int(carbup)/400))

	print "Got the sample Nutri"

	nutRatioMin = []
	for eachCon in constraints:
		nutRatioMin.append(currentNutri.nutCalRatio(eachCon))

	instrumentAttribute = [Food.mainType,Food.type,Food.food,Food.detail,Food.source,Food.amount,Food.unit,Food.gram,Food.cal_kcal,Food.calFat_kcal,Food.fat_g,Food.fat_pct,Food.saturFat_g,Food.polyunFat_g,Food.monounFat_g,Food.chol_mg,Food.sodium_mg,Food.carb_g,Food.fiber_g,Food.sugar_g,Food.protein_g,Food.vitA_pct,Food.vitC_pct,Food.calcium_pct,Food.iron_pct,Food.t0Water_g,Food.t0Energy_kcal,Food.t0Energy_kj,Food.t0Protein_g,Food.t0TotalLipidFat_g,Food.t0Carbohydrate_ByDifference_g,Food.t0Fiber_TotalDietary_g,Food.t0Sugars_Total_g,Food.t0Sucrose_g,Food.t0GlucoseDextrose_g,Food.t0Fructose_g,Food.t0Lactose_g,Food.t0Maltose_g,Food.t0Galactose_g,Food.t0Starch_g,Food.t0AdjustedProtein_g,Food.t1Calcium_Ca_mg,Food.t1Iron_Fe_mg,Food.t1Magnesium_Mg_mg,Food.t1Phosphorus_P_mg,Food.t1Potassium_K_mg,Food.t1Sodium_Na_mg,Food.t1Zinc_Zn_mg,Food.t1Copper_Cu_mg,Food.t1Manganese_Mn_mg,Food.t1Selenium_Se_mcg,Food.t1Fluoride_F_mcg,Food.t2VitaminC_TotalAscorbicAcid_mg,Food.t2Thiamin_mg,Food.t2Riboflavin_mg,Food.t2Niacin_mg,Food.t2PantothenicAcid_mg,Food.t2VitaminB_6_mg,Food.t2Folate_Total_mcg,Food.t2FolicAcid_mcg,Food.t2Folate_Food_mcg,Food.t2Folate_DFE_mcg_DFE,Food.t2Choline_Total_mg,Food.t2Betaine_mg,Food.t2VitaminB_12_mcg,Food.t2VitaminB_12_Added_mcg,Food.t2VitaminA_IU_IU,Food.t2VitaminA_RAE_mcg_RAE,Food.t2Retinol_mcg,Food.t2VitaminE_alpha_tocopherol__mg,Food.t2VitaminE_Added_mg,Food.t2Tocopherol_Beta_mg,Food.t2Tocopherol_Gamma_mg,Food.t2Tocopherol_Delta_mg,Food.t2VitaminKPhylloquinone_mcg,Food.t2Carotene_Beta_mcg,Food.t2Carotene_Alpha_mcg,Food.t2Cryptoxanthin_Beta_mcg,Food.t2Lycopene_mcg,Food.t2Lutein_Zeaxanthin_mcg,Food.t2VitaminD_IU,Food.t3Stigmasterol_mg,Food.t3Phytosterols_mg,Food.t3Beta_sitosterol_mg,Food.t3Campesterol_mg,Food.t3Cholesterol_mg,Food.t3FattyAcids_TotalMonounsaturated_g,Food.t3FattyAcids_TotalPolyunsaturated_g,Food.t3FattyAcids_TotalSaturated_g,Food.t3FattyAcids_TotalTrans_monoenoic_g,Food.t3FattyAcids_TotalTrans_polyenoic_g,Food.t3FattyAcids_TotalTrans_g,Food.t3MonounsaturatedFats14_1_g,Food.t3MonounsaturatedFats15_1_g,Food.t3MonounsaturatedFats16_1C_g,Food.t3MonounsaturatedFats16_1T_g,Food.t3MonounsaturatedFats16_1Undifferentiated_g,Food.t3MonounsaturatedFats17_1_g,Food.t3MonounsaturatedFats18_1C_g,Food.t3MonounsaturatedFats18_1T_g,Food.t3MonounsaturatedFats18_1Undifferentiated_g,Food.t3MonounsaturatedFats20_1_g,Food.t3MonounsaturatedFats22_1C_g,Food.t3MonounsaturatedFats22_1T_g,Food.t3MonounsaturatedFats22_1Undifferentiated_g,Food.t3MonounsaturatedFats24_1C_g,Food.t3PolyunsaturatedFats18_2CLAs_g,Food.t3PolyunsaturatedFats18_2I_g,Food.t3PolyunsaturatedFats18_2N_6C_c_g,Food.t3PolyunsaturatedFats18_2T_t_g,Food.t3PolyunsaturatedFats18_2TNotFurtherDefined_g,Food.t3PolyunsaturatedFats18_2Undifferentiated_g,Food.t3PolyunsaturatedFats18_3N_3C_c_c_g,Food.t3PolyunsaturatedFats18_3N_6C_c_c_g,Food.t3PolyunsaturatedFats18_3Undifferentiated_g,Food.t3PolyunsaturatedFats18_3i_g,Food.t3PolyunsaturatedFats18_4_g,Food.t3PolyunsaturatedFats20_2N_6C_c_g,Food.t3PolyunsaturatedFats20_3N_3_g,Food.t3PolyunsaturatedFats20_3N_6_g,Food.t3PolyunsaturatedFats20_3Undifferentiated_g,Food.t3PolyunsaturatedFats20_4N_6_g,Food.t3PolyunsaturatedFats20_4Undifferentiated_g,Food.t3PolyunsaturatedFats20_5N_3_g,Food.t3PolyunsaturatedFats21_5_g,Food.t3PolyunsaturatedFats22_4_g,Food.t3PolyunsaturatedFats22_5N_3_g,Food.t3PolyunsaturatedFats22_6N_3_g,Food.t3SaturatedFats10_0_g,Food.t3SaturatedFats12_0_g,Food.t3SaturatedFats13_0_g,Food.t3SaturatedFats14_0_g,Food.t3SaturatedFats15_0_g,Food.t3SaturatedFats16_0_g,Food.t3SaturatedFats17_0_g,Food.t3SaturatedFats18_0_g,Food.t3SaturatedFats20_0_g,Food.t3SaturatedFats22_0_g,Food.t3SaturatedFats24_0_g,Food.t3SaturatedFats4_0_g,Food.t3SaturatedFats6_0_g,Food.t3SaturatedFats8_0_g,Food.t4Alanine_g,Food.t4Arginine_g,Food.t4AsparticAcid_g,Food.t4Cystine_g,Food.t4GlutamicAcid_g,Food.t4Glycine_g,Food.t4Histidine_g,Food.t4Hydroxyproline_g,Food.t4Isoleucine_g,Food.t4Leucine_g,Food.t4Lysine_g,Food.t4Methionine_g,Food.t4Phenylalanine_g,Food.t4Proline_g,Food.t4Serine_g,Food.t4Threonine_g,Food.t4Tryptophan_g,Food.t4Tyrosine_g,Food.t4Valine_g,Food.t5Ash_g,Food.t5Alcohol_Ethyl_g,Food.t5Caffeine_mg,Food.t5Theobromine_mg]

	foodID = [171736 , 94657 , 164947 , 180796 , 46922 , 111670 , 37039 , 62948 , 198657 , 53070 , 180899 , 111400 , 112552 , 78970 , 24575 , 79938 , 180625 , 29700 , 88054 , 260211 , 123058 , 111231 , 229953 ]
	foodID2=[246554 , 30503 , 148898 , 82265 , 50136 , 180796 , 220669 , 56106 , 117036 , 256457 , 213503 , 178355 , 57882 , 76566 , 184412 , 94037 , 163676 , 54391 , 201864 , 91418 , 206392 , 180127 , 78173]
	foodID3=[226867 , 168586 , 146941 , 134588 , 150224 , 207908 , 221611 , 184531 , 223875 , 206392 , 204599 , 265355 , 181127 , 21913 , 215782 , 146578 , 111542 , 257333 , 181302 , 104275 , 56980 , 39604 , 113620 ]

	foodTest = []
# 	for i in range(len(constraints)):
# 		print i,
# 		iNut = constraints[i]
# 		minRatio = nutRatioMin[i]
# 		print iNut, minRatio
# 		while True:
# 			print "here"
# 			query = Food.query.filter(Food.type==choice(foodTypes)).filter(instrumentAttribute[iNut]/calUpper>minRatio).all()
# 			if query:
# 				break
# 		ratio = 5
# 		while ratio > 4:
# 			food = choice(query)
# 			ratio = (food.value(iNut))/calUpper
# 		foodTest.append(food)
# 	for i in range(len(foodTest)):
# 		print foodTest[i].food, foodTest[i].value(constraints[i])/(foodTest[i].t0Energy_kcal+1), "Min Ratio is: ", nutRatioMin[i]
# 
# 	for i in range(len(foodTest)):
# 		print foodTest[i].id, ",",

	for i in foodID3:
		foodTest.append(Food.query.filter(Food.id==i).first())
		
	print "Nutri ID:", currentNutri.id

	(check, nutriField, defaultGenlowerBound, defautGenupperBound)= getKeysBounds(currentNutri,0)


	(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimize(foodTest,constraints, defaultGenlowerBound, defautGenupperBound, 1, 41)
	reportTotal(constraints, outputFoodAmount, foodTest)


length = len(defaultGenlowerBound)
if stat == "Undefined":
	print "LEAVE BOUND OPEN \n\n\n"
	stat = "Optimal"
	pace = 5000
	while stat == "Optimal":
		pace -= 100
		defautGenupperBound = [pace for i in range(length)]
# 		defautGenupperBound = ["ND" for i in range(len(defautGenupperBound))]
		(outputFood, outputFoodAmount, stat, valobj, nullNut) = linearOptimize(foodTest,constraints, defaultGenlowerBound, defautGenupperBound, 1, 41)
		reportTotal(constraints, outputFoodAmount, foodTest)



# i = 0	 
# for eachKey in currentNutri.__table__.columns.keys():
# 	print i, eachKey, getattr(currentNutri,eachKey)
# 	i+=1
# 
# print "Cal", calUpper
	
# Getting Random age to generate case / don't have to wrry about conditions of women, if nutri is not find then we can skp

# Getting Random food that satisfy all the constraints minimum constraints




# Getting Cal values

# Linear Optimize / and if not then all all upper bounds are open

