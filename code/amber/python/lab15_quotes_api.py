# QUOTES API

import requests, json

qotd_url = f'https://favqs.com/api/qotd'

qotd_response = requests.get(
    qotd_url, headers={'Accept': 'application/json'})

qotd_data = json.loads(qotd_response.text)
#print(qotd_data)

qotd = qotd_data['quote']['body']
qotd_author = qotd_data['quote']['author']

#print(qotd)
#print(qotd_author)

# v.2 - list quotes by keyword --------------------

def load_page(page, keyword):

  url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'

  response = requests.get(
      url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

  data = json.loads(response.text)

  return data

page_counter = 1

keyword_input = input("enter a keyword to search for quotes: ")

while True:

  if keyword_input == 'quit':
    print('Cool beans, PEACE!')
    break

  data = load_page(page_counter, keyword_input)

  quotes_list = data['quotes']

  print(f'25 quotes associated with {keyword_input} - page {page_counter}')

  item_counter = 0

  for item in range(len(quotes_list)):
    quote = quotes_list[item]['body']
    author = quotes_list[item]['author']
    item_counter += 1
    quote_string = f'\n{item_counter}. "{quote}" - {author}\n'

    print(quote_string)

  next_page = input("enter 'next page' or 'done': ")

  if next_page == 'next page':
    page_counter += 1
    continue

  elif next_page == 'done':
    page_counter = 1
    keyword_input = input("enter a keyword to search for quotes or 'quit' to end: ")
    continue
