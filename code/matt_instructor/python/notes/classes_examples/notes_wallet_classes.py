

class Wallet:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.money_spent = 0

    def spend_money(self, money_spent):
        if self.money >= money_spent:
            self.money -= money_spent
            self.money_spent += money_spent
            return True
        return False


name = input("What is your name: ")
money = int(input("How much money do you have on you? "))

wallet = Wallet(name, money)

print(f"\nYou, {name} have $ {money}")


print('\nYou get a craving for swedish fish. Something about those tiny little sour children make you go to the store at 3am')
amount = int(input("Each Sour Patch Bag costs $1. How many do you want to buy: "))

if wallet.spend_money(amount) == True:
    print(f'\nYou spent $ {wallet.money_spent} and have a remanding balance of ${wallet.money}')
else:
    print(f'\nYou tried to spend ${amount}, but you only have ${wallet.money} available')
 
