#AVERAGE NUMBERS

nums = [5, 0, 8, 3, 4, 1, 6]

for num in nums:
  num += num

sum = num

length = len(nums)

average = sum / length

for i in range(length):
  print(nums[i])

print(sum)

print(average)
