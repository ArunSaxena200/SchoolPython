def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"'{removed}' has been removed from your list.")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()
