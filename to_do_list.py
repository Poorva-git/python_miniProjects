tasks = []

while True:

    print("\n====== TO DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added.")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks found.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task Removed.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")