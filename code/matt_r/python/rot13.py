



pre_rot = input('Enter a word to rot.:  ')


rot13 = {'n' : 'a', 'o' : 'b', 'p' : 'c', 'q' : 'd', 'r' : 'e', 's' : 'f',
        't' : 'g', 'u' : 'h', 'v' : 'i', 'w' : 'j', 'x' : 'k', 'y' : 'l',
        'z' : 'm', 'a' : 'n', 'b' : 'o', 'c' : 'p', 'd' : 'q', 'e' : 'r',
        'f' : 's', 'g' : 't', 'h' : 'u', 'i' : 'v', 'j' : 'w', 'k' : 'x',
        'l' :  'y', 'm' : 'z', ' ' : ' '
        }


for letter in pre_rot:
    new_letter = rot13[letter]
    pre_rot = pre_rot.replace(letter, new_letter)

print(pre_rot)