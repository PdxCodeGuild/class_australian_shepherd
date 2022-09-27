import data_list
import time
import datetime

# Unix Time ---------------------------------------------------------------------------------------------------------------------------------
# In computing, Unix time (also known as Epoch time, Posix time,[1] seconds since the Epoch,[2]
# Unix timestamp or UNIX Epoch time[3]) is a system for describing a point in time. It is the number
# of seconds that have elapsed since the Unix epoch, excluding leap seconds. The Unix epoch is 00:00:00 UTC on 1 January 1970.

# In otherwords, it's time counting forward from January 1st, 1970

# print the current date from Unix time
unix_time = round(time.time())
"""
print(f"\nThe current time in Unix Time is : {int(round(time.time() * 1000))}")
print("Current Date: ",
    datetime.datetime.fromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
"""
# Use Unix Time to get the time in milliseconds -------------------------------------------------------------------------------------------------

# Get the current Unix time, including milliseconds
# 1000 millisecond is equal to 1 second

milliseconds = int(round(time.time() * 1000))
# print(f"\nThe Unix Time in milliseconds is: {milliseconds}")
# https://www.unixtimestamp.com/


# Use Unix Time to show operation time ----------------------------------------------------------------------------------------------------------

# Populate a list showing the amount of time it took
"""
milliseconds_old = int(round(time.time() * 1000))
print(f"\nBefore running the operation {milliseconds_old} ")


dummy_data = []
for x in range(1000000):
    dummy_data.append(str(5* 21.8))


milliseconds_new = int(round(time.time() * 1000))
print(f"\nAfter running the operation {milliseconds_new} ")

duration = milliseconds_new - milliseconds_old
print(f"\nIt took {duration} milliseconds to run the operation\n")

"""
# Use the dataset that was imported --------------------------------------
"""
list_data = data_list.data

dummy_string = ''

milliseconds_old = int(round(time.time() * 1000))
print(f"Before running the operation {milliseconds_old} ")

for i in list_data:
    dummy_string += str(i)

milliseconds_new = int(round(time.time() * 1000))
print(f"After running the operation {milliseconds_new} ")


duration = milliseconds_new - milliseconds_old
print(f"\nOperation time: {duration} in milliseconds")
"""

# Big O Notation -------------------------------------------------------------------------------------------------------------------------

# Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a 
# particular value or infinity. Big O is a member of a family of notations invented by Paul Bachmann,[1] Edmund Landau,[2] and others, 
# collectively called Bachmann–Landau notation or asymptotic notation. The letter O was chosen by Bachmann to stand for Ordnung, meaning 
# the order of approximation.

# In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the 
# input size grows.[3] In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical 
# function and a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem. 
# Big O notation is also used in many other fields to provide similar estimates.


# Big O notation characterizes functions according to their growth rates: different functions with the same growth rate may be represented 
# using the same O notation. The letter O is used because the growth rate of a function is also referred to as the order of the function. 
# A description of a function in terms of big O notation usually only provides an upper bound on the growth rate of the function.

# Associated with big O notation are several related notations, using the symbols o, Ω, ω, and Θ, to describe other kinds of bounds on asymptotic growth rates.

list_data = data_list.data

single_char = []

operation_counter = 0

# string_item would be '123456789'
# character would be '1' and then '2' and then '3'... for each item in the list

milliseconds_old = int(round(time.time() * 1000))
print(f"\nBefore running the operation {milliseconds_old} ")


for string_item in list_data:
    operation_counter += 2
    for character in string_item:
        single_char.append(character)
        operation_counter += 3


milliseconds_new = int(round(time.time() * 1000))
print(f"After running the operation {milliseconds_new} ")

duration = milliseconds_new - milliseconds_old
print(f"\nOperation time: {duration} in milliseconds")


# There are 17028 items in the list
# There are 153,252 individual characters in this dataset 
print(operation_counter) # 493,812