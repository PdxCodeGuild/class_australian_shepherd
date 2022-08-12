# Lab Rot Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, 
# add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# import random
import string
lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
# special_char = list(string.punctuation)
# digits = list(string.digits)


# Version 1 ROT13
encrypt = input('VERSION 1 - Enter message here: ').lower()
encrypted = []
for letter in encrypt:
    if letter in lower_letters:
        if (lower_letters.index(letter)) <= 12:
            encrypted.append(lower_letters[(lower_letters.index(letter)) + 13])
        else: 
            encrypted.append(lower_letters[(lower_letters.index(letter)) - 13])
    else:
        encrypted.append(letter)
print(''.join(encrypted))

# Version 2 ROTn
# Allow the user to input the amount of rotation used in the encryption. (ROTN)
encrypt = input('VERSION 2 - Enter message here: ').lower()
rotation = input('Please enter any number to rotate the message: ')
requested_rotation = (int(rotation) + 25)
actual_rotation = requested_rotation - ((requested_rotation//25)*25)
encrypted = []
 
for value in encrypt:
    if value in lower_letters:
        if ((lower_letters.index(value)) + actual_rotation) > 25:      # ensures that equation doesn't request out of index range
            encrypted.append(lower_letters[((lower_letters.index(value)) + actual_rotation) - 26])
        else: 
            encrypted.append(lower_letters[(lower_letters.index(value)) + actual_rotation])
    else:
        encrypted.append(value)

print(''.join(encrypted))


# Version 3
# Add support for capital letters, numbers, and special characters. These can be handled in two different ways:
# Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").
# Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.

user_message = input('VERSION 3 - Enter message here: ')
rotation = input('Please enter any number to rotate the message: ')
requested_rotation = (int(rotation) + 6200) # Allows for any number to be inputted for rotations if I wanted to also rotate special characters & numbers
letter_rotation = requested_rotation - ((requested_rotation//25)*25)
symbol_rotation = requested_rotation - ((requested_rotation//25)*25)
encrypted = []
print(user_message)
 
for value in user_message:
    if value in lower_letters:
        if ((lower_letters.index(value)) + letter_rotation) > 25:      # ensures that equation doesn't request out of index range
            encrypted.append(lower_letters[((lower_letters.index(value)) + letter_rotation) - 26])
        else: 
            encrypted.append(lower_letters[(lower_letters.index(value)) + letter_rotation])
    elif value in upper_letters:
        if ((upper_letters.index(value)) + (letter_rotation)) > 25:       # ensures that equation doesn't request out of index range
            encrypted.append(upper_letters[((upper_letters.index(value)) + letter_rotation) - 26])
        else: 
            encrypted.append(upper_letters[(upper_letters.index(value)) + letter_rotation])
    # elif value in 
    else:
        encrypted.append(value)
print(''.join(encrypted))



