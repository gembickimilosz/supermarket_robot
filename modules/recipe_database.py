import json

class RecipeDatabase:
    def __init__(self, data_file="data/recipes.json"):
        with open(data_file) as f:
            self.recipes = json.load(f)

    def get_matching_recipes(self, ingredients):
        matches = []
        for recipe, recipe_ingredients in self.recipes.items():
            if all(ingredient in ingredients for ingredient in recipe_ingredients):
                matches.append(recipe)
        return matches