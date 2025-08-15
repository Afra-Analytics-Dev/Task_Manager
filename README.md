# Task Management App
A simple Python command-line application for managing your daily tasks with full CRUD (Create, Read, Update, Delete) functionality.
====================================================================================================================
## Features
- Add multiple tasks at once
- Update existing tasks
- Delete tasks
- View all tasks with numbering
- Simple menu-driven interface
- Input validation

=====================================================================================================================
# Usage:
1. Rung teh program: python task.py
2.  Follow the on-screen prompts to:
i. Enter initial tasks, ii. Choose operations from the menu, iii. Manage your task list

# The Example Workflow:
-----Welcome To The Task Management App-----
Enter how many tasks you want to add: 2
Enter task 1: Buy groceries
Enter task 2: Finish project

Today's tasks are:
['Buy groceries', 'Finish project']

Options:
1-Add
2-Update
3-Delete
4-View
5-Exit
Enter your choice (1-5): 2
Enter the task name you want to update: Finish project
Enter new task: Complete project documentation
Task updated from 'Finish project' to 'Complete project documentation'!

=================================================================================================================

# Improvement Suggestions
Consider these enhancements for future versions:
- Task Priorities: Add priority levels (High/Medium/Low)
- Due Dates: Allow setting deadlines for tasks
- Categories: Organize tasks into categories/projects
- Persistence: Save tasks to a file (JSON/CSV)
- Search Function: Find tasks by keyword

 Use this code for the enhancements/improvement:
 import json

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def task():
    tasks = load_tasks()  # Load from file
    # ... rest of existing code ...
    
    # Add save before exiting
    elif operation == 5:
        save_tasks(tasks)
        print("Tasks saved. Exiting the app. Goodbye!")
        break

============================================================================================================
