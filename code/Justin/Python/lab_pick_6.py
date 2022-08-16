
import random
def pick_6():
    for i in range(6):
        ticket = [random.randint(1,99) for number in range(6)]
    print(ticket)
    return ticket
winning = pick_6()

def winning_num(winning, ticket):
    win = []
    bal = 0
    for i, index in winning:
        for k, index in ticket:
            if index == index:
                win.append(index)
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
    bal -= 2
    print("balance", bal)
    print('matches', len(win))
    return bal
balance = 0
for plays in range(100):
    current_ticket = pick_6()
    balance += winning_num(winning, current_ticket)
    print('running_bal', balance)
print(balance)