# ##                     ROT 13         CIPHER                      ##
import string

rot_cipher_dict = {
    
'a': 'n',
'b': 'o',
'c': 'p',
'd': 'q',
'e': 'r',
'f': 's',
'g': 't',
'h': 'u',
'i': 'v',
'j': 'w',
'k': 'x',
'l': 'y',
'm': 'z',
'n': 'a',
'o': 'b',
'p': 'c',
'q': 'd',
'r': 'e',
's': 'f',
't': 'g',
'u': 'h',
'v': 'i',
'w': 'j',
'x': 'k',
'y': 'l',
'z': 'm'
}

users_string = input("Please enter text to have encrypted: ").lower()

for char in string.punctuation:
    users_string = users_string.replace(char, '')

# print(users_string)

users_string = list(users_string)
ciphered_list = []
for char in users_string:
    if char == ' ':
        ciphered_list.append(' ')
    else:
        ciphered_list.append(rot_cipher_dict[char])


ciphered_string = ''.join(ciphered_list)

print(ciphered_string)

##        VERSION 2           ##


# Allow the user to input the amount of rotation used in the encryption/decryption          #         TRY advancing the key forward one to encrypt the string from a different value on
ciphered_list_rot = []
for char in users_string:                      # try to make the char "key" a indice place to add 1 to further on in the code 
    if char == ' ':
        ciphered_list_rot.append(' ')
    else:
        ciphered_list_rot.append(rot_cipher_dict[char + 1])
        
print(ciphered_list_rot)
