import json

class RecipeDatabase:
    def __init__(self, data_file="data/recipes.json"):
        with open(data_file) as f:
            self.recipes = json.load(f)

    def get_matching_recipes(self, ingredients):
        full_matches = []
        partial_matches = []

        for recipe, recipe_ingredients in self.recipes.items():
            matched = [item for item in recipe_ingredients if item in ingredients]
            missing = [item for item in recipe_ingredients if item not in ingredients]

            if not missing:
                full_matches.append(recipe)
            elif matched and len(missing) <= 2:
                partial_matches.append((recipe, missing))

        return full_matches, partial_matches