file_handle = open('gettys.txt', 'r')
word_count = 0
character_count = 0
sentence_count = 0
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
book_string = ''
for line in file_handle:
    book_string += line

word_count = len(book_string.split(' '))
character_count = len(book_string)
period_count = len(book_string.split('.'))
question_count = len(book_string.split('?'))
exclamation_count = len(book_string.split('!'))
sentence_count = period_count + question_count + exclamation_count
#print(book_string)
equation = (4.71*(character_count/word_count)) + (0.5*(word_count/sentence_count)) - 21.43
print(round(equation))
print(character_count)
print(sentence_count)
print(question_count)
print(exclamation_count)
print(word_count)