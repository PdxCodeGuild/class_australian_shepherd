# Automated Readability Index

import math

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

with open('anthem.txt', encoding="utf8") as f:

    lines = f.read()   

characters = len(lines)
words = lines.split() 
sentences = lines.count(".")

ARI = (4.71 * (characters/len(words)) + 0.5 * (len(words)/sentences) - 21.43)

ARI = math.ceil(ARI)


print(f"The ARI for anthem.txt is {ARI}.\nThis corresponds to a {(ari_scale[ARI]['grade_level'])} level of difficulty\nthat is suitable for an average person {(ari_scale[ARI]['ages'])} years old.")

