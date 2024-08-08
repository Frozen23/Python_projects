import datetime
import msvcrt
import os
from operator import itemgetter
import main_menu as menu
import time

def delete_task(tasks):
    """Deletes a task by given name and creation date."""
    name = input("Enter the name of the task to delete: ")
    creation_date = input("Enter the creation date of the task to delete (in the format yyyy-mm-dd): ")
    creation_time = input("Enter the creation time of the task to delete (in the format hh:mm): ")
    for task_id, task in tasks.items():
        if task['name'] == name and task['creation_date'] == creation_date and task['creation_time'] == creation_time:
            del tasks[task_id]
            print("Task deleted.")
            return
    print("No task found with the given name and creation date.")
def load_tasks():
    """Loads tasks from a text file into a dictionary."""
    tasks = {}
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                name, realization_date, realization_time, priority, status, category, description, creation_date, creation_time, edit_date, edit_time = line.strip().split(',')
                task_id = str(len(tasks) + 1)
                tasks[task_id] = {
                    'name': name,
                    'realization_date': realization_date,
                    'realization_time': realization_time,
                    'priority': priority,
                    'status': status,
                    'category': category,
                    'description': description,
                    'creation_date': creation_date,
                    'creation_time': creation_time,
                    'edit_date': edit_date,
                    'edit_time': edit_time
                }
    except FileNotFoundError:
        print("Task file not found, starting with an empty task list.")
    return tasks


def save_tasks(tasks):
    """Saves tasks from the dictionary to a text file."""
    with open("tasks.txt", 'w') as file:
        for task_id, task in tasks.items():
            line = f"{task['name']},{task['realization_date']},{task['realization_time']},{task['priority']},{task['status']},{task['category']},{task['description']},{task['creation_date']},{task['creation_time']},{task['edit_date']},{task['edit_time']}\n"
            file.write(line)

def check_name(name):
    if name == "":
        print("You did not provide a name.")
        menu.main_menu()

def check_date(realization_date):
    if realization_date != "none":
        try:
            datetime.datetime.strptime(realization_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format.")
            menu.main_menu()

def check_time(realization_time):
    if realization_time != "none":
        try:
            datetime.datetime.strptime(realization_time, '%H:%M').time()
        except ValueError:
            print("Invalid time format.")
            menu.main_menu()

def check_date_and_time(date1, time1, date2, time2):
    if date1 != "none" and time1 != "none":
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
        time1 = datetime.datetime.strptime(time1, '%H:%M').time()
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        time2 = datetime.datetime.strptime(time2, '%H:%M').time()
        datetime1 = datetime.datetime.combine(date1, time1)
        datetime2 = datetime.datetime.combine(date2, time2)
        if datetime1 < datetime2:
            print("The realization time is earlier than the task creation time.")
            menu.main_menu()

def check_priority(priority):
    if priority != "LOW":
        if priority != "MID":
            if priority != "HIGH":
                print("Invalid priority.")
                menu.main_menu()

def check_status(status):
    status = int(status)
    if status > 100 or status < 0:
        print("Invalid status.")
        menu.main_menu()

def display_tasks(tasks):
    """Displays tasks from the dictionary."""
    for task_id, task in tasks.items():
        print(f" Name: {task['name']}")
        print(f" Realization (date): {task['realization_date']}")
        print(f" Realization (time): {task['realization_time']}")
        print(f" Priority: {task['priority']}")
        print(f" Status: {task['status']}")
        print(f" Category: {task['category']}")
        print(f" Description: {task['description']}")
        print(f" Created (date): {task['creation_date']}")
        print(f" Created (time): {task['creation_time']}")
        print(f" Last Edited (date): {task['edit_date']}")
        print(f" Last Edited (time): {task['edit_time']}")
        print("**********************************")


def add_task(tasks):
    """Adds a new task to the dictionary."""
    print("Mandatory fields are marked with *")
    name = input("Enter task name*: ")
    check_name(name)
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_time = datetime.datetime.now().strftime("%H:%M")
    realization_date = input("Enter realization date (in format yyyy-mm-dd)*: ")
    check_date(realization_date)
    realization_time = input("Enter realization time (in format hh:mm)*: ")
    check_time(realization_time)
    check_date_and_time(realization_date, realization_time, creation_date, creation_time)
    priority = input("Enter task priority (LOW, MID, HIGH)*: ")
    check_priority(priority)
    status = input("Enter task status (0-100)*: ")
    check_status(status)
    category = input("Enter category: ")
    description = input("Enter description: ")
    edit_date = creation_date
    edit_time = creation_time
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        'name': name,
        'realization_date': realization_date,
        'realization_time': realization_time,
        'priority': priority,
        'status': status,
        'category': category,
        'description': description,
        'creation_date': creation_date,
        'creation_time': creation_time,
        'edit_date': edit_date,
        'edit_time': edit_time
    }
    print("Task added.")

