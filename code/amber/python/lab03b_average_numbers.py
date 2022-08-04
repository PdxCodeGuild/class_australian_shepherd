#AVERAGE NUMBERS

import string

nums = [5, 0, 8, 3, 4, 1, 6]

sum = 0

for num in nums:
  sum += num
print(sum)

length = len(nums)

average = sum / length

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

  user_int = int(user_input)

  user_nums.append(user_int)

  sum += user_int

  length = len(user_nums)

  average = sum / length

print(f'''
numbers: {user_nums}
sum: {sum}
length: {length}
average: {average}
''')
