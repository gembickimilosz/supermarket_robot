"""
SpeechModule provides simple input/output methods to simulate speech interaction.
"""

class SpeechModule:

    # This method simulates getting input from the user.
    def get_input(self):
        return input("Customer: ")

    # This method simulates responding to the user.
    def respond(self, message):
        print(f"Robot: {message}")