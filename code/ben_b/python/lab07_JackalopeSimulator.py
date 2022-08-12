'''
benjamin_birky
08/05/2022
lab07_JackalopeSimulator
'''


year = 1

jacks = [0, 0]

while len(jacks) < 1000:
    for i in range(len(jacks)):
        jacks[i] += 1
    for i in range(len(jacks)):
        if 4 <= jacks[i] <=8:
            jacks.append(0)
    for i in range(len(jacks)-1, -1, -1):
        if jacks[i] == 10:
            jacks.pop(i)

    year += 1

print(f"It takes: {year} years to create {len(jacks)} jackalopes.")
#print(jacks)









