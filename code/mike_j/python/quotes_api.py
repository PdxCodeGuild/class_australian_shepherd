# Quotes API

# Version 1:

import requests, json

url = "https://favqs.com/api/qotd"

response = requests.get(url)

data = json.loads(response.text)

print(data)

# Version 2:

# import requests, json

# page = 1

# keyword = input('Please enter keyword: ')

# def quotes():

#     response = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={keyword}", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#     data = json.loads(response.text)['quotes']
    
#     for index, quote in enumerate(data):
#         print(index+1, quote['body'], "\n")

# while True:
    
#     quotes()
    
#     choice = input(
#         "Enter 'next' to view next page of results, 'new' to search for a new keyword or 'exit' to quit: ")
    
#     if choice == 'next':
#         page += 1
#         quotes()

#     elif choice == 'new':
#         page = 1
#         keyword = input(
#             'Please enter keyword: ')
#         quotes()

#     elif choice == 'exit':
#         break