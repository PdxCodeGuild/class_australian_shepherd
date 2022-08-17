with open('wizard-of-oz.txt', encoding="utf8" ) as f:
    lines = f.readlines()
    
book = ''
for item in lines:
    book += item
book_count = len(book)

sentences = []
for item in lines:
    sentences = len(lines)

words = 1
for i in book:
    if i == ' ':
        words += 1

ari = 4.7 * book_count / words + 0.5 * words / sentences - 21.43
ari = ari // 1
ari = int(ari)

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

ari_dicts = ari_scale[ari]
ages = ari_dicts['ages']
grade_level = ari_dicts['grade_level']

if ari in ari_scale:
    conclution = f"\nThe ARI for The Wonderful Wizard of Oz is {ari}. This corresponds to a {grade_level} level of difficulty and is suitable for an average person of {ages}. "

print(conclution)