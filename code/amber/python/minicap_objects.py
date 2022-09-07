# This is a supplement to the mini capstone which serves to populate the art.json file with valid objectIDs from which to generate URLs for viewing.

import requests, json, random

objects_url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects'

object_response = requests.get(
    objects_url, headers={'Accept': 'application/json'})

object_data = json.loads(object_response.text) # list of objectID numbers

object_id = object_data['objectIDs']

object_list = []

for counter in range(len(object_id)):
    if counter % 1000 == 0:
        object_list.append(counter)
        #print(counter)

with open("art.json", "w") as outfile:
    json.dump(object_list, outfile)

#print(type(object_id))
