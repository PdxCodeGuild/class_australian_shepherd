



new_contacts = []



# Open CSV and store information in the variable lines
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

# print(lines)




header = lines[0]
keys = header.split(',')


for index in range(1, len(lines)):
    profile = lines[index].split(',')


    person = {
        keys[0] : profile[0],
        keys[1] : profile[1],
        keys[2] : profile[2]
    }
    new_contacts.append(person)
# print(new_contact[1]['name'])




# # Create a single person
def create():
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")

    person = {
        'name': name,
        'age': age,
        'city' : city
    }

    write(person)

# Write the change
def write(person):
    new_contacts.append(person)

# print(new_contact)

# Retrieve a single person
def retrieve():
    name = input("Enter the name of the person you are searching for: ")
    for person in new_contacts:
        # print(person['city'])

        if person['name'] == name:
            print(f"""
            Name: {person['name']}
            Age: {person['age']}
            City: {person['city']}
            \n""")

    return name

def update():
    name = retrieve()
    choice = input("Update their name, age or city? ")
    new_value = input("Change the value to: ")

    for person in new_contacts:
        if person['name'] == name:
            if choice == 'name':
                person['name'] = new_value
            elif choice == 'age':
                person['age'] = new_value
            elif choice == 'city':
                person['city'] = new_value


def delete():
    name = retrieve()

    for index in range(len(new_contacts)):
        if name == new_contacts[index]['name']:
            new_contacts.pop(index)
            break

def list():
    counter = 1
    for person in new_contacts:
        print(f"{counter}. {person['name']}, {person['age']}, {person['city']}")
        counter += 1

def save():
    with open('new_contacts.csv', 'w') as file:
        # file.write(f'{header}\n')
        newest_contact = f'{header}\n'
        # newest_contact.append(header)
        for person in new_contacts:
            contact = f"{person['name']},{person['age']},{person['city']}\n"
            newest_contact += contact
            
        # print(newest_contact)
        file.write(newest_contact)


def main():
    while True:
        choice = input('''\nWelcome what would you like to do to your contacts
        1: Create a new contact
        2: Retrieve a record
        3: Update a record
        4: Delete a record
        5: List all records
        6: Save records
        ''')

        if choice == '1':
            create()

        elif choice == '2':
            retrieve()

        elif choice == '3':
            update()

        elif choice == '4':
            delete()

        elif choice == '5':
            list()

        elif choice == '6':
            save()
        else:
            break
main()

