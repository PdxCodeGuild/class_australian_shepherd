# Lab Optional Road Trip 
# Traveling from one city to an adjacent one is called a hop. Let the user enter a city. Print out all the cities connected to that city. 
# Then print out all cities that could be reached through two hops.

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

user_start = input('''
Where do you want to start?  
-- Boston
-- New York
-- Albany
-- Portland
-- Philadelphia
Enter a city: '''
).title()

print(f'\nFrom {user_start}, you can connect to: {", ".join(city_to_accessible_cities[user_start])}.')

# Version 2 
# Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
user_hops = int(input('How many additional hops do you want to make from there? '))
reachable_cities = []

counter = 0
for i in range(user_hops+1):
    if counter < 1:
        for city in list(city_to_accessible_cities[user_start]):
            if city not in reachable_cities:
                reachable_cities.append(city)
    else:
        for city in list(reachable_cities):
            for next_city in list(city_to_accessible_cities[city]):
                if next_city not in reachable_cities:
                    reachable_cities.append(next_city)
    counter += 1

print(f'With {user_hops + 1} hops, you will be able to reach the following cities: {", ".join((reachable_cities))}.')

end_location = input('''
Where do you want to end up?  
-- Boston
-- New York
-- Albany
-- Portland
-- Philadelphia
Enter a city: '''
).title()

if end_location in reachable_cities:

    # We've also mapped the travel time of each hop. When the user enters a city and a number of hops, print out the shortest travel times to each city. 
    # Paths with fewer hops are not necessarily those with the shorter travel times.

    master_travel_list = []
    final_travel_list = []

    counter = 0
    for i in range(user_hops + 1):
        if counter < 1:
            for city in (city_to_accessible_cities[user_start]):
                travel_list = []
                travel_list.append(user_start)
                travel_list.append(city)
                master_travel_list.append(travel_list)

        else: 
            for cities in master_travel_list:

                for new_city in (city_to_accessible_cities[cities[-1]]):
                    accessible_cities = list(cities)
                    accessible_cities.append(new_city)

                    if (accessible_cities[0] != accessible_cities[-2]) and (accessible_cities [-1] != accessible_cities [1]):
                        final_travel_list.append(accessible_cities)
                    else:
                        continue

            master_travel_list.clear()
               
        counter += 1
        for i in final_travel_list:
            master_travel_list.append(i)

    final_travel_list.clear()
    for i in master_travel_list:
        if (len(i) == (user_hops + 2)) and (i not in final_travel_list):
            final_travel_list.append(i)

    travel_time_list = []
    for routes in final_travel_list:
        # print(routes)
        counter = 1
        travel_time = 0
        for city in routes:
            if counter < (user_hops+2):
                travel_time += city_to_accessible_cities_with_travel_time[city][routes[counter]] 
                counter += 1
            else:
                travel_time_list.append([routes, travel_time])
        counter += 1

    suggested_travel = []

    counter = 0
    for i in travel_time_list:
        if i[0][-1] == end_location:
            if len(suggested_travel) == 0:
                suggested_travel.append(i)
            else:
                if i[-1] < suggested_travel[0][-1]:
                    suggested_travel.pop()
                    suggested_travel.append(i)
        counter += 1

    print(f'This will be your fastest route to get to {end_location} from {user_start} utilizing {user_hops + 1} hop. \n{", ".join(suggested_travel[0][0])} \nIt will take you {suggested_travel[0][-1]} units of time.')

else:
    print('Sorry you cant reach there with your number of hops. Goodbye!')
