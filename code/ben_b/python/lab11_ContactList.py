'''
benjamin_birky
lab11_ContactList
08/17/2022
'''
#---------------------------------------------Version 2 --------------------------------------------
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []
new_contacts = []
header_list = lines[0].split(',')

# Import CSV contacts
def importContacts():
    for line in range(1, len(lines)):
        temp_line = lines[line].split(',')
        csv_contact = dict(zip(header_list, temp_line))
        addContact(csv_contact)
    return
   
# Add contact
def addContact(person):
    contacts.append(person)

# Create a contact, add the person to contact list
def createContact():
    name = input("Name: ").lower()
    age = input("Age: ")
    city = input("City: ").lower()

    person = {
            'name' : name,
            'age' : age,
            'city' : city
    }
    addContact(person)
    return

# Retrieve a contact
def retrieveContact():
    name = input("What is the contact's name?: ")
    for person in contacts:
        if name == person['name']:
            print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
            break

# Update a contact
def updateContact():
    name = input("What is the contact's name?: ").lower()
    attribute = input("What attribute do you want to change?: ").lower()
    value = input("What is the new value for the attribute?: ")
    for person in contacts:
        if name == person['name']:
            person.update({attribute: value})
            contacts.append(person)
            break

# Delete a contact
def deleteContact():
    name = input("What is the contact's name?: ")
    for person in contacts:
        if name == person['name']:
            del person
            break

# Print contacts
def printContacts():
    for person in contacts:
        print(f"Name: {person['name']}\tAge: {person['age']} \tCity: {person['city']}")


# CRUD REPL
importContacts()

while True:
    option = input('''
1) Create a contact
2) Retrieve a contact
3) Update a contact
4) Delete a contact
Select a number or type any key to exit
What would you like to do?: ''')
    if option == '1':
        createContact()
    elif option == '2':
        retrieveContact()
    elif option == '3':
        updateContact()
    elif option == '4':
        deleteContact()
    else:
        break
         
printContacts()

#---------------------------------------------Version 3 --------------------------------------------
# Export to new_contacts.csv
for person in range(len(contacts)):    
    thisdict = contacts[0]
    thisdict = thisdict.get('name')
    print(thisdict)




dummy_data = lines[0]
with open('new_contacts.csv', 'w') as file:
        file.write(dummy_data)







'''
# Open CSV and store information in the variable lines
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

print(lines)


dummy_data = lines[0]

# Write to different csv
with open('new_contacts.csv', 'w') as file:
        file.write(dummy_data)

Version 3
When REPL loop finishes, write the updated contact info to the CSV file to be saved. 
I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''
