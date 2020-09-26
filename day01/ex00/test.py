from book import Book
from recipe import Recipe
import datetime
last_update = datetime.datetime(year=1999,month=10,day=10)
creation_update = datetime.datetime(year=1999,month=10,day=10)
# print(type(last_update))
test = Book("ktab",last_update,creation_update,{})

recipe = Recipe("otman",5,20,["wale"],"","lunch")
test.add_recipe(recipe)

print(test.recipe_list)
# print(test.get_recipe_by_types("lunch"))