import requests, json



url = "https://api.artic.edu/api/v1/artworks/27992?fields=id,title,image_id" 

response = requests.get(url)

data = json.loads(response.text)

print(data)

image_id = data['data']['image_id']

title = data['data']['title']

image_url = f'https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg'

print(f"""Title: {title}
    Url: {image_url}""")

# print(image_id)



