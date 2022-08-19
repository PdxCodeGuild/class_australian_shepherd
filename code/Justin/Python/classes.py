
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# your_car = Car('Subaru', 'WRX')

# print(your_car.make)

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

name = input('What is your name: ')
money = int(input("How much money do you have on you? "))

wallet = Wallet(name, money)
print(f'My name is {name} and I have {money}$ in my wallet.')
amount = int(input('this thing costs like 1$. How many do you want to buy?'))
if wallet.spend_money(amount) == True:
    print(f'Spent {wallet.money_spent}{wallet.money}')
else:
    print('no')