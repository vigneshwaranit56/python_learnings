expenses = []
next_id = 1

def display_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. List Expenses")
    print("4. Total Expenses")
    print("5. Category-wise Expenses")
    print("6. Exit")

def add_expenses():
    global next_id
    category = input("\n enter the category : ")
    description = input("\n enter the description : ")
    amount = int(input("\n enter the amount : "))
    id = next_id
    expenses.append({
        "id": id,
        "category": category,
        "description": description,
        "amount": amount
    })
    next_id += 1
    print(expenses[id-1])

def delete_expenses():
    expense_id = int(input("Enter the expense ID to delete: "))

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully.")
            break
    else:
        print("Expense ID not found.")


def list_expenses():

    print(" ID  Amount  Category Description")
    for expense in expenses:
        print(f"{expense['id']} {expense['amount']} {expense['category']} {expense['description']}")


def total_expenses():

    total_expenses = 0
    for expense in expenses:
        total_expenses += expense['amount']

    print(f" Total expenses: {total_expenses}")


def categoty_wise_expenses():

    category = {}

    for expense in expenses:

        if expense['category'] in category:
            category[expense['category']] = category.get(expense['category'])+expense['amount']
        else:
            category[expense['category']] = expense['amount']

    print(f" Total category expenses: {category}")

while True:
    display_menu()
    user_choice = input(" \n enter the input 1 to 6 : ").strip()

    if user_choice ==  "1":
        add_expenses()
    elif user_choice == "2":
        delete_expenses()
    elif user_choice == "3":
        list_expenses()
    elif user_choice == "4":
        total_expenses()
    elif user_choice == "5":
        categoty_wise_expenses()
    elif user_choice == "6":
        print(" closed application")
        break