x = input("Enter a number: ")
x = int(x)

# if x % 2 == 0:
#     print("It is divisible by two.")

for i in range(x):
    if x % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
    break

#nothing follows