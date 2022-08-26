# Lab 10: Contact List
# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. 
# Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
# The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

def csv_converter(user_file):
    contacts = []
    for index in range(len(user_file)):
        listed_person = user_file[index].split(',')
        if index != 0: 
            person = {
            (user_file[0].split(','))[0]:(listed_person[0]).title(), 
            (user_file[0].split(','))[1]:(listed_person[1]).title(), 
            (user_file[0].split(','))[2]:(listed_person[2]).title() 
        }
            contacts.append(person)
    return contacts
contacts = csv_converter(lines)

# Version 2 
# Implement a CRUD REPL
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
def create():
    print('Create a record.\n')
    name = input('Name: ').title()
    fruit = input('Favorite Fruit: ').title()
    color = input('Favorite Color: ').title()

    person = {
        'Name': name, 
        'Favorite Fruit': fruit, 
        'Favorite Color': color
    }
    contacts.append(person)
    print('\nRecord has been saved.')

# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
def retrieve():
    requested_name = input('Enter name to retrieve record: ').title()
    index_pos = 0
    for i in range(len(contacts)):
        if contacts[i]['Name'] == requested_name:
            print(f"""
Record retrieved.\n 
Name: {contacts[i]['Name']}
Favorite Fruit: {contacts[i]['Favorite Fruit']}
Favorite Color: {contacts[i]['Favorite Color']}""")
            index_pos += i
            return index_pos
        else:
            if (i+1) == len(contacts):
                print('Record not found.')
                return "0"


# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update(): 
    index_pos = retrieve()
    if index_pos == '0':
        print('\nReturning to main menu...')
    else:
        while index_pos != False:
            user_key_update = input('''
    What would you like to update? 
    -- Name?
    -- Favorite Fruit?
    -- Favorite Color? 

    Enter key exactly as written here: ''').title()
            user_value_update = input(f'What would you like to change information in "{user_key_update}" to? ').title()
            (contacts[index_pos]).update({user_key_update:user_value_update})

            user_loop = input('Update more? Enter "Yes" or "No". ').capitalize()
            if user_loop == 'Yes':
                continue
            else:
                print(f"""
    Updated Record.\n 
    Name: {contacts[index_pos]['Name']}
    Favorite Fruit: {contacts[index_pos]['Favorite Fruit']}
    Favorite Color: {contacts[index_pos]['Favorite Color']}""")
                print('\nReturning to main menu...')
                break

# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete():
    index_pos = retrieve()
    if index_pos == '0':
        print('\nReturning to main menu...')
    elif index_pos != False:
        user_input = input('\nAre you sure you want to delete this record?\nEnter "Yes" or "No". ').title()
        if user_input == 'Yes':
            contacts.pop(index_pos)
            print('\nRecord deleted.\nReturning to main menu...')
        else:
            print('\nReturning to main menu...')
    elif index_pos == 0:
        user_input = input('\nAre you sure you want to delete this record?\nEnter "Yes" or "No". ').title()
        if user_input == 'Yes':
            contacts.pop(index_pos)
            print('\nRecord deleted.\nReturning to main menu...')
        else:
            print('\nReturning to main menu...')


# To view the complete list
def view():
    for i in range(len(contacts)):
        print(f'''\n\t{i+1}) Name: {contacts[i]['Name']}
\t   Favorite Fruit: {contacts[i]['Favorite Fruit']}
\t   Favorite Color: {contacts[i]['Favorite Color']} ''')

# Version 3 
# When REPL loop finishes, write the updated contact info to the CSV file to be saved. 
def upload():
    new_contacts_list = ['Name,Favorite Fruit,Favorite Color']
    for i in range(len(contacts)):
        specific_contact = []
        for record in contacts[i]:
            specific_contact.append(contacts[i].get(record))
        line = ",".join(specific_contact)
        new_contacts_list.append(line)

    csv_insert = "\n".join(new_contacts_list)
    with open('contacts.csv', 'w') as new_file:
        new_file.write(csv_insert)
    print('CSV file updated.')

# Main Menu
def main():
    while True:
        print('\n***MAIN MENU***')
        choice = int(input("""What would you like to do? \n
        1: CREATE NEW RECORD
        2: RETRIEVE A RECORD
        3: UPDATE A RECORD
        4: DELETE A RECORD 
        5: VIEW COMPLETE RECORD LIST
        6: UPLOAD TO CSV FILE
        \nEnter # """))
        
        if choice == 1:
            create()
        elif choice == 2:
            retrieve()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            view()
        elif choice == 6:
            upload()
        else:
            break


# Run 
main()














