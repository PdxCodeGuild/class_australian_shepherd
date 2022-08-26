#------------------------------------------------------------------------------------------
#Version 2

english =	['a', 'b', 'c', 'd', 'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n', 'o',	'p', 'q',	'r', 's', 't', 'u', 'v', 'w',	'x', 'y', 'z']

user_rotated = []

secrets = input('Please enter words for encryption: ')
#print(secrets)

rotation = input('Please also enter an integer between 1 and 26 to denote how much rotation of your cipher you would like: ')

rotation = int(rotation)

#print(rotation)

for index in range(rotation, len(english)):
  user_rotated.append(english[index])
  #print(index, english[index])
for index in range(0, rotation):
  user_rotated.append(english[index])

print(user_rotated)

english_user_rot = {
  'a': user_rotated[0],
  'b': user_rotated[1],
	'c': user_rotated[2],
  'd': user_rotated[3],
  'e': user_rotated[4],
  'f': user_rotated[5],
  'g': user_rotated[6],
  'h': user_rotated[7],
  'i': user_rotated[8],
  'j': user_rotated[9],
  'k': user_rotated[10],
  'l': user_rotated[11],
  'm': user_rotated[12],
  'n': user_rotated[13],
  'o': user_rotated[14],
  'p': user_rotated[15],
  'q': user_rotated[16],
  'r': user_rotated[17],
  's': user_rotated[18],
  't': user_rotated[19],
  'u': user_rotated[20],
  'v': user_rotated[21],
  'w': user_rotated[22],
  'x': user_rotated[23],
  'y': user_rotated[24],
  'z': user_rotated[25]
}

for each in secrets:
 if each in english_user_rot.keys():
   secrets = secrets.replace(each, english_user_rot[each])

print(secrets)


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
