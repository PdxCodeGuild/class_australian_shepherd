with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

keys = lines[0]
keys = keys.split(',')
contacts = []

for index in range(1, len(lines)):
    values = lines[index].replace('\n', '').split(',')

    if values == '':
        break
    person = {
        keys[0]: values[0],
        keys[1]: values[1],
        keys[2]: values[2]
    }
    contacts.append(person)

 
def create():
    Name = input("Please enter name: ")
    favorite_food = input("Whats your favorite food?: ")
    favorite_color = input("Whats your favorite color?: ")

    person = {
        'name': Name,
        'favorite food': favorite_food,
        'favorite color' : favorite_color
    }
    write(person)



def write(person):
    contacts.append(person)

    output_string = keys[0] + ',' + keys[1] + ',' + keys[2] + '\n'

    for person in contacts:
        output_string += person['name'] + ',' + person['favorite food'] + ','+ person['favorite color'] + '\n'
    print(output_string)
    with open('contacts2.csv', 'w') as file:
        file.write(output_string)


def retrieve():
    name = input("Enter the name of the person youre looking for: ")
    for person in contacts:
        
        if person['name'] == name:
            print(f"""
            Name: {person['name']}
            favorite food: {person['favorite food']}
            favorite color: {person['favorite color']}
                """)
    return name




def update():
    name = retrieve()

    for person in contacts:
        if name == person['name']:
            new_data = input("Will you be changing their name, favorite food, or favorite color?: ")
            person[new_data] = input("What will you be changing this to?: ")


def delete():
    name = retrieve()
    for index in range(len(contacts)):
        if name == contacts[index]['name']:
            contacts.pop(index)
            break


def catalog():
    counter = 1
    for person in contacts:
        print(f"{counter}. {person['name']}, {person['favorite food']}, {person['favorite color']}")
        counter += 1


def main_menu():
    while True:
        options = input('''Welcome! what would you like to do to your contacts?
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

        elif options == '5':
            catalog()


main_menu()
