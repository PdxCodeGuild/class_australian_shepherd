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

city1 = input(f"Please enter what city you Where you'd like to start... \n{list(city_to_accessible_cities.keys())}:\n ").title()
destination = city_to_accessible_cities.get(city1)
print(destination)
for city2 in destination:
    city3 = city_to_accessible_cities.get(city2)
    for nextItem in city3:
        print(f"From {city1} to {city2} to {nextItem}")
