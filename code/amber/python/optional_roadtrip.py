# ROAD TRIP

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

print(list(city_to_accessible_cities.keys()))

city_input = input('Please enter a city from those listed above: ').title()

if city_input in city_to_accessible_cities.keys():
  print(f'The following is a list of cities directly connected to {city_input}: {city_to_accessible_cities[city_input]}.') #maybe fix this so it is not printed as dict

print(f'From the connections listed, the following additional connections can be made: ')

connects = city_to_accessible_cities.pop(city_input)

for connect in connects:
  if connect in city_to_accessible_cities.keys():
    hop_hop = list(city_to_accessible_cities.pop(connect))
    print(f'{connect}: {", ".join(hop_hop)}')
