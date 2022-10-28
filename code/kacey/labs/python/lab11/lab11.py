class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"User deposited ${amount}")
        return self.balance

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        return True

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.transactions.append(f"User withdrew $-{amount}")
        return self.balance

    def calc_interest(self):
        calc_interest = (self.balance * 0.1) / 100
        atm.deposit(calc_interest)
        self.transactions.append(f"<---- 'In Interest'")
        return round(calc_interest, 2)

    def print_transactions(self):
        # for transaction in self.transactions:
        #     self.transactions.append(transaction)
        print(self.transactions)


atm = ATM()  # create an instance of our class
print("Welcome to the ATM")

menu_options = {
    "1": "Balance",
    "2": "Deposit",
    "3": "Withdraw",
    "4": "Interest",
    "5": "Transactions",
    "6": "Exit",
}

while True:
    print()
    for label, option in menu_options.items():
        print(f"{label}. {option}")

    command = input("\nEnter the number of the option you would like to perform\n> ")
    command = menu_options.get(command)

    if command == "Balance":
        balance = atm.check_balance()  # call the check_balance() method
        print(f"Your balance is ${balance}")

    elif command == "Deposit":
        amount = float(input("How much would you like to deposit? "))
        success = atm.deposit(amount)  # call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f"Deposited ${amount}")

    elif command == "Withdraw":
        amount = float(input("How much would you like to withdraw?\n> $"))
        success = atm.check_withdrawal(amount)

        if not success:  # False
            print("Insufficient funds")
        else:  # True
            atm.withdraw(amount)
            print(f"Withdrew ${amount}")

    elif command == "Interest":
        amount = atm.calc_interest()  # call the calc_interest() method
        # atm.calc_interest()
        # print(f"Accumulated ${amount} in interest")

    elif command == "Transactions":
        # transactions = atm.transactions()
        # print(f"{self.transaction}")
        atm.print_transactions()
        # print(transactions)

    elif command == "Exit":
        print("Goodbye!")
        break

    else:
        print("Command not recognized")
