# Budget Analyser

A command-line expense tracker written in Python. Record transactions, review
monthly spending against a budget, and export a monthly report as CSV.

## Requirements

- Python 3.6 or newer
- No third-party packages

## Run

From the project directory, run:

```powershell
python "Budget analyser.py"
```

The program displays a menu with options to add, view, search, update, and
delete transactions; analyze a month; export a monthly report; change the
budget; or exit.

## Data and reports

- Transactions and the monthly budget are saved in `budget_data.json` beside
  the Python script. They are loaded when the program starts and saved after
  transactions or the budget change.
- If the saved JSON cannot be read or contains invalid data, the program
  reports the error and stops rather than replacing it with empty data.
- Option 7 creates `Monthly_Report_YYYY-MM.csv` in the current working
  directory. The CSV includes that month's transactions, budget status, and
  spending totals by category. Creating a report does not delete saved data.

## Input rules

- Months must use `YYYY-MM` format, with a month from `01` to `12`.
- Transaction categories cannot be empty.
- Amounts and the monthly budget must be finite numbers greater than zero.
- Transaction IDs must be positive integers.
- Category searches cannot be blank.

## Tests

Run the test suite from the project directory:

```powershell
python -m unittest
```
