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

#     GAME TYPE QUESTIONS PROMTS     #
num_questions = input(f'Please enter a number of questions to be asked!: 1-10: ') or '10'
category_choice = input(f'Please enter the category number for type of questions would like to play from!\n"9" = General Knowledge\n"10" = Entertainment: Books\n"11" = Entertainment: Film \n"12" = Entertainment: Music\n"13" = Entertainment: Musicals and Theatres\n"14" = Entertainment: Television\n"15" = Entertainment: Video Games\n"16" = Entertainment: Board Games\n"17" = Science and Nature\n"18" = Science: Computers\n"19" = Science: Mathematics\n"20" = Mythology\n"21" = Sports\n"22" = Geography\n"23" = History\n"24" = Politics\n"25" = Art\n"26" = Celebrities\n"27" = Animals\nEnter Number for chosen category:') or '9'
difficulty = input(f"Please enter the 'Questions' level of difficulty you will play at: {Fore.GREEN}'easy'{Style.RESET_ALL},{Fore.YELLOW}'medium'{Style.RESET_ALL},{Fore.RED}'hard'{Style.RESET_ALL}: {Style.RESET_ALL}") or 'easy'
match difficulty:
    case "easy" | "e":
        difficulty = "easy"
    case "medium" | "m":
        difficulty = "medium"
    case "hard" | "h":
        difficulty = "hard"
    case _:
        difficulty = "easy"
        
game_type = input(f'Please enter the type of "Questions" you will be asked: "multiple" or "boolean" = (True/False): ') or 'boolean'
match game_type:
    case "multiple" | "m":
        game_type = "multiple"
    

#      QUESTIONS REQUEST URL WITH CHOICE INPUTS     #
questions = requests.get(f"https://opentdb.com/api.php?amount={num_questions}&category={category_choice}&difficulty={difficulty}&type={game_type}")
# print(questions, ' questions response\n')

#      QUESTIONS REASSIGNED TO READABLE JSON FORMAT      #
questions = questions.json()
# print(questions, ' questions json readable')

questions = questions['results']
# print(questions)
# print(html.unescape(questions['results'][1]['question']).replace('%20', ' '))
different_colors = [Fore.GREEN,Fore.RED,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN,Fore.BLACK,Fore.WHITE]
score = 0

while True:
    for index in range(len(questions)):

        game_question = unescape(questions[index]['question'])# TRUE/FALSE Question
        correct_answer = unescape(questions[index]['correct_answer'])    # CORRECT ANSWER
        wrong_answers = unescape(questions[index]['incorrect_answers'])
        
        printable_wrong_answers = ""
        for wrong_answer in wrong_answers:
            printable_wrong_answers += f"{choice(different_colors)}{unescape(wrong_answer)}{Style.RESET_ALL} | "

        print(f"The question is: {game_question}\nPossible Answers are: {printable_wrong_answers}{choice(different_colors)}{correct_answer}{Style.RESET_ALL}")
        answer = input("What is your answer?: ")
        
        if answer == correct_answer:
            print("Great Job! That is correct")
            score += 1
            print(f"Score Total: {score}")
        elif answer == wrong_answer:
            print("Sorry, you answered incorrectly :(")
            print(f"Score Total: {score}")
    print(f"In total your score was {score}\nNot bad, not bad at all :D")        
    break

# print(f"The question is: {game_question}\nPossible Answers are: {printable_wrong_answers}{correct_answer}")
# for index in range(len(questions)):
#     print(f"{unescape(questions[index]['question'])}\n")
    
    
#     for index in range(len(questions)):
#   ASK A QUESTION, INPUT A RESPONSE, COMPARE THE ANSWER TO THE INPUT, THEN ASK NEXT QUESTION. 
# make a gooey, pop a screen out and play within that screen