import random

def pick6():
    winning_number = []
    for item in range(6):
        winning_number.append(random.randint(0, 99))
    return winning_number

winning_nunber= pick6()
player_ticket = pick6()

def num_matches(winner, user):
    user = player_ticket
    winner = winning_nunber
    balance = 0
    counter = int(0)

    if winner == user:
        balance = balance + 25000000
        return balance

    if winner[0] == user[0]:
        counter = counter + 1

    if winner[1] == user[1]:
        counter = counter + 1

    if winner[2] == user[2]:
        counter = counter + 1

    if winner[3] == user[3]:
        counter = counter + 1

    if winner[4] == user[4]:
        counter = counter

    if winner[5] == user[5]:
        counter = counter + 1


    if counter == 0:
        balance = balance

    elif counter == 1:
        balance = balance + 4

    if counter == 2:
        balance = balance + 7

    if counter == 3:
        balance = balance + 100

    if counter == 4:
        balance = balance + 50000

    if counter == 5:
        balance = balance + 1000000

    return balance

winnings = 0
playes = 100000
ticket_cost = 2

for x in range(playes):
    user = player_ticket
    winner = winning_nunber
    winnings += num_matches(winner, user)
    winnings -= ticket_cost


print('end balance', winnings)

earnings = winnings
expenses = playes * ticket_cost
roi = (earnings - expenses)/expenses

print(f'Your ROI is.: {roi}')