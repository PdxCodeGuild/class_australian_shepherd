# Importing random to choose a sock type at random
import random
# Creating a dictionary to loop through and pull a value from
socks = {
    1: 'ankle',
    2: 'crew',
    3: 'calf',
    4: 'thigh'
}
# Creating an empty dictionary to store our socks
sock = {}
# Creating a function to choose a random sock and add it to the dictionary
def sock_monster():
    new = random.choice(list(socks.values()))
    sock[i+1] = new
# Calling our function 100 times to add 100 socks to our dictionary
for i in range(100):
    sock_monster()
# Creating 0 balances to count up from
thigh = 0
crew = 0
calf = 0
ankle = 0
# Using a for statement to iterate through our dictionary values and count up for each sock type
for val in sock.values():
    if val == 'thigh':
        thigh += 1
    elif val == 'crew':
        crew += 1
    elif val == 'ankle':
        ankle += 1
    elif val == 'calf':
        calf += 1
# Calling our print statements containing the math to determine howmany loners and pairs we have
print(f'There are {thigh//2} pairs of thigh socks with {thigh % 2} loners.')
print(f'There are {crew//2} pairs of crew socks with {crew % 2} loners.')
print(f'There are {ankle//2} pairs of ankle socks with {ankle % 2} loners.')
print(f'There are {calf//2} pairs of calf socks with {calf % 2} loners.')