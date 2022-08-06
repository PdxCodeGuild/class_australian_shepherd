'''
BenjaminBirky
08/02/2022
lab03a_AverageNum
'''

#--------------------VERSION 1-----------------------------------
'''
# initialize the nums list and running_sum variables
nums = [5, 0, 8, 3, 4, 1, 6]
running_sum = 0

#loop through all the numbers in the nums list
for num in nums:
    running_sum = running_sum + num
    print(num)

# divide running_sum by the quantity of elements in nums
running_sum = running_sum / len(nums)
print(running_sum)
'''
#---------------------VERSION 2-----------------------------------

print("Lets average out all the numbers that you input.")

# initializing variables
nums =[]
inputting_nums = True

while inputting_nums == True:
    number = input("Enter a number, or 'done' : ")
    
    if number == 'done':
        break
    else: 
        number = float(number)
        nums.append(number)
        

running_sum = 0

for item in nums:
    running_sum = item + running_sum

running_sum = running_sum / len(nums)
print(running_sum)

#done









