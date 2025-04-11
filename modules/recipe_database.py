"""
RecipeDatabase loads recipes and finds matches based on user-provided ingredients.
"""

import json

class RecipeDatabase:
    # Load recipes from a JSON file
    def __init__(self, data_file="data/recipes.json"):
        # Dictionary to store recipes and their ingredients
        with open(data_file) as f:
            self.recipes = json.load(f)

    # Find recipes that match the provided ingredients
    def get_matching_recipes(self, ingredients):
        full_matches = []
        partial_matches = []


        for recipe, recipe_ingredients in self.recipes.items():
            # Normalize the recipe ingredients for consistent comparison
            matched = [item for item in recipe_ingredients if item in ingredients]
            missing = [item for item in recipe_ingredients if item not in ingredients]

            # Check if the recipe is fully matched or partially matched
            if not missing:
                full_matches.append(recipe)
            elif matched and len(missing) <= 2:
                partial_matches.append((recipe, missing))

        # If the recipe is not matched at all, we skip it
        return full_matches, partial_matches