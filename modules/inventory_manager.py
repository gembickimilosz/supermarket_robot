"""
InventoryManager handles tracking stock levels and changes.
Uses a stack to allow undo operations for stock changes.
"""

class InventoryManager:
    def __init__(self):
        self.stock = {}
        self.history = []  # Stack

    def set_stock(self, product, amount):
        self.stock[product] = amount

    def get_stock(self, product):
        return self.stock.get(product, 0)

    def decrease_stock(self, product, amount=1):
        if self.get_stock(product) >= amount:
            self.history.append((product, self.stock[product]))
            self.stock[product] -= amount
            return True
        return False

    def undo_last_change(self):
        if self.history:
            product, prev_amount = self.history.pop()
            self.stock[product] = prev_amount
