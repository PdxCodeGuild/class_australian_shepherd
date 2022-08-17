# Generate a list of 6 random numbers representing the winning ticket

import random

# winning_ticket = []
# for item in range(6):
#     winning_ticket.append(random.randint(0, 99))
# print(winning_ticket)
# ----------------------------------------------
# functions

def pick6():
    winning_ticket = []
    for item in range(6):
        winning_ticket.append(random.randint(0, 99))
    return winning_ticket
# # used this for winning ticket and my ticket

winning_ticket = pick6()
player_ticket = pick6()

def num_matches(winning, ticket):
    matches = 0
    for index in range(len(player_ticket)):
        if player_ticket[index] == winning_ticket[index]:
            matches += 1
    return matches
print(num_matches(winning_ticket, player_ticket))


# # ----------------------------------------------
# # Start your balance at 0
winnings = 0

# # Loop 100,000 times, for each loop:
while

# # Generate a list of 6 random numbers representing the ticket
# my_ticket = []

# # Subtract 2 from your balance (you bought a ticket)
# winnings -= winnings

# # Find how many numbers match
# winning_ticket == my_ticket

# # Add to your balance the winnings from your matches


# # After the loop, print the final balance (Hint: This will be negative)

