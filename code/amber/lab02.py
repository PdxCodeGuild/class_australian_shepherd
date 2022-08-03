# MADLIBS

import random

# "Everyone should have their minds blown at least once a day." - Neil deGrasse Tyson

person = input("enter a type of person/people (plural): ").title()
body_part = input("Enter a body part (plural): ")
action = input("Enter an action word (past tense): ")
unit_of_time = input("Enter a unit of time: ")
first_name = input("Enter a first name: ").title()
middle_name = input("Enter a middle name: ").title()
last_name = input("Enter a last name: ").title()

#madlib = f'"{person} should have their {body_part} {action} at least once a {unit_of_time}." - {first_name} {middle_name} {last_name}'

#print(madlib)

# v.2

names = [first_name, middle_name, last_name]

madlib = f'"{person} should have their {body_part} {action} at least once a {unit_of_time}." - {random.choice(names)} {random.choice(names)} {random.choice(names)}'

print(madlib)
