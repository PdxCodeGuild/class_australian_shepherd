'''
benjamin_birky
08/23/2022
lab18_QuotesApi
'''
import requests, json, time

'''
url = 'https://favqs.com/api/qotd'

response = requests.get(url)
data = json.loads(response.text)

quote = data['quote']['body']

print(quote)
'''
# Main body while loop
next_page = 'next page'
while True:
# Have user enter in a keyword, set the page number to 1
    user_keyword = input("Enter a keyword to search for in quotes: ")
    page_number = 5
# While loop for user to select the next page 
    while next_page == 'next page':
        url = f"https://favqs.com/api/quotes?page={page_number}&filter={user_keyword}"
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
# Conditional statement
# if there are no quotes left the loop will break
# else we will print the current quotes
        quote = data['quotes'][0]['body']
        if quote == 'No quotes found':
            print(f"----End of quotes----")
            break
        else:
            quote_quantity = len(data['quotes'])
            print(f"\n{quote_quantity} quotes associated with {user_keyword} - page {page_number}\n")
            i = 0
# Print off all the quotes on current page
            while i < quote_quantity:
                quote = data['quotes'][i]['body']
                print(quote)
                i += 1
# Conditional statement
# if the user wants the next page the page number increases by 1
# else break
            next_page = input("Enter 'next page' or 'done': ").lower()
            if next_page == 'next page':
                page_number += 1
            else:
                break

