import string
from collections import deque
from modules.speech_module import SpeechModule
from modules.product_database import ProductDatabase
from modules.recipe_database import RecipeDatabase
from modules.inventory_manager import InventoryManager

class Robot:
    def __init__(self):
        # Initialize the robot with necessary modules
        self.speech = SpeechModule()
        self.product_db = ProductDatabase()
        self.recipe_db = RecipeDatabase()
        self.inventory = InventoryManager()
        self.ingredient_list = []  # List for recipe matching
        self.request_queue = deque()  # Queue for customer requests

        # Set initial stock levels
        initial_stock = {
            "milk": 4,
            "bread": 15,
            "eggs": 20,
            "chicken": 8,
            "rice": 12,
            "tomato": 18,
            "cheese": 10
        }


        for product, amount in initial_stock.items():
            self.inventory.set_stock(product, amount)


    def handle_product_request(self, product):
        # Clean the product name by removing punctuation and converting to lowercase
        cleaned_product = product.translate(str.maketrans('', '', string.punctuation)).lower()
        # Get location from the product database
        location = self.product_db.get_product_location(cleaned_product)
        self.speech.respond(f"The {cleaned_product} is located at {location}.")

    def handle_recipe_request(self):
        # Check if the ingredient list is empty and inform user
        if not self.ingredient_list:
            self.speech.respond("Your ingredient list is empty. Please add ingredients first.")
            return

        # Get matching recipes from the recipe database
        full_matches, partial_matches = self.recipe_db.get_matching_recipes(self.ingredient_list)

        if full_matches:
            self.speech.respond(f"You can make: {', '.join(full_matches)}")

        if partial_matches:
            for recipe, missing in partial_matches:
                self.speech.respond(f"You can almost make '{recipe}'! Just pick up: {', '.join(missing)}")

        if not full_matches and not partial_matches:
            self.speech.respond("Sorry, no recipes match your current ingredients.")

    def handle_stock_check(self, product):
        # Clean and validate input, and show stock or error if product not found
        cleaned_product = product.translate(str.maketrans('', '', string.punctuation)).lower()
        if cleaned_product not in self.inventory.stock:
            self.speech.respond(f"There is no product named '{cleaned_product}'.")
            return
        stock = self.inventory.get_stock(cleaned_product)
        self.speech.respond(f"Current stock for {cleaned_product}: {stock}")

    def handle_full_stock_report(self):
        # Show full inventory to an employee
        if not self.inventory.stock:
            self.speech.respond("Stock is currently empty.")
            return

        self.speech.respond("Here is the current stock:")
        for product, amount in self.inventory.stock.items():
            self.speech.respond(f"{product.capitalize()}: {amount}")

    def handle_purchase(self, items):
        # Allow customers to buy multiple items at once
        items = [item.strip().lower() for item in items.split(',')]

        for item in items:
            if self.inventory.decrease_stock(item):
                self.speech.respond(f"{item.capitalize()} purchased successfully.")
                # Notify if stock is getting low
                if self.inventory.get_stock(item) < 3:
                    self.speech.respond(f"Stock for {item} is low. Notify employee to restock.")
            else:
                self.speech.respond(f"Not enough {item} in stock or item not found.")

    def handle_restock(self, command):
        # Handle restocking of items by employees
        # Example command: "restock milk 5"
        try:
            _, item, amount_str = command.strip().lower().split(maxsplit=2)
            amount = int(amount_str)
            current_stock = self.inventory.get_stock(item)
            self.inventory.set_stock(item, current_stock + amount)
            self.speech.respond(f"{item.capitalize()} restocked by {amount}. New stock: {current_stock + amount}")
        except ValueError:
            self.speech.respond("Invalid restock amount. Please provide a number.")
        except Exception:
            self.speech.respond("Usage: restock [item] [amount]")

    def report_low_stock_items(self):
        # Give employee a report of all items in low stock (less than 3)
        low_items = [item for item, qty in self.inventory.stock.items() if qty < 3]
        if not low_items:
            self.speech.respond("All items are sufficiently stocked.")
        else:
            self.speech.respond("The following items are low on stock:")
            for item in low_items:
                self.speech.respond(f"{item.capitalize()}: {self.inventory.get_stock(item)}")

    def add_customer_request(self, request):
        # Add a customer request to the queue
        self.request_queue.append(request)

    def process_requests(self):
        # Go through all queued requests and respond acordingly
        while self.request_queue:
            request = self.request_queue.popleft()
            command = request.lower()

            if "where is" in command:
                product = command.split("where is")[-1].strip()
                self.handle_product_request(product)

            elif "show stock" in command:
                self.handle_full_stock_report()

            elif "restock" in command:
                self.handle_restock(command)

            elif "stock" in command:
                product = command.split("stock")[-1].strip()
                self.handle_stock_check(product)

            elif "suggest recipe" in command:
                self.handle_recipe_request()

            elif "buy" in command:
                items = command.split("buy")[-1].strip()
                self.handle_purchase(items)

            else:
                self.speech.respond("I didn't understand your request.")