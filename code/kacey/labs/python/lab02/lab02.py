# Initial Commit

#       AVERAGE NUMBERS        #

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements

# for num in nums:
#     running_sum = num + num
#     print(num)
# print(running_sum)

# loop over the indices
# running_sum = 0
# for i in range(len(nums)):
#     running_sum += nums[i]
#     # print(nums[i])
# # print(running_sum)
# print(f'The average of {running_sum} is {running_sum/(len(nums))}')


#       VERSION 2        #

# nums = []
# while True:
#     for num in nums:
#         given_num = input("Please enter a number, or 'done' to display the average of all given values: ")
#         nums.append(given_num)
#         print(nums)

nums = []
while True:
    given_nums = input(
        "Please enter a number, or 'done' to display the average of all given values: "
    )

    if given_nums == "done":
        break
    else:
        try:
            nums.append(float(given_nums))
        except:
            print("ERROR: Must enter a number")

# print(nums)
print(f"The average of {nums} is {sum(nums)/len(nums)}")
