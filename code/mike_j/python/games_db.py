import csv, requests, json

games = []

with open('games_db.csv', 'r') as file:
   reader = csv.DictReader(file)

   for item in reader:
      games.append(item)

for item in games:
   item["Score"] = int(item["Score"])

def retrieve_all():
   for i in range(len(games)):
        print(games[i]["Platform"] + ": " + games[i]["Title"] + ", " + str(games[i]["Score"]))

def retrieve_plat():
    platform = input("Enter platform name: ")
    for i in range(len(games)):
        if (games[i]["Platform"]) == platform:
            print(games[i]["Title"] + ", " + str(games[i]["Score"]))

def kw_search():
    keyword = input("Enter search term: ")
    for i in range(len(games)):
        if keyword in (games[i]["Title"]):
            print(games[i]["Platform"] + ": " + games[i]["Title"] + ", " + str(games[i]["Score"]))

def online_search():
    search = input("Enter search term: ")
    url = f"https://api.rawg.io/api/games?key=4fae09a36f754b5bb3540f93edd09f3a&search={search}&page_size=500"
    response = requests.get(url)
    data = json.loads(response.text)
    for i in range(len(data['results'])):
        print(f"{data['results'][i]['platforms'][0]['platform']['name']}" + ": " + f"{data['results'][i]['name']}")            

def score():
    score = int(input("Enter minimum score: "))
    for i in range(len(games)):
        if (games[i]["Score"]) >= score:
            print(games[i]["Platform"] + ": " + games[i]["Title"] + ", " + str(games[i]["Score"]))

def score_plat():
    platform = input("Enter platform name: ")
    score = int(input("Enter minimum score: "))
    for i in range(len(games)):
        if (games[i]["Platform"]) == platform and (games[i]["Score"]) >= score:
            print(games[i]["Platform"] + ": " + games[i]["Title"] + ", " + str(games[i]["Score"]))

def create():
    title = input("title: ")
    platform = input("platform: ")
    score = input("score: ")

    game = {
        'Title': title,
        'Platform': platform,
        'Score' : score
    }

    games.append(game)

    save()

def update():
    title = input("Enter title of game: ")
    for i in range(len(games)):
        if (games[i]["Title"]) == title:
            print(f"""
            Title: {(games[i]["Title"])}
            Platform: {(games[i]["Platform"])}
            Favorite color: {(games[i]["Score"])}
            \n""")

    choice = input("Update title, platform or score? ")
    new_value = input("Change the value to: ")

    for i in games:
        if i["Title"] == title:
            if choice == 'title':
                i["Title"] = new_value
            elif choice == 'platform':
                i["Platform"] = new_value
            elif choice == 'score':
                i["Score"] = new_value      

    save()

def delete():
    title = input("Enter the title of game: ")
    for i in range(len(games)):
        if (games[i]["Title"]) == title:
            if title == (games[i]["Title"]):
                games.pop(i)
                break

    save()                   

def save():

   with open("games_db.csv", 'w',newline='') as csvfile:

      columns = ["Title", "Platform", "Score"]
      
      writer = csv.DictWriter(csvfile, fieldnames=columns)

      writer.writeheader()

      for key in games:
         writer.writerow(key)

def main():
    while True:
        choice = input('''\nWelcome to Games_db. Make a choice from the following list:
        1: Show all games in database
        2: Show all games in database for specific platform
        3: Search for games in database by keyword
        4: Search for games online by keyword
        5: Filter all games in database by minimum score
        6: Filter all games in database by minimum score for specific platform
        7: Create a new database record
        8. Update a database record
        9. Delete a database record
        10. Exit
        ''')
        
        if choice == '1':
            retrieve_all()

        elif choice == '2':
            retrieve_plat()

        elif choice == '3':
            kw_search()

        elif choice == '4':
            online_search()

        elif choice == '5':
            score()

        elif choice == '6':
            score_plat()

        elif choice == '7':
            create()

        elif choice == '8':
            update()

        elif choice == '9':
            delete() 

        elif choice == '10':
            break      

main()         