'''
benjamin_birky
08/10/2022
lab_RotCipher
'''

'''
#Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
English	= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ROT13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


input_str = input("Enter a string: ").lower().replace(' ', '')

output_list = []
output_str = ''

for index1 in range(len(input_str)):
    for index2 in range(len(English)):
        if input_str[index1] == English[index2]:
            output_list.append(ROT13[index2])

for item in range(len(output_list)):
    output_str = output_str + output_list[item]

print(f"You input: {input_str}")
print(f"Your output: {output_str}")

'''


English	= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']

# Rotation list before 'n' rotations
ROTN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("\nThis ROT Cipher will encrypt all text minus numbers and special characters.")

input_str = input("\nEnter some text: ")
input_int = input("Enter the number of rotations: ")
input_int = int(input_int)

output_list = []
output_str = ''

n = 0

# Rotating the English list onto the ROTN list by 'n' rotations 
while n < input_int:
    pop = ROTN.pop(0)
    ROTN.append(pop)
    n += 1    

# Looping through the input string until it matches the English index; 
# Then find the corresponding index on ROTN, then copying onto a new list
for index1 in range(len(input_str)):

# This for loop adds in the special characters without a cipher
    for index2 in range(len(special_char)):
        if input_str[index1] == special_char[index2]:
            output_list.append(input_str[index1])
            break
# This for loop ciphers lower case and capital letters only
    for index3 in range(len(English)):
        if input_str[index1] == English[index3]:
            output_list.append(ROTN[index3])
            break
            
        

# converting the items in the list onto a string for output
for item in range(len(output_list)):
    output_str = output_str + output_list[item]

print(f"Plain text: {input_str}")
print(f"Encrypted text: {output_str}")
