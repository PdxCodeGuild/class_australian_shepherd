########## BLACKJACK ADVICE ###########

player_cards = []

cards_value = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


while len(player_cards) < 3:

    players_picks = ""
    while players_picks not in cards_value:
        if players_picks != "":
            print(
                "Please entere a valid card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)"
            )
        players_picks = input(f"What is your card number {player_cards}: ").upper()
    else:
        player_cards.append(players_picks)


def summ(player_cards):
    total = 0
    card_counter = 0
    for card in player_cards:
        card_counter += 1
        if card == "A" and card_counter == 3:
            if total <= 10:
                total = total + 11
            else:
                total = total + 1
        elif card == "A" and card_counter == 2:
            if total == 1:
                total = total + 11
            else:
                total = total + 1
        else:
            total = total + cards_value[card]

    return total


cards_total = summ(player_cards)


if cards_total < 17:
    result = "Hit"
elif cards_total >= 17 and cards_total < 21:
    result = "Stay"
elif cards_total == 21:
    result = "BLACKJACK"
else:
    result = "Already Busted"

print(f"{cards_total} is {result}")
