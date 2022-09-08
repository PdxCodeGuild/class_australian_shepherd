import requests, json

link= 'https://favqs.com/api/qotd'
# link2= 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'

response= requests.get(link)
data = json.loads(response.text)

# header= Authorization: Token token="YOUR_APP_TOKEN"

def random_quote():
    for i in data:
        # if 
            quote= {i['body']}
            quote= int(quote)

    print(quote)


def quote_repl():
    choice= input('''\nEnter your choice below.
    1: Random Quote
    2: Keyword Search
    ''')

    if choice == '1':
        random_quote()
quote_repl()