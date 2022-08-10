import random

sock_types = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}
socks_list = ['ankle', 'crew', 'calf', 'thigh']


def random_socks():
    socks = []
    for i in range(100):
        socks.append(random.choice(socks_list))
    # print(socks)
    return socks

def match_socks(socks):
    for sock in socks:
        for sock_type in sock_types.keys():
            if sock == sock_type:
                sock_types[sock_type] += 1
    return sock_types
        
def find_loners(sock_types):
    for sock_type in sock_types.keys():
        if sock_types[sock_type] % 2 != 0:
            # loners.append(sock_types[sock_type])
            # print(sock_types[sock_type] % 2)
            print(f'\n{sock_types[sock_type] % 2} {sock_type} loner')
        print(f'\n{sock_types[sock_type] // 2} {sock_type} pairs')
            


find_loners(match_socks(random_socks()))



###################        NOTES ON DICTIONARYS!!!!             ##############

# example_dict = {
#     'a' : 1,
#     'b' : 2, 
#     'c' : 3
# }

# print(example_dict['c']) #3

# address dictionary

# address = {
#     'street' : '1231 NE Main Street',
#     'city' : 'Portalnd',
#     'state' : 'Oregon',
#     'zip' : 97267
# }

# # print(f'The location is {address["street"]} {address["city"]} {address["state"]} {address["zip"]}')


# person = {
#     'name' : 'Tim',
#     'age' : 33, 
#     'weight' : 190,
#     'address' : {
#         'street' : '1231 NE Main Street',
#         'city' : 'Portalnd',
#         'state' : 'Oregon',
#         'zip' : 97267
#     }
# }

# print(f"{person['name']} lives in {person['address']['city']}")


# print(f"{person['name']} is {person['age']} years old")


# users = [
#     {
#         'name' : 'Tim', 
#         'age' : 33,
#         'weight' : 190,
#         'address' : {
#             'street' : '1231 NE Main Street',
#             'city' : 'Portland',
#             'state' : 'Oregon',
#             'zip' : 97267
#         }
#     },
#     {
#         'name' : 'Jill',
#         'age' : 27,
#         'weight' : 150,
#         'address' : {
#             'street' : '5321 SW Lasso Blvd',
#             'city' : 'Austin',
#             'state' : 'Texas',
#             'zip' : 97254
#         }
#     }
# ]

# print(type(users)) #class list
# print(users[0]) #{'name': 'Tim', 'age': 33, 'weight': 190, 'address': {'street': '1231 NE Main Street', 'city': 'Portland', 'zip': 97267}}

# print(type(users[0])) # class dict

# print(users[1])

# user_1 = users[0]

# user_2 = users[1]

# print(user_1)
# print(user_2)




# if user_1['address']['state'] == user_2['address']['state']:
#     print(f"Both {user_1['name']} and {user_2['name']} both live in {user_1['address']['state']}")
# elif user_1['address']['state'] != user_2['address']['state']:
#     print(f"{user_1['name']} lives in {user_1['address']['state']}\nBut {user_2['name']} lives in {user_2['address']['state']}")

# for dict_item in users:
#     print(f"Name: {dict_item['name']}\t Zip: {dict_item['address']['zip']}")



############## NESTED DATA STRUCTURES  ##################


# library_inventory = []

# library_inventory = ['Lord of the rings', 'The Raven', 'Moby Dick']


# lord_of_the_rings_author = library_inventory[1]

# moby_dick_author = library_inventory[3]



# library_inventory = ['Animal Farm', 'George Orwell', 'Lord of the Rings', 'J.R.R. Tolkein'] # added new information which would change the program to the incorrect information

# library_inventory = [
#     ['Lord of the Rings', 'J.R.R. Tokien']
#     ['Moby Dick', 'Herman Melville']
#     ['The Raven', 'Edgar Allan Poe']
# ]


# library_inventory = [
#     ['Animal Farm', 'George Orwell'] # THE NEW INPUT OF BOOK AND AUTHOR CHANGED INDICES VALUES
#     ['Lord of the Rings', 'J.R.R. Tokien']
#     ['Moby Dick', 'Herman Melville']
#     ['The Raven', 'Edgar Allan Poe']
# # ]

# book = {
#     'title' : 'Alice in Wonderland',
#     'author' : 'Lewis Carrol', 
#     'pub_date' : '11/18/1555',
#     'location' : 'literature 2b',
#     'stock' : 7
# }

# print(f"The book {book['title']} was written by {book['author']}, published on {book['pub_date']}. There are currently {book['stock']} and they are located at {book['location']}")

# print('Welcome to the Library')
# book_title = input('Search for a title: ')

# print(f"""
#     ----------------------------
#     {library_inventory[book_title]['title']}, by {library_inventory[book_title]['author']}
    
    
    
    
    
#     ----------------------------
#     """)

