import csv
import os

transactions = []
monthly_budget = 10000.0
next_id = 1

def is_valid_month(month_str):
    if len(month_str) != 7:
        return False
    if month_str[4] != "-":
        return False
    try:
        year = int(month_str[:4])
        month = int(month_str[5:7])
        if 1900 <= year <= 2100 and 1 <= month <= 12:
            return True
    except ValueError:
        return False
    return False

def export_to_csv(month, transactions_list, monthly_budget, category_totals):
    filename = f"Monthly_Report_{month}.csv"
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerow(["MONTHLY BUDGET REPORT"])
            writer.writerow(["Month", month])
            writer.writerow(["Monthly Budget (Rs.)", monthly_budget])
            writer.writerow([])
            
            month_transactions = [t for t in transactions_list if t["month"] == month]
            total_spent = sum(t["amount"] for t in month_transactions)
            
            writer.writerow(["TRANSACTIONS"])
            writer.writerow(["ID", "Category", "Amount (Rs.)", "Month"])
            
            for transaction in month_transactions:
                writer.writerow([
                    transaction["id"],
                    transaction["category"],
                    transaction["amount"],
                    transaction["month"]
                ])
            
            writer.writerow([])
            writer.writerow(["SUMMARY"])
            writer.writerow(["Total Spent (Rs.)", total_spent])
            
            if total_spent <= monthly_budget:
                writer.writerow(["Money Remaining (Rs.)", monthly_budget - total_spent])
                writer.writerow(["Status", "Within Budget"])
            else:
                writer.writerow(["Over Budget By (Rs.)", total_spent - monthly_budget])
                writer.writerow(["Status", "Over Budget"])
            
            writer.writerow([])
            writer.writerow(["SPENDING BY CATEGORY"])
            writer.writerow(["Category", "Amount (Rs.)"])
            
            for category in sorted(category_totals.keys()):
                writer.writerow([category, category_totals[category]])
        
        print(f"CSV report saved as: {filename}")
        print(f"File location: {os.path.abspath(filename)}")
        return True
    except IOError as e:
        print(f"Error creating CSV file: {e}")
        return False

print("Budget Analyser is running.")

while True:
    print("\n==============================")
    print("       BUDGET ANALYSER")
    print("==============================")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Search Transactions")
    print("4. Update Transaction")
    print("5. Delete Transaction")
    print("6. Monthly Analysis")
    print("7. Generate Monthly Report (text)")
    print("8. Set / View Budget")
    print("9. Exit")

    choice = input("Choose an option (1-9): ").strip()

    if choice == "1":
        category = input("Enter category, such as Food or Travel: ").strip()

        try:
            amount = float(input("Enter amount: Rs. "))
        except ValueError:
            print("Please enter the amount as a number.")
            continue

        if category == "" or amount <= 0:
            print("Enter a category and an amount greater than zero.")
            continue

        month = input("Enter month (YYYY-MM, such as 2026-10): ").strip()

        if not is_valid_month(month):
            print("Invalid month format. Please use YYYY-MM format (e.g., 2026-10).")
            continue

        transaction = {
            "id": next_id,
            "category": category.title(),
            "amount": amount,
            "month": month
        }

        transactions.append(transaction)
        print("Transaction added. Its ID is", next_id)
        next_id = next_id + 1

    elif choice == "2":
        if len(transactions) == 0:
            print("No transactions have been added yet.")
        else:
            print("\nAll Transactions:")
            for transaction in transactions:
                print(
                    "ID:", transaction["id"],
                    "| Month:", transaction["month"],
                    "| Category:", transaction["category"],
                    "| Amount: Rs.", transaction["amount"]
                )

    elif choice == "3":
        search_word = input("Enter a category to search for: ").strip().lower()
        found = False

        for transaction in transactions:
            if search_word in transaction["category"].lower():
                print(
                    "ID:", transaction["id"],
                    "| Month:", transaction["month"],
                    "| Category:", transaction["category"],
                    "| Amount: Rs.", transaction["amount"]
                )
                found = True

        if not found:
            print("No matching transactions found.")

    elif choice == "4":
        try:
            transaction_id = int(input("Enter the ID to update: "))
        except ValueError:
            print("Enter a valid ID number.")
            continue

        found = False

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                new_category = input("Enter the new category: ").strip()

                valid_amount = False
                while not valid_amount:
                    try:
                        new_amount = float(input("Enter the new amount: Rs. "))
                        if new_amount <= 0:
                            print("Amount must be greater than zero.")
                        else:
                            valid_amount = True
                    except ValueError:
                        print("Please enter the amount as a number.")

                if new_category != "":
                    transaction["category"] = new_category.title()
                transaction["amount"] = new_amount
                print("Transaction updated.")
                found = True
                break

        if not found:
            print("Transaction ID not found.")

    elif choice == "5":
        try:
            transaction_id = int(input("Enter the ID to delete: "))
        except ValueError:
            print("Enter a valid ID number.")
            continue

        found = False

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transactions.remove(transaction)
                print("Transaction deleted.")
                found = True
                break

        if not found:
            print("Transaction ID not found.")

    elif choice == "6" or choice == "7":
        month = input("Enter month (YYYY-MM, such as 2026-10): ").strip()

        if not is_valid_month(month):
            print("Invalid month format. Please use YYYY-MM format (e.g., 2026-10).")
            continue

        total_spent = 0
        category_totals = {}

        for transaction in transactions:
            if transaction["month"] == month:
                total_spent = total_spent + transaction["amount"]
                category = transaction["category"]

                if category in category_totals:
                    category_totals[category] = (
                        category_totals[category] + transaction["amount"]
                    )
                else:
                    category_totals[category] = transaction["amount"]

        if choice == "6":
            print("\nMonthly Analysis for", month)
        else:
            print("\nMonthly Report for", month)

        print("Monthly budget: Rs.", monthly_budget)
        print("Total spent: Rs.", total_spent)

        if total_spent <= monthly_budget:
            print("Money remaining: Rs.", monthly_budget - total_spent)
            print("Status: Within budget")
        else:
            print("Over budget by: Rs.", total_spent - monthly_budget)
            print("Status: Over budget")

        if len(category_totals) == 0:
            print("No transactions recorded for this month.")
        else:
            print("Spending by category:")
            for category in category_totals:
                print(category + ":", "Rs.", category_totals[category])
        
        if choice == "7":
            print("\nGenerating CSV report...")
            export_to_csv(month, transactions, monthly_budget, category_totals)

    elif choice == "8":
        print("Current monthly budget: Rs.", monthly_budget)
        change = input("Set a new budget? (y/n): ").strip().lower()

        if change == "y":
            try:
                new_budget = float(input("Enter the new monthly budget: Rs. "))
                if new_budget > 0:
                    monthly_budget = new_budget
                    print("Budget updated.")
                else:
                    print("Budget must be greater than zero.")
            except ValueError:
                print("Please enter the budget as a number.")

    elif choice == "9":
        print("Goodbye.")
        break

    else:
        print("Please type a number from 1 to 9.")