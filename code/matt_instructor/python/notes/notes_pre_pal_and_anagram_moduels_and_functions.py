'''
Modules and Functions 
'''

# import the_raven
from re import L
import the_raven

# print(the_raven.the_raven_text)


# Python comes with many built in modules. These are files on your computer that python knows to look for when given their key words. 
# here are examples of a few.

import random
import string
import turtle
import math
import email

# note that normally, all imports would be directly on top in your file. This is so the whole contents of our file has access to the imformation

# Random is very useful. By importing it, we have access to many powerful math methods and fuctions which make it so we don't have to build them ourselves

# Generate a random number between 1 and 100

number = random.randint(1, 100)

students = ['justin', 'ben', 'amber', 'ignacio', 'kacey', 'matt', 'mike', 'rick', 'paul']

choosen_student = random.choice(students)
# print(choosen_student)


# Function ---------------------------------------------------------------------------------------------------------------------

# A function is a block of code which only runs when it is called.
# You can pass data, known as arugments, into a function.
# A function returns data as a result.
# If no data is returned, Python by default returns None

# define a function---------------------------------------------------------------------------------------------------------------------

# This function named add_numbers, takes in two numbers and returns the sum of the two numbers

def add_numbers(number_1, number_2):
    return number_1 + number_2

# Call the function with () after its name to run it and get the returend value
result = add_numbers(3, 7)

# print(result + 5, 'is the number + 5')


# Parameters and Arguments ---------------------------------------------------------------------------------------------------------------------

# Arguments is the data being provided to the function
# Parameters are clones of that data that ONLY exist inside the function. The are empty vessels until data is given to them


def minus(num1, num2):
    num1 = 900
    return num1 - num2

number_1 = 1
number_2 = 2

# print(minus(number_1,number_2))

# print(num1) #   NameError: name 'num1' is not defined

# Scope. Block and Global  ---------------------------------------------------------------------------------------------------------------------

dog = 'roger' #Global scope

def add(num1, num2):
    # print(dog) # it works becuse it is a global scope variable
    cat = 'tim' # block
    return num1 + num2

# print(add(1, 2))

# print(cat, 'is the name of the cat') # does not work becaues it is block scope variable



# another example

def tell_dogo_what_they_are(name, sex):
    return f'{name} is a good {sex}'

dog = 'Dug'
gender = 'boy'


# print(tell_dogo_what_they_are(dog, gender))

# Questions
# print(tell_dogo_what_they_are()) # TypeError: tell_dogo_what_they_are() missing 2 required positional arguments: 'name' and 'sex'
# print(tell_dogo_what_they_are(dog)) # TypeError: tell_dogo_what_they_are() missing 1 required positional argument: 'sex'
# print(tell_dogo_what_they_are(gender, dog)) # boy is a good Dug

# Question. Why is dog, name and gender, sex?



# Make a function that returns True or False

def is_user_banned(user_name):
    banned_users = ['Evil_Greg', 'Tim', 'Tammy', 'All_Karens']

    if user_name in banned_users:
        return True
    else:
        return False


# user = input('Enter a username to see if banned: ')

# attempt = is_user_banned(user)

# if attempt != True:
#     print(f'this attempt failed')
# else:
#     print(f'The attempt was sucessful')


# Grading Lab WIHOUT Functions ---------------------------------------------------------------------------------------------------------
"""
grade = input("enter the sore and I will tell you a letter grade: ")
grade = int(grade)

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else: 
    letter_grade = 'F'

rival_grade = random.randint(0, 100)

if rival_grade >= 90:
    rivial_letter_grade = 'A'
elif rival_grade >= 80:
    rivial_letter_grade = 'B'
elif rival_grade >= 70:
    rivial_letter_grade = 'C'
elif rival_grade >= 60:
    rivial_letter_grade = 'D'
else:
    rivial_letter_grade = 'F'
"""
# print(f"\nYou scored a {grade} receiving a {letter_grade} and your rival scored a {rival_grade} receiving a {rivial_letter_grade}")


# Grading Lab WITH Functions: 
# reduces the repetitive nature of this code 

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else: 
        return 'F'

grade = input("Enter the numeric score you got on your test: ")
grade = int(grade)

rival_grade = random.randint(1, 100)

user_score = get_letter_grade(grade)
rival_score = get_letter_grade(rival_grade)

print(user_score, rival_score)