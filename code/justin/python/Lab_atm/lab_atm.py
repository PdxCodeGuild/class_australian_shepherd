# Creating our class
class ATM:
    def __init__(self, balance = 0):
        self.balance = balance

    def check_balance(self):
        pass

    # Creating a function(class method) to deposit a certain amount of money into our ATM
    def deposit(self, amount):
        self.amount = amount
        if amount > 0:
            self.balance = self.balance + self.amount
            return True

    # Creating a function(class method) to check if the amount of requested withdraw can be covered by our current balance
    def check_withdrawal(self, amount):
        self.amount = amount
        if self.amount <= self.balance:
            return True

    # Creating a function(class method) to with draw an amount from our balance
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        return self.balance

    # Creating a function(class method) to calculate our interested based on our current balance
    def calc_interest(self, interest = 0.001):
        self.interest = interest
        return self.balance * interest

# create an instance of our class
atm = ATM()
print('Welcome to the ATM')

# Using a dictionary to iterate through to select our options from
menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
}

# Using a while loop to let the user continue with their transaction until they are finished
while True:
    print()
    # Using a for loop to print our key and value
    for label, option in menu_options.items():
        print(f'{label}. {option}')
    #Taking a user input to select which option they want to use
    command = input(
        '\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    # Using if/elif/else statements to let the user select from the list and calling our methods depending on the selection
    if command == 'Balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${atm.balance}')

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount) # call our deposit() method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount) # Calling our check_withdraw() function
        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)# Calling our withdraw() function if our check_withdraw() passes
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount) # Calling our deposit() method to deposit our interest into our account
        print(f'Accumulated ${round(amount, 2)} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')