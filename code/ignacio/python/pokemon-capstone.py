from calendar import prmonth
import requests, json
import pprint

# this shall be a basic pokedex. that means this program will simplpy search and return pokemon. FOR NOW


# how to return and calculate weakness mulitplier????

def advantage(current_type):
    with open('pokeweakness.json') as f:
        types = json.load(f)
        print(f"Advantage over:")
        for item in types[current_type.title()].items():
            if item[1] > 1:
                print(f"{item[0]}")
            # print(item[1])
        # print(current_type)
        # print(f"Are at a disadvantage")
    

def search_poke():

    name = input('Enter a pokemon name or number from 1 to 905: ')
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    responce = requests.get(url)
    data = json.loads(responce.text)
    poke_name = data['name']
    poke_name = poke_name.title()
    poke_ability = data["abilities"][0]['ability']['name'].title()
    poke_id = data['id']
    poke_type = data['types']
    type_list = []
    for index in poke_type:
        type_list.append(index['type']['name'])
   
    new_list = ', '.join(type_list).title()
    # print(type_list)
    poke_result = f"Name: {poke_name} \nNumber: {poke_id} \nType: {new_list}\nAbility: {poke_ability}"

    print(poke_result)
    advantage(type_list[0])

# pokemon = get_poke()
while True:
    choice = input("""\nEnter your selction
    1: Search for pokemon
    2: Exit
    """)

    if choice == '1':
        search_poke()
    elif choice == '2':
        print("Goodbye!!")
        break
