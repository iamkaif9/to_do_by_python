tasks = []

while True:
    print("\n------ TO-DO APP ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(" Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\n Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nSelect a task to delete:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            delete_task = int(input("Enter task number: "))

            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
