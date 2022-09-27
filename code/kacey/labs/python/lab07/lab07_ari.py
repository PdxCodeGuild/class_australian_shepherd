# import requests
# response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
# response.encoding = 'utf-8' # set encoding to utf-8
# print(response.text)


with open("alice.txt", "r", encoding="utf-8") as file:
    text = file.read()
# print(text)

characters = len(text)
# print(characters, ' this is the amount of all characters')

words = len(text.split())  # 26440
# print('Number of words in the book:', words)

sentences_period = text.count(".")
# print(sentences_period)
sentences_question = text.count("?")
# print(sentences_question)
sentences_exlamation = text.count("!")
# print(sentences_exlamation)

total_all_sentences = sentences_period + sentences_question + sentences_exlamation
# print(type(words))

ari_math = (4.71 * (characters / words)) + (0.5 * (words / total_all_sentences)) - 21.43

# print(ari_math)
# ari_math = 15
# print(ari_math % 1)
# ari_math = int(ari_math)
if ari_math % 1 < 1:
    ari_math = (ari_math // 1) + 1
if ari_math > 14:
    ari_math = 14
# print(ari_math)
ari_math = int(ari_math)
ari_scale = {
    1: {"ages": "5-6", "grade_level": "Kindergarten"},
    2: {"ages": "6-7", "grade_level": "1st Grade"},
    3: {"ages": "7-8", "grade_level": "2nd Grade"},
    4: {"ages": "8-9", "grade_level": "3rd Grade"},
    5: {"ages": "9-10", "grade_level": "4th Grade"},
    6: {"ages": "10-11", "grade_level": "5th Grade"},
    7: {"ages": "11-12", "grade_level": "6th Grade"},
    8: {"ages": "12-13", "grade_level": "7th Grade"},
    9: {"ages": "13-14", "grade_level": "8th Grade"},
    10: {"ages": "14-15", "grade_level": "9th Grade"},
    11: {"ages": "15-16", "grade_level": "10th Grade"},
    12: {"ages": "16-17", "grade_level": "11th Grade"},
    13: {"ages": "17-18", "grade_level": "12th Grade"},
    14: {"ages": "18-22", "grade_level": "College"},
}

print(f"The ARI for Alice in Wonderland is {ari_math}")
print(
    f"This corresponds to the {(ari_scale[ari_math])['grade_level']} level of difficulty\nthat is suitable for an average person {(ari_scale[ari_math])['ages']} years old"
)
