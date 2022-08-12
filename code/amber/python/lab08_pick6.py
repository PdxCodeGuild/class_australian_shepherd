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
  expenses = 0
  earnings = 0
  total_matches = 0

  while counter < 100000:
    ticket = pick_6()
    counter += 1
    balance -= 2.00
    expenses += 2.00

    match = 0

    for i in range(0, len(ticket)):
      if winning[i] == ticket[i]:
        match += 1
        total_matches += 1

    if match == 6:
      balance += 25000000.00
      earnings += 25000000.00

    elif match == 5:
      balance += 1000000.00
      earnings += 1000000.00

    elif match == 4:
      balance += 50000.00
      earnings += 50000.00

    elif match == 3:
      balance += 100.00
      earnings += 100.00

    elif match == 2:
      balance += 7.00
      earnings += 7.00

    elif match == 1:
      balance += 4.00
      earnings += 4.00

    roi = (earnings - expenses) / expenses # v.2


  print(f'''
    Earnings = {earnings}
    Expenses = {expenses}
    Return on Investment = {roi}
    ''')

  return f'Total matches: {total_matches}, Ending balance: ${balance}'

print(num_matches(winning_ticket, picked_ticket))
