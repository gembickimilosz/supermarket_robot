from modules.inventory_manager import InventoryManager

# Setup
inv = InventoryManager()
inv.set_stock("milk", 10)

# Test basic stock
assert inv.get_stock("milk") == 10

# Test decrease
assert inv.decrease_stock("milk", 2)
assert inv.get_stock("milk") == 8

# Test rollback
inv.undo_last_change()
assert inv.get_stock("milk") == 10

# Test fail to decrease more than stock
assert not inv.decrease_stock("milk", 999)