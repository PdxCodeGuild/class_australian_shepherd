# Declaring our empty variables to add our counts too
word_count = 0
character_count = 0
sentence_count = 0

# Copying the provided dictionary of information to pull from
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

# Opening our file to iterate through and pull our information from
with open('gettys.txt', 'r') as file:
    file_count = file.read()
    # Using the count method on . to count the number of sentences inside the file
    sentence_count += file_count.count('.')
    # Using a for loop with split and replace to ensure that we are only counting our words and not our punctuation
    for word in file_count.split(' '):
        word.replace(',', '')
        word_count += 1
    # Counting our total characters using the len of our file as well as stripping the whie space
    character_count = len(file_count.strip())

# Using our equation needed to gain the ARI of our selected book
equation = (4.71*(character_count/word_count) + 0.5*(word_count/sentence_count)) - 21.43

# Using if/else statements to pull our information from our dictionary to print using get method
if equation >= 14:
    print(f'The ARI for {file.name} is {round(equation)}.')
    print(f"This corresponds to a {ari_scale.get(14).get('grade_level')} level of difficulty.")
    print(f"This is suitable for an average person of {ari_scale.get(14).get('ages')} years old.")
else:
    print(f'The ARI for {file.name} is {round(equation)}.')
    print(f"This corresponds to a {ari_scale.get(equation).get('grade_level')} level of difficulty.")
    print(f"This is suitable for an average person of {ari_scale.get(equation).get('ages')} years old.")