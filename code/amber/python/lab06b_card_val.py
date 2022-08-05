# CREDIT CARD VALIDATION

user_cc = '4556737586899855'

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

  sum_digit = int(split_sum[-1])

  if sum_digit == check_digit:
    return True
