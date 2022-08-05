#       MADLIB LAB!      #


# print("Let's make a MADLIB! Walmart Lib :D")

# verb = input("Please enter a verb: ")
# adjective = input("Please enter a adjective: ")
# noun = input("Please enter a pluralized noun: ")
# adjective2 = input("Please enter another adjective: ")
# verbing = input('Please enter a verb ending with "ing": ')
# verb2 = input("Please enter a verb: ")
# number = input("Please enter a number: ")
# adjective3 = input("Please enter another adjective: ")
# noun2 = input("Please enter another pluralized noun: ")
# noun3 = input("Please enter another pluralized noun: ")
# noun4 = input("Please enter another pluralized noun: ")
# last_name = input("Please enter your pluralized family name: ")
# adjective4 = input("Please enter another adjective: ")
# adjective5 = input("Please enter another adjective: ")
# noun5 = input("Please enter one last noun: ")

# madlib = f"Come {verb} at WALMART, where you`ll receive {adjective} discounts on all of your favorite brand name {noun}. Our {adjective2} and {verbing} associates are there to {verb2} you {number} hours a day. Here you will find {adjective3} prices on the {noun2} you need. {noun3} for the moms, {noun4} for the kids and all the latest electronics for the {last_name}. So come on down to your {adjective4} {adjective5} WALMART where the {noun5} come first."

# print(madlib)

# #    VERSION TWO        #

# import random

# print("Let's make a madlib! Be Kind Lib :D")


# nouns = input("Please enter at least 3 or more nouns separted by commas: ").strip(" ")

# nouns = nouns.split(", ")

# # print(nouns)
# random_noun = random.choice(nouns)
# random_noun2 = random.choice(nouns)
# random_noun3 = random.choice(nouns)
# random_noun4 = random.choice(nouns)
# # print(random_noun)

# adjectives = input("Please enter at least 3 or more adjectives separted by commas: ")

# adjectives = adjectives.split(", ")

# random_adjective = random.choice(adjectives)
# random_adjective2 = random.choice(adjectives)

# # print(random_adjective)

# places = input("Please entere at least 3 or more places separated by commas: ").strip(
#     " "
# )

# places = places.split(", ")

# random_place = random.choice(places)

# # print(random_place)


# madlib = f"""\nBe kind to your {random_noun}-footed {random_noun2}
# For a duck may be somebody`s {random_noun3},
# Be kind to your {random_adjective} in {random_place}
# Where the weather is always {random_adjective2}.

# You may think that this is the {random_noun4},
# Well it is."""

# print(madlib)

# #  VERSION 3      #

# import random

# while True:
#     print("Let's make a madlib! Be Kind Lib :D")

#     nouns = input("Please enter at least 3 or more nouns separted by commas: ").strip(
#         " "
#     )

#     nouns = nouns.split(", ")

#     # print(nouns)
#     random_noun = random.choice(nouns)
#     random_noun2 = random.choice(nouns)
#     random_noun3 = random.choice(nouns)
#     random_noun4 = random.choice(nouns)
#     # print(random_noun)

#     adjectives = input(
#         "Please enter at least 3 or more adjectives separted by commas: "
#     )

#     adjectives = adjectives.split(", ")

#     random_adjective = random.choice(adjectives)
#     random_adjective2 = random.choice(adjectives)

#     # print(random_adjective)

#     places = input(
#         "Please entere at least 3 or more places separated by commas: "
#     ).strip(" ")

#     places = places.split(", ")

#     random_place = random.choice(places)

#     # print(random_place)

#     madlib = f"""\nBe kind to your {random_noun}-footed {random_noun2}
#     For a duck may be somebody`s {random_noun3},
#     Be kind to your {random_adjective} in {random_place}
#     Where the weather is always {random_adjective2}.

#     You may think that this is the {random_noun4},
#     Well it is."""

#     print(madlib)

#     again = input("Do you want to play again? yes or no: ")
#     if again == "no":
#         print("Thanks for playing")
#         break
