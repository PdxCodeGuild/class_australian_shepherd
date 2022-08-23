

word= input("Enter A Word:")
word2= input("Enter another word:")


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
check_palindrome(word)

def check_anagram(words):
    word_ = word[::1]
    
    if word == word_:
        return True
    else:
        return False
results = check_anagram(word)

if results == True:
    print ("This is an anagram")
else:
    print("not a anagram")
check_anagram(word)
