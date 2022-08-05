# Lab 3: Average Numbers 
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list.
# Remember len will give you the length of a list.

# nums = [5, 0, 8, 3, 4, 1, 6]
# running_sum = 0

# for num in nums:
#     running_sum += num

# avg = round((running_sum / len(nums)),2)

# print(running_sum)
# print(avg)

# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. 

nums_list = []
running_sum = 0

while True: 

    user_nums = input("\nEnter a number or 'done' to calculate: ")

    if user_nums == 'done':
        print(f'\nThank you for entering these numbers: {nums_list}')
        break

    nums_list.append(int(user_nums))

for num in nums_list:
    running_sum += num

avg = round((running_sum / len(nums_list)),2)

print(f'Sum of your numbers are: {running_sum}.')
print(f'Average is {avg}.')


    