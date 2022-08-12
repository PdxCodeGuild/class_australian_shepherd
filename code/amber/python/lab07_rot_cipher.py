#------------------------------------------------------------------------------------------
#Version 2

#Allow the user to input the amount of rotation used in the encryption / decryption.

#Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
english =	['a', 'b', 'c', 'd', 'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n', 'o',	'p', 'q',	'r', 's', 't', 'u', 'v', 'w',	'x', 'y', 'z']

rot_13 =	['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',	'k', 'l',	'm']
# starts at 13th index
user_rotated = []

#secrets = input('Please enter words for encryption: ')
#print(secrets)

rotation = input('Please also enter an integer between 1 and 26 to denote how much rotation of your cipher you would like: ')

rotation = int(rotation)

#rotation = english[rotation]
print(rotation)


for index in range(rotation, len(english)):
  user_rotated.append(english[index])
  #print(index, english[index])
for index in range(0, rotation - 1):
  user_rotated.append(english[index])

print(user_rotated)

#for each in secrets:
#  if each in english_rot.keys():
#    secrets = secrets.replace(each, english_rot[each])

#print(secrets)


'''
# ROT CIPHER

english_rot = {
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

secrets = input('Please enter words for encryption: ')
#print(secrets)

for each in secrets:
  if each in english_rot.keys():
    secrets = secrets.replace(each, english_rot[each])

print(secrets)
'''
