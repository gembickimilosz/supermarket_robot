"""
InventoryManager handles tracking stock levels and changes.
Uses a stack to allow undo operations for stock changes.
"""

class InventoryManager:
    def __init__(self):
        # Dictionary to track stock levels for each product
        self.stock = {}

        # Stack to keep a history of stock changes
        self.history = []

    def set_stock(self, product, amount):
        # Set the stock quantity for a product
        self.stock[product] = amount

    def get_stock(self, product):
        # Retrieve currect stock level
        return self.stock.get(product, 0)

    def decrease_stock(self, product, amount=1):
        # Attempt to decrease stock, only if there's enough stock
        if self.get_stock(product) >= amount:
            # Save current state before modifying
            self.history.append((product, self.stock[product]))
            self.stock[product] -= amount
            return True
        return False # Not enough stock to decrease

    def undo_last_change(self):
        # Undo the last stock change if there's a history
        if self.history:
            product, prev_amount = self.history.pop()
            self.stock[product] = prev_amount
