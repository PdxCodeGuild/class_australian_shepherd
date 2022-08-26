# Importing requests and JSON
import requests
import json
# Setting our headers to accept application/json
headers = {'Accept': 'application/json'}
# Settting our responses with our header for our webpage
response = requests.get("https://icanhazdadjoke.com", headers=headers)
# Using json method to load our request as text
data = json.loads(response.text)
# Setting our joke to a variable
joke = data['joke']
# Printing our joke
print(joke)
