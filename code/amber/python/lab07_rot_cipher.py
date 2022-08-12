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

print(secrets)

for each in secrets:
  if each in english_rot.keys():
    secrets = secrets.replace(each, english_rot[each])

print(secrets)
