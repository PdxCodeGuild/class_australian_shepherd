from collections import Counter

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

def check_anagram(word, word2):
    if(Counter(word) == Counter(word2)):
        print("These are anagrams")
    else:
        print("Nah Fam, these aint it")
check_anagram(word, word2)

    #nothing follows