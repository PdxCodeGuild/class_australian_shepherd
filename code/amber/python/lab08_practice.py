# PICK 6

import random

def pick_6():
  nums = []

  while len(nums) < 6:
    nums.append(random.randint(1, 99))

  return nums


winning_ticket = pick_6()

balance = 0.00

picked_ticket = []
