import sqlite3

def connect():
    con = sqlite3.connect("finance.db")
    return con

def create_table():
    con = connect()
    cursor = con.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        type TEXT,
        date TEXT
    );
    '''
    cursor.execute(create_table_query)
    
    con.commit()

    con.close()

create_table()


def add_transaction(amount, category, type, date):
    with sqlite3.connect('finance.db') as con:
        cursor = con.cursor()

        insert_query = '''
        INSERT INTO transactions (amount, category, type, date)
        VALUES(?, ?, ?, ?)
        '''
        transaction_data = (amount, category, type, date)

        cursor.execute(insert_query, transaction_data)
        
        con.commit()

def get_all_transactions():
    with sqlite3.connect('finance.db') as con:
        cursor = con.cursor()

        select_query = "SELECT * FROM transactions;"

        cursor.execute(select_query)

        all_transactions = cursor.fetchall()

        print("All transactions:")
        for trns in all_transactions:
            print(trns)


get_all_transactions()

