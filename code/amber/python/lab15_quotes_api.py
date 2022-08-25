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
