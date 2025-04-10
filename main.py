from modules.robot import Robot

def main():
    robot = Robot()
    mode = "customer"

    def print_customer_menu():
        print("\n🛒 Customer Menu:")
        print(" - 'Where is [product]?'")
        print(" - 'Stock [product]'")
        print(" - 'Suggest Recipe'")
        print(" - 'Add Ingredient [item]'")
        print(" - 'Buy [product]' (comma-separated for multiple)")
        print(" - 'Switch to employee'")
        print(" - 'Exit'")

    def print_employee_menu():
        print("\n🔧 Employee Menu:")
        print(" - 'Show Stock'")
        print(" - 'Restock [item] [amount]'")
        print(" - 'Low Stock'")
        print(" - 'Switch to customer'")
        print(" - 'Exit'")

    print("🛒 Welcome to the Supermarket Helper Robot!")
    print_customer_menu()

    while True:
        prompt_label = "Employee" if mode == "employee" else "Customer"
        user_input = input(f"{prompt_label}: ").strip()

        if not user_input:
            continue

        command = user_input.lower()

        if command == "exit":
            print("👋 Goodbye!")
            break

        elif command == "switch to employee":
            mode = "employee"
            robot.speech.respond("🔧 Switched to Employee Mode.")
            print_employee_menu()
            robot.report_low_stock_items()

        elif command == "switch to customer":
            mode = "customer"
            robot.speech.respond("🛍️ Switched to Customer Mode.")
            print_customer_menu()

        elif mode == "employee":
            if command == "show stock":
                robot.handle_full_stock_report()
            elif command.startswith("restock"):
                robot.handle_restock(user_input)
            elif command == "low stock":
                robot.report_low_stock_items()
            elif command.startswith("add ingredient") or command.startswith("buy") or command.startswith("suggest"):
                robot.speech.respond("❌ You are in Employee Mode. Switch to Customer Mode to perform customer actions.")
            else:
                robot.speech.respond("❌ Unknown employee command.")

        elif mode == "customer":
            if command.startswith("add ingredient"):
                ingredient = command.replace("add ingredient", "").strip()
                if ingredient:
                    robot.ingredient_list.append(ingredient)
                    robot.speech.respond(f"Added {ingredient} to ingredient list.")
                else:
                    robot.speech.respond("Please specify an ingredient to add.")
            elif command.startswith("restock") or command.startswith("show stock") or command == "low stock":
                robot.speech.respond("❌ You are in Customer Mode. Switch to Employee Mode to perform employee actions.")
            else:
                robot.add_customer_request(user_input)
                robot.process_requests()

if __name__ == "__main__":
    main()