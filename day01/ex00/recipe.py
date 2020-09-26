

class Recipe(object):
	

	def __init__(self, name, cooking_lvl, cooking_time,
	ingredients, descriptio, recipe_type):
		# try:
			# if type(name) == type("") and
				# type(cooking_time) == type(1):
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.recipe_type = recipe_type
		# except expression as identifier:
		# 	pass
	def __str__(self):
	 txt = "this is my class"
	 return txt
	