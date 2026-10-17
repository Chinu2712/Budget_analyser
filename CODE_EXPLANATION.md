# Budget Analyser - Code Explanation

## Overview
The **Budget Analyser** is a command-line Python application that helps users track their monthly expenses and manage their budget. It allows users to add, view, update, and delete financial transactions, analyze spending patterns, and generate monthly reports.

---

## Table of Contents
1. [Global Variables](#global-variables)
2. [Main Menu Structure](#main-menu-structure)
3. [Core Features](#core-features)
4. [Data Structure](#data-structure)
5. [Program Flow](#program-flow)

---

## Global Variables

```python
transactions = []
monthly_budget = 10000.0
next_id = 1
```

| Variable | Type | Purpose |
|----------|------|---------|
| `transactions` | List | Stores all transaction records as dictionaries |
| `monthly_budget` | Float | Sets the spending limit for the current month (default: Rs. 10,000) |
| `next_id` | Integer | Counter to assign unique IDs to each transaction |

---

## Main Menu Structure

The program displays a menu with 9 options in an infinite loop:

```
1. Add Transaction
2. View All Transactions
3. Search Transactions
4. Update Transaction
5. Delete Transaction
6. Monthly Analysis
7. Generate Monthly Report (text)
8. Set / View Budget
9. Exit
```

Each option is handled through conditional statements (`if-elif-else`).

---

## Core Features

### **1. Add Transaction (Option 1)**

**Purpose:** Record a new expense

**Process:**
- Prompts user for category (e.g., "Food", "Travel")
- Prompts user for amount in Rupees
- Prompts user for month in `YYYY-MM` format

**Validation:**
- Checks if amount is a valid number
- Ensures category is not empty
- Ensures amount is greater than zero

**Action:**
- Creates a transaction dictionary with:
  - `id`: Unique identifier
  - `category`: Expense category (title-cased)
  - `amount`: Expense amount
  - `month`: Month of transaction
- Adds transaction to the list
- Increments `next_id` for the next transaction

**Example:**
```python
transaction = {
    "id": 1,
    "category": "Food",
    "amount": 500.0,
    "month": "2026-10"
}
```

---

### **2. View All Transactions (Option 2)**

**Purpose:** Display all recorded transactions

**Process:**
- Checks if transactions list is empty
- If empty: Shows "No transactions have been added yet"
- If not empty: Displays all transactions in formatted output

**Output Format:**
```
ID: [id] | Month: [month] | Category: [category] | Amount: Rs. [amount]
```

---

### **3. Search Transactions (Option 3)**

**Purpose:** Find transactions by category

**Process:**
- Asks user to enter a category name
- Converts search term to lowercase for case-insensitive matching
- Loops through all transactions and checks if search term is contained in category name
- Displays matching transactions

**Example:**
- Search for "food" will match "Food", "Fast Food", "Food Delivery", etc.

**Output:**
- Shows all matching transactions in the same format as "View All Transactions"
- Shows "No matching transactions found" if nothing matches

---

### **4. Update Transaction (Option 4)**

**Purpose:** Modify an existing transaction

**Process:**
- Asks user for transaction ID to update
- Finds the transaction with matching ID
- Prompts for new category and new amount
- Updates both fields if valid

**Validation:**
- Checks if ID is a valid number
- Ensures amount is greater than zero
- Ensures category is not empty (only updates if new category is provided)

**Error Handling:**
- Shows "Transaction ID not found" if ID doesn't exist
- Shows appropriate error messages for invalid inputs

---

### **5. Delete Transaction (Option 5)**

**Purpose:** Remove a transaction from records

**Process:**
- Asks user for transaction ID to delete
- Finds the transaction with matching ID
- Removes it from the transactions list

**Validation:**
- Checks if ID is a valid number
- Verifies transaction exists before deletion

**Feedback:**
- Shows "Transaction deleted" on success
- Shows "Transaction ID not found" if ID doesn't exist

---

### **6. Monthly Analysis (Option 6)**

**Purpose:** Analyze spending for a specific month

**Process:**
1. User enters month in `YYYY-MM` format
2. Program calculates:
   - **Total Spent**: Sum of all transactions for that month
   - **Spending by Category**: Breakdown of spending per category
3. Compares with monthly budget

**Logic:**
```python
total_spent = 0
category_totals = {}

for transaction in transactions:
    if transaction["month"] == month:
        total_spent += transaction["amount"]
        
        if category in category_totals:
            category_totals[category] += transaction["amount"]
        else:
            category_totals[category] = transaction["amount"]
```

**Output:**
- Monthly budget amount
- Total spent
- **Budget Status:**
  - If within budget: "Money remaining: Rs. [amount]" and "Status: Within budget"
  - If over budget: "Over budget by: Rs. [amount]" and "Status: Over budget"
- Spending breakdown by category

**Example Output:**
```
Monthly Analysis for 2026-10
Monthly budget: Rs. 10000.0
Total spent: Rs. 3500.0
Money remaining: Rs. 6500.0
Status: Within budget
Spending by category:
Food: Rs. 2000.0
Travel: Rs. 1500.0
```

---

### **7. Generate Monthly Report (Option 7)**

**Purpose:** Generate a text report (identical to Monthly Analysis)

**Process:** Same as Option 6, but labeled as "Monthly Report" instead of "Monthly Analysis"

---

### **8. Set / View Budget (Option 8)**

**Purpose:** View current budget and optionally change it

**Process:**
1. Displays current monthly budget
2. Asks if user wants to set a new budget (y/n)
3. If yes:
   - Prompts for new budget amount
   - Validates that amount is greater than zero
   - Updates `monthly_budget` variable

**Validation:**
- Ensures input is a valid number
- Ensures budget is positive

**Example:**
```
Current monthly budget: Rs. 10000.0
Set a new budget? (y/n): y
Enter the new monthly budget: Rs. 12000
Budget updated.
```

---

### **9. Exit (Option 9)**

**Purpose:** Terminate the program

**Action:**
- Prints "Goodbye"
- Breaks the infinite loop
- Program ends

---

## Data Structure

### Transaction Dictionary

Each transaction is stored as a Python dictionary with 4 keys:

```python
{
    "id": int,           # Unique identifier
    "category": str,     # Expense category
    "amount": float,     # Amount in Rupees
    "month": str         # Month in YYYY-MM format
}
```

### Category Totals Dictionary

Used temporarily during analysis to aggregate spending:

```python
{
    "Food": 2000.0,
    "Travel": 1500.0,
    "Entertainment": 500.0
}
```

---

## Program Flow

```
┌─ START ─────────────────────────────────────┐
│  Initialize:                                │
│  - transactions = []                        │
│  - monthly_budget = 10000.0                 │
│  - next_id = 1                              │
│                                             │
│  Display "Budget Analyser is running"      │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
        ┌─ MAIN LOOP (Infinite) ─────┐
        │  Display Menu              │
        │  Get User Choice (1-9)     │
        │                            │
        ├─ Choice 1: Add Transaction │
        ├─ Choice 2: View All       │
        ├─ Choice 3: Search         │
        ├─ Choice 4: Update         │
        ├─ Choice 5: Delete         │
        ├─ Choice 6: Analysis       │
        ├─ Choice 7: Report         │
        ├─ Choice 8: Budget         │
        │                            │
        ├─ Choice 9: EXIT ──────────┐
        │                            │ (breaks loop)
        │                            │
        └─ Invalid Choice: Error ──┐ │
                                    │ │
                  (Loop continues)  │ │
                  <─────────────────┘ │
                                      │
                                      ▼
                              ┌─ END ──────┐
                              │ "Goodbye"  │
                              │ Program    │
                              │ Terminates │
                              └────────────┘
```

---

## Key Concepts

### Input Validation
The program uses `try-except` blocks to handle invalid inputs:
```python
try:
    amount = float(input("Enter amount: Rs. "))
except ValueError:
    print("Please enter the amount as a number.")
    continue
```

### String Processing
- `.strip()` removes leading/trailing whitespace
- `.lower()` converts to lowercase for case-insensitive search
- `.title()` capitalizes the first letter of each word

### Conditional Checks
- Empty list checks: `if len(transactions) == 0`
- Budget comparison: `if total_spent <= monthly_budget`
- Dictionary lookups: `if category in category_totals`

### Loop Control
- Infinite `while True` loop for menu
- `for` loops to iterate through transactions
- `break` statement to exit on choice 9 or after updates
- `continue` statement to skip to next iteration on errors

---

## Usage Example Scenario

```
1. User adds transaction: "Food", 500, "2026-10"
2. User adds transaction: "Travel", 1500, "2026-10"
3. User views all transactions (sees both)
4. User searches for "Food" (finds one)
5. User analyzes month "2026-10":
   - Total: 2000, Budget: 10000
   - Status: Within budget
6. User updates transaction ID 1 to 600
7. User analyzes again: Total now 2100
8. User exits program
```

---

## Limitations

1. **No Persistent Storage:** Data is lost when the program closes (stored only in memory)
2. **No Date Validation:** Program doesn't verify if entered month is valid
3. **Simple Search:** Only searches by category name, not by amount or date range
4. **No Budgeting by Category:** Budget is global, not per-category

---

## Potential Enhancements

- Save/load transactions to a file (CSV, JSON, or database)
- Add date validation for month input
- Implement category-wise budget limits
- Add more detailed filtering and sorting options
- Create data visualization (charts, graphs)
- Add recurring transaction functionality
