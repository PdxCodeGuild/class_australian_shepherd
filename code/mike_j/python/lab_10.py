# Contact List

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []

lines.pop()

headers = lines[0]
headers = headers.split(',')

for i in range(1, len(lines)):

  data = lines[i].split(',')

  contact = {
    headers[0]: data[0],
    headers[1]: data[1],
    headers[2]: data[2]
}
  contacts.append(contact)

def create():
    name = input("name: ")
    fruit = input("favorite fruit: ")
    color = input("favorite color: ")

    person = {
        'name': name,
        'fruit': fruit,
        'color' : color
    }

    write(person)

    save()

def write(person):
    contacts.append(person) 

def retrieve():
    name = input("Enter the name of the person you are searching for: ")
    for person in contacts:

        if person['name'] == name:
            print(f"""
            Name: {person['name']}
            Favorite fruit: {person['fruit']}
            Favorite color: {person['color']}
            \n""")

    return name

def update():
    name = retrieve()
    choice = input("Update their name, favorite fruit or favorite color? ")
    new_value = input("Change the value to: ")

    for person in contacts:
        if person['name'] == name:
            if choice == 'name':
                person['name'] = new_value
            elif choice == 'favorite fruit':
                person['fruit'] = new_value
            elif choice == 'favorite color':
                person['color'] = new_value      

    save()

def delete():
    name = retrieve()

    for i in range(len(contacts)):
        if name == contacts[i]['name']:
            contacts.pop(i)
            break

    save()    

def list():
    counter = 1
    for person in contacts:
        print(f"{counter}. {person['name']}, {person['fruit']}, {person['color']}")
        counter += 1        

def save():

    with open('contacts.csv', 'w') as file:

        file.write("name" + "," + "fruit" + "," + "color\n")    
        
        for person in contacts:
        
            new_contacts = (person['name']) + ',' + (person['fruit']) + ',' + (person['color'])

            file.write(new_contacts)
            file.write("\n")    
        
def main():
    while True:
        choice = input('''\nPlease make a choice from the following list:
        1: Create a new contact
        2: Retrieve a record
        3: Update a record
        4: Delete a record
        5: List all records
        6: Exit
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
            break      

main()            