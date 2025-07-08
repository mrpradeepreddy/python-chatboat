def chatbot():
    print("Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hello! How can I help you?")
        elif user_input == "what's your name?":
            print("Bot: I'm your Python chatbot.")
        elif user_input == "tell me a joke":
            print("Bot: Why did the programmer quit his job? Because he didn't get arrays!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that.")
chatbot()