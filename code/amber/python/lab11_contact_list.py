# CONTACT LIST

with open('lab11_contact.csv', 'r') as file:
    lines = file.read().split('\n')

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

# v.3

dummy_data = f"name,fruit,color\n{contact['Name']},{contact['Favorite Fruit']},{contact['Favorite Color']}"


with open('lab11_new_contact.csv', 'w') as file:
    file.write(dummy_data)

  # v.2 -------------------------

def create():

  name = input('Name: ').title()
  fruit = input('Favorite Fruit: ').title()
  color = input('Favorite Color: ').title()

  contact = {
    'Name': name,
    'Favorite Fruit': fruit,
    'Favorite Color': color
  }
  contact_list.append(contact)
  write() # v.3

  print(f'New contact added: {contact}')

def write():
  # v.3
  writing_string = headers[0] + ',' + headers[1] +  ',' + headers[2] + '\n'

  for person in contact_list:
    writing_string += person['Name'] +  ',' + person['Favorite Fruit'] +  ',' + person['Favorite Color'] + '\n'

  with open('lab11_new_contact.csv', 'w') as file:
    file.write(writing_string)

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
  write() # v.3

def delete():
  name = retrieve()

  for index in range(len(contact_list)):
    if name == contact_list[index]['Name']:
      contact_list.pop(index)
      print(f'Contact successfully deleted.')
      break

  write() # v.3

def list():
  counter = 1
  for contact in contact_list:
    print(f"{counter}. Name: {contact['Name']}, Favorite Fruit: {contact['Favorite Fruit']}, Favorite Color: {contact['Favorite Color']}")
    counter += 1

  write() # v.3

def main():
    while True:
        choice = input('''\nWelcome what would you like to do to your contacts? Enter a number from the choices listed below.
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
          print('Goodbye.')
          break

main()
