# Lab 9 Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards using a Dictionary. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. 
# Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

import random

card_values = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def advice(count, dealer_count):
    if count <= 11: 
        return 'Hit'
    elif count <= 16 and dealer_count <= 6:
        return 'Stay'
    elif count <= 16 and dealer_count > 6:
        return 'Hit'
    else:
        return 'Stay'

def result(count, dealer_count):
    if dealer_count == 21 and count == 21:
        return 'Push!'
    elif count > 21:
        return 'Bust!'
    elif (dealer_count >=17 and dealer_count <22) and count < dealer_count:
        return 'You lost!'
    elif count >=17 and dealer_count > 21:
        return 'You won!'
    else:
        return 'You won!'

user_start = input('\nPress ENTER to deal.')
user_cards = []
dealer_cards = []
if user_start == '':
    while len(user_cards) < 2:
        user_cards.append((random.choice(card_list)))
    dealer_cards.append((random.choice(card_list)))
   
print(f"""
Your cards are: {', '.join(user_cards)}
Dealer face card is: {''.join(dealer_cards)}
""")

sum = 0 
dealer_sum = 0
sum += (card_values[user_cards[0]] + card_values[user_cards[1]])
dealer_sum += (card_values[dealer_cards[0]])

user_advice = advice(sum, dealer_sum)
print(f"Here's some advice: {user_advice}!\n")

second_move = int(input("Enter '1' to STAY or '2' to HIT."))        

if second_move == 1:
    while dealer_sum <= 16:
        dealer_cards.append((random.choice(card_list)))
        dealer_sum += card_values[str(dealer_cards[-1])]        

elif second_move == 2:
    while dealer_sum <= 16:
        dealer_cards.append((random.choice(card_list)))
        dealer_sum += card_values[str(dealer_cards[-1])]
        continue
    user_cards.append((random.choice(card_list)))
    sum += card_values[user_cards[2]]

results = result(sum, dealer_sum)
print(f"""
Your cards are: {', '.join(user_cards)}
Dealer cards are: {', '.join(dealer_cards)}
{results}
""")