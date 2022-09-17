import requests, json

source = 'https://icanhazdadjoke.com/'
response= requests.get(source, headers={'Accept': 'application/json'})
joke= response.json()



# for item in joke:
#     if item == joke:
# print("This is the joke", joke)
# print("This is the type", type(joke))
#This is the joke {'id': 'fqWgFt4Edxc', 'joke': 'Why do crabs never give to charity? Because they’re shellfish.', 'status': 200}

joke_string= joke['joke']
print(joke_string)