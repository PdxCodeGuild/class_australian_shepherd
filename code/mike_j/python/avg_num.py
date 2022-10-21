# # Version 1:

nums = [5, 0, 8, 3, 4, 1, 6]

x = 0

for num in nums:
    x += num
    print(x)

avg = x/len(nums)

print(avg)

# Version 2:

# nums = []

# x = 0

# while x != "done":
#     x = input("Enter number or 'done': ")
#     if x == "done":
#         break
#     nums.append(int(x))   

# print(sum(nums)/len(nums))