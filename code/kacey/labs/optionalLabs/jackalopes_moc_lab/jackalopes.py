############################# JJJJJJJJJAAAAAAAAAAACCCCCCCCCCKKKKKKKKKKKKKKAAAAAAAAAALLLLLLLLLLOOOOOOOOOPPPPPPPPEEEEEEEEEEESSSSSSSSSSSSSSS   MOC LAB    #########################


"""

The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

1 Jackalopes are reproductive from ages 4-8 and die at age 10.
two jacks both age 0

Gestation is instantaneous. Each gestation produces two offspring.

Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

With these conditions in mind, we can represent our population as a list of ints.


"""


year = 1

jacks = [0, 0]

while len(jacks) < 1000:
    for i in range(len(jacks)):
        jacks[i] += 1
    for i in range(len(jacks)):
        if 4 <= jacks[i] <=8:
            jacks.append(0)
    for i in range(len(jacks) -1, -1, -1):
        if jacks[i] == 10:
            jacks.pop(jacks[i])

    year += 1

print(f"It takes: {year} years to create {len(jacks)} jackalopes.")
print(jacks)

