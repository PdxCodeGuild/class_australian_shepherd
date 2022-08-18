
#        LAB10       CONTACTS.CSV         #


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
    
    
# headers to create are     NAME,    Favorite FRUIT,    Favorite COLOR





headers = lines[0].split(",")
contacts_csv = []
for line in range(1, len(lines)):
    values = lines[line].split(",")
    contact = {}
    for i in range(len(headers)):
        contact[headers[i]] = values[i]
    contacts_csv.append(contact)

print(contacts_csv)


# name = input("Please enter a name: ")
# favorite_fruit = input("Please enter their Favorite Fruit: ")
# favorite_color = input("Please enter their Favorite Color: ")

# contacts_dict = {
#     'Name': name,
#     'Favorite Fruit': favorite_fruit,
#     'Favorite Color': favorite_color
# }

def create():
    new_user = {}
    for header in headers:
        new_user[header] = input(f"Please enter the new users {header}: ")
    return new_user
    
def retrieve(csv_list):
    users_name = input("Please enter a users name to display their information: ")
    
    for index in range(len(csv_list)):
        if csv_list[index]['Name'] == users_name:
            
            return csv_list[index]
def update():
    user_update = input("Please enter the name of the user you would like to update their information: ")
    
    contact = retrieve(contacts_csv)
    for value in contact:
        update = ({value}: {contact[value]})
    
    
    
    
    
while True:
    user_input = input("""Type the number of the command you want: 
        1 = Create
        2 = Retrieve
        3 = Update
        4 = Delete
        5 = "Exit"\n
        """)
    
    if user_input == "1":
        contacts_csv.append(create())
        print(contacts_csv)
    elif user_input == "2":
        contact = retrieve(contacts_csv)
        for value in contact:
            print(f"{value}: {contact[value]}\n")
        
    elif user_input == "3":
        # update()
        pass
    elif user_input == "4":
        # delete()
        pass
    else:
        break
    
    
    
    # how to add lines to the csv
    
# person = {
#         'name': "matt",
#         'fruit': 'apple',
#         'color': 'green'
#     }
    
# dummy_data = f"name,fruit,color\n{person['name']},{person['fruit']},{person['color']}"
    
# with open('new_contacts.csv', 'w') as file:
#     file.write(dummy_data)