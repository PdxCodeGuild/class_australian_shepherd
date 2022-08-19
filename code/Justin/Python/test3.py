contacts = [

]


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    keys = lines[0].split(',')
for index in range(1, len(lines)):
    # values = lines[index]
    new_dict = dict(zip(keys, lines[index].split(',')))
    contacts.append(new_dict)
print(contacts)