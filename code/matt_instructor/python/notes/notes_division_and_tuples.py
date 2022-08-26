'''
Division and Tuples
'''
import random

# Three kinds of divisiion

# Regular
# Floor
# Modulus 


# Regular Division -------------------------------------------------------------------------------------------
# uses the single /
# always returns a Float
# basically just normal division

result = 5 / 2
# print(result) # 2.5

result_2 = 1 / 1
# print(result_2) # 1.0

# Floor Division -------------------------------------------------------------------------------------------
# uses two //
# always returns an Integer
# think of it as always rounding down

result = 5 // 2 
# print(result) # 2   (revmoves the .5)

result_2 = 1 // 1
# print(result_2) # 1

# What is floor division good for?
    # When you do not care about the remainder
    #  Example. You have 5 setudents and you want to represent them each in a number 1 though 5
    # Student 1.5 does not exist, so any calcuations should be integers, not float

students = ['jill', 'tim', 'billy', 'bob', 'sara']



# student_index = random.randint(1, 5)

# student_index = 2.0 # this will not work, must be an integer

# print(student_index)

# print(f'Random student: {students[student_index]}')


# What is floor division good for?
    # Finding how many dimes could go into your dollar amount (or all other change)

dollars = 1.59

total_pennies = dollars * 100
# print('Total pennies', total_pennies)

total_dimes = total_pennies // 10
# print(f"The are {int(total_dimes)} dimes in ${dollars}")



# Modulus Division -------------------------------------------------------------------------------------------
# uses %
# Modulus Operator is an inbuilt operator that returns the remaining numbers by dividing the first number from the second

# Wait what? In English please

# Fine, just look at this example

# // and % are compliments

# Modulus grabbed the remainer as a whole number.




# Ok why does this matter?  -------------------------------------------------------------------------------------------

# Modulus is extreemly powerful to solve some common problems

# 1: Modulus is useful when
    # we want to find even a number is even or odd

number = 2

# if a number % 2 is equal to 0, then the number is even
# print(number % 2) # 0 even

number = 3
# if a number % 2 is equal to 1, the number is odd
# print(number % 2) # 1 odd


"""

# Finding even or odd with conditional statements
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f'{number} is an even number')
elif number % 2 == 1:
    print(f"{number} is an odd number")

"""


# Tuples -------------------------------------------------------------------------------------------
# What is a tuple?
# it's an ordered and unchangeable (immutable) list defined by using ( ) instead of [ ]

date_of_birth = ('May', 1988)
# print(date_of_birth[1])

# Tuples use index positions just like normal lists
# Tuples do everything just like normal lists, except change 

colors = ('red', 'blue', 'green')

# colors[0] = 'teal' # TypeError: 'tuple' object does not support item assignment

# Lists can do this
# colors = ['red', 'blue', 'green']

# colors[0]  = 'teal'
# print(colors) # ['teal', 'blue', 'green']

# this means Tuples cant use most list methods

colors = ('red', 'blue', 'green')

# colors.append('teal') # AttributeError: 'tuple' object has no attribute 'append'



# Why use Tuples? Over lists if they have less features??? -----------------------------------
    # 1: Tuples are more memory efficient.
        # in programming, anything that is changable takes more memory. More memory means more processing. Less memory means faster// 
    # 2: Tuples require less memory 
        # In python, we don't often have to think about memory, but we can still run into issues when dealing with larger data sets
    # 3: Python will not tolerate you changing them
        # A date of birth can never change. Why make it a possibility to accidently be manipulated?

# It was Tuples all along...
# Many methods, function and processes in python use Tuples to return their results to you. Why? Because its faster and is more efficient