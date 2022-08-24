# QUOTES API

import requests, json

qotd_url = f'https://favqs.com/api/qotd'

qotd_response = requests.get(
    qotd_url, headers={'Accept': 'application/json'})

qotd_data = json.loads(qotd_response.text)

qotd = qotd_data['quote']['body']
qotd_author = qotd_data['quote']['author']

print(qotd)
print(qotd_author)
