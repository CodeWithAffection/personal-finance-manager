# Personal Finance Manager

A simple command-line application for tracking personal income and expenses. Built with Python and SQLite.

## What it does

- Add income and expense transactions with category and date
- View all transactions
- Check current balance (income minus expenses)
- Filter transactions by category
- View monthly spending statistics

## Project structure

- `database.py` — database connection, table creation, adding and reading transactions
- `finance.py` — balance calculation, category filtering, monthly statistics
- `main.py` — interactive menu for the user
