# Importing string to pull a list of the alphabet
#import string
# Creating a variable using our ascii method
#alphabet = list(string.ascii_lowercase)
#alpha_dict = {}
#rev_alpha_dict ={}
# Creating a for loop to loop through index and element
#for index, element in enumerate(alphabet):
    #alpha_dict[index] = element
    #if index >= 0 and index < 13:
        #index += 13
    #elif index >= 13:
        #index -= 13
    #rev_alpha_dict[index] = element
#Taking an input of a user entered word to create a cipher for
#word = input('Please enter a word: ')
#Creating a for loop to check our user input to our dictionary to determine the index, the loop then searches for the same index in the second dictonary to return our cipher
#new_word = []
#for letter in word:
    #indx = [indx for indx, ky in alpha_dict.items() if letter in ky]
    #for key in indx:
        #if key in rev_alpha_dict.keys():
            #new_word.append(rev_alpha_dict.get(key))
#print(*new_word)

# Importing string to pull a list of the alphabet
import string
# Creating a variable using our ascii method
alphabet = list(string.ascii_lowercase)
alpha_dict = {}
rev_alpha_dict ={}
# Take a user input to determine the offset of our cihper
chipher_num = int(input('Please enter the offset of your cipher: '))
# Creating a for loop to loop through index and element
for index, element in enumerate(alphabet):
    alpha_dict[index] = element
    # Run our index against our user input to determine the offset of our cipher
    if index >= 0 and index < chipher_num:
        index += chipher_num
    elif index >= chipher_num:
        index -= chipher_num
    rev_alpha_dict[index] = element
#Taking an input of a user entered word to create a cipher for
word = input('Please enter a word: ')
#Creating a for loop to check our user input to our dictionary to determine the index, the loop then searches for the same index in the second dictonary to return our cipher
new_word = []
for letter in word:
    indx = [indx for indx, ky in alpha_dict.items() if letter in ky]
    for key in indx:
        if key in rev_alpha_dict.keys():
            new_word.append(rev_alpha_dict.get(key))
print(*new_word)