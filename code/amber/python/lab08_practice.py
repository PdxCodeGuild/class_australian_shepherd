# PICK 6

import random

def pick_6():
  nums = []

  while len(nums) < 6:
    nums.append(random.randint(1, 99))

  return nums


winning_ticket = pick_6()

#balance = 0.00

picked_ticket = []


def num_matches(winning, ticket):

  balance = 0.00
  counter = 0

  while counter < 10: # make this 100000 later
    ticket = pick_6()
    counter += 1
    balance -= 2.00
    match = 0

    for i in range(0, len(ticket)):
      if winning[i] == ticket[i]:
        print(f'{winning[i]} and {ticket[i]} match!')
        match += 1











# num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Find how many numbers match
