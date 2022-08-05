# CREDIT CARD VALIDATION

user_cc = input('Please enter your credit card number: ')

def cc_validator(cc_num):

  cc_num_list = list(cc_num)
  for i in range(len(cc_num_list)):
    cc_num_list[i] = int(cc_num_list[i])

  check_digit = []
  check_digit.append(cc_num_list.pop())

  reversed_digits = []
  for i in range(len(cc_num_list)):
    reversed_digits.append(cc_num_list.pop())

  for i in range(0, len(reversed_digits), 2):
    reversed_digits[i] *= 2

  for i in range(len(reversed_digits)):
    if reversed_digits[i] > 9:
      reversed_digits[i] -= 9

  sum = 0
  for i in range(len(reversed_digits)):
    sum += reversed_digits[i]

  split_sum = list(str(sum))
  for i in range(len(split_sum)):
    split_sum[i] = int(split_sum[i])

  sum_digit = []

  sum_digit.append(split_sum.pop())

  if sum_digit == check_digit:
    return True

if cc_validator(user_cc) == True:
  print('Valid!')

'''
user_cc = input('Please enter your credit card number: ')

def cc_validator(cc_num):

# Convert the input string into a list of ints

  cc_num_list = list(cc_num)
  for i in range(len(cc_num_list)):
    cc_num_list[i] = int(cc_num_list[i])

  print(cc_num_list)

# Slice off the last digit. That is the check digit.

  check_digit = []
  check_digit.append(cc_num_list.pop())

  print(check_digit)

# Reverse the digits.

  reversed_digits = []
  for i in range(len(cc_num_list)):
    reversed_digits.append(cc_num_list.pop())

  print(reversed_digits)

# Double every other element in the reversed list.

  for i in range(0, len(reversed_digits), 2):
    reversed_digits[i] *= 2

  print(reversed_digits)

# Subtract nine from numbers over nine.

  for i in range(len(reversed_digits)):
    if reversed_digits[i] > 9:
      reversed_digits[i] -= 9

  print(reversed_digits)

# Sum all values.

  sum = 0
  for i in range(len(reversed_digits)):
    sum += reversed_digits[i]

  print(sum)

# Take the second digit of that sum.

  split_sum = list(str(sum))
  for i in range(len(split_sum)):
    split_sum[i] = int(split_sum[i])

  print(split_sum)


  sum_digit = []

  sum_digit.append(split_sum.pop())


  print(sum_digit, type(sum_digit))

# If that matches the check digit, the whole card number is valid.

  if sum_digit == check_digit:
    return True

if cc_validator(user_cc) == True:
  print('Valid!')
'''
