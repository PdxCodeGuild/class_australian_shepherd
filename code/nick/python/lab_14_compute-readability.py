# Lab 9: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
# The general formula to compute the ARI is as follows:
# 4.71(characters/words) + 0.5(words/sentences) - 21.43

# The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 0.5, 
# and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

# Scores correspond to the following ages and grad levels:
#  Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

import string
alphabet = list(string.ascii_letters)

with open('pride_n_prejudice.txt', encoding='utf8') as file:
    book = file.readlines()
book_list = list(book)
# character count
characters_count = 0
for letter in book_list:
    letters_list = list(letter)
    for character in letters_list:
        if character in alphabet:
            characters_count += 1
print(f'There are this many characters: {characters_count}.')

# word count
word_count = 0
for words in book_list:
    word_list = words.split()
    word_count += (len(word_list))
print(f'There are this many words: {word_count}.')

# sentence count
sentence_count = 0 
end_sentence = ['?', '.', '!'] #sentences will end with one of these, so any element of a list containing this will be counted as a sentence.
for sent in book_list:
    sentence_lists = list(sent)
    for punc in sentence_lists:
        if punc in end_sentence:
            sentence_count += 1
print(f'There are this many sentences: {sentence_count}.')

ari_formula = round((4.71 * (characters_count/word_count)) + (0.5 * (word_count/sentence_count)) - 21.43)

print(f'''
--------------------------------------------------------
The ARI for pride_n_prejudice.txt is {ari_formula}
This corresponds to a {ari_scale[ari_formula]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari_formula]['ages']} years old.
--------------------------------------------------------
''')