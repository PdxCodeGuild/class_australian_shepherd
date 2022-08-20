# # Defining a function to calculate our list average
# def avg_list():
#     # Creating a starting total to add our list too
#     tot = 0
#     # Use a for loop to add each number in our list to our starting total
#     for number in nums:
#         number = int(number)
#         tot += number
#     # Printing our statement
#     print(f" The average for the list {nums} is {round(tot/len(nums), 2)}")
# # Creating our list
# nums = [5, 0, 8, 3, 4, 1, 6]
# # Calling our function
# avg_list()

# Defining a function to calculate our list average
def avg_list():
    # Creating a starting total to add our list too
    tot = 0
    # Use a for loop to add each number in our list to our starting total
    for number in nums:
        number = int(number)
        tot += number
    # Printing our statement
    print(f" The average for the list {', '.join(nums)} is {round(tot/len(nums), 2)}")
# Creating our empty list
nums = []
# Using a while loop to take user input until user types done
while True:
    # Creating our input
    inp = input('Please enter a number to add to the list, or type done when finished: ')
    # Using an if statement to break our loop when the user types done
    if inp == 'done':
        break
    nums.append(inp)
# Calling our function
avg_list()