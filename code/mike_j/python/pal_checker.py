# # Palindrome:

# def check_palindrome(x):
#     if x == x[::-1]:
#         return True
#     else:
#         return False    

# x = input("Please enter a word: ")

# check_palindrome(x)

# if check_palindrome(x):
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

# Anagram:

def check_anagram(x,y):
    x = x.replace(" ","").lower()
    y = y.replace(" ","").lower()
    if sorted(x) == sorted(y):
        return True
    else:
        return False

x = input("Please enter first word: ")
y = input("Please enter second word: ")            

check_anagram(x,y)

if check_anagram(x,y):
    print("This is an anagram")
else:
    print("This is not an anagram")



