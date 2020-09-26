import datetime
import sys

class mydict(dict):
	def __init__(self):
		self["starter"] = ""
		self["lunch"] = ""
		self["dessert"] = ""

class Book(object):
	

	def __init__(self, name, last_update,
	creation_update, recipe_list):
		try:
			if	(isinstance(name, str) and
				isinstance(last_update,datetime.datetime) and
				isinstance(creation_update, datetime.datetime) and
				isinstance(recipe_list, dict)):
					self.name = name
					self.last_update = last_update
					self.creation_update = creation_update
					self.recipe_list = recipe_list
			else:
				raise TypeError
		except:
			print("type Error",file=sys.stderr)
	def __str__(self):
	 txt = "this is my class"
	 return txt
	def get_recipe_by_name(self, name):
		return self.recipe_list[name]
	def get_recipe_by_types(self, recipe_type):
		return self.recipe_list[recipe_type]
	def add_recipe(self, recipe):
		self.recipe_list[recipe.name] = recipe