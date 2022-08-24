# Pick6

import random

def pick6():
  numbers = []

  while len(numbers) < 6:
    numbers.append(random.randint(1, 99))

  return numbers

winning_ticket = pick6()

player_ticket = []

def num_matches(winning_ticket, ticket):

  balance = 0.00
  attempts = 0
  expenses = 0.00
  earnings = 0.00
  total_matches = 0

  while attempts < 100000:
    ticket = pick6()
    attempts += 1
    balance -= 2.00
    expenses += 2.00

    match = 0

    for i in range(0, len(ticket)):
      if winning_ticket[i] == ticket[i]:
        match += 1
        total_matches += 1

    if match == 1:
      balance += 4.00
      earnings += 4.00

    elif match == 2:
      balance += 7.00
      earnings += 7.00

    elif match == 3:
      balance += 100.00
      earnings += 100.00

    elif match == 4:
      balance += 50000.00
      earnings += 50000.00

    elif match == 5:
      balance += 1000000.00
      earnings += 1000000.00

    elif match == 6:
      balance += 25000000.00
      earnings += 25000000.00

    roi = (earnings - expenses) / expenses

  print("Earnings: " + str(earnings))
  print("Expenses: " + str(expenses))
  print("Return on investment: " + str(roi))

  return ("Total matches: " + str(total_matches), ("Ending balance: " +str(balance)))
  
print(num_matches(winning_ticket, player_ticket))