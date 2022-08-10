'''
Nested Data Structures 
'''

# Nested data is simply data structures that make saving, collecting, accessing, accumulating data more sensible sometimes.
# It at first seems complex, but with proper nesting, it makes working a simplified process



# An example of a list with no data in it -----------------------------------------------------------------------------------

library_inventory = []


# An example of a list thats populated with strings. Notice the books are in alphabetical order  -------------------------------------------------------------------------------

library_inventory = ['Lord of the Rings', 'The Raven', "Moby Dick"] # The list stores only the books name. 


# The above list does not store information on each of these books. A library will want other data with it such as the author

# 🚨 DONT DO THIS 🚨


library_inventory = ['Lord of the Rings', 'J.R.R. Tolkien', 'Moby Dick', 'Herman Melville', 'The Raven', 'Edgar Allan Poe']

# the problem with this approach is there is no true relationship in the datastructures between author and book. Currently, it just happens to be the next index

lord_of_the_rings_author = library_inventory[1]
moby_dick_author = library_inventory[3]

# print(f'\nThe author of LOTF is {lord_of_the_rings_author} and the author of Moby Dick is {moby_dick_author}.') # The author of LOTF is J.R.R. Tolkien and the author of Moby Dick is Herman Melville



# But if a new book was added, the previous way of accessing the values is incorrect. 

library_inventory = ['Animal Farm', 'George Orwell', 'Lord of the Rings', 'J.R.R. Tolkien', 'Moby Dick', 'Herman Melville', 'The Raven', 'Edgar Allan Poe']

lord_of_the_rings_author = library_inventory[1] # Wrong, information
moby_dick_author = library_inventory[3]         # Wrong, information

# print(f'\nThe author of LOTF is {lord_of_the_rings_author} and the author of Moby Dick is {moby_dick_author}.') # The author of LOTF is George Orwell and the author of Moby Dick is J.R.R. Tolkien.



library_inventory = [
    ['Lord of the Rings', 'J.R.R. Tolkien'],
    ['Moby Dick', 'Herman Melville'],
    ['The Raven', 'Edgar Allan Poe']
]

# The example above makes each item in the list its own list, nesting the data, but we still have the same problem as before. 
# Problem: The books are stored through index positions, that would be changed if another book was added
# it is not easy to search the outer list for the data

library_inventory = [
    ['Animal Farm', 'George Orwell'],
    ['Lord of the Rings', 'J.R.R. Tolkien'],
    ['Moby Dick', 'Herman Melville'],
    ['The Raven', 'Edgar Allan Poe']
]

lord_of_the_rings = library_inventory[1]
moby_dick = library_inventory[2]

# print(lord_of_the_rings)# ['Lord of the Rings', 'J.R.R. Tolkien']
# print(moby_dick) # ['Moby Dick', 'Herman Melville']


library_inventory = [
    ['Alice in Wonderland', 'Lewis Carrol'],
    ['Animal Farm', 'George Orwell'],
    ['Lord of the Rings', 'J.R.R. Tolkien'],
    ['Moby Dick', 'Herman Melville'],
    ['The Raven', 'Edgar Allan Poe']
]

lord_of_the_rings = library_inventory[1]
moby_dick = library_inventory[2]


# print(lord_of_the_rings) # ['Animal Farm', 'George Orwell']  Wrong, information
# print(moby_dick) # ['Lord of the Rings', 'J.R.R. Tolkien']   Wrong, information






# A single dictionary is better for storing the information of a single book apposed to a list -------------------------------------------------------------


# Below is a raw dictionary for alice in wonderland
book = {
    'title': 'Alice in Wonderland',
    'author': 'Lewis Carrol',
    'pub_date': '11/18/1865',
    'location': 'literature 2b',
    'stock': 7,
}

# it's now very easy to return all the information in a fast and safe way.

# print(f"\nThe book {book['title']} was written by {book['author']}, published on {book['pub_date']}. There are currently {book['stock']} in stock and they are located in at {book['location']}")


# Nested Dictionaries: How we should approach this problem -------------------------------------------------------------------------------------------------------------------------------------------


