# # Importing requests and JSON
# import requests
# import json
# # Setting our headers to accept application/json
# headers = {'Accept': 'application/json'}
# # Settting our responses with our header for our webpage
# response = requests.get("https://icanhazdadjoke.com", headers=headers)
# # Using json method to load our request as text
# data = json.loads(response.text)
# # Setting our joke to a variable
# joke = data['joke']
# # Printing our joke
# print(joke)

import requests
import json
# Setting our headers to accept application/json
headers = {'Accept': 'application/json'}
parameters = {'Accept': 'term'}
# Settting our responses with our header for our webpage
search_term = input('What type of joke would you like to hear? \n ==>').lower()
response = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}",
                        headers=headers, params=parameters)
# Using json method to load our request as text
data = json.loads(response.text)['results']
# Cleaning up print data
for jokes in data:
    j = jokes['joke']
    print(j+'\n')
