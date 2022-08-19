dictionary = [
    {'name': 'justin',
     'age' : 36,
     'city': 'savannah'
    }
]
lis = []
for item in dictionary:
    for key in item:
        lis.append(key)
x = str(lis)
print(x.strip())
for item in x:
    x.join(' ')
print(x)
for item in dictionary:
    for value in item:
        print(item.values())