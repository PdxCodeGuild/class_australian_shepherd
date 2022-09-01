class ATM:
    def __init__(self):
        self.interest= 0.001
        self.balance= 0
        
    
    # Returns account balance
    def check_balance(self):
        return self.balance
        
        
       

    # deposits the given amount to the account    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True
        
    # withdraws the amount from the account and returns the amount
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
        
       
    
    # returns the amount of interest calculated on the account
    def calc_interest(self):
        return self.balance * self.interest
        

        
atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
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

    else:
        print('Command not recognized')
