from tokenize import Name

import requests, json
import pprint

# this shall be a basic pokedex. that means this program will simplpy search and return pokemon. FOR NOW

def weakness():
    name = ''
    url = f"https://pokeapi.co/api/v2/type/{name}"
    responce = requests.get(url)
    data = json.loads(responce.text)
    
    print(data)

weakness()
    
# pokemon_list = []
# def search_poke():

#     name = input('choose a mon: ')q
#     url = f"https://pokeapi.co/api/v2/pokemon/{name}"
#     responce = requests.get(url)
#     data = json.loads(responce.text)
#     poke_name = data['name']
#     poke_name = poke_name.title()
#     poke_ability = data["abilities"][0]['ability']['name'].title()
#     poke_id = data['id']
#     poke_type = data['types']
#     type_list = []
#     for index in poke_type:
#         type_list.append(index['type']['name'])
    
#     new_list = ', '.join(type_list).title()
#     poke_result = f"Name: {poke_name} \nNumber: {poke_id} \nType: {new_list}\nAbility: {poke_ability}"



#     # poke_dict = {
#     #     'name' : 'x',
#     # }

#     # pokemon_list.append(poke_dict)
#     # return data 
#     print(poke_result)


# # pokemon = get_poke()
# while True:
#     choice = input("""Enter your selction
#     1: Search for pokemon
#     2: Done
#     """)

#     if choice == '1':
#         search_poke()
#     elif choice == '2':
#         break
