"""
Notes Pre Lab 3: Average Numbers
Variable re asignment, Conditionals, loops 
"""

# Adding to value stored in an Variable ---------------------------------------------------------------------------------------------------------

# number = 10
# print(number)

# number = number + 5
# print(number) # 15

# Shorthand version ---------------------------------------------------------------------------------------------------------

number = 10
number += 5
# print(number) # 15


name = 'Matt'
name = name + ' ' + 'Chimenti'
# print(name) Matt Chimenti

name = 'Matt'
name += ' ' + 'Chimenti'
# print(name) # Matt Chimenti



# Booleans---------------------------------------------------------------------------------------------------------

# Datatype: boolean (bool)
# True / False

a = True
b = False

# print(a, type(a))
# print(b, type(b))

# ----------------------------------------------------------------------- #

word_1 = 'cat'
word_2 = 'catt'

# print(word_1 == word_2) # True because they are equal

# x = word_1 == word_2
# print(x == False)


# print(word_1 != word_2) # True because they are not equal to each other

x = 5

# not - flip a boolean 

# print(x < 0) # False
# print(not x < 0) # True

# print(not False) # True
# print(not True) # False

# ------------------------------------------------------------------------------------ #

# check if a character is in a string using the   'in'    keyword

word = 'book'

# print('k' in word) # True
# print('z' not in word) # True



# Comparison Operators - compare two pieces of data and result in a boolean -----------------------------------------


x = 5
y = 5

# print(x == y) # == check equality - True
# print(x != y) # != check inequality - False

# print(x < y) # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y) # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True



# check the result of some math
# print(x / 2 == 2.5) # True


# check for a particular value in a variable
# print(x == 5) # True
# print(x == 9) # False




# (if statements) Conditional Statements --------------------------------------------------------------------------------------

# Conditional Statements - run different 'code blocks' based on the outcome of comparisons
# keywords: if, elif, else

# code block - A section of code that executes together.
#              In Python, code blocks are defined using horizontal indentation

'''
Conditional Statements
----------------------
- must start with an if
- every single if will be checked
- elif will only be checked if the preceding if and other elifs were False
- else will run if all other conditions were False
- if/elif will only be checked until a True condition is found
'''

'''
if/elif combos
--------------
if
if / else
if / elif
if / elif / else
if / elif / elif / ... / elif
if / elif / elif / ... / else
'''
"""
# ask the user for a color
color = input("Enter a color: ")

if color == 'purple' or color == 'yellow':
    output = f"I like the color {color}"

elif color == 'blue' or color == 'orange':
    output = f"{color.upper()}"

elif 'p' in color:
    output = f"The color {color} contains the letter 'p'"


elif not color:
    output = "color cannot be blank"

else:
    output = f"I'm indifferent to the color '{color}'"

# print(output)


"""

# Sequences ---------------------------------------------------------------------------------------------------------

# Some datatypes are sequences. A sequence is a positionally ordered collection of items. And you can refer to any item 
# in the sequence by using its index number 

# Examples

string_variable = 'A string is a sequence'
# print(string_variable)

list_variable = [1, 2, 3, 4, 5]
# print(list_variable)


# Both strings and lists are ordered, becuase they are sequences
# Because of this, we can use index positions

# print(string_variable[0]) # A
# print(list_variable[0]) # 1


# Lists ---------------------------------------------------------------------------------------------------------

# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# In other languages they are often called "Arrays"

# Adding items to the end of a list 

colors = []

colors.append('red')
# print(colors)

colors.append('blue')

colors.append('green')

# print(colors) # ['red', 'blue', 'green']



# Removing an item from the end of the list

# colors.pop()
# print(colors) # ['red', 'blue']


popped_item = colors.pop()
# print(popped_item, colors)



# Values from index ---------------------------------------------------------------------------------------------------

# we can use index positions in order to grab values from our sequences. Index's count up form 0


letters = ['a', 'b', 'c']

# print(letters[0]) # 'a'
# print(letters[1]) # 'b'
# print(letters[2]) # 'c'

# print(letters[3]) # IndexError: list index out of range

name = 'Morty'

# print(name[0]) # M
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])


# Length of a sequence  ---------------------------------------------------------------------------------------------------

# an inportant ability in programming is to find the length of a sequence. 
# For example is the number of elements in a list or string 

'Hi' # has 2 elements, meaning it has a len of 2
[10, 20, 30] # has 3 elements, meaning it has a len of 3

# use the len() to return an interger with then number of elements in the sequence
# len () returns a int

lengeth_of_string = len('hello')
# print(lengeth_of_string) # 5

length_of_list = len([10, '20', 30321313651654161565165165165])
# print(length_of_list) # 3



# for loop: Get each value from the sequence ---------------------------------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f']

# Loop over the elements in the sequence
"""
for item in letters:
    print(item)
"""

"""
for index in range(len(letters)):
    print(letters[index])
"""

"""
# remove any item with the value of 'd'
length_of_letters = len(letters)

# Loop over the indicies
for index in range(length_of_letters):
    # print(letters[index])

    if letters[index] == 'd':
        remove_index = index

letters.pop(remove_index)
print(letters)
"""

# while loop REPL ---------------------------------------------------------------------------------------------------

"""
# make an infinite loop
while True:
    print('\n we are stuck in an infinite loop! Help!!!') # break out with control c 
"""

"""
number = 1

while number == 1:
    print("we are in the loop")
    number = 0
print('we finished looping becaues number is now 0, and its while False ')
"""

"""
keep_looping = True

while keep_looping == True:
    print("Welcome to the game")
    keep_looping = input("Would you like to keep looping? yes no: ")

    if keep_looping == 'no':
        print("Thanks for playing :)")
        break
    else:
        keep_looping = True
"""

# populate a list within a REPL ---------------------------------------------------------------------------------------------------

# initilize the list before the loop, not inside of it
"""

colors = []

while True:

    color = input("\nEnter a color or 'done' to quit: ")

    if color == 'done':
        print(f"\nThank you for entering {', '.join(colors)}")
        break

    colors.append(color)
    print(colors)

colors = ['red', 'blue', 'green']


"""
# print(', '.join(colors)) # red, blue, green