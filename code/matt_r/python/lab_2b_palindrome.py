



ammount = input('what is the dollar ammount?  :')

ammount = float(ammount)

# print(ammount, type(ammount))

# ammount = 15.89

pennies = ammount*100

# print(pennies)

quart = pennies//25

# print(int(quart))

pennies = pennies-quart*25

# print(int(pennies))

dimes = pennies//10

# print(int(dimes))

pennies = pennies-dimes*10

# print(int(pennies))

nickles = pennies//5

# print(int(nickles))

pennies = pennies-nickles*5

# print(pennies)

penns = pennies

print(f'Your change is {int(quart)} quarters, {int(dimes)} dimes, {int(nickles)} nickles, and {int(penns)} pennies') 