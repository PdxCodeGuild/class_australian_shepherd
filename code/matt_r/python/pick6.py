



import random

def make_ticket():
    ticket = []
    for x in range(6):
        number = random.randint(1,99)
        ticket.append(number)
    # print(ticket)
    return ticket

winning_ticket = make_ticket()
# print(winning_ticket)

balance = 0
balance = int(balance)

def num_matches(winner, user):
    user = current_ticket
    winner = winning_ticket
    balance = 0
    counter = int(0)

    if winner == user:
        balance = balance + 25000000
        return balance

    if winner[0] == user[0]:
        counter = counter + 1
        # print(counter)
    if winner[4] == user[4]:
        counter = counter
        # print(counter)
    if winner[1] == user[1]:
        counter = counter + 1
        # print(counter)
    if winner[2] == user[2]:
        counter = counter + 1
        # print(counter)
    if winner[3] == user[3]:
        counter = counter + 1
        # print(counter)
    if winner[5] == user[5]:
        counter = counter + 1
        # print(counter)

    # counter = 5


    if counter == 0:
        balance = balance
        # print('0 matches', balance)
    elif counter == 1:
        balance = balance + 4
        # print('1 matched', balance)

    if counter == 2:
        balance = balance + 7
        # print('2 matched', balance)

    if counter == 3:
        balance = balance + 100
        # print('3 matched', balance)

    if counter == 4:
        balance = balance + 50000
        # print('4 matched', balance)

    if counter == 5:
        balance = balance + 1000000
        # print('5 matched', balance)

    return balance
 

# print(balance)

winnings = 0

playes = 100000
ticket_cost = 2

for x in range(playes):
    current_ticket = make_ticket()
    user = current_ticket
    winner = winning_ticket
    winnings += num_matches(winner, user)
    winnings -= ticket_cost
    
    # print('winning', winning_ticket)
    # print('current', current_ticket)
print('end balance', winnings)


###    I know i made the roi part more complicates than it needed to but i was thinking with 'inputs' you can change how many times you play and how much you 'bet' per ticket
earnings = winnings
expenses = playes * ticket_cost
roi = (earnings - expenses)/expenses

print(f'Your ROI is.: {roi}')
