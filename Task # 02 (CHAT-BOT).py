def chatbot(user_input):  # This function is for chatbot
    user_input = user_input.lower()  # lower casing the user input so, we can compare it easily.
    if user_input in ["hello"]:  # if user input is in our list, chatbot will respond according to its memory.
        return "Hi"
    elif user_input in ["how are you"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye"]:
        return "Goodbye!"
    else:  # if user type something that's not in chatbot memory, it will also respond.
        return "Sorry, your input is not in my memory"


def chatwithchatbot():                  # A Sub-routine to chat with ChatBot
    print("ChatBot: Welcome, Type to talk. Type 'BYE' to Exit.!")
    while True:                         # Always true so that user can talk until he enters "bye"
        user_input = input("\nYou: ")
        chatbot_response = chatbot(user_input)
        print("ChatBot: ", chatbot_response)
        if user_input.lower() in ["bye"]:
            break


chatwithchatbot()
