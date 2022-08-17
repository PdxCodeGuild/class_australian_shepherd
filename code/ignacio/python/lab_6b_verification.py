step_1 = []

cc = (input('Enter credit card number: '))
# cc = '123456789'

# print(step_1)

# Convert the input string into a list of ints
cc_list = list(cc)

# Slice off the last digit. That is the check digit.
check_digit = cc_list.pop()
print(cc_list)
# Reverse the digits.

# Double every other element in the reversed list.
# think about it carefully
# Subtract nine from numbers over nine.

# Sum all values.

# Take the second digit of that sum.

# If that matches the check digit, the whole card number is valid.