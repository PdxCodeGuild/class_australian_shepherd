# Lab 12: ATM

# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
# Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account
import random
import time

class ATM:
    def __init__(self, name, transactions, timestamp):
        self.name = name
        self.timestamp = timestamp
        initial = random.randint(500, 1000)
        self.transactions = transactions
        if name not in transactions:
            transactions[name] = {f'{timestamp} Initial balance': initial}
        pass

    def check_balance(self):
        transaction_list = []
        for amount in transactions[name].values():
            transaction_list.append(amount)
        total = sum(transaction_list)
        return total
        # Returns account balance

    def deposit(self, amount):
        if amount > 0:
            transactions[name].update({f'{timestamp} Deposit': amount})
            return True
        else:
            return False
        # deposits the given amount to the account

    def check_withdrawal(self, amount):
        if (amount < 0) or (amount > (atm.check_balance())):
            return False
        else:
            return True
        # returns true if the withdrawn amount won't put the account in the negative

    def withdraw(self, amount):
        transactions[name].update({f'{timestamp} Withdraw': (amount * -1)})
        # withdraws the amount from the account and returns the amount
        pass

    def calc_interest(self):
        interest = (0.1/100) * (atm.check_balance())
        return round(interest, 2)
        # returns the amount of interest calculated on the account

# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
# Add a new method print_transactions() to your class for printing out the list of transactions.
    def print_transaction(self):
        transactions_list = []
        for transaction_type, amount in transactions[name].items():
            individual_item = []
            individual_item.append(transaction_type)
            individual_item.append(amount)
            transactions_list.append(individual_item)
        return transactions_list

# To mark transactions with timestamp
unix_time = time.time()
timestamp = time.ctime(unix_time)
  
print('Welcome to the ATM')
name = input('What is your name? ').title()
transactions = {}
atm = ATM(name, transactions, timestamp) # create an instance of our class
print(transactions)

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Transaction Summary', 
    '6': 'Exit'
}

while True:
    unix_time = time.time()
    timestamp = time.ctime(unix_time)
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input(
        '\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount)  # call the deposit(amount) method
        if success == False:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if success == False:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break

    elif command == 'Transaction Summary':
        for item in atm.print_transaction():
            print(f'{item[0]}: ${item[1]}')

    else:
        print('Command not recognized')