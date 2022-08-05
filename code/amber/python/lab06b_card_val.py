# CREDIT CARD VALIDATION

user_cc = input('Please enter your credit card number: ')

def cc_validator(cc_num):

  cc_num_list = list(cc_num)
  for i in range(len(cc_num_list)):
    cc_num_list[i] = int(cc_num_list[i])

  print(cc_num_list)


  check_digit = []
  check_digit.append(cc_num_list.pop())

  print(check_digit)


  reversed_digits = []
  for i in range(len(cc_num_list)):
    reversed_digits.append(cc_num_list.pop())

  print(reversed_digits)

  for i in range(0, len(reversed_digits), 2):
    reversed_digits[i] *= 2

  print(reversed_digits)


  for i in range(len(reversed_digits)):
    if reversed_digits[i] > 9:
      reversed_digits[i] -= 9


  print(reversed_digits)

  sum = 0
  for i in range(len(reversed_digits)):
    sum += reversed_digits[i]

  print(sum)


  split_sum = list(str(sum))
  for i in range(len(split_sum)):
    split_sum[i] = int(split_sum[i])

  print(split_sum)


  sum_digit = []

  sum_digit.append(split_sum.pop())


  print(sum_digit, type(sum_digit))


  if sum_digit == check_digit:
    return True

if cc_validator(user_cc) == True:
  print('Valid!')
