'''
benjamin_birky
08/02/2022
lab_RoadTrip
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

destination = input(f"Please enter what city you Where you'd like to start... \n{list(city_to_accessible_cities.keys())}:\n ").title()
city1 = city_to_accessible_cities.get(destination)
print(city1)
for city2 in city1:
    city3 = city_to_accessible_cities.get(city2)
    for nextItem in city3:
        print(f"From {destination} to {city2} to {nextItem}")
