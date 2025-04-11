from modules.robot import Robot

robot = Robot()

# Add ingredient and check suggestion logic
robot.ingredient_list = ["bread", "cheese"]
robot.handle_recipe_request()  # Should suggest Cheese Toast or similar

# Stock alert simulation
robot.inventory.set_stock("rice", 2)
robot.handle_purchase("rice")  # Should warn stock is low