'''
Python Dictionary's
'''

# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. ------------------
# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.

from audioop import add


exmaple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}


# We use the key's to get the value.
# if I wanted to get 3 from this dictionary, I need to name the dictionary and then use [] after its name putting the appropriate key in it

# print(exmaple_dict['c']) # 3

# Dictionary's are useful as they store pairs of data. A key give access to its value which can be a literal like 3 or even another 
# dictionary or list. It can store any datatype



# Address Dictionary 

address = {
    'street': '1231 Ne Main Street',
    'city': 'Portland',
    'state': 'Oregon',
    'zip': 97032
}

# print(f"The location is {address['street']} {address['city']} {address['state']}, {address['zip']}")
# The location is 1231 Ne Main Street Portland Oregon, 97032


# Person Dictionary

person = {
    'name': 'Tim',
    'age': 33,
    'weight': 190
}


# print(f"{person['name']} is {person['age']} years old")


# if The address dictionary was for the person, Tim, they would not be meaningfully connected.
# By nesting these two dictionary's in each other we get a meaningful collection of workable data

person = { 
    'name': 'Tim',
    'age': 33,
    'weight': 190,
    'address': {
        'street' : '1231 Ne Main Street',
        'city': 'Portland',
        'state': 'Oregon',
        'zip': 97213
    }
}


# print(f"{person['name']} lives in {person['address']['city']}") # Tim lives in Portland



# However, this is just one single person.


# What if we needed to have multiple people or users?

# store these in lists


users = [
    {
        'name' : 'Tim',
        'age': 33,
        'weight': 190,
        'address': {
            'street': '1231 Ne Main Street',
            'city': 'Portland',
            'state': 'Oregon',
            'zip': 97213
        }
    },
    {
        'name': 'Jill',
        'age': 27,
        'weight': 150,
        'address': {
            'street': '5312 Sw Lasso Blvd',
            'city': 'Austin',
            'state': 'Texas',
            'zip': 54321
        }
    }
]

# print(type(users)) #<class 'list'>
# print(users[0]) # {'name': 'Tim', 'age': 33, 'weight': 190, 'address': {'street': '1231 Ne Main Street', 'city': 'Portland', 'zip': 97213}}
# print(type(users[0])) # <class 'dict'>

user_1 = users[0]

user_2 = users[1]

# print(user_1)
# print(user_2)


# Make a program that finds out of user 1 and 2 live in the same state -----------------------------------------------------------------------------------------

user_1 = users[0]
user_2 = users[1]

# print(user_1)
"""
if user_1['address']['state'] == user_2['address']['state']:
    print(f"Both {user_1['name']} and {user_2['name']} both live in {user_1['address']['state']}")
else:
    print(f"{user_1['name']} lives in {user_1['address']['state']}")
    print(f"But {user_2['name']} lives in {user_2['address']['state']}")

"""

# Make a program that tells you where each user name and zip code -----------------------------------------------------------------------------------------

for dict_item in users:
    print(f"Name: {dict_item['name']}\t Zip: {dict_item['address']['zip']}")