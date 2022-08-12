import string

with open('darwin.txt', 'r', encoding='utf-8') as file:
    text = file.read()
#print(text)

# 4.71 (characters / words) + 0.5 (words / sentances) - 21.43

# 4.71 * (894889 / 136535) + 0.5 (136535 / 3087) - 21.43

characters = 0

words = 0

for char in text:
  characters += 1
#print(characters) # characters = 894899

  if char == ' ':
    words += 1
#print(words) # words = 136535


sentance_list = text.rsplit('. ')
#print(sentance_list)

sentances = len(sentance_list)
#print(sentances) # sentances = 3087

ari = (4.71 * (characters / words)) + (0.5 * (words / sentances)) - 21.43
#print(ari) # ari = 31.555529353773466

print(characters / words)
print(4.71 * characters / words)

print(words / sentances)
print(0.5 * words / sentances)



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
