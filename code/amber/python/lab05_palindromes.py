# PALINDROMES

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


# ANAGRAM CHECKER

def check_anagram(word_1, word_2):
  word_1 = list(word_1).sort()
  word_2 = list(word_2).sort()

  if word_1 == word_2:
    return word_1, word_2
