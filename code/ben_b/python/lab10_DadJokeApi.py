'''
benjamin_birky
08/22/2022
lab10_DadjokeApi
'''

import requests, json, time


while True:
    user_input = input("Please enter a type of joke you would like to hear, i.e. Hipster, or 'Quit' : ").title()
    if user_input == 'Quit':
        break
    url = f"https://icanhazdadjoke.com/search?term={user_input}"

    header = {'Accept': 'application/json'}
    response = requests.get(url, headers=header)
    data = json.loads(response.text)
    i = data['total_jokes'] - 1

    while True:
        if i < 0:
            print("Finished!")
            break
        the_whole_joke = data['results'][i]['joke']
        split_joke = the_whole_joke.split('? ')

        time.sleep(2)
        print(f"\n{split_joke[0]}?")
        time.sleep(1)
        print(f".")
        time.sleep(1)
        print(f"..")
        time.sleep(1)
        print(f"...")
        time.sleep(1)
        print(f"{split_joke[1]}")
        i -= 1

