# CSV Export Feature - Budget Analyser

## Overview
The Budget Analyser now automatically generates Excel-compatible CSV files when you use **Option 7: Generate Monthly Report (text)**.

---

## What is a CSV File?

**CSV** stands for "Comma-Separated Values". It's a simple text format that:
- Can be opened in Microsoft Excel, Google Sheets, LibreOffice Calc, and any spreadsheet application
- Stores data in rows and columns
- Is widely compatible and lightweight
- Can be easily imported into databases or other tools

---

## Feature Details

### When is the CSV Created?

The CSV file is automatically generated **only when you select Option 7** (Generate Monthly Report).

**Option 6** (Monthly Analysis) does **NOT** create a CSV file - it only displays the analysis on screen.

### File Naming

The CSV file is automatically named with the following format:

```
Monthly_Report_YYYY-MM.csv
```

**Examples:**
- `Monthly_Report_2026-10.csv` (for October 2026)
- `Monthly_Report_2026-11.csv` (for November 2026)
- `Monthly_Report_2025-01.csv` (for January 2025)

### File Location

The CSV file is saved in the **same folder** as your Python script (Budget Analyser).

The program will display:
```
CSV report saved as: Monthly_Report_2026-10.csv
File location: C:\Users\...\Budget analyser (1).csv
```

---

## CSV File Contents

The CSV file contains detailed budget information organized in sections:

### 1. Header Section
```
MONTHLY BUDGET REPORT
Month,2026-10
Monthly Budget (Rs.),10000
```

### 2. Transactions Section
Lists all transactions for that month:
```
TRANSACTIONS
ID,Category,Amount (Rs.),Month
1,Food,500,2026-10
2,Travel,1500,2026-10
3,Food,250,2026-10
```

### 3. Summary Section
Shows overall spending status:
```
SUMMARY
Total Spent (Rs.),2250
Money Remaining (Rs.),7750
Status,Within Budget
```

OR (if over budget):
```
SUMMARY
Total Spent (Rs.),12500
Over Budget By (Rs.),2500
Status,Over Budget
```

### 4. Category Breakdown
Shows spending by category (sorted alphabetically):
```
SPENDING BY CATEGORY
Category,Amount (Rs.)
Entertainment,300
Food,750
Travel,1200
```

---

## How to Use the CSV File

### Opening in Excel

1. **Navigate** to the folder containing your Python script
2. **Find** the CSV file with the month you want (e.g., `Monthly_Report_2026-10.csv`)
3. **Double-click** the file to open it in Excel automatically
4. OR **Right-click** → **Open with** → **Microsoft Excel**

### Opening in Google Sheets

