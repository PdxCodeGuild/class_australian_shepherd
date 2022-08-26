
"""
The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
"""

jacks = [0, 0]
years = 0

while len(jacks) < 1000:
    years += 1
    # print('looping')

    # age jacks
    for index in range(len(jacks)):
        jacks[index] += 1
    # print(jacks)

    new_jacks = []
    # Kill jacks
    for item in jacks:
        if item <= 9:
            # print(item)
            new_jacks.append(item)

    jacks = new_jacks

    # Number of jacks who can have babies
    frisky_jacks = 0
    for index in range(len(jacks)):
        if jacks[index] > 3 and jacks[index] < 9:
            frisky_jacks += 1

    print(f'Year {years}: frisky: {frisky_jacks} ')


    # find if odd number of frisky jacks, and minus 1 if it is odd
    if frisky_jacks % 2 != 0:
        frisky_jacks -= 1
    

    baby_jacks = frisky_jacks
    print('baby jacks', baby_jacks)

    for num in range(baby_jacks):
        jacks.append(0)
    print('total jacks', len(jacks))
    print()

print(years, len(jacks))




