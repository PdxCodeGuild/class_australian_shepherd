








word1= input("Enter A Word:")
word2= input("Enter another word:")


def check_palindrome(word): #[::-1] <---- This is for string slicing. These are lists below. Do not use.
    word = list(word)
    rev_word = list(reversed(word)) #<--- this reverse method creates a new list instead of changing the original list
    print(word)
    print(rev_word)
    if word == rev_word:
        print("This is a palindrome")
    else:
        print("Nah. Not a Palindrome")
# check_palindrome(word1)
    

def check_anagram():  #<---- Anagram lab from 102 reference. 
    list_1= list(word1)
    list_2= list(word2)
    list_1.sort()
    list_2.sort()
    if list_1==list_2:
        print("These are anagrams")
    
    else:
        print("These are not anagrams")
check_anagram()
