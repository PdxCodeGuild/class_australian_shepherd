# Creating our function to check if a credit card is valid or not
def check_card():
    # setting a blank total to run a for loop to append the enter number to our function in a list
    tot = []
    for num in cc_num:
        tot.append(num)
    # slicing the last didit our of credit card and then using the .pop() method to remove the last digit
    check_digit = tot[-1]
    tot.pop()
    # slicing to reverse our credit card number
    cc_rev = tot[::-1]
    # Setting an empty list to double our reversed credit card number then using the index of the number to double every other number.
    doub = []
    for index, element in enumerate(cc_rev):
        # Using an if/else statment to append each number to our list
        if index % 2 == 0:
            element = int(element)
            element = element * 2
            doub.append(element)
        else:
            element = int(element)
            doub.append(element)
    # Creating a new empty list to append our numbers too
    new = []
    for nums in doub:
        # Using an if/else statement to append each item to our list, while subtracting 9 from each number over 9
        if nums > 9:
            nums = nums - 9
            new.append(nums)
        else:
            new.append(nums)
    sums = 0
    # Using a for list to sum all the numbers in our list together
    for num in new:
        sums += num
    # Using an if statement to check our sums number second digit compared to our check_digit
    if str(check_digit) == str(sums)[-1]:
        print('Card is valid')
    else:
        print('Card is not valid')
# Using a try/except statement to ensure if the user includes non integer characters there is no handling exception
try:
    tries = 0
    while True:
        # Creating our using input to take a credit card number
        c_num = input('Please enter your card number: ').replace(' ', '')
        cc_num = []
        for dig in c_num:
            cc_num.append(dig)
        if len(cc_num) != 16:
            print(f'Credit card number does not contain the correct amount of digits, you have {2-tries} attempts left.')
            tries += 1
            if tries == 3:
                print('Sorry, you have exceeded the max amount of tries. Goodbye')
                break
        else:
            check_card()
            break
except:
    print('Please enter a valid credit card number.')
