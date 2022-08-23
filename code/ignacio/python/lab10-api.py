import requests, json

url = 'https://icanhazdadjoke.com/'
responce = requests.get(url, headers = {'Accept': 'application/json'})
data = json.loads(responce.text)
print(data['joke'])
