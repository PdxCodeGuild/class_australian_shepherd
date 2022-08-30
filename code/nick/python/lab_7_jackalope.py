jacks = [0, 0]
years = 0
while len(jacks) < 1000:
    years += 1
    for jack in range(len(jacks)):
        jacks[jack] += 1 
    for jack in jacks:
        if jack > 3 and jack < 9:
            jacks.append(0)
    while 10 in jacks:
        jacks.remove(10)    
    

print(years, {len(jacks)})