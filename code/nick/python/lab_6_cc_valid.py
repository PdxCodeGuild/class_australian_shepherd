# Lab 6: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

def validation(cc_number):
# cc_number = '4556737586899855'
# Convert the input string into a list of ints
    number_list = list(cc_number)
    # Slice off the last digit. That is the check digit.
    check_digit = number_list.pop()
    reverse_list = (number_list.copy())
    # Reverse the digits.
    reverse_list.reverse()
    
    new_list = []
    x = 0
    # Double every other element in the reversed list.
    for number in reverse_list:   
        if (x % 2) == 0:
            doubled_num = int(reverse_list[x]) * 2
            new_list.append(doubled_num)
        else:
            new_list.append(number)
        x += 1

    new_new_list = []
    # Subtract nine from numbers over nine.
    for number in new_list:
        if int(number) > 9:
            new_new_list.append(int(number) - 9)
        else:
            new_new_list.append(number)
   
    sum = 0
    # Sum all values.
    for number in new_new_list:
        sum += int(number)
    # Take the second digit of that sum.
    final_list = list(str(sum))
    # If that matches the check digit, the whole card number is valid.
    if final_list[1] == check_digit:
        return True
    else:
        return False

user_cc_number = input('Input CC # here: ')
if validation(user_cc_number) == True:
    print('This is a valid CC number, thank you.')
else:
    print('This CC number is not valid.')
