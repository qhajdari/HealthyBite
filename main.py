from models.recipe import Recipe
from utils.db_handler import DatabaseHandler

db = DatabaseHandler()
recipes = db.get_all_recipes()

for recipe in recipes:
    print(f"Name: {recipe[1]}")
    print(f"Category: {recipe[2]}")
    print(f"Ingredients: {recipe[3]}")
    print(f"Guidlines: {recipe[4]}")
    print(f"Preparation Time: {recipe[5]} min")
    print("-" * 30)


