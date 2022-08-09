'''
benjamin_birky
08/04/2022
lab06b_CreditCardValidation
'''


#-------step 1. Convert the input string into a list of ints

card_number = input("Please enter a 16-digit credit card number: ")
card_number = card_number.replace(' ','')
card_listNumber = list(card_number)

for num in range(len(card_listNumber)):
    card_listNumber[num] = int(card_listNumber[num])

#-------step 2. Slice off the last digit. That is the check digit.

last_digit = card_listNumber.pop()

#-------step 3. Reverse the digits.

card_listNumber.reverse()

#-------step 4. Double every other element in the reversed list.

for num in range(0, len(card_listNumber), 2):
    card_listNumber[num] = card_listNumber[num] * 2

#-------step 5. Subtract nine from numbers over nine.

for num in range(0, len(card_listNumber)):
    if card_listNumber[num] > 9:
        card_listNumber[num] = card_listNumber[num] - 9

#-------step 6. Sum all values.

num_sum = 0

for num in range(0, len(card_listNumber)):
    num_sum += card_listNumber[num]

#-------step 7. Take the second digit of that sum.

second_digit = num_sum % 10

#-------step 8. If that matches the check digit, the whole card number is valid.

if second_digit != last_digit:
    print("Not a valid number")
else:
    print("Valid number")