# PALINDROMES
'''
import string

word_input = input("Enter a word to check if its a palindrome: ")

word_list = list(word_input.lower())

list_reversed = []

for i in range(len(word_list)):
  list_reversed.append(word_list.pop())

backward = ('').join(list_reversed)

if word_input == backward:
  print(f'{word_input} is a palindrome.')

else:
  print(f'{word_input} is NOT a palindrome.')
'''

# ANAGRAM CHECKER

def check_anagram(word_1, word_2):
  word_1_list = list(word_1)
  word_2_list = list(word_2)
  word_1_list.sort()
  word_2_list.sort()

  print(word_1_list, word_2_list)

  if word_1_list == word_2_list:
    return True

first_word = input("Enter the first word: ").lower()

second_word = input("Enter the second word: ").lower()

if check_anagram(first_word, second_word) == True:
  print(f"'{first_word}' and '{second_word}' are anagrams.")

else:
  print(f"'{first_word}' and '{second_word}' are NOT anagrams.")
