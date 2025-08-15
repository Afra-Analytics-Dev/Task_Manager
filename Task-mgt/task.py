def task():
    tasks = []  # Empty list to store tasks
    print("-----Welcome To The Task Management App-----")

    # Add initial tasks
    total_task = int(input("Enter how many tasks you want to add: ")) 
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    
    print(f"\nToday's tasks are:\n{tasks}")

    while True:
        print("\nOptions:")
        operation = int(input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\nEnter your choice (1-5): "))
        
        # Add a new task
        if operation == 1:
            new_task = input("Enter task you want to add: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added successfully!")
        
        # Update an existing task
        elif operation == 2:
            old_task = input("Enter the task name you want to update: ")
            if old_task in tasks:
                new_task = input("Enter new task: ")
                index = tasks.index(old_task)
                tasks[index] = new_task
                print(f"Task updated from '{old_task}' to '{new_task}'!")
            else:
                print("Error: Task not found!")
        
        # Delete a task
        elif operation == 3:
            delete_task = input("Enter task to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f"Task '{delete_task}' deleted!")
            else:
                print("Error: Task not found!")
        
        # View all tasks
        elif operation == 4:
            print("\nCurrent Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        
        # Exit the program
        elif operation == 5:
            print("Exiting the app. Goodbye!")
            break
        
        # Invalid input
        else:
            print("Invalid choice! Please enter 1-5.")

# Run the function
task()