with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts_list = []
contact_dict = {}

header_list = lines[0].split(',')

for line in range(1, len(lines)):
    temp_line = lines[line].split(',')
    contact = dict(zip(header_list, temp_line))
    contacts_list.append(contact)
   

print(contacts_list)









'''
# Open CSV and store information in the variable lines
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

print(lines)


dummy_data = lines[0]

# Write to different csv
with open('new_contacts.csv', 'w') as file:
        file.write(dummy_data)


    contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]

# CRUD 

# CRUD L 


contacts = [
    {
        'name': 'sara',
        'age': 25,
        'city': 'portland'
    },
        {
        'name': 'bob',
        'age': 99,
        'city': 'florida'
    }
]


# Crete a single person
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
    contacts.append(person)



# Retrieve a single person
def retrieve():
    name = input("Enter the name of the person you are searching for: ")
    for person in contacts:
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

    for person in contacts:
        if person['name'] == name:
            if choice == 'name':
                person['name'] = new_value
            elif choice == 'age':
                person['age'] = new_value
            elif choice == 'city':
                person['city'] = new_value


def delete():
    name = retrieve()

    for index in range(len(contacts)):
        if name == contacts[index]['name']:
            contacts.pop(index)
            break

def list():
    counter = 1
    for person in contacts:
        print(f"{counter}. {person['name']}, {person['age']} {person['city']}")
        counter += 1



def main():
    while True:
        choice = input(Welcome what would you like to do to your contacts
        1: Create a new contact
        2: Retrieve a record
        3: Update a record
        4: Delete a record
        5: List all records
        )

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
    
    
main()


    '''