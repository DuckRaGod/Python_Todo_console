from asyncio.windows_events import NULL
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
help = """To create new task: 'New task'.
mark task as done: 'done'.
mark task as not done: 'not done'.
for help: 'help'.
Clear tasks list: 'clear'.
Load list: 'load'.
Save list: 'save'.
Rename task: 'rename'.
To quit: 'Quit'!"""
# Functions ------------------------------------------------------------------------------------------------------------

# Todo! 
def Save_list():
    print("saved")

def Save():
    print("path to save the todo list!")
    save = input("Enter any key!")  
    Save_list()

def Load():
    print("path to the todo list file!")
    load = input("Enter any key!")  

def Function(_task_number):
    user_input = input("Enter Input: ")

    if("new task" in user_input.lower().strip()):
        global task_number
        task_number = _task_number
        user_input_name = input("Enter task name: ")
        user_input_description = input("Enter task description: ")
        new_task = Task(user_input_name,user_input_description,task_number)
        tasks.append(new_task)
        task_number +=1

    elif("done" in user_input.lower().strip()):
        user_input_task_number = input("Enter task number: ")   
        if(int(user_input_task_number) < len(tasks)):
            tasks[int(user_input_task_number)].done = True

    elif("not done" in user_input.lower().strip()):
        user_input_task_number = input("Enter task number: ")   
        if(int(user_input_task_number) < len(tasks)):
            tasks[int(user_input_task_number)].done = False

    elif("help" in user_input.lower().strip()):
        print(help)
        wait = input("Enter any key!")   

    elif("rename" in user_input.lower().strip()):
        rename_task_index = input("Enter index of task to rename: ")
        if(int(rename_task_index) < len(tasks)):
            new_task_name = input("Enter new task name: ")
            tasks[int(rename_task_index)].name = new_task_name 
    
    elif("save" in user_input.lower().strip()):
        Save()

    elif("load" in user_input.lower().strip()):
        Load()

    elif("quit" in user_input.lower().strip()):
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
    
    else:
        print(help)
        time.sleep(.7)
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
    os.system('cls')

    if(len(tasks) > 0):
        for task in tasks:
            print(task)
    Function(task_number)
