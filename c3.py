import os
import json

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return {'tasks': []}

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks['tasks']:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks['tasks'], start=1):
            print(f"{idx}. {task['title']} - {task['description']}")

def add_task(tasks, title, description):
    tasks['tasks'].append({'title': title, 'description': description})
    save_tasks(tasks)
    print("Task added successfully!")

def update_task(tasks, index, title, description):
    if 1 <= index <= len(tasks['tasks']):
        tasks['tasks'][index - 1] = {'title': title, 'description': description}
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks['tasks']):
        del tasks['tasks'][index - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '3':
            display_tasks(tasks)
            index = int(input("Enter the task index to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            update_task(tasks, index, title, description)
        elif choice == '4':
            display_tasks(tasks)
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
