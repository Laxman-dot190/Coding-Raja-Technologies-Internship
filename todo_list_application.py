
import json
import os
from datetime import datetime

# Define the file where tasks will be stored
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter the task title: ")
    priority = input("Enter the task priority (high, medium, low): ").lower()
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    tasks.append({
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    save_tasks(tasks)
    print("Task added.")

# Remove a task
def remove_task(tasks):
    list_tasks(tasks)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Invalid task number.")

# Mark a task as completed
def complete_task(tasks):
    list_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = 'Done' if task['completed'] else 'Pending'
            print(f"{index}. {task['title']} (Priority: {task['priority']}, Due: {task['due_date']}, Status: {status})")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
