#AVERAGE NUMBERS

from curses.ascii import isalpha

nums = [5, 0, 8, 3, 4, 1, 6]

for num in nums:
  num += num

sum = num

length = len(nums)

average = sum / length

for i in range(length):
  print(nums[i])

print(sum)

print(average)

# v.2

user_nums = []

sum = 0

while True:

  user_input = input("Enter a number or 'done' to quit: ")

  if user_input == 'done':
    break

  elif user_input.isalpha() == True:
    print('INVALID ENTRY!')
    continue
