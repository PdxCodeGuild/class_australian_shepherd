
import requests, json

link= 'https://icanhazdadjoke.com/'

ping= requests.get(link)
info= json.loads(ping.text)

