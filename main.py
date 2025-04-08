from modules.robot import Robot

def main():
    robot = Robot()

    print("🛒 Welcome to the Supermarket Helper Robot!")
    print("Type a command (e.g. 'Where is milk?', 'Suggest recipe', 'Stock chicken')")
    print("Type 'add ingredient [item]' to build a recipe list.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = robot.speech.get_input()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        elif user_input.lower().startswith("add ingredient"):
            ingredient = user_input.lower().replace("add ingredient", "").strip()
            robot.ingredient_list.append(ingredient)
            robot.speech.respond(f"Added {ingredient} to ingredient list.")
        else:
            robot.add_customer_request(user_input)
            robot.process_requests()

if __name__ == "__main__":
    main()