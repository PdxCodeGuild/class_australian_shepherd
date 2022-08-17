import random

#I think I need create a deck that accesses the dict. And maybe some appends to account for the fact that blackjack is played w// multiple decks??
#I know I want to create a function that plays the game as well as creating a deck of cards correctly.
#I think I need to establish a global variable so the function will pull BOTH the dealer hand and the player hand from card_value dict.
#I do not think I can efficiently do this without a while loop after the def blackjack game function. I am going to try and figure a way to use len() to deal the cards
#I could not figure out how to make the program run when I made functions for the player hand and dealer hand being dealt separately
#I am not quite done yet -----> I might need to get a breakout room for the functions




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
elif card_total >= 17 and card_total > 21:
    print(card_total, "Stay Put!")
elif card_total == 21:
    print(card_total, "Blackjack!")
else:
    card_total > 21
    print(card_total, "Already Busted, house wins!")






# deck= []
# for card in card_value:
#     deck.append(card_value[card])

#     def black_jack(deck):
#         global card_value
#         player_hand= []
#         dealer_hand= []
#         player_total= 0
#         dealer_total= 0
        
        
#         while len(player_hand) <2:
#             player_hand= random.choice(deck)
#             player_hand.append(player_hand)
#             deck.remove(player_hand)
#             player_total += player_hand.card_value

#             if len(player_hand) == 2:
#                 if player_hand[0].card_value == 11 and player_hand[1].card_value == 11:
#                     player_hand[0].card_value= 1
#                     player_total -= 10
#                     if player_total < 17:
#                         print(player_total, player_hand, "Hit")
#                     elif player_total >= 17:
#                         print(player_total, player_total, "Stay Put!")
#                     elif player_total == 21:
#                         print(player_total, "Blackjack!")
#                     else:
#                         player_total > 21
#                         print(player_total, "Already Busted, house wins!")
    
#         while len(dealer_hand) <2: 
#             dealer_hand= random.choice(deck)
#             dealer_hand.append(dealer_hand)
#             deck.remove(dealer_hand)
#             dealer_total += dealer_total.card_value
    
#             if len(dealer_hand) == 2:
#                 if dealer_hand[0].card_value == 1 and dealer_hand[1].card_value == 1:
#                     dealer_hand[0].card_value= 11
#                     dealer_total -= 10
#                     dealer_total <= 21
#                     if dealer_total > player_total:
#                         print("The house wins!")
#                     black_jack()    
                    
                    

                

                        
            








