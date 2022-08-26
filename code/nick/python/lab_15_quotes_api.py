# Lab 15 Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. 
# To accomplish this we'll be using the requests library.

import requests, json

# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

# url = "https://favqs.com/api/qotd"
# response = requests.get(url, headers= headers, params= parameters)
#     data = json.loads(response.text)
#     # print(data)
#     # print(f"\"{data['quote']['body']}\"")
#     # print((data['quote']['author_permalink']).replace('-', ' ').title())


# Version 2: The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
# Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. 
# You can use string concatenation to build the URL.

user_keyword = input('Enter a keyword to search for quotes: ').lower()
url = "https://favqs.com/api/quotes?page=<page>&filter=<keyword>"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
}
parameters = {
    'page': 1,
    'filter': user_keyword
}

def quote_printer():
    counter = 1
    for quote in data['quotes']:
        if quote["body"] != 'No quotes found':
            print(f'{counter}. "{quote["body"]}" -{(quote["author_permalink"]).replace("-", " ").title()}')
            counter += 1
        else:
            print(quote["body"])

while True: 
    response = requests.get(url, headers= headers, params= parameters)
    data = json.loads(response.text)

    print(f'\nHere are {len(data["quotes"])} quotes associated with {user_keyword.upper()}. \n\n\tPAGE {data["page"]}\n')

    if data["page"] == 1 and data["last_page"] == True:
        quote_printer()
        print('\nThis is the last page.')
        user_keyword = input('Enter a new keyword to search for quotes: ').lower()
        parameters['filter'] = user_keyword
        
    elif data["last_page"] == False:
        quote_printer()
        # If it's not the first page
        if data['page'] != 1:
            user_input = input('Enter "NEXT", "LAST", or "DONE": ').upper()
            if user_input == 'NEXT':
                parameters['page'] += 1
            elif user_input == 'LAST':
                parameters['page'] -= 1
            elif user_input == 'DONE':
                user_keyword = input('\nEnter a new keyword to search for quotes: ').lower()
                parameters['filter'] = user_keyword
            else:
                print('Bye!')
                break
        else:
            user_input = input('Enter "NEXT" or "DONE": ').upper()
            if user_input == 'NEXT':
                parameters['page'] += 1
            elif user_input == 'DONE':
                user_keyword = input('\nEnter a new keyword to search for quotes: ').lower()
                parameters['filter'] = user_keyword
            else:
                print('Bye!')
                break
    else: 
        quote_printer()
        print('\nThis is the last page.')
        user_input = input('Enter "LAST" or "DONE": ').upper()
        if user_input == 'LAST':
            parameters['page'] -= 1
        elif user_input == 'DONE':
            user_keyword = input('Enter a new keyword to search for quotes: ').lower()
            parameters['filter'] = user_keyword
        else:
            print('Bye!')
            break
