



rot13 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# rot = 13
rot = int(input('How much rot do you want?:  '))

# print(len(rot13))

pre_rot = input('Enter a word to rot.:  ')
# pre_rot = 'hello'
pre_rot = list(pre_rot)

new_words = ''

for letter in pre_rot:
    if letter != ' ':
        i_of_letter = rot13.index(letter)
        # print('letter index', i_of_letter)
        i_of_letter += rot
        if i_of_letter > 26:
            i_of_letter -= 26
        new_letter = rot13[i_of_letter]
        new_words += new_letter
    else:
        new_words += ' '

    # print('new index of letter', i_of_letter)
    # print(new_letter)
print('Rotten word is ', new_words)