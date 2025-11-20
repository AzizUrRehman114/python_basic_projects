from models.expense import Expense
from utils.file_handler import load_expenses, save_expenses

def add_expense(expenses):
    amount = float (input("Amount: "))
    category = input("Category: ")
    note = input("Note (optional): ")
    expense = Expense(amount=amount, category=category, note=note)
    expenses.append(expense)
    save_expenses(expenses=expenses)

def list_expenses(expenses):
    for e in expenses:
        print(f"{e.date_time} | {e.category} | ${e.amount} | {e.note}")

def filter_by_category(expenses):
    cat = input("Enter category to filter: ")
    filtered = [e for e in expenses if e.category.lower() == cat.lower()]
    list_expenses(filtered)

def monthly_total(expenses):
    month = input("Enter month (MM/YYYY): ")
    total = 0
    for exp in expenses:
        date_str = exp.get("date")
        date_only = date_str.split(" ")[0]

        if date_only.endswith(month):
            amount = exp.get("amount")
            total+=amount
    print(f"Total expenses in {month}: ${total}")

def menu():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. List Expenses\n3. Filter4 by Category\n4. Monthly Total\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            filter_by_category(expenses)
        elif choice == "4":
            monthly_total(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()