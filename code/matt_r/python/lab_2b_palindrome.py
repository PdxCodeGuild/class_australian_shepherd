# palindrome


# # word = 'racecar'
# # word = "newb"


def check_palindrome(word):
    word_list = list(word)
    word_list_2 = list(word)
    word_list_2.reverse()
    word_list == word_list_2

    if word_list == word_list_2:
       return print(f'{word} is a palindrome!')

    else:
        return print(f'{word} is not a palindrome!')


word = input('Enter a word to see if its a palindrome:  ') 


check_palindrome(word)
print(f'Thanks for playing,')


first = input('Enter the first word:  ')
second = input('Enter the second word:  ')
#   anagram
def anagram(first, second):
    first = first.lower()
    second = second.lower()
    first = first.replace(" ","")
    second = second.replace(" ","")
    first_2 = list(first)
    second_2 = list(second)
    first_2.sort()
    second_2.sort()


    if first_2 == second_2:
        return f'{first} and {second} are anagrams'
    else:
        return f'{first} and {second} are not anagrams'


        


print(anagram(first, second))