import json

def run_app(u):
    print('Welcome to the tracker!')
    
    expense_list = []

    while True:
        amount = (input('Enter your expense amount or type "done" to exit: '))

        if amount.lower() == 'done':
            break

        try:
            expense = float(amount)
            description = input('Enter the description of your expense: ')

            entry = {"amount": expense, "desc": description}
            expense_list.append(entry)
        except ValueError:
            print("Please enter a valid amount!")

    final_data = {
        "uname": u,
        "expenses": expense_list
    }

    with open('./Projects/Secure CLI Expense Tracker/expense_data.txt', 'w') as file:
        json.dump(final_data, file, indent=4)

    print("\nExpense Added!")
    print(final_data)
    return final_data