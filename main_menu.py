import sys
import functions1 as f1
import sub_menu as p

def main_menu():
    tasks = f1.load_tasks()
    # print(dictionary)
    while True:
        print("What would you like to do?")
        print("1. [🖥️] Display tasks")
        print("2. [+] Add a task")
        print("3. [🗑️] Remove a task")
        print("4. [🔧] Other operations")
        print("5. [⤷] Exit")

        try:
            choice = int(input("Choose [1-5]: "))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            if tasks == {}:
                print("No tasks available")
                f1.clear_screen()
            else:
                f1.display_tasks(tasks)
                f1.clear_screen()
                break
        elif choice == 2:
            tasks = f1.load_tasks()
            f1.add_task(tasks)
            f1.save_tasks(tasks)
            f1.clear_screen()
        elif choice == 3:
            f1.display_tasks(tasks)
            f1.delete_task(tasks)
            f1.save_tasks(tasks)
        elif choice == 4:
            print(p.submenu())
        elif choice == 5:
            print("See you next time!")
            sys.exit(0)
        else:
            print("Invalid choice!")