
import random
# Defining a function to draw our 6 random numbers


def pick_6():
    for i in range(6):
        ticket = [random.randint(1, 99) for number in range(6)]
    return ticket


winning = pick_6()
ticket = pick_6()
# Creating empty dictionaries to store our pulls
wins = {}
ticks = {}
# Creating a function to loop through our pulls to check for winning numbers


def winning_num(wins, ticks):
    win = {}
    bal = 0
    # Using a for loop to check our dictionaries to check for matching numbers
    for key in wins:
        if (key in ticks) and (wins[key] == ticks[key]):
            win[key] = ticks[key]
    # Using if/elif statments to determine our winning amount
    if len(win) == 1:
        bal += 4
    elif len(win) == 2:
        bal += 7
    elif len(win) == 3:
        bal += 100
    elif len(win) == 4:
        bal += 50000
    elif len(win) == 5:
        bal += 1000000
    elif len(win) == 6:
        bal += 25000000
    return bal


# Creating an empty balance to store of final value of our tickets
balance = 0
# Creating a for loop to determine the number of plays
num_tickets = 0
num_plays = int(
    input('Enter the number of tickets you would like to purchase: '))
num_tickets += num_plays
for plays in range(num_tickets):
    ticket = pick_6()
    # Storing our index and elements inside of our empty dictionaries
    for index, element in enumerate(ticket):
        wins[index] = element
    for index, element in enumerate(winning):
        ticks[index] = element
    # Keeping our running balance of our tickets
    balance += winning_num(wins, ticks)
    winnings = balance
expenses = 2 * num_plays
roi = (winnings - expenses)/expenses * 100


def statement():
    if roi < 0:
        return 'Better luck next time.'
    else:
        return 'Winner, winner, chicken dinner.'


print(f'''          Pick 6 Lotto
--------------------------------
Your total winnings comes to ${winnings}.
Your total expenses are ${expenses}.
Your return on investment is {roi}%
Your final balance is ${balance-expenses}.
{statement()}''')
