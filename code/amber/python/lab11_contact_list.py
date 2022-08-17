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


#Implement a CRUD REPL

#Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.

def create():
  name = input('Name: ').title()
  fruit = input('Favorite Fruit: ').title()
  color = input('Favorite Color: ').title()

  person = {
    'Name': name,
    'Favorite Fruit': fruit,
    'Favorite Color': color
  }

  write(person)

def write(person):
  contact_list.append(person)

create()

#print(f'contact list with "C": {contact_list}')

#Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

#Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

#Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.












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
