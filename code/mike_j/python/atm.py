class ATM:
    def __init__(self):
        self.balance = 0.0
        self.interest_rate = 0.001

    def check_balance(self):
        return round(self.balance, 2)

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
        interest = (round(self.balance * self.interest_rate, 2))
        return interest

atm = ATM() 
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
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
        balance = atm.check_balance()
        print(f'Your balance is ${balance}')

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        attempt = atm.deposit(amount) 
        if not attempt:
            print("Deposit amount must be a positive number.")
        else:
            deposit_amount = f'User deposited ${amount}'
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        attempt = atm.check_withdrawal(amount)

        if not attempt:
            print('Insufficient funds')
        else:
            withdraw_amount = f'User withdrew ${amount}'
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest() 
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized') 