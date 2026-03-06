def simplechatbot(inputdata):
        user_input = inputdata.lower()
        print(user_input)
        if "hello" in user_input:
            return "Hello! How can I assist you today?"
        elif "how are you" in user_input:
            return "I'm just a simple chatbot, but I'm doing great! Thanks for asking."
        elif "what's your name" in user_input:
            return "I'm a simple chatbot created to assist you."
        elif "bye" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "Sorry, I didn't understand your requirement . Can you please rephrase?"


user_input = input("You: ") 
response = simplechatbot(user_input)
print("Chatbot:", response)
