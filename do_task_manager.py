# Author: Cold Id-deen 
# Date: 4/17/2025
# Purpose: Practice Python to talk with the user using input, conditionals, loops, and a function.

from tqdm import tqdm
import time


name = input("Hello over there! You are using Cold's First Python Program. Be aware...there might be some uh bugs.\n===============================\nWhat is your first name?")
print(f"Hello, {name}! Welcome to the To-Do List Manager! ")

tasks = []

while True:
    options = input("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit! ")

    if options == "1":
        print("You chose to add tasks.")
        task = input("What task do you would like to add? ")
        print("Please wait.")
        
        with tqdm(total=100, desc="Adding the task", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)

             
        print(f"You had been succesfully added '{task}' to the list of tasks.\nBack to the menu!\n===============")
        tasks.append(task)

    elif options == "2":
        print("You chose to view tasks.")
        with tqdm(total=100, desc="Adding the task", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)

        print("The list of the tasks: ")
        print(tasks)
        print("=============")
    
    elif options == "3":
        print("You chose to remove tasks. ")
        with tqdm(total=100, desc="Adding the task", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)

        tasks.remove(task)

    elif options == "4":
        print("You chose to exit the program.\nExiting...")
        with tqdm(total=100, desc="Adding the task", bar_format="{l_bar}{bar} [ TIME LEFT: {remaining} ]") as pbar:
            for i in range(100):
                time.sleep(0.05)
                pbar.update(1)
        print(f"Goodbye, {name}! Come back when you can. ")
        break