def change_priority(tasks):
    name = input("Enter task name: ")
    creation_date = input("Enter task creation date (in format yyyy-mm-dd): ")
    creation_time = input("Enter task creation time (in format hh:mm): ")
    update_date = datetime.datetime.now().strftime("%Y-%m-%d")
    update_time = datetime.datetime.now().strftime("%H:%M")
    for task_id, task in tasks.items():
        if task['name'] == name and task['creation_date'] == creation_date and task['creation_time'] == creation_time:
            print("Old priority: " + task['priority'])
            new_priority = input("Enter new task priority: ")
            check_priority(new_priority)
            task['priority'] = new_priority
            task['edit_date'] = update_date
            task['edit_time'] = update_time
            print("Priority changed.")
            return
    print("Task not found.")

def change_date_and_time(tasks):
    name = input("Enter task name: ")
    creation_date = input("Enter task creation date (in format yyyy-mm-dd): ")
    creation_time = input("Enter task creation time (in format hh:mm): ")
    update_date = datetime.datetime.now().strftime("%Y-%m-%d")
    update_time = datetime.datetime.now().strftime("%H:%M")
    for task_id, task in tasks.items():
        if task['name'] == name and task['creation_date'] == creation_date and task['creation_time'] == creation_time:
            print("Old date: " + task['realization_date'])
            print("Old time: " + task['realization_time'])
            new_date = input("Enter new realization date: ")
            check_date(new_date)
            new_time = input("Enter new realization time: ")
            check_time(new_time)
            task['realization_date'] = new_date
            task['realization_time'] = new_time
            check_date_and_time(new_date, new_time, creation_date, creation_time)
            task['edit_date'] = update_date
            task['edit_time'] = update_time
            print("Date and time changed.")
            return
    print("Task not found.")

def change_realization(tasks):
    name = input("Enter task name: ")
    creation_date = input("Enter task creation date (in format yyyy-mm-dd): ")
    creation_time = input("Enter task creation time (in format hh:mm): ")
    update_date = datetime.datetime.now().strftime("%Y-%m-%d")
    update_time = datetime.datetime.now().strftime("%H:%M")
    for task_id, task in tasks.items():
        if task['name'] == name and task['creation_date'] == creation_date and task['creation_time'] == creation_time:
            print("Old completion status: " + task['status'])
            new_status = input("Enter new completion status: ")
            check_status(new_status)
            task['status'] = new_status
            task['edit_date'] = update_date
            task['edit_time'] = update_time
            print("Completion status changed.")
            return
    print("Task not found.")

def compare_creation(tasks):
    dates = []
    for i in range(1, len(tasks) + 1):
        task = str(i)
        date = datetime.datetime.strptime(tasks[task]['creation_date'], '%Y-%m-%d').date()
        time = datetime.datetime.strptime(tasks[task]['creation_time'], '%H:%M').time()
        dates.append((date, time))
    print("Earliest task creation date and time: " + str(min(dates)))
    print("Latest task creation date and time: " + str(max(dates)))
    clear_screen()

def sort_by_realization_date(tasks):
    dates = []
    sorted_dates = []
    for i in range(1, len(tasks) + 1):
        task = str(i)
        date = datetime.datetime.strptime(tasks[task]['realization_date'], '%Y-%m-%d').date()
        time = datetime.datetime.strptime(tasks[task]['realization_time'], '%H:%M').time()
        dates.append((date, time))
    sorted_dates = sorted(dates, key=itemgetter(0, 1))
    for date in sorted_dates:
        print("Date: " + str(date[0]))
        print("Time: " + str(date[1]))
        print("**********************************")
    clear_screen()

def sort_by_creation_date(tasks):
    dates = []
    sorted_dates = []
    for i in range(1, len(tasks) + 1):
        task = str(i)
        date = datetime.datetime.strptime(tasks[task]['creation_date'], '%Y-%m-%d').date()
        time = datetime.datetime.strptime(tasks[task]['creation_time'], '%H:%M').time()
        dates.append((date, time))
    sorted_dates = sorted(dates, key=itemgetter(0, 1))
    for date in sorted_dates:
        print("Date: " + str(date[0]))
        print("Time: " + str(date[1]))
        print("**********************************")
    clear_screen()

def sort_by_priority(tasks):
    priorities = {'LOW': 1, 'MID': 2, 'HIGH': 3}
    task_ids = list(tasks.keys())
    sorted_task_ids = sorted(task_ids, key=lambda task_id: priorities[tasks[task_id]['priority']])
    for task_id in sorted_task_ids:
        task = tasks[task_id]
        print(f"Task name: {task['name']}, Priority: {task['priority']}")
    clear_screen()
def sort_by_status(tasks):
    sorted_task_ids = sorted(tasks.keys(), key=lambda task_id: int(tasks[task_id]['status']), reverse=True)
    for task_id in sorted_task_ids:
        task = tasks[task_id]
        print(f"Task name: {task['name']}, Completion status: {task['status']}")
    clear_screen()
def clear_screen():
    print("Press any key to continue")
    time.sleep(3)
    # msvcrt.getch()
    os.system("cls")
    menu.main_menu()


    
   