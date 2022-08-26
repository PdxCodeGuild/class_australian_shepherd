'''
enumerate()
'''


"""
colors = ['red', 'blue', 'green', 'teal', 'pink']

# a for loop to grab each value and do the code block
for item in colors:
    print(item)

"""

"""
colors = ['red', 'blue', 'green', 'teal', 'pink']

# Does not work as it does NOT grab index position
# use a for loop to change any item that is 'blue' to 'black'
for item in colors:
    if item == 'blue':
        item = 'black'

print(colors)
"""

"""
# use a for loop to change any item that is 'blue' to 'black' using a counter
# it works, but extra lines

colors = ['red', 'blue', 'green', 'teal', 'pink']

counter = 0

for item in colors:
    if item == 'blue':
        colors[counter] = 'black'
    counter += 1

print(colors)
"""


"""
# use a rang loop to change any item that is 'blue' to 'black' using a counter

colors = ['red', 'blue', 'green', 'teal', 'pink']

for index in range(len(colors)):
    if colors[index] == 'blue':
        colors[index] = 'black'

print(colors)

"""


# use enumerate to do the same thing in less lines

colors = ['red', 'blue', 'green', 'teal', 'pink']

for index, value in enumerate(colors):
    if value == 'blue':
        colors[index] = 'black'

print(colors)