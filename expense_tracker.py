expenses = []

def add_expense():
    Name = input("Enter expense name: ")

    if not Name.replace(" ", "").isalpha():
        print("invalid name! use letters only. ")
        return
    try:
        Amount = float(input("Enter amount: "))


    except ValueError:
        print("Invalid entry! Use numbers only. ")
        return


    expense = {
        "Name" : Name,
        "Amount": Amount
    }

    expenses.append(expense)

    print("Expense added successfully! ")



def view_expenses():
    if not expenses:
        print("No expenses recorded yet. ")
        return

    for expense in expenses:
        print(f" {expense["Name"]}:$ {expense ["Amount"] }  ")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense ["Amount"]

    print(f"Total expenses: ${total}")


def main():
    while True:
        print("\n---EXPENSE TRACKER ---")
        print("1. Add expense")
        print("2.view expenses")
        print("3.Calculate total")
        print("4.Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("come again soon!")
            break

        else:
            print("Invalid choice!")


main()
