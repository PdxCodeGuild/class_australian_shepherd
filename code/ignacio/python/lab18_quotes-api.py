import requests, json
# -----------------------------------------------version 1-------------------------------------------------
# url = 'https://favqs.com/api/qotd'
# responce = requests.get(url)
# data = json.loads(responce.text)
# author = data['quote']["author"]
# body = data['quote']["body"]

# print(f"""\n"{body}"
# -{author}
# """)


# -----------------------------------------------version 2-------------------------------------------------
def search_quotes():
    page = 1
    while True:
        
        topic = input("enter a keyword for quotes to search: ")
        url = f"https://favqs.com/api/quotes?page={page}&filter={topic}"

        while True:
            headers = headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
            responce = requests.get(url, headers = headers)
            data = json.loads(responce.text)
            print('page', page, 'number of quotes', len(data['quotes']))
            for index in range(len(data['quotes'])):
                quote = data['quotes'][index]['body']
                print(quote,'\n') 
            while True:
                decide = input("enter 'next page' or 'done': ")
                if decide == 'next page':
                    page += 1
                    break
                elif decide == 'done':
                    break
            break
                  
search_quotes()