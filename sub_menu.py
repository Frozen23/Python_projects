import functions1 as f1
import main_menu as menu
from operator import itemgetter

def submenu():
    tasks = f1.load_tasks()
    while True:
        print("What would you like to do?")
        print("1. Change priority")
        print("2. Change date and time of completion")
        print("3. Change completion status")
        print("4. Display tasks sorted by creation date and time (ascending)")
        print("5. Display tasks sorted by creation date and time (descending)")
        print("6. Display tasks sorted by last updated date and time (ascending)")
        print("7. Display tasks sorted by last updated date and time (descending)")
        print("8. Main menu")

        try:
            choice = int(input("Choose [1-8]: "))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            f1.display_tasks(tasks)
            f1.change_priority(tasks)
            f1.save_tasks(tasks)
            f1.clear_screen()
        elif choice == 2:
            f1.display_tasks(tasks)
            f1.change_date_and_time(tasks)
            f1.save_tasks(tasks)
            f1.clear_screen()
        elif choice == 3:
            f1.display_tasks(tasks)
            f1.change_realization(tasks)
            f1.save_tasks(tasks)
            f1.clear_screen()
        elif choice == 4:
            f1.sort_by_creation_date(tasks)
            f1.clear_screen()
        elif choice == 5:
            f1.sort_by_creation_date(tasks)
            f1.clear_screen()
        elif choice == 6:
            f1.sort_by_priority(tasks)
            f1.clear_screen()
        elif choice == 7:
            f1.sort_by_status(tasks)
            f1.clear_screen()
        elif choice == 8:
            print(menu.main_menu())
        else:
            print("Invalid choice!")