1. Go to [Google Sheets](https://sheets.google.com)
2. Click **File** → **Open**
3. Click **Upload** tab
4. Select your CSV file from your computer
5. Google Sheets will convert it to a spreadsheet automatically

### Opening in LibreOffice Calc

1. Open LibreOffice Calc
2. Go to **File** → **Open**
3. Select the CSV file
4. Accept the default delimiter settings
5. Click **OK**

---

## Example Workflow

### Step 1: Add Transactions
```
Option: 1
Category: Food
Amount: 500
Month: 2026-10

Option: 1
Category: Travel
Amount: 1500
Month: 2026-10
```

### Step 2: Generate Monthly Report with CSV
```
Option: 7
Month: 2026-10

Output:
Monthly Report for 2026-10
Monthly budget: Rs. 10000.0
Total spent: Rs. 2000.0
Money remaining: Rs. 8000.0
Status: Within budget
Spending by category:
Travel: Rs. 1500.0
Food: Rs. 500.0

Generating CSV report...
CSV report saved as: Monthly_Report_2026-10.csv
File location: C:\Users\Shaurya Salke\OneDrive\Desktop\VS\college_computational\budget_nav\Monthly_Report_2026-10.csv
```

### Step 3: Open CSV in Excel
- Navigate to the folder
- Double-click `Monthly_Report_2026-10.csv`
- View the data in Excel with proper formatting

---

## CSV File Structure

The CSV file is well-structured for easy analysis:

```
Row 1:   MONTHLY BUDGET REPORT
Row 2:   Month, 2026-10
Row 3:   Monthly Budget (Rs.), 10000
Row 4:   [Empty]
Row 5:   TRANSACTIONS
Row 6:   ID, Category, Amount (Rs.), Month
Row 7:   1, Food, 500, 2026-10
Row 8:   2, Travel, 1500, 2026-10
Row 9:   [Empty]
Row 10:  SUMMARY
Row 11:  Total Spent (Rs.), 2000
Row 12:  Money Remaining (Rs.), 8000
Row 13:  Status, Within Budget
Row 14:  [Empty]
Row 15:  SPENDING BY CATEGORY
Row 16:  Category, Amount (Rs.)
Row 17:  Food, 500
Row 18:  Travel, 1500
```

---

## Benefits of CSV Export

✅ **Share Reports** - Email the CSV file to others easily  
✅ **Archive Data** - Keep monthly reports as backup  
✅ **Further Analysis** - Use Excel formulas for custom calculations  
✅ **Import Data** - Load into accounting software  
✅ **Create Charts** - Excel can create graphs from the data  
✅ **Professional Format** - Looks professional when printed or shared  

---

## Multiple Reports

You can generate CSV reports for multiple months:

```
Monthly_Report_2026-09.csv (September 2026)
Monthly_Report_2026-10.csv (October 2026)
Monthly_Report_2026-11.csv (November 2026)
```

Each month's report is stored separately and can be accessed anytime.

---

## Important Notes

⚠️ **CSV Created Only for Option 7**
- Option 6 does NOT generate a CSV file
- You must choose Option 7 to get the Excel export

⚠️ **Overwrites Previous File**
- If you generate a report for the same month twice, the new CSV will overwrite the old one
- If you want to keep historical versions, rename the file before generating a new report

✅ **No Data Loss**
- Generating a CSV does NOT delete your transactions
- Your data in the program remains unchanged

---

## Troubleshooting

### Q: Where is my CSV file?
**A:** Check the same folder where your Python script is located. The file should be named `Monthly_Report_YYYY-MM.csv`

### Q: Can't open the CSV file?
**A:** Try these steps:
1. Right-click the CSV file
2. Select "Open with"
3. Choose Microsoft Excel or another spreadsheet application

### Q: CSV file is blank or shows errors?
**A:** Make sure you:
1. Have transactions for that month
2. Used the correct month format (YYYY-MM)
3. Generated the report (Option 7) after adding transactions

### Q: How do I keep multiple reports?
**A:** Before generating a new report for the same month, rename the old file:
- `Monthly_Report_2026-10.csv` → `Monthly_Report_2026-10_BACKUP.csv`

---

## Technical Implementation

The CSV export uses Python's built-in `csv` module:

```python
import csv
import os

def export_to_csv(month, transactions_list, monthly_budget, category_totals):
    filename = f"Monthly_Report_{month}.csv"
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header information
        writer.writerow(["MONTHLY BUDGET REPORT"])
        writer.writerow(["Month", month])
        writer.writerow(["Monthly Budget (Rs.)", monthly_budget])
        # ... more rows written ...
        
        print(f"CSV report saved as: {filename}")
```

This ensures:
- Proper CSV formatting for Excel compatibility
- Automatic file creation in the current directory
- Error handling if file cannot be created

---

## Summary

| Feature | Details |
|---------|---------|
| **When to Use** | Option 7: Generate Monthly Report |
| **File Format** | CSV (Excel-compatible) |
| **File Naming** | `Monthly_Report_YYYY-MM.csv` |
| **Location** | Same folder as Python script |
| **Contents** | Transactions, summary, category breakdown |
| **Overwrite** | Yes, if report generated for same month again |
| **Data Loss** | No, program transactions remain unchanged |

The CSV export feature makes it easy to analyze your budget data in Excel and share reports with others! 📊
