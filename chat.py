# Author: Cold Id-deen 
# Date: 4/17/2025
# Purpose: Practice Python to talk with the user using input, conditionals, loops, and a function.

# Greet the user
print("Hello! I'm RoboPal! Let's chat")

# Ask for the user's name
name = input("What's your name? ")

# Print a greeting using the user's name
print(f"Nice to meet you, {name}! ")

# Define the chatbot conversation function
def ask_questions():
    '''
    This function runs an interactive chatbot that asks the user questions
    about pizza, favorite colors, and a fun choice between the moon or sea. 
    It keeps running until the user says "bye".
    '''
    
    while True:  # Loop to keep the conversation going
        # Ask if the user likes pizza
        pizzy = input("Do you like pizza? Yes or no. ")

        if pizzy.lower() == "yes":
            print("Nice!")

            # Ask for the user's favorite color
            color = input("What's your favorite color? ")
            
            if color:
                # Respond to the color
                print(f"Interesting....{color} is your favorite color, huh? ")
            else:
                # Ask them to try again if they didn't type anything
                print("Try again!")
                continue  # Restart the loop

        elif pizzy.lower() == "no":
            # If they don’t like pizza, move on
            print("Understandable...next question! ")

            # Ask for favorite color
            color = input("What's your favorite color? ")

            if color:
                print(f"Nice, {color} is a cool color! ")
            else:
                print("Hmm, you forget to tell me your color! ")
                continue  # Restart the loop

            # Ask the next fun question
            moon_dive = input("Would you rather go to the moon or dive under the sea? Moon or Sea. ")

            if moon_dive.lower() == "moon":
                print("The moon is great, dosen't it? ")
            elif moon_dive.lower() == "sea":
                print("I see!")
            else:
                print("Try again!")
                continue  # Restart if invalid input

            # Ask if the user wants to end the chat
            end_chat = input("Say bye if you want to finish chatting with me! ")
            if end_chat.lower() == "bye":
                print("Goodbye! It was fun chatting with you! ")
                break  # Exit the loop and end chat

# Call the chatbot function to start the chat
ask_questions()
