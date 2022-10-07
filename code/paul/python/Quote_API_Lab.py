import requests, json

link= 'https://favqs.com/api/qotd'

response= requests.get(link)
data = json.loads(response.text)

# print(data['quote']['body']) #<----- Random Quote
# print(data['quote']['author']) #<----- Author of Random Quote
page = 1
choice= input("Enter a keyword to get quotes or type random to get a random quote: ")

while True:
    link2= 'https://favqs.com/api/quotes'
    response2= requests.get(link2, params={'filter': choice, 'page': page}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data2= json.loads(response2.text)
    # print(data2)

    print(f"\nThere are 25 quotes with the keyword {choice}\n\n")
    for item in data2['quotes']:
        print(item['body'])
    user_input= input("\nType next page, enter another keyword, or Type done to exit:")

    if user_input == 'next page':
        if not data2['last_page']:
            page += 1
        else:
            print('We are on the last page.')
            continue

    elif user_input == 'keyword':
        choice= input('Type in a new keyword: ')    
    
    else:
       
        break
