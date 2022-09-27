



import requests, json, time




# url = 'https://icanhazdadjoke.com/'


# response = requests.get(url,headers={'Accept':'application/json'})

# # print(response.text)

# data = json.loads(response.text)

# # print(data)

# print(data['joke'])
# num = random.randint

url = f'https://icanhazdadjoke.com/search?'

term = input('What would you like to search?:  ')

searched_url = f'https://icanhazdadjoke.com/search?term={term}'

new_response = requests.get(searched_url,headers={'Accept':'application/json'})
data = json.loads(new_response.text)


results = data['results']

for jokes in results:
    print(jokes['joke'],'\n'), time.sleep(3)



# print(results)





# $ curl -H "Accept: application/json" "https://icanhazdadjoke.com/search?term=hipster"
# {
#   "current_page": 1,
#   "limit": 20,
#   "next_page": 1,
#   "previous_page": 1,
#   "results": [
#     {
#       "id": "GlGBIY0wAAd",
#       "joke": "How much does a hipster weigh? An instagram."
#     },
#     {
#       "id": "xc21Lmbxcib",
#       "joke": "How did the hipster burn the roof of his mouth? He ate the pizza before it was cool."
#     }
#   ],
#   "search_term": "hipster",
#   "status": 200,
#   "total_jokes": 2,
#   "total_pages": 1
# }