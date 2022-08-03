# Lab 2a
# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.

welcome_message = 'Hi, welcome to the Mad Lib lab'
print(welcome_message)
dog_name = input('Give me a name: ').capitalize()
age = input('Give me a number between 1-15: ')
weight = input('Give me another number between 1-100: ')
emotion = input('Give me an adjective: ')


print(f'''
Here's your Mad Lib:
You bought a dog and named it {dog_name}.
It is {age} years old and {weight} pounds.
When you see it, it makes you feel {emotion}!
'''
)