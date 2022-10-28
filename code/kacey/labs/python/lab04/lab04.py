# credit card validation

def credit_card_validator(credit_card_number):
    # convert the credit_card_number to a list of strings
    input_list = list(credit_card_number)
    
    # loop over the credit_card_number list(input_list) and convert them to a list of intigers
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
        
        print(input_list, ' this is the input list cc number converted to a list of strings')
        # pull the check digit and assign it to a variable called check_digit via .pop() method
        check_digit = input_list.pop(-1) # 5
        # print(check_digit)
        
        print(input_list, ' this is the input list with the check_digit popped from it')
        # revers the input list after removing the check_digit from it using reverse() method
        input_list.reverse()
        
        print(input_list, ' this is the input list reversed')
        
        # created an empty list to input values with every other digit doubled
        doubled_list = [] 
        
        # loop over the input_list(# the "reversed" input list without the check digit 5 included), loop over it and for every other digit including the first gets doubled
        for i in range(len(input_list)):
            if i % 2 == 0:
                input_list[i] = (int(input_list[i])) * 2
                doubled_list.append(input_list[i])
            else:
                doubled_list.append(int(input_list[i]))
                
        print(doubled_list, ' this is the list with every other digit including the first doubled')
        # assign the double_list to a new variable called subtrac_nine
        subtract_nine = doubled_list
        # for every digit in the subtract_nine(#double_list) that has a value greater than 9, subtract nine from it using a for loop
        for i in range(len(subtract_nine)):
            if (int(subtract_nine[i])) > 9:
                subtract_nine[i] = (subtract_nine[i]) - 9
                
        print(subtract_nine, ' this is the doubled list with every digit over 9 taken and then subtracted 9 from it')
        
        sum_values = sum(subtract_nine)
        
        print(sum_values, ' this is the sum of all the new digits that have been manipluated thus far(#9 subtracted from anything over 9, etc)')
        #assigning second digit variable to the value of the second digit from the sum_value variable
        second_digit = str(sum_values)[1]
        
        print(second_digit)
        
        answer = second_digit == check_digit
        
        return answer
    
user_credit_card_number = input('Please enter a credit card number to check for validation: ').replace(' ', '')
print(credit_card_validator(user_credit_card_number))