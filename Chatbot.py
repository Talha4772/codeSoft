def chatbot():
    # Define the assistant's greeting
    assistant_greeting = input("Hello, how can I help you today?")
    # Define the user's request
    user_request = input("User: ")
    # Define the assistant's response
    if user_request == "I want to watch a movie":
        assistant_response = "Which movie would you like to watch?"
    elif user_request == "I want to watch the new Batman movie":
        assistant_response = "Okay, which theater would you like to go to?"
    elif user_request == "I want to go to the AMC theater in Mountain View":
        assistant_response = "What time would you like to see the movie?"
    elif user_request == "I want to see it at 7:00 PM":
        assistant_response = "Okay, how many tickets would you like?"
    elif user_request == "I want two tickets":
        assistant_response = "Great, your tickets have been booked. Enjoy the movie!"
    else:
        assistant_response = "I'm sorry, I didn't understand that."
    # Print the conversation between the assistant and the user
    print(assistant_greeting)
    print(user_request)
    print(assistant_response)
# Call the chatbot function
chatbot()