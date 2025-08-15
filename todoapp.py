tasks = []

while True:
    print("\n Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task description: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")
            print("Please add a task first.")
    
    elif choice == "3":
        searchtask = input("Enter task to search: ")
        found = False
        for task in tasks:
            if task.lower() == searchtask.lower():
                print(f"Found task: {task}")
                found = True
                break
        if not found:
            print("Task not found.")
    elif choice == "4":
        removetask = input("Enter task to remove: ")
        for i, task in enumerate(tasks):
            if task.lower() == removetask.lower():
                del tasks[i]
                print("Task removed successfully.")
                break
        else:
            print("Task not found.")

    elif choice == "5":
        print("Exiting Task Manager.")
        break

    
