#          PICK 6        LOTTERRRYYYYY        #


import random
# function that creates ticket numbers(used for both the winning ticket numbers and the purchased lottery ticket)
def pick6():
    ticket_numbers = [] # empty list for the random numbers to be returned to
    for x in range(6): # loop through a total of 6 times for 6 random numbers between 1 and 99
        ticket_numbers.append(random.randint(1, 99)) # add each loops random number to the empty ticket_numbers list
    return ticket_numbers # return the random numbers to the empty ticket_number list
# function that compares both sets of numbers "winning" and "ticket" to return a number of matches
def num_matches(winning, ticket): # function with two parameters of "winning" and "ticket"
    matches = 0 # set the number of matches to 0 to start off with
    
    for number in range(6): #for each number in the comparison, loop through each number and compare each same indice of both tickets to determine matches
        
        if winning[number] == ticket[number]:
            matches += 1 # if the first indice of winning ticket number and first indice of purchased ticket number are a match, then add a counter to matches(loops through all indice spots)
            
    return matches  # return the matches to the matches counter

winning_ticket = pick6() # create the winning_ticket numbers with the pick6() function that's previously been created
earnings = 0 # create a variable for earnings and set it to 0
runs = 100000
expenses = runs * 2

for x in range(runs):
    match_counter = 0
    
    match_counter += num_matches(winning_ticket, pick6())
    
    if match_counter == 1:
        earnings += 4
    elif match_counter == 2:
        earnings += 7
    elif match_counter == 3:
        earnings += 100
    elif match_counter == 4:
        earnings += 50000
    elif match_counter == 5:
        earnings += 1000000
    elif match_counter == 6:
        earnings += 25000000
        
payout = earnings - expenses
print(f"You've won/lost a grand total of {payout} dollars!!!")

#        VERSION 2       #

return_on_investment = (earnings - expenses) / expenses

print(f"You're return on investment was {return_on_investment}!!!")
