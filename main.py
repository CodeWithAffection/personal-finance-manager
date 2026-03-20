import database
import finance

database.create_table()

while(True):
    print("Input a number of an operation you need")
    print()
    print("1 - Add transaction")
    print("2 - Show all transactions")
    print("3 - Show balance")
    print("4 - Filter by category")
    print("5 - Monthly stats")
    print("6 - Exit")

    while(True):
        try:
            value = int((input("Enter the number: ")))
            break
        except ValueError:
            print("Incorrect type, try one more time")

    if value == 1:
        print('Your choice is "1 - "Add transaction"')
        while(True):
            try:  
                amount = float(input("Enter the amount: "))
                break
            except ValueError:
                print("Incorrect type, try one more time")
        category = input("Enter the category: ")
        while(True):
            type = input("Enter the type of the operation (income/expense)")
            if type == "income" or type == "expense":
                break
            else:
                print("Incorrect type, try one more time")
        date = input("Enter the date of the transaction: ")
        database.add_transaction(amount, category, type, date) 
    elif value == 2:
        print('Your choice is "2 - "Show all transactions"')
        database.get_all_transactions()
    elif value == 3:
        print('Your choice is "3 - "Show balance"')
        finance.get_balance()
    elif value == 4:
        print('Your choice is "4 - Filter by category", enter the category you want to sort')
        category = input()
        finance.filter_by_category(category)
    elif value == 5:
        print('Your choice is "5 - Monthly stats", enter the month you want to see your exponses')
        while(True):
            try:
                month = int(input("Enter the number of the month: "))
                break
            except ValueError:
                print("Incorrect type value, try one more time")
        finance.monthly_stats(month)
    elif value == 6:
        print('Your choice is 5 - "Exit"')
        break
    else:
        print("Incorrent number, try one more time")

        