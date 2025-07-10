import re

# -------------------------------------------------
# Simple Rule-Based Chatbot
# -------------------------------------------------

def chatbot():
    # Greet the user at the start
    print("Chatbot: Hello! I'm your assistant. Type 'bye' or 'exit' to end the chat.\n")

    # Define the set of rules: regex patterns mapped to responses
    rules = {
        r"(hi|hello|hey)": "Hello! How can I assist you today?",
        r"what(.*)your name": "I am a simple rule-based chatbot.",
        r"how are you": "I'm just a program, but I'm functioning as expected!",
        r"(bye|exit|quit)": "Goodbye! Have a wonderful day!"
    }

    while True:
        # Read user input from the console
        user_input = input("You: ").lower().strip()

        found_match = False

        # Check each pattern to see if it matches the user input
        for pattern, response in rules.items():
            if re.search(pattern, user_input):
                print("Chatbot:", response)
                found_match = True

                # If user wants to end the conversation, exit
                if re.search(r"(bye|exit|quit)", user_input):
                    return
                break

        # Default fallback response if no pattern matched
        if not found_match:
            print("Chatbot: I'm sorry, I didn't quite understand that. Can you please rephrase?")

# Run the chatbot if this file is executed directly
if __name__ == "__main__":
    chatbot()
