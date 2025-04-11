from modules.recipe_database import RecipeDatabase

recipes = RecipeDatabase("data/recipes.json")

# Exact match for recipe
full, partial = recipes.get_matching_recipes(["chicken", "rice", "egg"])
assert "Chicken Fried Rice" in full

# Partial match
_, partial = recipes.get_matching_recipes(["chicken"])
assert any("Chicken" in recipe for recipe, _ in partial)

# No match
full, partial = recipes.get_matching_recipes(["bubblegum"])
assert not full and not partial