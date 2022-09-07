from tkinter import PROJECTING
import requests, json
import pprint
url = f"https://pogoapi.net/api/v1/type_effectiveness.json"
responce = requests.get(url)
data = json.loads(responce.text)
# pprint.pprint(data)

with open("pokeweakness.json", "w") as file:
    json.dump(data, file)