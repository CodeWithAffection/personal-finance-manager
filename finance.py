import database
import sqlite3


def get_balance():
    with sqlite3.connect('finance.db') as connection:
        cursor = connection.cursor()

        select_query_incomes = '''
        SELECT SUM(amount) FROM transactions WHERE type = 'income'
        '''

        select_query_expenses = '''
        SELECT SUM(amount) FROM transactions WHERE type = 'expense'
        '''

        cursor.execute(select_query_incomes)
        all_incomes = cursor.fetchone()[0] or 0

        cursor.execute(select_query_expenses)
        all_expenses = cursor.fetchone()[0] or 0

        
        print(all_incomes - all_expenses)

def filter_by_category(category):
    with sqlite3.connect('finance.db') as connection:
        cursor = connection.cursor()

        select_query_categories = '''
        SELECT * FROM transactions WHERE category = ?
        '''

        cursor.execute(select_query_categories, (category,))
        
        sorted_by_categories = cursor.fetchall()

        for sbc in sorted_by_categories:
            print(sbc)

def monthly_stats(month):
    with sqlite3.connect('finance.db') as connection:
        cursor = connection.cursor()

        monthly_stats = '''
        SELECT SUM(amount) FROM transactions WHERE date LIKE ?
        '''

        cursor.execute(monthly_stats, ('%' + str(month) + '%',))

        montly_stat = cursor.fetchall()

        print(f"'Number of month number {month}:")
        for ms in montly_stat:
            print(ms)

