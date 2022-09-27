import requests, json
import time



# url = "https://api.artic.edu/api/v1/artworks/27992?fields=id,title,image_id" 

# response = requests.get(url)

# data = json.loads(response.text)

# # print(data)

# image_id = data['data']['image_id']

# title = data['data']['title']

# image_url = f'https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg'

# print(f"""Title: {title}
#     Url: {image_url}""")

# print(image_id)

url = "https://icanhazdadjoke.com/"
# print(response.text)
# print(joke)

#-------------     VERSION 1    ----------------#


# answer = True
# while answer:
#     response = requests.get(url, headers={'Accept': 'application/json'})
#     data = json.loads(response.text)
#     joke = data['joke']
#     answer = input("Wanna hear a dad joke?, Yes or No: ").lower()
    
    
#     if answer == "yes":
#         print(joke)
#         time.sleep(3)
#         print("hahaha")
#         answer = True
#     if answer == "no":
#         print("Okay, your loss!")
#         answer = False
    
#-------------     VERSION 2      --------------#    

term = input("Please enter a search term: ")

url = f"https://icanhazdadjoke.com/search?term={term}"
# print(url)
response = requests.get(url, headers={'Accept': 'application/json'})

data = json.loads(response.text)
for i in range(len(data)):
    print(data['results'][i]['joke'], "\n")

