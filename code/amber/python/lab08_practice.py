# PICK 6

import random

def pick_6():
  nums = []

  while len(nums) < 6:
    nums.append(random.randint(1, 99))

  return nums


winning_ticket = pick_6()

picked_ticket = []


def num_matches(winning, ticket):

  balance = 0.00
  counter = 0

  while counter < 100000:
    ticket = pick_6()
    counter += 1
    balance -= 2.00
    match = 0

    for i in range(0, len(ticket)):
      if winning[i] == ticket[i]:
        print(f'{winning[i]} and {ticket[i]} match!')
        match += 1


    if match == 6:
      balance += 25000000.00
      message = f'JACKPOT!!! You got 6 matches and won $25,000,000!'

    elif match == 5:
      balance += 1000000.00
      message = f'You got 5 matches and won $1,000,000!'

    elif match == 4:
      balance += 50000.00
      message = f'You got 4 matches and won $50,000!'

    elif match == 3:
      balance += 100.00
      message = f'You got 3 matches and won $100.00!'

    elif match == 2:
      balance += 7.00
      message = 'You got 2 matches and won $7.00!'

    elif match == 1:
      balance += 4.00
      message = f'You got 1 match and won $4.00!'

    else:
      message = 'Sorry, no matches this time.'

    print(f'''{message}
    Winning numbers = {winning}
     Ticket numbers = {ticket}
    ''')

  return f'Ending balance: ${balance}'

print(num_matches(winning_ticket, picked_ticket))
