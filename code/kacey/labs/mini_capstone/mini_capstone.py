"""
    
    -------------------Mini Capstone idea-------------------------
    
    
    Create a Trivia Game
    
    Add ability to change the Number of Questions
    
    Add ability to change the Category of Questions
    
    Add ability to change the Difficulty of Questions
    
    Add ability to change between Multiple Choice or True/False Questions
    
    After the settings are decided by the user, start the game.
    
    Give the user either a Grade, or maybe just a list of their questions with their answer and the correct answers, 
        or some points value to their completed game to compare to their friends game
    
    Ask user if they would like to play Trivia Game again!
    
    

"""

"""
Questions needed answered before I begin writing code:

1 - Can the API be given variables for each of the different aspects to the game?
    ie: inputs of Number, Category, Difficulty, Game Type before the game is created
2 - 
"""

import requests
from html import unescape
from random import shuffle, choice
from colorama import Fore, Back, Style

from tkinter import *
from tkinter import ttk


#      SESSION TOKEN URL      #
# session_token = "https://opentdb.com/api.php?amount=10&token=YOURTOKENHERE"
# session_token = session_token.json ????????? what do i put here....maybe nothing since i don't have the actual session token yet. . . . . .
# print(session_token, ' this is the session token "USING"')
#                                                                                                   SESSION TOKENS FRIGGEN NOT NEEDED!!!! HOW DUMMMMMMMMMMMMMMMMB
# #      RETRIEVE a SESSION TOKEN    #
# retrieve_token = "https://opentdb.com/api_token.php?command=request"
# retrieve_token = requests.get("https://opentdb.com/api_token.php?command=request")
# print(retrieve_token, ' this is the token itself being retrieved')
#     WELCOME PROMPT      #
# print("Welcome to Trivia Game!!!\nPlease enter the following choices to start your game!")
# category_id_here = input(
#     "Enter a category id here to search how many questions are available for that specific category: "
# )

#     GAME TYPE QUESTIONS PROMTS     #
def game_play_selection():
    global length_of_questions
    global questions
    global questions_count
    category_choice = (
        input(
            f'Please enter the category number for type of questions would like to play from!\n"9" = General Knowledge\n"10" = Entertainment: Books\n"11" = Entertainment: Film \n"12" = Entertainment: Music\n"13" = Entertainment: Musicals and Theatres\n"14" = Entertainment: Television\n"15" = Entertainment: Video Games\n"16" = Entertainment: Board Games\n"17" = Science and Nature\n"18" = Science: Computers\n"19" = Science: Mathematics\n"20" = Mythology\n"21" = Sports\n"22" = Geography\n"23" = History\n"24" = Politics\n"25" = Art\n"26" = Celebrities\n"27" = Animals\nEnter Number for chosen category:'
        )
        or "9"
    )
    category_questions_count_lookup = requests.get(
        f"https://opentdb.com/api_count.php?category={category_choice}"
    )
    category_questions_count_lookup = category_questions_count_lookup.json()
    print(
        category_questions_count_lookup["category_question_count"]["total_question_count"],
        "= Total Question Count",
    )
    print(
        category_questions_count_lookup["category_question_count"][
            "total_easy_question_count"
        ],
        "= Total Easy Question Count",
    )
    print(
        category_questions_count_lookup["category_question_count"][
            "total_medium_question_count"
        ],
        "= Total Medium Question Count",
    )
    print(
        category_questions_count_lookup["category_question_count"][
            "total_hard_question_count"
        ],
        "= Total Hard Question Count",
    )

    difficulty = (
        input(
            f"Please enter the 'Questions' level of difficulty you will play at: {Fore.GREEN}'easy'{Style.RESET_ALL},{Fore.YELLOW}'medium'{Style.RESET_ALL},{Fore.RED}'hard'{Style.RESET_ALL}: {Style.RESET_ALL}"
        )
        or "any"
    )
    num_questions = input(f"Please enter a number of questions to be asked!: ") or "10"

    match difficulty:
        case "easy" | "e":
            difficulty = "easy"
            questions_count = category_questions_count_lookup["category_question_count"][
                "total_easy_question_count"
            ]
        case "medium" | "m":
            difficulty = "medium"
            questions_count = category_questions_count_lookup["category_question_count"][
                "total_medium_question_count"
            ]
        case "hard" | "h":
            difficulty = "hard"
            questions_count = category_questions_count_lookup["category_question_count"][
                "total_hard_question_count"
            ]
        case _:
            difficulty = "easy"
            questions_count = category_questions_count_lookup["category_question_count"][
                "total_easy_question_count"
            ]

    game_type = (
        input(
            f'Please enter the type of "Questions" you will be asked: "multiple" or "boolean" = (True/False): '
        )
        or "boolean"
    )
    match game_type:
        case "multiple" | "m":
            game_type = "multiple"


    #      QUESTIONS REQUEST URL WITH CHOICE INPUTS     #
    questions = requests.get(
        f"https://opentdb.com/api.php?amount={num_questions}&category={category_choice}&difficulty={difficulty}&type={game_type}"
    )
    print(f"https://opentdb.com/api.php?amount={num_questions}&category={category_choice}&difficulty={difficulty}&type={game_type}")
    length_of_questions = (len(questions.text[1]))
    # print(questions, ' questions response\n')

    #      QUESTIONS REASSIGNED TO READABLE JSON FORMAT      #
    questions = questions.json()
    # print(questions, ' questions json readable')

    questions = questions["results"]
# print(questions)
# print(html.unescape(questions['results'][1]['question']).replace('%20', ' '))
different_colors = [
    Fore.GREEN,
    Fore.RED,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.BLACK,
    Fore.WHITE,
]
game_play_selection()
score = 0
replay = 0
while True:
    for index in range(length_of_questions):
        
            
        game_question = unescape(questions[index]["question"])
        correct_answer = unescape(questions[index]["correct_answer"])
        wrong_answers = unescape(questions[index]["incorrect_answers"])
        answers = [correct_answer] + wrong_answers
        shuffle(answers)
        print(type(answers))

        printable_answers = ""
        for answer in answers:
            printable_answers += (
                f"{choice(different_colors)}{unescape(answer)}{Style.RESET_ALL} | "
            )

        print(
            f"\nThe question is: {game_question}\nPossible Answers are: {printable_answers}"
        )
        answer = input("What is your answer?: ")
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text=f"\nThe question is: {game_question}\nPossible Answers are: {printable_answers}").grid(column=0, row=0)
        # i = 0
        for i, answer in enumerate(answers):
            ttk.Button(frm, text=f"{answer}", command=root.destroy).grid(column=1, row=i)

        root.mainloop()
        if answer == correct_answer:
            print("Great Job! That is correct")
            score += 1
            print(f"Score Total: {score}")
        elif answer != correct_answer:
            print(
                f"Sorry, you answered incorrectly :(\nThe Correct answer is {correct_answer}"
            )
            print(f"Score Total: {score}")

    print(f"In total your score was {score}\nNot bad, not bad at all :D")
    playagain = input("\nWould you like to play again? Yes or No: ").lower()
    if playagain == "yes":
        replay += 1
        index = index + (replay * int(length_of_questions))
        if index >= length_of_questions:
            game_play_selection()
        print("Okay! Let's play again!\n")

    else:
        print("\nThank you for playing the Trivia Game!")
        break


# make a gooey, pop a screen out and play within that scree

