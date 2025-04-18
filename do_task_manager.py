# Author: Cold Id-deen 
# Date: 4/17/2025
# Purpose: Practice Python to talk with the user using input, conditionals, loops, and a function.

from time import sleep
from tqdm import tqdm

name = input("Hello over there! You are using Cold's First Python Program. Be aware...there might be some uh bugs.\n===============================\nWhat is your first name?")
print(f"Hello, {name}! Welcome to the To-Do List Manager! ")

tasks = []

while True:
    options = input("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit! ")

    if options == "1":
        print("You chose to add tasks.")
        for i in tqdm(range(10)):
            sleep(0.11)
        task = input("What task do you would like to add? ")
        print("Adding the task to the task list...\nPlease wait.")
        for i in tqdm(range(10)):
            sleep(0.11)
            
        print("You had been succesfully added the task.")

        tasks.append(task)

    elif options == "2":
        print("You chose to view tasks.")
        for i in tqdm(range(10)):
            sleep(0.11)

        print("The list of the tasks: ")
        print(tasks)
        print("=============")
    
    elif options == "3":
        print("You chose to remove tasks. ")
        for i in tqdm(range(10)):
            sleep(0.11)

        tasks.remove(task)

    elif options == "4":
        print("You chose to exit the program.\nExiting...")
        for i in tqdm(range(10)):
            sleep(0.11)
        print(f"Goodbye, {name}! Come back when you can.  ")
        break

