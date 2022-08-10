'''
benjamin_birky
08/03/2022
lab05_PalindromeAndAnagram
'''
#------------------------------------------Palindrome---------------------------------------

'''
user_word = input("Enter a word: ")
def check_palindrome(palindrome):
    reversed = palindrome [::-1]
    print(reversed)
    print(palindrome)
    if palindrome == reversed:
        return "Yes"
    else:
        return "No"
print(f"Is {user_word} a palindrome?: {check_palindrome(user_word)}")
'''

#--------------------------------------------Anagram----------------------------------------

#'''
user_word = input("Enter a word: ")
user_word2 = input("Enter second word: ")
def check_anagram(anagram1, anagram2):
    anagram1 = anagram1.replace(' ','').lower()
    anagram2 = anagram2.replace(' ','').lower()
    anagram1 = sorted(anagram1)
    anagram2 = sorted(anagram2)

    if anagram1 == anagram2:
        return True
    else:
        return False

print(f"These words are anagrams?: {check_anagram(user_word, user_word2)}")
#'''