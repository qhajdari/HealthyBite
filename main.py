from models.recipe import Recipe
from utils.db_handler import DatabaseHandler

# Create a new recipe
r = Recipe("Avocado Salad", "VEGAN", ["Avocado", "Lemon", "Salt"], "Mix all and serve fresh", 10)

# Insert the recipe into the database
db = DatabaseHandler()
db.insert_recipe(r.name, r.category, r.get_ingredient_list(), r.instructions, r.prep_time)

# Print all recipes from the database
for row in db.get_all_recipes():
    print(row)
