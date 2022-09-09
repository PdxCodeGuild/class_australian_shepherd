import requests, json

link= 'https://favqs.com/api/qotd'

response= requests.get(link)
data = json.loads(response.text)
# print(data['quote']['body']) #<----- Random Quote
# print(data['quote']['author']) #<----- Author of Random Quote
page = 1

while True:
    choice= input("Enter a keyword to get quotes or type random to get a random quote: ")
    

    link2= 'https://favqs.com/api/quotes'
    response2= requests.get(link2, params={'filter': choice, 'page': page}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data2= json.loads(response2.text)
    # print(data2)

    
    for item in data2['quotes']:
        print(item['body'])
    next_page= input("Next Page: Type next page, enter another keyword, or Type done to exit: ")

    if next_page == 'next page':
        page += 1
        
    else:
        choice == 'done'
        break
