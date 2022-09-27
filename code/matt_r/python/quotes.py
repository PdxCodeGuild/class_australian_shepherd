



from ast import keyword
import requests, json



#################################### version 1 #################################

"""
url = 'https://favqs.com/api/qotd'


response = requests.get(url)

# print(response.text)

data = json.loads(response.text)

# print(data)

print(f'Your quote is: ', data['quote']['body'],'\n','The author is: ', data['quote']['author'])

"""


#################################### version 2 #################################



# word = 'dog'
word = input('Enter a keyword to search for quotes:  ')

page = 1

url = f'https://favqs.com/api/quotes?page={page}&filter={word}'

response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

# print(response.text)

data = json.loads(response.text)
quotes_list = data['quotes']
# print(quotes_list[0]['body'])

# print(data)
counter = 0

while True:
    print(page)
    for quote in quotes_list:
       
        print(quotes_list[counter]['body'],'\n')
        counter += 1

    next_page = input("Would you like to continue to the next page yes or no?  ")
    if next_page == 'yes':
        page += 1
        counter = 0    
        url = f'https://favqs.com/api/quotes?page={page}&filter={word}'
        response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = json.loads(response.text)
        quotes_list = data['quotes']
    else:
        break
    
# print(page)