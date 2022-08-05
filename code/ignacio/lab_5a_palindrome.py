# import string


# word_1 = input('Enter first word: ') 
# word_2 = input('Enter second word: ') 

# def check_anagram(check_1, check_2):
#     check_1 = sorted(word_1) 
#     check_2 = sorted(word_2)
#     if check_1 == check_2:
#         return True
#     else:
#         return False


# answer = check_anagram(word_1, word_2)

# if answer == True:
#     print(f'{word_1} and {word_2} are anagrams')
# else:
#     print(f'{word_1} and {word_2} are not anagrams')
# --------------------------------------------------

subject = input('enter a word: ')

def check_palindrome(pal_check):
    reverse_check = list(pal_check)
    reverse_check.reverse()
    reverse_check = ''.join(reverse_check)
    print(reverse_check)
    # return True

check_palindrome(subject)