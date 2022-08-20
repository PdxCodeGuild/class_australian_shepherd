# Creating a dictionary of our card values for easy reference
card_dict = {
    'a': 1,
    'j': 10,
    'q': 10,
    'k': 10,
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

# Creating a function that takes three user inputs 
def blackjack():
    # Creating a variable with a zero value to add our card points value from our dictionary
    card_count = 0
    # Creating a variable to count down how many cards we have
    cards = 3
    # Using a while loop to keep track of our cards variable
    while cards > 0:
        # Taking a user input to pull information from our dictionary
        hand = input("What's your first card? ")
        # Using a for loop to iterate through our dictionary to pull our values from
        for key in card_dict:
            if hand == key:
                card_count += card_dict.get(hand)
        cards -= 1
    # Returning our card_count value
    return card_count

# Calling our function as a variable
advice = blackjack()

# Using if/else statements to print our advice from
if advice < 17:
    print(f'{advice} Hit.')
elif advice >= 17 and advice < 21:
    print(f'{advice} Stay.')
elif advice == 21:
    print(f'{advice} Blackjack!!')
else:
    print(f'{advice} Already busted.')