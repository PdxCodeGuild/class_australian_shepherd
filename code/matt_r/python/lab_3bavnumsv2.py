total = 0

nums = []


while True:

    digit = input('Please enter a number, or enter "done":  ')
    



    if digit == 'done':
        break 
    
    digit = int(digit)
    nums.append(digit)

# loop over the indices
for item in range(len(nums)):
        # print(nums[item])

    total = total + nums[item]
    answer = total / len(nums)
    
# print(total)
print(f'Your average is {answer}!  ')
# print(nums)