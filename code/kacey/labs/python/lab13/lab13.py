# Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote,
# and then allow the user to find quotes by keyword. 
# To accomplish this we'll be using the requests library.

# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, 
# parse the JSON in the response into a python dictionary, and show the quote and the author.

# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with a 
# given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
# Prompt the user for a keyword, list the quotes you get in response, and prompt the user 
# to either show the next page or enter a new keyword. You can use string concatenation to 
# build the URL.

# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:
# This API endpoint requires an API key be included in a request header. You can find documentation
# of specifying request headers here and documentation on authorization with the Favqs API here 
# under "Authorization".

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

import requests, json

# ------------- VERSION 1 ---------------- #

# url = "https://favqs.com/api/qotd"

# response = requests.get(url)

# data = json.loads(response.text)

# # print(data)
# author = data['quote']['author']
# quote = data['quote']['body']

# print(f"""Author: {author}
# Quote: {quote}""")

# -------------- VERSION 2 -----------------#


page_number = 1
search_term = input("Please enter a keyword to search for quotes: ").lower()

while True:
    url = f"https://favqs.com/api/quotes?page={page_number}&filter={search_term}"
    response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    json_response = response.json()
    # print(json_response)
    # break
    quotes_list = json_response['quotes']
    print(f'Quotes: {len(quotes_list)}, Page: {page_number}\n')
    for quote in range (len(quotes_list)):
        
        if quotes_list[quote]['body'] != 'No quotes found':
            
            author_json = quotes_list[quote]['author']
            quote_json = quotes_list[quote]['body']
        
            print(f'"{quote_json}"\n\tBy: {author_json}\n')
        else:
            print('No quotes found\n')

    if json_response['last_page'] == False:
        response = input("enter 'next' or 'done' or 'keyword':  ").lower()
        if response == 'next':
            page_number += 1
        elif response == 'keyword':
            search_term = input("What is the new keyword?: ")
            
            page_number = 1
        elif response == 'done':
            print("This concludes your program")
            break
        else:
            print("Invalid Command")