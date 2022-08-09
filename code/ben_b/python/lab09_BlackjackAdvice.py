'''
benjamin_birky
08/05/2022
lab09_BlackjackAdvice
'''
import random

card = ''
suit = ''

# dict of card values
card_value = {
    "o" : 0,
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

# generating a random card function, outputting a (str, int) tuple
def randomCard(random_int):
    random_int = random.randint(1, 13)
    if random_int == 13:
        random_str = 'K'
    elif random_int == 12:
        random_str = 'Q'
    elif random_int == 11:
        random_str = 'J'
    elif random_int == 10:
        random_str = '10'
    elif random_int == 9:
        random_str = '9'
    elif random_int == 8:
        random_str = '8'
    elif random_int == 7:
        random_str = '7'
    elif random_int == 6:
        random_str = '6'
    elif random_int == 5:
        random_str = '5'
    elif random_int == 4:
        random_str = '4'
    elif random_int == 3:
        random_str = '3'
    elif random_int == 2:
        random_str = '2'
    else:
        random_str = 'A'
    return random_str, random_int

# generate random suits function
def randomSuits(random_suit):
    random_suit = ('♦','♠','♥','♣')
    temp_int = random.randint(0, 3)
    suit = random_suit[temp_int]
    return suit

# advice function based off player score
def scoreAdvice(score_int):
    if score < 17:
        return "Dealer advice: Hit"
    elif score >= 17 and score < 21:
        return "Dealer advice: Stand"
    else:
        return

# generate cards for the player; calculate player score; allow the player to 'hit' or 'stand' 
player_card1 = randomCard(card)
player_card2 = randomCard(card)
score = card_value.get(player_card1[0]) + card_value.get(player_card2[0])
print(f"{player_card1[0]}{randomSuits(suit)}  {player_card2[0]}{randomSuits(suit)}\n*Score*: {score}")

while score < 21:
    print(scoreAdvice(score))
    next_move = input("Hit or Stand?: ").lower()
    if next_move == 'hit':
        next_card = randomCard(card)
        score += card_value.get(next_card[0])
        print(f"{next_card[0]}{randomSuits(suit)}")
        print(f"*Score*: {score}")
    elif next_move != 'hit':
        print(f"*Final Score*: {score}")
        break
    if score == 21:
        print("\n\U0001F60E \U0001F60E \U0001F60E \U0001F60E !BLACKJACK! \U0001F60E \U0001F60E \U0001F60E \U0001F60E\n")
        break
    elif score > 21:
        print("\n\U0001F4A9 \U0001F4A9 \U0001F4A9 \U0001F4A9 !BUST! \U0001F4A9 \U0001F4A9 \U0001F4A9 \U0001F4A9\n")
        break


  









