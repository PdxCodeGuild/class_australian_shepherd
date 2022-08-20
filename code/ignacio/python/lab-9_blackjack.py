def int_converter(card):
    if card == 'a':
        card = 1
    elif card == '2':
        card = 2
    elif card == '3':
        card = 3
    elif card == '4':
        card = 4
    elif card == '5':
        card = 5
    elif card == '6':
        card= 6
    elif card == '7':
        card= 7
    elif card == '8':
        card = 8
    elif card == '9':
        card = 9
    elif card == '10':
        card = 10
    elif card == 'j':
        card = 10
    elif card == 'q':
        card = 10
    elif card == 'k':
        card = 10
    return card

card1 = input("What is your first card?: ")
card2 = input("What is your second card?: ")
card3 = input("What is your third card?: ")

card1 = int_converter(card1)
card2 = int_converter(card2)
card3 = int_converter(card3)

hand = card1 + card2 + card3


if hand < 17:
    advice = "Hit"
elif hand > 21:
    advice = "Already Busted"
elif hand == 21:
    advice = "Blackjack!!!"
else:
    advice = "Stay"
print(hand, advice)