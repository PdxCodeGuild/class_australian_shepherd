# CONTACT LIST


with open('lab11_contact.csv', 'r') as file:
    lines = file.read().split('\n')

###### need to create a function to write lines back into new csv (DONT GET THIS PART): ######

# Write to different csv
#with open('lab11_new_contact.csv', 'w') as file:
    #file.write(???)

lines.pop()

headers = lines[0]
headers = headers.split(',')

contact_list = []

for index in range(1, len(lines)):

  contact_info = lines[index].split(',')

  contact = {
    headers[0].title(): contact_info[0].title(),
    headers[1].title(): contact_info[1].title(),
    headers[2].title(): contact_info[2].title()
}

  contact_list.append(contact)

  # V. 2 -------------------------

####### NEED TO ADD ERROR HANDLING FOR INPUTS #########

#Implement a CRUD REPL

#Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.

def create():

  name = input('Name: ').title()
  fruit = input('Favorite Fruit: ').title()
  color = input('Favorite Color: ').title()

  contact = {
    'Name': name,
    'Favorite Fruit': fruit,
    'Favorite Color': color
  }

  write(contact)

  print(f'New contact added: {contact}')

def write(contact):
  contact_list.append(contact)

#create()
#print(f'contact list with "C": {contact_list}')


#Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

def retrieve():

  name = input('Enter the name of the person you are searching for: ').title()

  for contact in contact_list:
    if contact['Name'] == name:
      print(f"""
            Name: {contact['Name']}
            Favorite Fruit: {contact['Favorite Fruit']}
            Favorite Color: {contact['Favorite Color']}
            \n""")

  return name

#Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

def update():

  name = retrieve()
  choice = input('Which field would you like to update: name, fruit, or color? ')
  new_value = input('Enter new value: ').title()

  for contact in contact_list:
    if contact['Name'] == name:
      if choice == 'name':
        contact['Name'] = new_value
      elif choice == 'fruit':
        contact['Favorite Fruit'] = new_value
      elif choice == 'color':
        contact['Favorite Color'] = new_value

  print(f'Contact updated: {contact}')

#Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


def delete():
  name = retrieve()

  for index in range(len(contact_list)):
    if name == contact_list[index]['Name']:
      contact_list.pop(index)
      print(f'Contact successfully deleted.')
      break

def list():
  counter = 1
  for contact in contact_list:
    print(f"{counter}. Name: {contact['Name']}, Favorite Fruit: {contact['Favorite Fruit']}, Favorite Color: {contact['Favorite Color']}")
    counter += 1

def main():
    while True:
        choice = input('''\nWelcome what would you like to do to your contacts? Enter a number from the choices listed below.
        1: Create a new contact
        2: Retrieve a record
        3: Update a record
        4: Delete a record
        5: List all records
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


main()









# NOTES ------------------

'''
# open and read CSV file and assign lines variable name to data
with open('lab11_contact.csv', 'r') as file:
    lines = file.read().split('\n')


# remove blank line from end
lines.pop()
#print(f'lines: {lines}')

# create list of header titles from first line of csv file
headers = lines[0]
headers = headers.split(',')
#print(f'headers: {headers}')

contact_list = []

# for loop to break up lines
for index in range(1, len(lines)):
  #print(f'lines[index]:{index} {lines[index]}')

  #break off each line of lines list into contact info list
  contact_info = lines[index].split(',')
  #print(f'contact info: {contact_info}')

  #plug everything into a single contact dictionary
  contact = {
    headers[0].title(): contact_info[0].title(),
    headers[1].title(): contact_info[1].title(),
    headers[2].title(): contact_info[2].title()
}
  #print(f'contact: {contact}')

  #append each contact to contact list
  contact_list.append(contact)

print(f'contact list: {contact_list}')
'''
