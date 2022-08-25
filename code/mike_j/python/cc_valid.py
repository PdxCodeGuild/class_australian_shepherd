def cc_valid(card_number):

    card_number = list(map(int, str(card_number)))

    check_digit = card_number.pop()

    card_number.reverse()

    card_number[0::2] = [x*2 for x in card_number[0::2]]

    sub_nine = []

    for num in card_number:
        if num > 9:
            sub_nine.append(num - 9)
        else:
            sub_nine.append(num)

    total = sum(sub_nine)

    total = list(map(int, str(total)))

    if total[1] == check_digit:
        return True
    else:
        return False    

user_number = int(input("Please enter card number: "))

if cc_valid(user_number):
    print("Valid!")
else:
    print("Invalid!")