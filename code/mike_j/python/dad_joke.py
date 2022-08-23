import requests, json

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"}, )

data = json.loads(response.text)

print(data)