library_inventory = {
    'Alice in Wonderland': {
        'title': 'Alice in Wonderland',
        'author': 'Lewis Carrol',
        'pub_date': '11/18/1865',
        'location': 'literature 2b',
        'stock': 7,
    }, 
    'Animal Farm': { 
        'title': 'Animal Farm',
        'author': 'George Orwell',
        'pub_date': '08/17/1945',
        'location': 'literature 6b',
        'stock': 3
    },
    'Lord of the Rings' :{
        'title': 'Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'pub_date': '07/29/1954',
        'location': 'fiction 1a',
        'stock': 0
    },
    'Moby Dick' : {
        'title': 'Moby Dick',
        'author': 'Herman Melville',
        'pub_date': '08/18/1854',
        'location': 'literature 2d',
        'stock': 3
    },
    'The Raven' :{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'pub_date': '01/29/1845',
        'location': 'literature 2a',
        'stock': 7
    },

}

# print(library_inventory['Alice in Wonderland'])


# Example of how easy it is to work with this data
'''
print('Welcome to the Library')
book_title = input("Search for a title: ")

print(f"""
--------------------------------------------------------------------
{library_inventory[book_title]['title']}, by {library_inventory[book_title]['author']}
Publication date: {library_inventory[book_title]['pub_date']}

NUmber in stock: {library_inventory[book_title]['stock']}
Located on section: {library_inventory[book_title]['location']}
--------------------------------------------------------------------

""")

'''


# But what if we need information in one of these books that isnt singular?  -------------------------------------------------------------------------------------------------------------
# Nest again, either using a List or another Dictionary

library_inventory = {
    'Alice in Wonderland': {
        'title': 'Alice in Wonderland',
        'author': 'Lewis Carrol',
        'pub_date': '11/18/1865',
        'location': 'literature 2b',
        'stock': 7,
        'characters': ['Alice', 'Mad Hatter']
    },
    'Animal Farm' : { 
        'title': 'Animal Farm',
        'author': 'George Orwell',
        'pub_date': '08/17/1945',
        'location': 'literature 6b',
        'stock': 3,
        'characters': ['Napoleon', 'Snowball', 'Boxer']
    },
    'Lord of the Rings' :{
        'title': 'Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'pub_date': '07/29/1954',
        'location': 'fiction 1a',
        'stock': 0,
        'characters': ['Frodo', 'Sam', 'Gandalf']
    },
    'Moby Dick' : {
        'title': 'Moby Dick',
        'author': 'Herman Melville',
        'pub_date': '08/18/1854',
        'location': 'literature 2d',
        'stock': 3,
        'characters': ['Ishmael', 'Father Mapple']
    },
    'The Raven' :{
        'title': 'The Raven',
        'author': 'Edgar Allan Poe',
        'pub_date': '01/29/1845',
        'location': 'literature 2a',
        'stock': 7,
        'characters': ['The Raven', 'Lenore']
    },
}

'''

print("Welcome to the Library ")
book_title = input("Search for a title and I will tell you the characters in the book: ")


print(f"""
--------------------------------------------------
{library_inventory[book_title]['title']}, by {library_inventory[book_title]['author']}
Publication date: {library_inventory[book_title]['pub_date']}

Characters: {', '.join(library_inventory[book_title]['characters'])}
--------------------------------------------------
""")
'''


library_inventory2 = {
    'Lord of the Rings' : {
        'title': 'Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'pub_date': '07/29/1954',
        'location': 'fiction 1a',
        'stock': 0,
        'characters': [
            {
                'name': 'Frodo',
                'species': 'hobbit',
            },
            {
                'name': 'Sam',
                'species': 'hobbit',
            },      
            {
                'name': 'Gandalf',
                'species': 'Wizard',
            }    
        ]
    }
}


# Search for a character to see if it is in the book


title = 'Lord of the Rings'
character = input(f"Enter the name of the character to see if it is in {title}: ").title()

book = library_inventory2[title]
characters_list = book['characters']

message = ''
for character_dict in characters_list:
    if character_dict['name'] == character:
        message = f"\n{character} is in the book {title}."

if not message:
    message = f"\n{character} is NOT in the book {title}."

print(message)