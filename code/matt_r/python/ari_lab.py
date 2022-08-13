



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




with open('holmes.txt', encoding="utf8" ) as f:
    lines = f.readlines()
# print(type(lines))



sentences = 0

for line in lines:
    for char in line:
        if char == '.':
            sentences += 1
        if char == '?':
            sentences += 1
        if char == '!':
            sentences += 1

# print(sentences)




words = 0

for line in lines:
    for char in line:
        if char == ' ':
            words += 1

# print(words)




charactures = 0


for line in lines:
    for index in range(len(line)):  
        if([index] != ' '):  
            charactures += 1;  

# print(charactures)



ari_score1 = charactures / words * 4.71
ari_score2 = words / sentences / 2
ari_score = ari_score1 + ari_score2 - 21.43
ari_score = int(ari_score)

# print(ari_score1, ari_score2, ari_score)

# print(ari_scale[ari_score]['ages'])



print(f"""The ARI for 'Sherlock Holmes' is {ari_score}
This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari_score]['ages']} years old.""")