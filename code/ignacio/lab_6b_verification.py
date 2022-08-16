def credit_card_verification():
    step_1 = []

    cc = (input('Enter credit card number: '))
    # cc = '4556737586899855'


    cc_list = list(cc)

    check_digit = cc_list.pop()

    reverse_check = cc_list
    reverse_check.reverse()

    for index in range(len(cc_list)):
        if index % 2 == 0:
            cc_list[index] = int(cc_list[index]) * 2
        else:
            index % 2 == 1
            cc_list[index] = int(cc_list[index])

    for i in range(len(cc_list)):
        if cc_list[i] >= 10:
            cc_list[i] -= 9

    cc_list = sum(cc_list)

    cc_list = cc_list % 10
    # print(cc_list)
    check_digit = int(check_digit)
    if cc_list == check_digit:
        outcome = 'valid'
        print(outcome)
    else:
        print('invalid')

credit_card_verification()