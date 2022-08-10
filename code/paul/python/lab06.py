#Convert the input string into a list of ints
from re import I


cc_num= input("Enter your card number: ")
cc_num=list(cc_num)


for index in range(len(cc_num)):
    cc_num[index]= int(cc_num[index])
print("CC Nuber: " , cc_num)
#print to check the input is coverted into a list
# print(cc_num)

#Slice off the last digit. That is the check digit.

check_digit= cc_num.pop()


#verify check_digit is sliced. use statements as labels. 
# print("Sliced Number: ", cc_num) 
# print("Check Digit: ", check_digit)

#Reverse the digits.
cc_num.reverse()
# print("Reversed Number: " ,cc_num)


#double every other element
for index in range(len(cc_num)):
    if index % 2 == 0:
        cc_num[index] = cc_num[index] * 2
# print(cc_num)



#Subtract nine from numbers over nine. 
def subnnine(cc_num):
    for index in range(len(cc_num)):
        if cc_num[index] > 9:
            cc_num[index] -= 9
    return cc_num
subnnine(cc_num)
# print(cc_num)

#Sum all values.

total = sum(cc_num)

print(total)

#Take the second digit of that sum.
print(total % 10)
print("This is the check digit: ", check_digit)
print(cc_num)

#If that matches the check digit, the whole card number is valid
if total % 10 == check_digit:
    print("Valid Card Number!")
else:
    print("Invalid Card Number!")




#nothing follows




    