cipher = {
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
    'z': 'm',
    ' ': ' '
}

subject = input('Enter name to encode it: ')
subject = list(subject)

secret = []
for char in subject:
    secret.append(cipher[char])

secret = ''.join(secret)

print(f"\n Your code name is '{secret}' guard it with your life")