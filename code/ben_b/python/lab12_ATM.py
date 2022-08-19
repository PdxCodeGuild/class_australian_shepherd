'''
benjamin_birky
08/18/2022
lab12_ATM
'''

class ATM:
    def __init__(self):
        self.balance = 0.0
        self.interest_rate = 0.001

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount

    def calc_interest(self):
        interest_earned = self.balance * self.interest_rate
        return interest_earned

    def print_transactions(self):
        return transactions

transactions = []
atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Print Transactions',
    '6': 'Exit'
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
        attempt = atm.deposit(amount)  # call the deposit(amount) method
        if not attempt:
            print("Deposit amount must be a positive number.")
        else:
            deposit_amount = f'User deposited ${amount}'
            transactions.append(deposit_amount)
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        attempt = atm.check_withdrawal(amount)

        if not attempt:
            print('Insufficient funds')
        else:
            withdraw_amount = f'User withdrew ${amount}'
            transactions.append(withdraw_amount)
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Print Transactions':
        print(atm.print_transactions())

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')