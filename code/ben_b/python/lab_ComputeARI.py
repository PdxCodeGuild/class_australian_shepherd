'''
benjamin_birky
lab_ComputeARI
08/12/2022
'''

special_characters = '~`!@#$%^&*()_+-=}{][|\\;:\'"></?,'
character_count = 0.0
word_count = 0.0
sentence_count = 0.0

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

# Opening the alice.txt 
with open('alice.txt', encoding="utf8" ) as f:
    alice = f.read()

# Removing the special characters in the text
for special in special_characters:
    alice = alice.replace(special, "").lower()

# Counting the words and sentences by spaces and periods before removing spaces
sentence_count = alice.count(".")
word_count = alice.count(" ")

# Removing all spaces for a character count
for space in alice:
    alice = alice.replace(" ", "")
character_count = len(alice)
    
# Compute ARI
ARI = (4.71 * (character_count / word_count)) + (0.5 * (word_count / sentence_count)) - 21.43
ARI = int(ARI)
grade = ari_scale[ARI]['grade_level']
ages = ari_scale[ARI]['ages']

print(f'''The ARI for Alice in Wonderland is {ARI}
This corresponds to a {grade} grade level of difficulty 
that is suitable for an average person {ages} years old.''')