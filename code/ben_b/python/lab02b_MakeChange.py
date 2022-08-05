'''
benjamin_birky
08/03/2022
lab02b_MakeChange
'''

#-----------------------------Version 1-------------------------------------

'''
dollar_amount = input("Enter a dollar amount: $")
dollar_amount = float(dollar_amount)
dollar_amount = dollar_amount * 100
dollar_amount = int(dollar_amount)

quarters = dollar_amount // 25
dollar_amount = dollar_amount - (quarters * 25)

dimes = dollar_amount // 10
dollar_amount = dollar_amount - (dimes * 10)

nickels = dollar_amount // 5
dollar_amount = dollar_amount - (nickels * 5)

pennies = dollar_amount

print(f"\nThe quantity of coins are... \n{quarters} Quarters \n{dimes} Dimes \n{nickels} Nickels \n{pennies} Pennies ")
'''

#-----------------------------Version 2-------------------------------------

dollar_amount = input("Enter a dollar amount: $")
dollar_amount = float(dollar_amount)
dollar_amount = dollar_amount * 100
dollar_amount = int(dollar_amount)

coins = []

quarters = dollar_amount // 25
dollar_amount = dollar_amount - (quarters * 25)
#coins[0[0]] += 'Quarters'
#coins[0[1]] += quarters

dimes = dollar_amount // 10
dollar_amount = dollar_amount - (dimes * 10)

nickels = dollar_amount // 5
dollar_amount = dollar_amount - (nickels * 5)

pennies = dollar_amount

print(f"\nThe quantity of coins are... \n{quarters} Quarters \n{dimes} Dimes \n{nickels} Nickels \n{pennies} Pennies ")


