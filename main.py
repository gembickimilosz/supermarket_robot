"""
Main program loop that runs the supermarket robot interface.
Supports both Customer and Employee modes with a command-line menu.
"""

from modules.robot import Robot

def main():
    # Initialize the robot and set the initial mode
    robot = Robot()
    mode = "customer"

    # Print the initial menu for the customer
    def print_customer_menu():
        print("\n Customer Menu:")
        print(" - 'Where is [product]?'")
        print(" - 'Stock [product]'")
        print(" - 'Suggest Recipe'")
        print(" - 'Add Ingredient [item]'")
        print(" - 'Buy [product]' (comma-separated for multiple)")
        print(" - 'Switch to employee'")
        print(" - 'Exit'")

    # Print the initial menu for the employee
    def print_employee_menu():
        print("\n Employee Menu:")
        print(" - 'Show Stock'")
        print(" - 'Restock [item] [amount]'")
        print(" - 'Low Stock'")
        print(" - 'Switch to customer'")
        print(" - 'Exit'")

    # Print the welcome message
    print("Welcome to the Supermarket Helper Robot!")
    print_customer_menu()

    # Main loop to handle user input
    while True:
        prompt_label = "Employee" if mode == "employee" else "Customer"
        user_input = input(f"{prompt_label}: ").strip()

        if not user_input:
            continue # Skip empty input

        command = user_input.lower()

        if command == "exit":
            print("Thanks & Goodbye!")
            break

        ## Handle commands based on the current mode
        elif command == "switch to employee":
            mode = "employee"
            robot.speech.respond("Switched to Employee Mode.")
            print_employee_menu()
            robot.report_low_stock_items()

        elif command == "switch to customer":
            mode = "customer"
            robot.speech.respond("Switched to Customer Mode.")
            print_customer_menu()

        # Handle commands in Employee Mode
        elif mode == "employee":
            if command == "show stock":
                robot.handle_full_stock_report()
            elif command.startswith("restock"):
                robot.handle_restock(user_input)
            elif command == "low stock":
                robot.report_low_stock_items()

            # Restrict customer actions in Employee Mode
            elif command.startswith("add ingredient") or command.startswith("buy") or command.startswith("suggest"):
                robot.speech.respond("You are in Employee Mode. Switch to Customer Mode to perform customer actions.")
            else:
                robot.speech.respond("Unknown employee command.")

        # Handle commands in Customer Mode
        elif mode == "customer":
            if command.startswith("add ingredient"):

                # Extract and add ingredient
                ingredient = command.replace("add ingredient", "").strip()
                if ingredient:
                    robot.ingredient_list.append(ingredient)
                    robot.speech.respond(f"Added {ingredient} to ingredient list.")
                else:
                    robot.speech.respond("Please specify an ingredient to add.")

            elif command.startswith("restock") or command.startswith("show stock") or command == "low stock":

                # Restrict employee actions in Customer Mode
                robot.speech.respond("You are in Customer Mode. Switch to Employee Mode to perform employee actions.")
            else:
                # Handle all other customer commands
                robot.add_customer_request(user_input)
                robot.process_requests()

# Entry point for the program
if __name__ == "__main__":
    main()