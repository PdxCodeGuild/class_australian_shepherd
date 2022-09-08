#ROT13 is Rotation by 13

import string

alpha_char= []

for i in string.ascii_uppercase: 
    alpha_char.append(i)
    

user_message= input("Enter your message: ")
rotation= int(input("How many rotations: "))



rot=''

for i in user_message.upper():
    rot += alpha_char[(alpha_char.index(i) + rotation) % 26] #<------ %26 is used in case the user enters a 'Z' or 'z' in their message (user_message).
    
print(rot.lower())
    
#uryyb- 13 Rotations
#ufzq 5 Rotations

            

    



