# PICK 6

import random

def pick_6():
  nums = []

  while len(nums) < 6:
    nums.append(random.randint(1, 99))

  return nums
