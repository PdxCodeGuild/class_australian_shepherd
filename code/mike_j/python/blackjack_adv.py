# Blackjack Advice

card_value = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
 }

first = input("What's your first card?: ")
second = input("What's your second card?: ")
third = input("What's your third card?: ")

total = (card_value[first] + (card_value[second] + card_value[third]))

if total == 21:
    print(total, "Blackjack!")    
elif total > 21:
    print(total, "Busted!")
elif total < 17:
    print(total, "Hit")
elif total > 17 or total == 17:
    print(total, "Stay")