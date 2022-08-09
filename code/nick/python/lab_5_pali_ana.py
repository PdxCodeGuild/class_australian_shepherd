# Lab 5: Palindrome and Anagram

# PALIDROME 
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.
# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

def palidrome(word):
    word_letters = list(word)
    reverse_list = word_letters.copy()
    reverse_list.reverse()
    if word_letters == reverse_list:
        return True
    else:
        return False

user_word = input('Enter a word: ')
if palidrome(user_word) == True:
    print(f'Your word, {user_word}, is a palidrome!')
else:
    print(f'Your word, {user_word}, is NOT a palidrome...')

# ANAGRAM
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. 
# The procedure for comparing the two strings is as follow:

# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal

def anagram(word_one, word_two):
    first_word_list = list(word_one.lower())
    second_word_list = list(word_two.lower())

    first_word_list.sort()
    second_word_list.sort()
    while ' ' in first_word_list:
        first_word_list.remove(' ')
    while ' ' in second_word_list:
        second_word_list.remove(' ')

    if first_word_list == second_word_list:
        return True
    else:
        return False


first_word = input('First word: ')
second_word = input('Second word: ')
if anagram(first_word, second_word) == True:
    print(f'{first_word} and {second_word} are anagrams!')
else:
    print(f'{first_word} and {second_word} are NOT anagrams!')