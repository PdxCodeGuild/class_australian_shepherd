

word= input("Enter A Word:")

def check_palindrome(word):
    reversed_word= word[::-1]
    
    if word == reversed_word:
        return True
    else:
        return False



results= check_palindrome(word)

if results == True:
    print ("This is a palindrome")
else:
    print("not a palindrome")

    #nothing follows