# ATM

class ATM:
    def __init__(self, balance, interest, log):
        self.balance = balance
        self.interest = interest
        self.transaction_log = log

    def check_balance(self):
        # Returns account balance
        return self.balance

    def deposit(self, amount):
        # deposits he given amount to the account
        self.balance += amount
        self.transaction_log += f'You deposited ${amount}\n'
        return self.balance

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        if self.balance >= amount:
          return True
        else:
          return False

    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        self.balance -= amount
        self.transaction_log += f'You withdrew ${amount}\n'
        return self.balance

    def calc_interest(self):
        # returns the amount of interest calculated on the account
        self.interest = self.balance * .001
        return self.interest

# v.2
    def print_transactions(self):
        return self.transaction_log


atm = ATM(0, 0, '')  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit',
    '6': 'Transactions'
}

while True:
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
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            #log += f'You deposited ${amount}'
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
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

    elif command == 'Transactions':
        log = atm.print_transactions()  # call the method
        balance = atm.check_balance()  # call the check_balance() method
        print(log)
        print(f'''----------------------------------\nYour current balance is ${balance}.''')

    else:
        print('Command not recognized')
