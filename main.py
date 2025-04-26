import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")


def print_list(list):
    if not list:
        print("The list is empty!")
    for i, task in enumerate(list, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {status} {task['description']}")
    print("\n")


def list_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print_list(tasks)


def list_completed_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        completed_tasks = []
        for i, task in enumerate(tasks, 1):
            if task["completed"]:
                completed_tasks.append(task)
    print_list(completed_tasks)


def list_pending_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        pending_tasks = []
        for i, task in enumerate(tasks, 1):
            if task["completed"] == False:
                pending_tasks.append(task)
    print_list(pending_tasks)


def update_task():
    tasks = load_tasks()
    list_all_tasks()
    index = int(input("Enter task number you want to update: "))
    if 1 <= index <= len(tasks):
        new_description = input("New description or press 'Enter' to skip: ")
        if new_description:
            tasks[index - 1]["description"] = new_description
        completed = input("Competed 'T' for true or 'F' for false: ").upper()
        if completed == "T":
            tasks[index - 1]["completed"] = True
        else:
            tasks[index - 1]["completed"] = False
        save_tasks(tasks)
        print(f"Task {index} updated!")
    else:
        print("Invalid task number.")


def delete_task():
    tasks = load_tasks()
    list_all_tasks()
    index = int(input("Enter task number you want to delete: "))
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed['description']}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("Simple To-Do List CLI")
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. View pending tasks")
        print("5. Edit a task")
        print("6. Delete a task")
        print("0. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, or 0): ")

        if choice == "1":
            description = input("Enter task details: ")
            add_task(description)
        elif choice == "2":
            list_all_tasks()
        elif choice == "3":
            list_completed_tasks()
        elif choice == "4":
            list_pending_tasks()
        elif choice == "5":
            update_task()
        elif choice == "6":
            delete_task()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, enter values 1, 2, 3, 4, 5, 6, or 0")


if __name__ == "__main__":
    main()
