#ROT13 is Rotation by 13

import string

alpha_char= []

for i in string.ascii_uppercase: 
    alpha_char.append(i)
    

user_message= input("Enter your message: ")
rotation= int(input("How many rotations: "))



rot=''

for i in user_message.upper():
    rot += alpha_char[(alpha_char.index(i) + rotation) % 26]
    
print(rot.lower())
    
#uryyb- 13 Rotation
#ufzq 

            

    



