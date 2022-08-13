# Rot Cipher

# rot13 = {
#     "a": "n",
#     "b": "o",
#     "c": "p",
#     "d": "q",
#     "e": "r",
#     "f": "s",
#     "g": "t",
#     "h": "u",
#     "i": "v",
#     "j": "w",
#     "k": "x",
#     "l": "y",
#     "m": "z",
#     "n": "a",
#     "o": "b",
#     "p": "c",
#     "q": "d",
#     "r": "e",
#     "s": "f",
#     "t": "g",
#     "u": "h",
#     "v": "i",
#     "w": "j",
#     "x": "k",
#     "y": "l",
#     "z": "m"
# }

# user_word = list(input("Please enter a word: "))

# converted = []

# conv_string  = ""

# for i in (user_word):
#     converted.append((rot13[i]))

# print(conv_string.join(converted))

# Version 2

def encode():
    text = input("Please enter a word: ")
    shift = int(input("Please enter desired shift: "))
    cipher = ""
    for i in text:
        if i.isalpha():
            shifted = ord(i) + shift
        if shifted > ord('z'):
            shifted -= 26
        finalLetter = chr(shifted)
        cipher += finalLetter

    print ("Encoded text: ", cipher)

encode()

def decode():
    encoded = input("Please enter your encoded word: ")
    shift = int(input("Please enter desired shift: "))
    decipher = ""
    for i in encoded:
        if i.isalpha():
            shifted = ord(i) - shift
        if shifted > ord('z'):
            shifted += 26
        finalLetter1 = chr(shifted)
        decipher += finalLetter1

    print ("Decoded text: ", decipher)

decode()