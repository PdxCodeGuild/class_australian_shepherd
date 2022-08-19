# Creating our starting list of dictionaries nested inside of a list
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

# Creating a while loop for our repl
while True:
    # Taking a user input to determine which action they want to take
    command = input('''
    Select from the following options:

    1: Add a new contact entry.
    2: Retrieve information from your contacts.
    3: Update information from your contacts.
    4: Delete a contact.

    ''')
    # Creating a function to append a new contact to our list of dictionaries
    def new_contact():
        name = input('Name: ')
        age = input('Age: ')
        city = input('City: ')
        new_dict = {
            'name': name,
            'age': age,
            'city': city
        }
        contacts.append(new_dict)
        
    # Creating a function to take a user input and search through our list of dictionaries to return any information for the contact
    def find_contact():
        contact_found = False
        contact_name = input('Please enter a name to search: ')
        for data in contacts:
            if contact_name in data.values():
                print(f"Name ==> {data.get('name').title()}")
                print(f"Age ==> {data.get('age')}")
                print(f"City ==> {data.get('city').title()}")
                contact_found = True
        if contact_found == False:
            return False
        elif contact_found == True:
            return contact_name
                
    # Creating a function that updates our dictionaries
    def update_contact():
        # find_contact()
        x = find_contact()
        if x == False:
            print('No contact information found.')
        else:
            update_input = input('Please enter the information you would like to update: ')
            for entry in contacts:                  
                if update_input in entry.keys() and x == entry['name']:
                    updates = input(f'Change {update_input} to : ')
                    entry[update_input] = updates
                elif update_input not in entry.keys():
                    print('Please select a valid entry.')

    #Creating a function to delete a contact within our list
    def delete_contact():
        find_contact()
        #Taking a user input to ensure they want to delete the contact
        delete_item = input('Are you sure you want to remove this contact y/n: ')
        if delete_item == 'y':
            contacts.pop()
        else:
            print('Contact not deleted.')
            close()

    # Creating a function to ask the user if they want to quit, or continue searching
    def close():
        while True:
            check = input('Would you like to continue y/n: ')
            if check == 'y':
                break
            elif check == 'n':
                exit()
            else:
                print('Please enter a valid command.')

    # Taking if/elif statements with our user input to determine the correct action our application needs to take
    if command == '1':
        new_contact()
    elif command == '2':
        if find_contact() == False:
            print('Contact information not found.')
    elif command == '3':
        update_contact()
    elif command == '4':
        delete_contact()
    close()

    
