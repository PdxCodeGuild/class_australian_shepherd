'''
BenjaminBirky
08/04/2022
lab_SockSorter
'''

from ast import Num
import random

color_style = ["black ankle", "black crew", "black calf", "black thigh",
                "white ankle", "white crew", "white calf", "white thigh",
                "blue ankle", "blue crew", "blue calf", "blue thigh"]

my_socks = {
    "black ankle": 0,
    "black crew": 0,
    "black calf": 0,
    "black thigh": 0,
    "white ankle": 0,
    "white crew": 0,
    "white calf": 0,
    "white thigh": 0,
    "blue ankle": 0,
    "blue crew": 0,
    "blue calf": 0,
    "blue thigh": 0
}

# Loop through 100 times and generate random types of socks

iteration = 0

while iteration < 100:
    
    random_int = random.randint(0, 11)
    random_sock = color_style[random_int]
   
    for key, value in my_socks.items():
        
        if key == random_sock:
            my_socks[key] += 1
        
        

    iteration += 1

# create pairs and loners from the 100 socks

index = 0

for key, value in my_socks.items():
    pairs = my_socks.get(key) 
    pairs = pairs // 2
    loners = my_socks.get(key)
    loners = loners % 2
    print(f"You have {pairs} pairs of {color_style[index]} socks and {loners} loners.")
    index += 1


print(my_socks)

'''
Used multiple sources for dicts, nested dicts and looping through nested dicts. Here are some sources that I used.


https://btechgeeks.com/python-how-to-iterate-over-nested-dictionary-dict-of-dicts/

https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values

https://www.geeksforgeeks.org/python-how-to-iterate-over-nested-dictionary/


'''