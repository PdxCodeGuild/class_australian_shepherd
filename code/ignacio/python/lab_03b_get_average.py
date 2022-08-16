#nums = [5, 0, 8, 3, 4, 1, 6]
#sum = 0

#for num in nums:
#    sum += num

#average = len(nums)
#outcome = sum / average
#
#print(outcome)



nums =[]
total = 0
while True:
    num = input("Enter number, or 'done': ")
    if num == 'done':
        
        average = total / len(nums)
        print(f'Your average is:{average} ')
        break
    nums.append(int(num))
    # total = int(total) + int(num)
    total = sum(nums)
    print(nums)