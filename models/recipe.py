class Recipe:
    def __init__(self, name, category, ingredients, instructions, prep_time):
        self.name = name
        self.category = category
        self.ingredients = ingredients  # list of strings
        self.instructions = instructions
        self.prep_time = prep_time  # in minutes

    def get_ingredient_list(self):
        return ", ".join(self.ingredients)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.prep_time} min\nIngredients: {self.get_ingredient_list()}"
