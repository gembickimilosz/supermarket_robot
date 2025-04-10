"""
ProductDatabase loads and retrieves product locations from a JSON file.
"""

import json

class ProductDatabase:
    def __init__(self, data_file="data/products.json"):
        with open(data_file) as f:
            self.products = json.load(f)

    def get_product_location(self, product_name):
        return self.products.get(product_name.lower(), "Product not found.")