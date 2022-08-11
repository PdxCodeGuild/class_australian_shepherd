import random

card1= input("Enter your first card: ")
card2= input("Enter your second card: ")
card3= input("Enter your third card: ")
player_hand= card1, card2, card3

deck= {
    'A': 1,
    'K': 10,
    'Q': 10,
    'J': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10
}

for i in deck:
    i= player_hand[deck]
    print(player_hand)




