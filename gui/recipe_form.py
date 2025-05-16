import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from models.recipe import Recipe
from utils.db_handler import DatabaseHandler

def submit_recipe():
    name = entry_name.get()
    category = entry_category.get()
    ingredients = entry_ingredients.get()
    instructions = entry_instructions.get("1.0", tk.END)
    prep_time = entry_prep_time.get()

    if not name or not ingredients or not instructions or not prep_time:
        messagebox.showwarning("Error", "Please fulfill all fields!")
        return

    try:
        prep_time = int(prep_time)
        recipe = Recipe(name, category, ingredients.split(','), instructions.strip(), prep_time)
        db = DatabaseHandler()
        db.insert_recipe(recipe.name, recipe.category, recipe.get_ingredient_list(), recipe.instructions, recipe.prep_time)
        messagebox.showinfo("Success", "Recipe added succesfuly!")
        clear_fields()
    except ValueError:
        messagebox.showerror("Error", "Prep time should be number!")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_ingredients.delete(0, tk.END)
    entry_instructions.delete("1.0", tk.END)
    entry_prep_time.delete(0, tk.END)

# UI
window = tk.Tk()
window.title("Add Recipe")
window.geometry("400x400")

tk.Label(window, text="Recipe Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Category (opsional):").pack()
entry_category = tk.Entry(window)
entry_category.pack()

tk.Label(window, text=" Ingredients (with coma):").pack()
entry_ingredients = tk.Entry(window)
entry_ingredients.pack()

tk.Label(window, text="Guidlines:").pack()
entry_instructions = tk.Text(window, height=5)
entry_instructions.pack()

tk.Label(window, text="Prep time (min):").pack()
entry_prep_time = tk.Entry(window)
entry_prep_time.pack()

tk.Button(window, text="Add recipe", command=submit_recipe).pack(pady=10)

window.mainloop()
