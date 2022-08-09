import random
import math


number = random.randint(1, 100)

students = [
    "justin",
    "ben",
    "amber",
    "ingacio",
    "kacey",
    "matt",
    "mike",
    "rick",
    "paul",
]

# choose_student = random.choice(students)
# print(choose_student)

# students.append('greg')
# # print(students)

# def add_numbers(number_1, number_2):

#     return number_1 + number_2

# result = add_numbers(3, 7)

# # print(result)

# # print(result + 5, ' is the number plus 5')


# def add(num1, num2):
#     return num1 + num2

# print(add(1, 2))

# def minus(num_1, num_2):
#     return

# number_1 = 1
# number_2 = 2


# another example

# def tell_doggo_what_they_are(name, sex):
#     return f'{name} is a good {sex}'

# dog = 'Dug'
# gender = 'boy'

# print(tell_doggo_what_they_are(dog, gender))

# def is_user_banned(user_name):

#     banned_users = ['Evil_Greg', 'Tim', 'Tammy', 'All_Karens']

#     if user_name in banned_users:
#         return True

# user = 'Evil_Greg'

print(is_user_banned("Evil Greg"))


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"


grade = input("enter a numeric score you got on your test: ")
grade = int(grade)

rival_grade = random.randint(1, 100)

user_score = get_letter_grade(grade)
rival_score = get_letter_grade(rival_grade)

print(user_score, rival_score)
