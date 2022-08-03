# Lab 2a
# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.

# welcome_message = 'Hi, welcome to the Mad Lib lab'
# print(welcome_message)
# dog_name = input('Give me a name: ').capitalize()
# age = input('Give me a number between 1-15: ')
# weight = input('Give me another number between 1-100: ')
# emotion = input('Give me an adjective: ')


# print(f'''
# Here's your Mad Lib:
# You bought a dog and named it {dog_name}.
# It is {age} years old and {weight} pounds.
# When you see it, it makes you feel {emotion}!
# '''
# )

# Version 2
# Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, 
# then use the .split() function to store each adjective and later use it in your story.
# Add randomness! Use the random module, rather than selecting which adjective goes where in the story

welcome_message = 'Hi, welcome to the Mad Lib lab'
print(welcome_message)
i = 0
dog_name_list = []
age_list = []

while i < 3:
    dog_name = input('Give me a name: ').capitalize()
    dog_name_list.append(dog_name)
    i += 1

while i < 6:
    age = input('Give me a number between 1-15: ')
    age_list.append(age)
    i += 1

print(dog_name_list)
print(age_list)

# 
# weight = input('Give me another number between 1-100: ')
# weight_list = []
# emotion = input('Give me an adjective: ')
# emotion_list = []


# print(f'''
# Here's your Mad Lib:
# You bought a dog and named it {dog_name}.
# It is {age} years old and {weight} pounds.
# When you see it, it makes you feel {emotion}!
# '''
# )