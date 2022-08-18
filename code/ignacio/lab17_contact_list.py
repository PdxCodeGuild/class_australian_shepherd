# Open CSV and store information in the variable lines


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
# lines = contact csv data as a list
# EXAMPLE of what to aim for
# contacts =[
# {'name':'name', 'favorite food': 'favorite food', 'favorite color': 'favorite color'},
# {'name':'iggy', 'favorite food':'curry', 'favorite color':'orange'},
# {'name':'oscar', 'favorite food':'chicken', 'favorite color': 'black'}
# ]

keys = lines[0]
keys = keys.split(',')
contacts = []

for index in range(1, len(lines)):
    values = lines[index].split(',')
    person = {
        keys[0]: values[0],
        keys[1]: values[1],
        keys[2]: values[2]
    }
    contacts.append(person)
    # print(keys)
    # print(lines[index])
# print(contacts)


def main_menu():
    while True:
        options = input('''Welcome what would you like to do to your contacts
        1: Create a new contact
        2: Retrieve a contact
        3: Update a contact
        4: Delete a contact
        5: List all contacts
        ''')

        if options == '1':
            create()

        elif options == '2':
            retrieve()

        elif options == '3':
            update()

        elif options == '4':
            delete()

        elif choice == '5':
            list()


def create():
    Name = input("please enter name: ")
    favorite_food = input("whats your favorite food?: ")
    favorite_color = input("whats your favorite food?: ")

    person = {
        'name': Name,
        'favorite food': favorite_food,
        'favorite color' : favorite_color
    }
    write(person)

def write(person):
    contacts.append(person)

def retrieve():
    name = input("")

# dummy_data = lines[0]
# print(lines)
print(contacts)


# Write to different csv
# with open('contacts2.csv', 'w') as file:
#         file.write(dummy_data)
# file.write() will insert data to contacts2

# make dict thats easy to work with. dict will be used to influence contacts.csv and change contacts2