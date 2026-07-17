expenses = []

while True:

    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])

        print("Expense Added Successfully.")

    elif choice == "2":

        if len(expenses) == 0:
            print("No Expenses Found.")

        else:
            print("\nYour Expenses:")

            for i in range(len(expenses)):
                print(i + 1, ".", expenses[i][0], "-", expenses[i][1])

    elif choice == "3":

        total = 0

        for item in expenses:
            total = total + item[1]

        print("Total Expense =", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")