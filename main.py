from asyncio.windows_events import NULL
from glob import glob
import time
import os

# Classes --------------------------------------------------------------------------------------------------------------
class Task:
    done = False
    def __init__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number

    def __str__(self) -> str:
        if(self.done == True):
            return str(self.number) + ". " + self.name + ": " + self.description + ". : Done"
        return str(self.number) + ". " + self.name + ": " + self.description + ". : Not Done"
# Varibales ------------------------------------------------------------------------------------------------------------
task_number = 0
tasks = []
help = "To create new task: 'New task'.\nmark task as done: 'done'.\nmark task as not done: 'not done'.\nfor help: 'help'.\nClear tasks list: 'clear'\nLoad list: 'load'\nSave list: 'save'\nTo quit: 'Quit'!"
# Functions ------------------------------------------------------------------------------------------------------------

# Todo! 
def Save_list():
    print("saving")
    time.sleep(1)
    print("saving.")
    time.sleep(1)
    print("saving..")
    time.sleep(1)
    print("saving...")
    quit()

def Save():
    print("path to save the todo list!")
    save = input("Enter any key!")  

def Load():
    print("path to the todo list file!")
    load = input("Enter any key!")  

def Function(_task_number):
    user_input = input("Enter Input: ")
    if(user_input.lower() == "new task"):
        global task_number
        task_number = _task_number
        user_input_name = input("Enter task name: ")
        user_input_description = input("Enter task description: ")
        new_task = Task(user_input_name,user_input_description,task_number)
        tasks.append(new_task)
        task_number +=1

    elif(user_input.lower() == "done"):
        user_input_task_number = input("Enter task number: ")   
        if(int(user_input_task_number) < len(tasks)):
            tasks[int(user_input_task_number)].done = True

    elif(user_input.lower() == "not done"):
        user_input_task_number = input("Enter task number: ")   
        if(int(user_input_task_number) < len(tasks)):
            tasks[int(user_input_task_number)].done = False

    elif(user_input.lower() == "help"):
        print(help)
        wait = input("Enter any key!")   

    elif(user_input.lower() == "save"):
        Save()

    elif(user_input.lower() == "load"):
        Load()

    elif(user_input.lower() == "quit"):
        save_input = input("Save Todo list?: ")
        if(save_input.lower() == "no"):
            os.system('cls')
            print("See you later")
            time.sleep(1)
            print(":)")
            time.sleep(0.1)
            quit()
        else:
            # Todo! Save Function
            Save_list()
    os.system('cls')

# Start ----------------------------------------------------------------------------------------------------------------
 
os.system('cls')
print("Hello to the 'Todo' app made in python!")
print("---------------------------------------")
print("Input are not case sensitive!")
print(help)
print("________________")
Function(task_number)

# Loop -----------------------------------------------------------------------------------------------------------------
while True:
    if(len(tasks) > 0):
        for task in tasks:
            print(task)
    Function(task_number)
