import string
from collections import deque
from modules.speech_module import SpeechModule
from modules.product_database import ProductDatabase
from modules.recipe_database import RecipeDatabase
from modules.inventory_manager import InventoryManager

class Robot:
    def __init__(self):
        self.speech = SpeechModule()
        self.product_db = ProductDatabase()
        self.recipe_db = RecipeDatabase()
        self.inventory = InventoryManager()
        self.ingredient_list = []  # List for recipe matching
        self.request_queue = deque()  # Queue for customer requests

    def handle_product_request(self, product):
        # Remove punctuation and lowercase the input
        cleaned_product = product.translate(str.maketrans('', '', string.punctuation)).lower()
        location = self.product_db.get_product_location(cleaned_product)
        self.speech.respond(f"The {cleaned_product} is located at {location}.")

    def handle_recipe_request(self):
        recipes = self.recipe_db.get_matching_recipes(self.ingredient_list)
        if recipes:
            self.speech.respond(f"You can make: {', '.join(recipes)}")
        else:
            self.speech.respond("No recipes found with the given ingredients.")

    def handle_stock_check(self, product):
        stock = self.inventory.get_stock(product)
        self.speech.respond(f"Current stock for {product}: {stock}")

    def add_customer_request(self, request):
        self.request_queue.append(request)

    def process_requests(self):
        while self.request_queue:
            request = self.request_queue.popleft()
            command = request.lower()
            if "where is" in command:
                product = command.split("where is")[-1].strip()
                self.handle_product_request(product)
            elif "suggest recipe" in command:
                self.handle_recipe_request()
            elif "stock" in command:
                product = command.split("stock")[-1].strip()
                self.handle_stock_check(product)
            else:
                self.speech.respond("I didn't understand your request.")