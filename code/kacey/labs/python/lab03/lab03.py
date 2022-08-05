#   PALINDROME CHECKER    #


def check_palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False


word1 = input("Please enter a word: ")

print(f"{word1} is a palindrome: {check_palindrom(word1)}")

#       ANAGRAM CHECKER      #


def check_anagram(word1, word2):
    word1 = sorted(word1.lower().replace(" ", ""))

    word2 = sorted(word2.lower().replace(" ", ""))

    if word1 == word2:
        return True
    else:
        return False


given_word = input("Enter a first word: ")
given_word2 = input("Enter the second word: ")


print(
    f"{given_word.title()} and {given_word2.title()} is an anagram: {check_anagram(given_word, given_word2)}."
)
