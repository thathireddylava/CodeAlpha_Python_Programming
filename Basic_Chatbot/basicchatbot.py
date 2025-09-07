def chatbot_response(user_input):
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

print("Chatbot is ready! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    reply = chatbot_response(user_input)
    print("Bot:", reply)
    if user_input == "bye":
        break
