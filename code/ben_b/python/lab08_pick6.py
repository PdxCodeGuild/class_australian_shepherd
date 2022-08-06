'''
benjamin_birky
08/04/2022
lab08_pick6
'''
import random


winning_ticket = [0, 0, 0, 0, 0, 0,]
my_ticket = [0, 0, 0, 0, 0, 0,]
balance = 0
counter = 0
earnings = 0
roi = 0

prizes = (
    (0, 0),
    (1, 4),
    (2, 7),
    (3, 100),
    (4, 50000),
    (5, 1000000),
    (6, 25000000),
)



def ticket_generator(ticket):
    

    for num in range(6):
        ticket[num] = random.randint(1, 99)

    return ticket
    
iteration = 0

while iteration < 100000:
    ticket_generator(my_ticket)
    ticket_generator(winning_ticket)

    for num in range(6):
            
        if winning_ticket[num] == my_ticket[num]:
            counter += 1
    
    for num in reversed(range(1, 7)):
        if counter == prizes[num][0]:
            balance += prizes[num][1]
            earnings += prizes[num][1]
            continue
    counter = 0
    balance -= 2
    iteration += 1

roi = (earnings - 200000) / 200000

print(f"BALANCE: ${balance}   ROI: {roi}%")






