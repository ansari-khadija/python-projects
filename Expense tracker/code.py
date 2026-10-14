
expenses = []

while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category (Food/Travel/Shopping): ")

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid amount.")
            continue

        expense = {
            "category": category,
            "amount": amount,
            "paid": True
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(
                    "Category:", expense["category"],
                    "| Amount:", expense["amount"],
                    "| Paid:", expense["paid"]
                )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Spending:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")