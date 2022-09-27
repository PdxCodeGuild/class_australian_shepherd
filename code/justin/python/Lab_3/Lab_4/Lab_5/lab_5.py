""" #Creating a function that checks a user input to see if it is a palindrome
def check_palindrome():
    # Using slicing we reverse our word
    rev_word = word[::-1]
    # Using if/else statment to print our results
    if rev_word == word:
        print(f'{word.title()} is a palindrome.')
    else:
        print(f'{word.title()} is not a palindrome.')
# Creating an input for users to check a word
word = input('Please enter a word you would like to check: ')
# Calling our function
check_palindrome()
 """

#Creating a function to check 
def check_anagram():
    # Using the lower and replace method to replace any capital letters and spaces in our input
    word_1 = inp_1.lower().replace(' ', '')
    # Using the sorted method to sort our string into a list, then using the join method to turn it back into a string. If we do not convert our string, it will throw an AttributeError.
    word_1 = sorted(''.join(word_1))
    word_2 = inp_2.lower().replace(' ', '')
    word_2 = sorted(''.join(word_2))
    # Using if/else statements to compare our sorted strings to see if they are anagrams.
    if word_1 == word_2:
        print(f'{inp_1} and {inp_2} are anagrams.')
    else:
        print(f'{inp_1} and {inp_2} are not anagrams.')
# Creating our user input to take two words
inp_1 = input('Please enter your first word: ')
inp_2 = input('Please enter your second word: ')
# Calling our function
check_anagram()