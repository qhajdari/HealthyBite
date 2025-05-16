import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from utils.db_handler import DatabaseHandler


class RecipeListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthyBite - Lists of Recipes")
        self.db = DatabaseHandler()

        # Listbox for recipes
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        self.listbox.bind('<<ListboxSelect>>', self.show_recipe_details)

        # Panel for recipe details
        self.detail_text = tk.Text(root, width=50, height=20)
        self.detail_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.load_recipes()

    def load_recipes(self):
        self.recipes = self.db.get_all_recipes()
        self.listbox.delete(0, tk.END)
        for recipe in self.recipes:
            self.listbox.insert(tk.END, recipe[1])  #Recipe name

    def show_recipe_details(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            recipe = self.recipes[index]
            details = (
                f"Name: {recipe[1]}\n"
                f"Category: {recipe[2]}\n"
                f"Ingredients: {recipe[3]}\n"
                f"Guidelines:\n{recipe[4]}\n"
                f"Preparation Time: {recipe[5]} min\n"
            )
            self.detail_text.delete("1.0", tk.END)
            self.detail_text.insert(tk.END, details)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeListApp(root)
    root.mainloop()
