import random

card_value= {
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

card1= card_value[input("What's the first card?").upper()]
card2= card_value[input("What's the second card?").upper()]
card3= card_value[input("What's the third card?").upper()]

card_total= card1 + card2 + card3

if card_total < 17:
    print(card_total, "Hit")
elif card_total >= 17 and card_total < 21: #correction from > 21 to < 21
    print(card_total, "Stay Put!")
elif card_total == 21:
    print(card_total, "Blackjack!")
else:
    card_total > 21
    print(card_total, "Already Busted, house wins!")















