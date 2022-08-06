"""
Fundamentals
# Pre MadLibs Lab
"""

# Variables ---------------------------------------------------------------------------------------------------------
# Variables are names given to objects. These allow us to specify the operations we'd like to perform on 
# that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables.
# Everything in Python is an object.

x = 5

# print(x) # 5

# We can easily re-assign a varaible in python. Re assign the value of x to 10

x = 10

# print(x) # 10

# Python does not need us to declare the data type of our variables. It is the data type of whatever is stored in it.
# Re assign x to a string without issue

x = 'Hello World'

# print(x) # 'Hello World'


# Manipulating the data already stored in a varable -----------------------------------------------------------------

color = 'red' #

# variable 'color' IS a string because it CONTAINS a string
# print(type(color)) # <class 'str'>

color = color.upper() 
# print(color) # RED



# Python variable naming conventions -----------------------------------------------------------------

'''
Python Variable Names
- must start with a letter or underscore character
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are three different variables)
'''

age = 18   
Age = 19
AGE = 20  # all three different storage spaces

# python_variable_and_function_names_use_snake_case
# all lowercase words separated with underscores

# ThisIsTitleOrPascalCase - used in Python for defining classes (custom datatypes)
# ALLCAPS - generally used for constant variables


# Basic built in Function --------------------------------------------------------------------------------------------------------

# print('hello')
# input()

# print() prints data in the terminal. Returns None
# It can take multiple comma seperated arguments. PLEASE use this to label your data with testing. It helps
# stop confusion.

x = 3.14

# print("Pie: ", x) # Pie: 3.14

# input() allows the user to interact with the terminal as it pauses and waits for the users to type in information. Once the user
# hits enter, anything typed into the terminal will be returned in place. We can then store it into a variable

# name = input("Enter a name: ")

# print(name)


# Datatypes ---------------------------------------------------------------------------------------------------------
# Since everything in Python is an object, we can check the data type of the object, or a variables value by using
# the type()

# print(type(None)) # <class 'NoneType'>
# print(type(False))  # <class 'boolean'>
# print(type(5)) # <class 'int'>
# print(type('5')) # <class 'str'>
# print(type('hello')) # <class 'str'>
# print(type(3.14)) # <class 'float'>
# print(type([])) # <class 'list'>

# Check type() on variables

x = 5

# print(type(x)) # <class 'int'>

# print(x + ' is a number') # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Typecasting --------------------------------------------------------------------------------------------------------

# In Python, we can easily convert our literals or variables value by using typecasting functions

# Typecast on literals 

# print(str(5)) # '5'
# print(float('5')) # 5.0
# print(int('5')) # 5
# print(bool('True')) # True



# Typecast on variables

x = 5
x = str(x)

# print(type(x), x)  # <class 'str'> 5

y = '5'
y = float(y)
# print(y) # 5.0


# Concatenation --------------------------------------------------------------------------------------------------------
# Adding strings together to return a combined string

# print('hi' + ' ' + 'class') # hi class

# print('Welcome' + ' ' + 'class ' + 'Australian ' + 'Shepherd ')

name = 'Morty'

message = 'Hello'

greeting = message + ' ' + name

# print(greeting) # Hello Morty



# Working with Data returned from input() -------------------------------------------------------------------------------

# the input() always returns a string. This works perfectly with concatenation

# name = input("Enter your name: ")
# print('Welcome ' + name) # Welcome Matt


# Since the input() always returns a string, it will not work with operations like normal math

# number = input("Enter a number: ")
# print(number + 5) #TypeError: can only concatenate str (not "int") to str

# print(number + number) # 55




# number = input("Enter a number: ")

# number = int(number)
# print(number + 7)
# print(type(number), number) # <class 'int'> 5



# F strings -------------------------------------------------------------------------------
# stands for formatted. F strings make printing easier

city = 'Portland'
temp = 70

message = 'Welcome to ' + city + '! The temp today was ' + str(temp) + ' degrees!'
# print(message)

# concatenation only works between strings
# other datatypes will need to be "typecast" as strings using str()
# str(object) - return a string representation of the object

# message = 'Welcome to ' + city + '! The temp today was ' + str(temp) + ' degrees!'
# print(message) # Welcome to Portland! The temp today was 70 degrees!

message = f"Welcome to {city}! The temp today was {temp} degrees!"
# print(message) 


# maths = f'if you add up numbers, it works {5 + 9 * 15}'
# print(maths)


#-------------------------------------------------------------------------------
# Find the area of a rectangle with user-defined sides

height = input("Enter the height: ")
width = input("Enter the width: ")

height = float(height)
width = float(width)

area = height * width

# Display the results

result = f"""
Area of a Rectangle
-------------------
height ... {height}
width .... {width}
area ..... {area}"""

# print(result)