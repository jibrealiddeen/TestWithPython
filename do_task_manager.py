# Author: Cold Id-deen 
# Date: 4/17/2025
# Modified: 4/19/2025
# Purpose: Practice Python to talk with the user using input, conditionals, loops, and a function.

from tqdm import tqdm  # Imports tqdm for progress bars
import time  # Imports time module to simulate waiting time

# Ask for the user's name at the beginning
name = input("Hello over there! You are using Cold's First Python Program. Be aware...there might be some uh bugs.\n===============================\nWhat is your first name?")
print(f"Hello, {name}! Welcome to the To-Do List Manager! ")

tasks = []  # Creates an empty list to store the user's tasks

# Start a loop that keeps running until the user chooses to exit
while True:
    # Display menu options
    options = input("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")

    # If user chooses to add a task
    if options == "1":
        print("You chose to add tasks.")
        task = input("What task do you would like to add? ")
        print("Please wait.")
        
        # Show a progress bar to simulate adding a task
        with tqdm(total=100, desc="Adding the task", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)
             
        print(f"You had been succesfully added '{task}' to the list of tasks.\nBack to the menu!\n===============")
        tasks.append(task)  # Add the task to the list

    # If user chooses to view the task list
    elif options == "2":
        print("You chose to view tasks.")
        
        # Simulated loading bar before showing tasks
        with tqdm(total=100, desc="???????", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)

        # Show the list of tasks
        print("The list of the tasks: ")
        print(tasks)
        print("=============")
    
    # If user chooses to remove a task
    elif options == "3":
        print("You chose to remove tasks.")
        
        # Simulate checking/loading
        with tqdm(total=100, desc="Checking", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)

        tasks.remove(task)  # Remove the task from the list (this uses the last task entered)

    # If user chooses to exit the program
    elif options == "4":
        print("You chose to exit the program.")
        
        # Simulate saving progress
        with tqdm(total=100, desc="Saving", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)
                
        print(f"Goodbye, {name}! Come back when you can. ")
        break  # Ends the loop and exits the program
