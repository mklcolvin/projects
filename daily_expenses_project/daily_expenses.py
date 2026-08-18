expenses = []
print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    command = int(input())
    if command != 5:
        if command == 1:
            value = float(input())
            expenses.append(value)
            print("Expense added successfully!")
        if command == 2:
            if expenses == []:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for i in range(len(expenses)):
                    print(f"{i+1}. {expenses[i]}")
        if command == 3:
            if expenses == []:
                print("No expenses recorded yet.")
            else:
                num_expenses = len(expenses)
                total_expenses = 0
                for i in range(num_expenses):
                    total_expenses += expenses[i]
                average = total_expenses / num_expenses
                print(f"Total expense: {total_expenses}")
                print(f"Average expense: {average}")
        if command == 4:
            expenses.clear()
            print("All expenses cleared.")

        # command handling logic would go here
        if command < 1 or command >5:
            print("Invalid choice. Please try again.")
            
        continue
    else:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

