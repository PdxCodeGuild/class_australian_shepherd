# Initial Commit
#         VERSION 1        #

while True:

    print("Welcome to the change maker 5000!!! (TM)")

    dollar_amount = ""
    while type(dollar_amount) != float:
        dollar_amount = input("Enter a dollar amount: ")

        try:
            dollar_amount = float(dollar_amount)

        except:
            print(f'Please enter a valid float: example --> "1.57"')
    original_dollar_amount = dollar_amount
    # total amount converted to pennies
    dollar_amount = dollar_amount * 100
    # print(dollar_amount, ' dollar amount in pennies(x100)')

    #  Half dollars
    half_dollars = dollar_amount // 50
    # print(half_dollars, ' floor division of dollar_amount by 50')
    dollar_amount = dollar_amount % 50
    # print(half_dollars, ' these are half dollars')  # giving 7 remaining pennies(or just the remainder of pennies)

    # Quarters
    quarters = dollar_amount // 25
    # print(quarters, ' these are quarters')
    dollar_amount = dollar_amount % 25

    # Dimes
    dimes = dollar_amount // 10
    # print(dimes, ' these are dimes')
    dollar_amount = dollar_amount % 10

    # Nickles
    nickels = dollar_amount // 5
    # print(nickels, ' these are nickels')
    dollar_amount = dollar_amount % 5

    # Pennies
    pennies = dollar_amount // 1
    # print(pennies, ' these are the pennies')
    dollar_amount = dollar_amount % 1
    print(
        f"There are {half_dollars} half dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies in ${original_dollar_amount}"
    )
    break

print("\n\n\n VERSION 2 \n\n\n")


#      VERSION       2   #

coins = [
    ("quarter", 25),
    ("dime", 10),
    ("nickel", 5),
    ("penny", 1),
]

dollar_amount = input("Please enter a dollar amount: ")
pennies = float(dollar_amount) * 100

quarters = pennies // coins[0][1]
pennies = pennies % coins[0][1]

dimes = pennies // coins[1][1]
pennies = pennies % coins[1][1]

nickles = pennies // coins[2][1]
pennies = pennies % coins[2][1]

print(
    f"{dollar_amount}, {coins[0][0]}: {quarters}, {coins[1][0]}: {dimes}, {coins[2][0]}: {nickles}, {coins[3][0]}: {pennies}"
)
