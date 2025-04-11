"""
ProductDatabase loads and retrieves product locations from a JSON file.
"""

import json

class ProductDatabase:
    # Load product locations from a JSON file
    def __init__(self, data_file="data/products.json"):
        # Dictionary to store product locations
        with open(data_file) as f:
            self.products = json.load(f)

    # Retrieve the location of a product by its name
    def get_product_location(self, product_name):
        # Normalize the product name to lowercase for consistent lookup
        return self.products.get(product_name.lower(), "Product not found.")