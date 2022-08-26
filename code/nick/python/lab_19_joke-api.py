# Lab 19 Dad Joke API
# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. 
# You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

# Fetch a random joke in JSON format
# GET https://icanhazdadjoke.com/

import requests, json, time, random

while True:
    print('\nHere\'s a dad joke, in...')
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"}, )
    data = json.loads(response.text)
    countdown = 3
    for i in range(3):
        print(f'\n{countdown}')
        countdown -= 1
        time.sleep(1)
    print(f"\n{data['joke'].upper()}")
    user_input = input('\nWanna hear another? Yes or No? ').title()
    if user_input != "Yes":
        print('\nBye!')
        break

# Part 2 (Work in progress)
# Add the ability to "search" for jokes using another endpoint. 
# Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.

# while True:
#     user_search = input('Give me one work to search dad jokes for: ').lower()
#     print('\nHere\'s a dad joke, in...')
#     url = f"https://icanhazdadjoke.com/search?term={user_search}"
#     response = requests.get(url, headers={"Accept": "application/json"}, )
#     data = json.loads(response.text)
#     countdown = 3
#     for i in range(3):
#         print(f'\n{countdown}')
#         countdown -= 1
#         time.sleep(1)
#     print(f"\n{data['joke'].upper()}")
#     user_input = input('\nWanna hear another? Yes or No? ').title()
#     if user_input != "Yes":
#         print('\nBye!')
#         break

# user_search = input('Give me one word to search dad jokes for: ').lower()
# parameters = {
#     'page': 0
# }
# url = f"https://icanhazdadjoke.com/search?term={user_search}"
# response = requests.get(url, headers={"Accept": "application/json"}, params=parameters)
# data = json.loads(response.text)
# print(type(data['results']), (data['results']))
# # print(data)
# # print(f"Page(s) of jokes relating to {user_search}: {data['total_pages']}")
# parameters['page'] = data['next_page']
# response = requests.get(url, headers={"Accept": "application/json"}, params=parameters)
# data = json.loads(response.text)
# last_page = {data['total_pages']}
# print(last_page)
# print(parameters['page'])
# print(type(data['results']), (random.choice(data['results'])))
# counter = 1
# for joke in data['results']:
#     # print(joke['joke'])
#     print(f'{counter}. {joke["joke"]}')
#     counter += 1

# for joke in data['results']:
#     print(joke['joke'])


# def random_joke():
#     rand_page = random.randint(1, last_page)
#     parameters['page'] = rand_page
#     response = requests.get(url, headers={"Accept": "application/json"}, params=parameters)
#     data = json.loads(response.text)
#     print((random.choice(data['results'])))

# random_joke()

# menu_options = {
#     '1': 'View single joke',
#     '2': 'View jokes, page by page',
#     '3': 'View all jokes',
# }

# while True:
#     url = f"https://icanhazdadjoke.com/search?term={user_search}"
#     response = requests.get(url, headers={"Accept": "application/json"}, params=parameters)
#     data = json.loads(response.text)

#     command = input(
#         '\nEnter the number of the option you would like to perform\n> ')
#     command = menu_options.get(command)

#     if command == 'View single joke':
        