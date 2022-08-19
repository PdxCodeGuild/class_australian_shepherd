#        LAB10       CONTACTS.CSV         #


with open("contacts.csv", "r") as file:
    lines = file.read().split("\n")
    # print(lines)


# headers to create are     NAME,    Favorite FRUIT,    Favorite COLOR

headers_with_commas = lines[0]
headers = headers_with_commas.split(",")

contacts_csv = []
for line in range(1, len(lines)):
    values = lines[line].split(",")
    contact = {}
    for i in range(len(headers)):
        contact[headers[i]] = values[i]
    contacts_csv.append(contact)

# print(contacts_csv, ' this is whats in contact_csv')


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


def retrieve(csv_list, users_name):
    for index in range(len(csv_list)):
        if csv_list[index]["Name"] == users_name:

            return csv_list[index]


def update(contacts_csv, user_update):

    # contacts = retrieve(contacts_csv, user_update)
    # print(contacts)
    # contact_updates = contacts
    # print(contact_updates.keys(), contact_updates.values(), ' this is the contact_updates keys & values')
    # bring forth users information to change/update
    which_value = input(f"What value do you wish to update?:\n{headers} ").lower()
    update_value = input(f"What is the updated value?: ")
    for contact in contacts_csv:
        if contact["Name"] == user_update:
            if which_value == "name":
                contact["Name"] = update_value
            if which_value == "favorite fruit":
                contact["Favorite Fruit"] = update_value
            if which_value == "favorite color":
                contact["Favorite Color"] = update_value
        # print(contact)


def delete(contacts_csv, which_contact):

    for contact in range(len(contacts_csv)):

        if contacts_csv[contact]["Name"] == which_contact:

            del contacts_csv[contact]
            print(contacts_csv)
            break
    print(contacts_csv)


def save(contacts_csv, headers_string, headers_list):
    with open("contacts.csv", "w") as file:
        working_string_csv = ""
        working_string_csv += headers_string + "\n"

        for contact in contacts_csv:

            string_line = ""
# try using an f string to add the contact
            string_line += contact[headers_list[0]]
            string_line += "," + contact[headers_list[1]]
            string_line += "," + contact[headers_list[2]]

            working_string_csv += string_line + "\n"
        working_string_csv = working_string_csv[:-1]

        file.write(working_string_csv)


while True:
    user_input = input(
        """Type the number of the command you want: 
        1 = Create
        2 = Retrieve
        3 = Update
        4 = Delete
        5 = Save
        6 = "Exit"\n
        """
    )

    if user_input == "1":
        contacts_csv.append(create())
        # print(contacts_csv)

    elif user_input == "2":
        users_name = input("Please enter a users name to display their information: ")
        contact = retrieve(contacts_csv, users_name)
        for value in contact:
            print(f"{value}: {contact[value]}\n")

    elif user_input == "3":
        user_update = input(
            "Please enter the name of the user you would like to update their information: "
        )
        update(contacts_csv, user_update)
        pass

    elif user_input == "4":
        which_contact = input(f"Which contact would you like to delete?: ")
        delete(contacts_csv, which_contact)

    elif user_input == "5":
        save(contacts_csv, headers_with_commas, headers)

    else:
        break
