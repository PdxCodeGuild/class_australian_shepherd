



from pprint import pprint
import requests
import config as config

key = config.API_KEY



year  = input('What year are you looking for?:  \n')
make  = input('What make are you looking for?:  \n')
model = input('What model are you looking for?: \n')




api_url = f'https://api.api-ninjas.com/v1/cars?make={make}&year={year}&limit=10&model={model}'
response = requests.get(api_url, headers={'X-Api-Key': key})

if response.status_code == requests.codes.ok:
    pprint(response.text)
else:
    print("Error:", response.status_code, response.text)