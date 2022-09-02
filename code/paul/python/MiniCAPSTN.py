#The House Stock Watcher API https://housestockwatcher.com/api

import requests, json

#The link below on line seven gives us all of the transactions that have been transcribed
source= 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'
response= requests.get(source)
data = json.loads(response.text)


print('Welcome to Money Watch! Thank you all for visiting.')
print('''Disclaimer- Please read carefully before continuing.
This is a project that has been built in a classroom setting.
The information that will be presented is for EDUCATIONAL 
PURPOSES ONLY. Respectfully, please keep political opinions,
views, and ideals to yourself. See PDX Code Guild's Code of
Conduct Policy for clarification.
Anywho, let's see what our politicians are investing in!
''')

def search_by_date():
    year= input('Enter a year: ')
    year= int(year)
    for item in data:
        if year == item['disclosure_year']:
            print(f"{item['representative']} purchased between {item['amount']} on {item['disclosure_date']}")

def search_by_name():
    name= input('Enter a name: ')
    for item in data:
        if name == item['representative']:
            print(f"{item['representative']} is a representative in district {item['district']}.")
            break

def search_by_district():
    print('''\nEnter your state below in district format
    Example: User enters 'NC05', that is North Carolina,
    District 5.
    ''')
    state= input("Enter your state: ")
    for item in data:
        if state == item['district']:
            print(f"{item['amount']} : {item['representative']} : {item['disclosure_date']}")
            

def search_by_ticker():
    print('''\nA ticker is simply a symbol that represents a 
    company that is listed on the stock exchange.
    Example: User enters 'XPO', that is XPO 
    Logistics Inc.
    ''')
    org= input("What is the ticker (symbol): ")
    for item in data:
        if org == item['ticker']:
            print(f"{item['ticker']} : {item['asset_description']}", {item['representative']})

        
def find(data, index):
    return data[index]['representative']
pass

while True:
    choice= input('''\nEnter your choice: 
    1: Search by date
    2: Search by Name
    3: Search by District
    4: Search by ticker
    5: Exit
    
    ''')
    if choice == '1':
        search_by_date()
    elif choice == '2':
        search_by_name()
    elif choice == '3':
        search_by_district()
    elif choice == '4':
        search_by_ticker()
    else:
        choice == '5'
        break

            




