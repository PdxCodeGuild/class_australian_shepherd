# Lab 8 Pick6
# Have the computer play pick6 many times and determine net earning.

import random

def pick6(tickets):
    
    ticket_queue = []
    expense = 0
# Start your earning at 0
    earning = 0
   
# Generate a list of 6 random numbers representing the ticket
    for times in range(int(tickets)):
        ticket_nums = []
        for num in range(6):
            ticket_nums.append(random.randint(1,99))
        ticket_queue.append(ticket_nums)
        # print(ticket_nums)
# a ticket costs $2
# Subtract 2 from your earning (you bought a ticket)
        expense -= 2
    print(f'''
    Your change in account balance: {expense} dollars.
    ''')
    
    while True:
        check_ticket = input("Would you like to see if you won? Enter 'Y' to see if you won! ").capitalize()
        if check_ticket == 'Y':
# Generate a list of 6 random numbers representing the winning ticket  
            winning_nums = []
            for num in range(6):
                winning_nums.append(random.randint(1,99))    
            # print(f'\nThe winning numbers are: {winning_nums}\n')
            win_ticket_count = []
# Find how many numbers match
            for ticket in ticket_queue:
                winning_nums_count = 0
                win_count = 0
                for number in ticket:
                    # print(ticket)
                    # print(number)
                    # x = winning_nums[winning_nums_count]
                    # print(x)
                    # print(winning_nums)
                    if number == winning_nums[winning_nums_count]:
                        win_count += 1
                        # print('MATCH!')
                    # else:
                        # print('No match..')
                    winning_nums_count += 1
                win_ticket_count.append(win_count)
                # print(f'Matches for each ticket checked: {win_ticket_count}')
# Add to your earning the winnings from your matches    
            for win in win_ticket_count:
                if win == 0:
                    continue
                    # if 1 number matches, you win $4
                elif win == 1:
                    earning += 4
                    # if 2 numbers match, you win $7
                elif win == 2:
                    earning += 7
                    # if 3 numbers match, you win $100
                elif win == 3:
                    earning += 100
                    # if 4 numbers match, you win $50,000
                elif win == 4:
                    earning += 50000
                    # if 5 numbers match, you win $1,000,000
                elif win == 5:
                    earning += 1000000
                    # if 6 numbers match, you win $25,000,000
                else:
                    earning += 25000000
            balance = expense + earning
# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
# Calculate your ROI, print it out along with your earnings and expenses.
            roi = round((((earning - (expense * -1)) / (expense * -1) * 100)),2)
# After the loop, print the final earning (Hint: This will be negative)
            print(f'''
            Your final change in balance is: {balance} dollars.
            ROI: {roi}%
            ''')
            break


buy_tickets = input('How many tickets do you want??? ')
pick6(buy_tickets)
        
        
 










