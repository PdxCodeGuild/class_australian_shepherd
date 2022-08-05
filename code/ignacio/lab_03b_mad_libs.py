#nums = [5, 0, 8, 3, 4, 1, 6]
#sum = 0

#for num in nums:
#    sum += num

#average = len(nums)
#outcome = sum / average
#
#print(outcome)



nums =[]
while True:
    num = input("Enter number, or 'done': ")

    if num == "done":
        print(f"Average:  ")
        break


    nums.append(num)
    print(nums)