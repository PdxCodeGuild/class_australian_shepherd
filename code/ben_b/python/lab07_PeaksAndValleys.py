'''
benjamin_birky
08/04/2022
lab07_PeaksAndValleys
'''





data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#index  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20

def peaks(data):
    for index in data:
        if data > data[index + 1] and data > data[index - 1]:
            return
        else:
            continue
    