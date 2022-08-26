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
import html
from html import unescape
from random import shuffle, choice

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
difficulty = input(f"Please enter the 'Questions' level of difficulty you will play at: 'easy','medium','hard': ") or 'easy'
game_type = input(f'Please enter the type of "Questions" you will be asked: "multiple" or "boolean" = (True/False): ') or 'boolean'


#      QUESTIONS REQUEST URL WITH CHOICE INPUTS     #
questions = requests.get(f"https://opentdb.com/api.php?amount={num_questions}&category={category_choice}&difficulty={difficulty}&type={game_type}")
print(questions, ' questions response\n')

#      QUESTIONS REASSIGNED TO READABLE JSON FORMAT      #
questions = questions.json()
# print(questions, ' questions json readable')

questions = questions['results']
# print(html.unescape(questions['results'][1]['question']).replace('%20', ' '))

for index in range(len(questions)):
    # print(questions[index]['question'])   #    no ENCODE type, gives random ass characters 
    print(html.unescape(questions[index]['question']))# TRUE/FALSE Question
    print(questions[index]['correct_answer'] + "\n")     # CORRECT ANSWER
# answer = print(html.unescape(questions['results'][1]['correct_answer']).replace('%20', ' '))
# print(answers)


# print(len(questions))

# #       CODE THAT DOESN'T WORK ANYMORE       #
# for question in range(0,len(questions['results'])):
#     print(question, ' questions')
#     correct_answers = questions['results'][question]['correct_answer']
#     print(correct_answers, ' correct answers')
#     # incorrect_answers = questions['results'][question]['incorrect_answer']
#     # print(incorrect_answers, ' incorrect_answers')
#     # answers = correct_answers.append(incorrect_answers)
    
#     # print(answers, ' answers')
    
#     print(unescape(questions['results'][question]['question']))
    
#     print(unescape(questions['results'][question]['correct_answer']).lower())
    

#         REWRITE CODE TO CREATE THE GAME SESSION        #





























