j = 0
j_c = 2
y = 0
while j_c < 1000:
    if j < 10:
        j += 1
        if j >= 4 and j <= 8:
            j_c += 2
        if j == 10:
            j_c -= 1
        print(j_c)
    y += 1
    print(y)