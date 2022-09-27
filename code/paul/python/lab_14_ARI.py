#This lab cannot be ran with the play button. Nav to file and run it in the terminal.
#The ARI dictionary is given in lab in the github repo (Lab 14, ARI)
#Formula: ARI = 4.71 * (characters/words)+ 0.5 * words/sentence) -21.43
#Calculate individual charcters, words, and sentences (see unix time notes and nested data structure notes).
#Can I do this in a function (ARI calculation)


#Call your file
with open('book.txt') as f:
    book = f.read()

characters = len(book)
# print(book)
sentences= 0
word_count= 0

#Sentence Count.
for char in book:
    if char == '.':
        sentences += 1

    
#Word Count. Used the same logic above on lines 17-19. Appended the spaces so the score is not misleading.
for words in book:
    if words != ' ':
        word_count += 1
print(word_count)


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

#Calculate the score. See lab 14 on github or line two comment above.
ARI = 4.71 * (characters/word_count)+ 0.5 * (word_count/sentences) -21.43
ARI= int(ARI)
if ARI > 14:
    ARI = 14
print(ari_scale[ARI])

print(f"This book's ARI is {ARI} ages: {ari_scale[ARI]['ages']}, grade_level: {ari_scale[ARI]['grade_level']}")



print(ARI)



