# BLACKJACK ADVICE

# ask the player for cards using a dictionary

card_dict = {
  'A': 1,
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
  'K': 10
  }

def bj_machine(card_input):
  card_value = 0

  for item in card_dict.items():
    key = item[0]
    value = item[1]

    if card_input == key:
      card_value += value

  if card_input not in card_dict.keys():
    return False

  return card_value

total_value = 0
