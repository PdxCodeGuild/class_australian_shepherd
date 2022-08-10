



# card_num = '4556737586899855'
card_num = input('Please enter a card number to see if its valid:  ')

def validate(card_num):
    card_num = list(card_num)
    for i in range(len(card_num)):
        card_num[i] = int(card_num[i])
    print(card_num)


    check_digit = card_num.pop()
    check_digit = str(check_digit)
    print(card_num)

    card_num.reverse()
    print(card_num)


    for i in range(len(card_num)):
        if i % 2 != 1:
       
            card_num[i] = card_num[i] * 2
        

    print(card_num)


    for i in range(len(card_num)):
        if card_num[i] > 9:
            card_num[i] = card_num[i] - 9

    print(card_num)


    total = 0
    for i in card_num:
        total = total + i

    print(total)

    total = list(str(total))
    total_last = total[1]
    print(total_last)


    if check_digit == total_last:
        print('Valid!')
    else:
        print('Not valid')
        return


validate(card_num)