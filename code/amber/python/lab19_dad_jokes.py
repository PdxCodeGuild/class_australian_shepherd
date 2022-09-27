# DAD JOKE API

import requests, json

url = f'https://icanhazdadjoke.com/'

response = requests.get(
    url, headers={'Accept': 'application/json'})

data = json.loads(response.text)

joke = data['joke']

print(joke)
