# Lab 2b Make Change
# Let's convert a dollar amount into a number of coins. The input will be the total amount, 
# the output will be the number of quarters, dimes, nickles, and pennies. 
# Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
# First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division //, 
# which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# coins_list = [
#     ('half-dollar', 50),
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]


coins_list = [
    {'1': 50,
    '2': 25,
    '3': 10,
    '4': 5,
    '5': 1}
]

# change_left = 0
user_coins_list = []

user_amount = input('''
    How much money do you have? $''' )
user_amount = float(user_amount) * 100

user_coins_message = print('''
    What type of coins do you want to use? Pick from the below list.
    (Type "done" when finished.) ''')    

while True:
    user_coins = input('''
    1-half-dollar
    2-quarter
    3-dime
    4-nickel
    5-penny
    Enter coin #: ''')

    if user_coins == 'done':
        break

    user_coins_list.append(user_coins)
    
# print(user_coins_list)       
for coin in user_coins_list:
    print(coins_list[0][coin])
    print(user_amount)
    change_left = 0
    # print(coins_used)
    # print(change_remaining)
    # print(change_left)
    coins_used = float(user_amount) // float(coins_list[0][coin])
    print(coins_used)
    change_remaining = user_amount - (coins_used * float(coins_list[0][coin]))
    print(change_remaining)
    change_left += round(change_remaining, 2)
    print(change_left)
    if change_remaining == 0:
 
    else:
        more_coins_used = change_left / float(coins_list[0][coin])
        print(coins_list[0][coin])
        print(f'{more_coins_used} is left')
        change_left += round(change_remaining, 2)
        print(change_left)
        if change_remaining == 0:
            break

    

# for coin in coins_list:
#     print(coin)
#     print(coins_list[0]) 
#     print(user_coins_list)
    
    
    
    # if coin in user_coins_list:
    #     if change_left == 0: 
    #         coins_used = float(user_amount) / float(coins_list[0][coin])
    #         change_remaining = coins_used - (float(user_amount) // float(coins_list[0][coin]))
    #         change_left += round(change_remaining, 2)
    #         if change_remaining == 0:
    #             break

    #     else:
    #         change_left / float(coins_list[0][coin])
    #         change_remaining = coins_used - (float(user_amount) // float(coins_list[0][coin]))
    #         change_left += round(change_remaining, 2)
    #         if change_remaining == 0:
    #             break
    # else:
    #     break
        
    
# print(coins_list[0][coin])







