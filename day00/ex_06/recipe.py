import sys

# sandwitch = {}
# cake = {}
# salad = {}
def create_dict(ingredients,meal,prep_time):
	return {"ingredients": ingredients,
			"meal": meal,
			"prep_time": prep_time}
coockbook = {	"sandwitch": create_dict(1,2,3),
				"cake":create_dict(1,2,3),
				"salad":create_dict(1,2,3)}

# def print_keys(dictionary):
# 	for key,_ in coockbook[dictionary].items():
# 		print(key)
def del_recipe(dictionary):
	del coockbook[dictionary]
def add_recipe(recipe,ingredients,meal,prep_time):
	coockbook[recipe] = create_dict(ingredients,meal,prep_time)
# print_keys("sandwitch")
del_recipe("sandwitch")
add_recipe("halwa",1,2,3)
for key,_ in coockbook.items():
	print(key)