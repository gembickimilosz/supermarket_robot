from modules.product_database import ProductDatabase

product_db = ProductDatabase("data/products.json")

# Known product
assert product_db.get_product_location("milk").startswith("Aisle")

# Unknown product
assert product_db.get_product_location("dragonfruit") == "Product not found."