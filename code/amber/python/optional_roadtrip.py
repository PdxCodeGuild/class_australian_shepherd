# ROAD TRIP

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

cities_list = list(city_to_accessible_cities.keys())

print(", ".join(cities_list))

city_input = input('''
Please enter a city from those listed above: ''').title()

hop = list(city_to_accessible_cities[city_input])

if city_input in city_to_accessible_cities.keys():
  print(f'''\nCities that directly connect to {city_input}:

{", ".join(hop)}.

  ''')

print(f'''From the connections listed, the following connections are possible: ''')

connects = city_to_accessible_cities.pop(city_input)

for connect in connects:
  if connect in city_to_accessible_cities.keys():
    hop_hop = list(city_to_accessible_cities.pop(connect))
    print(f'\n{connect}: {", ".join(hop_hop)}.\n')
