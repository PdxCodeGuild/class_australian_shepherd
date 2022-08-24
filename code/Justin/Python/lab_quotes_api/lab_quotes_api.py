# # Importing requests and JSON
import requests
import json
# # Setting our headers to accept application/json
# # headers = {'Accept': 'application/json'}
# # Settting our responses with our header for our webpage
# response = requests.get("https://favqs.com/api/qotd")
# # Using json method to load our request as text
# data = json.loads(response.text)['quote']
# # Setting our quote to a variable
# print('The quote of the day is:\n')
# print(data['body'])
# print(f"By: {data['author']}")

# Setting our initial page number
page_number = 1
# Creating a search term to determine which quotes we want to hear
search_term = input('What quote topic would you like to hear? \n ==> ').lower()

# Creating a function to pull our API information


def get_quotes():
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    parameters = {'Accept': 'term'}
    # Settting our responses with our header for our webpage
    response = requests.get(f"https://favqs.com/api/quotes?page={page_number}&filter={search_term}",
                            headers=headers, params=parameters)
    # Using json method to load our request as text
    data = json.loads(response.text)['quotes']
    # Printing our overall quote data from the API
    print(
        f'There are {len(data)} quotes associated with {search_term} on page {page_number}\n')
    # Using a for loop with enumerate to list the quote and quote number
    for index, quote in enumerate(data):
        print(index+1, quote['body'], "\n")


# Asking for user inputs utilizing a while loop to iter through the pages of the API to pull information from
while True:
    # Calling our function
    get_quotes()
    # Declaring our user check value
    check_val = input(
        "Enter 'next' to see the results on the next page, or type done to search for a new keyword: ").lower()
    # Using if/else statements to iter through the pages one at a time, reset and search a new term, or exit the program
    if check_val == 'next':
        page_number += 1
        get_quotes()
    elif check_val == 'done':
        page_number = 1
        search_term = input(
            'What quote topic would you like to hear? \n ==> ').lower()
        get_quotes()
    else:
        break
