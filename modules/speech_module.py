class SpeechModule:
    def get_input(self):
        return input("Customer: ")

    def respond(self, message):
        print(f"Robot: {message}")