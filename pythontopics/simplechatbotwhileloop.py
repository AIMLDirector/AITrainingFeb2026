def simplechatbot1():
    print("Welcome to the simple chatbot! Type 'bye' or 'goodbye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if "bye" in user_input or "goodbye" in user_input:
            print("Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("I'm just a simple chatbot, but I'm doing great! Thanks for asking.")
        elif "what's your name" in user_input:
            print("I'm a simple chatbot created to assist you.")
        else:
           print("Sorry, I didn't understand your requirement . Can you please rephrase?")
       

simplechatbot1()