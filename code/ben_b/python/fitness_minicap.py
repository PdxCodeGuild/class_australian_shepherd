'''
benjamin_birky
fitness_minicap
08/29/2022
'''
import json 
import matplotlib.pyplot as plt
import numpy as np

f = open('input_data.json')
data = json.load(f)

fitness_dict = {}
bmi = 0

# Calculate BMI
def calculate_bmi(user_height_inches, user_weight):
    user_bmi = (user_weight / (user_height_inches ** 2)) * 703
    return user_bmi
 
'''
bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])() 

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

'''


# Create a new entry based off the date
# The new dictionary's name will be the date entered
def create_entry():
    response = True
    while response == True:
        date = input("Date - YYMMDD: ")
        calories_consumed = int(input("Calories consumed: "))
        calories_burned = int(input("Calories burned: "))
        total_miles = int(input("Enter miles travelled: "))
        weight_lifted = int(input("Enter total weight lifted: "))
        weight = int(input("Enter your weight: "))
        height = int(input("Enter your height: "))
        user_input = input(f"Is {date} the correct date? Type 'yes' or any key: ")

        if user_input == 'yes':
            break

    input_data = {
            "calorie goal": 2110,
            "calories consumed": calories_consumed,
            "calories burned": calories_burned, 
            "total miles": total_miles,
            "weight lifted": weight_lifted,
            "weight": weight,
            "bmi": calculate_bmi(height, weight)
        }

    data[date] = input_data     
    return

# Retrieve an entry using the date 
def retrieve_entry():
    date = input("What date are you searching for? YYMMDD: ")
    for entry in data:
        if entry == date:
            print(json.dumps(data[entry]))
            break
            
# Update an entry based off the date
def update_entry():
    date = input("Enter the date of the entry that you want to update YYMMDD: ")
    attribute = input("Enter the attribute that you want to update: ")
    value = int(input("Enter the value that you would like to change: "))
    for entry in data:
        if entry == date:
            data[entry].update({attribute: value})
            break

# Delete an entry based off the date
def delete_entry():
    date = input("Enter the date of the entry that you want to delete - YYMMDD: ")
    for entry in data:
        if entry == date:
            data.pop(entry)
            break

# Print all entries with json dumps for clarity inside the terminal
def print_entries():
    print(json.dumps(data, indent=4))
    return

# Take a list of dates and convert them into new strings with better readability
def format_dates(date_list):
    new_list = []
    for index in range(len(date_list)):
        item = date_list.pop(0)
        new_item = item[2:4] + "/" + item[4:] + "/" + item[0:2]
        new_list.append(new_item)
    return new_list

# Plot points based off the int values of user selected keys
def plot_entry(user_input):
    y1 = []
    y2 = []
    x1 = []
    
    # Pull 'date' keys from dictionary then sort them in a list
    for item in data:
        x1.append(item)
    x1.sort()
    
    # Pull 'user input' keys from dictionary in the same order as the x1 sorted list
    # This will allow values to match their corresponding dates
    # After that we format the dates for better readability
    for date in x1:
        y1.append(data[date][user_input])
    x1 = format_dates(x1)

    # Each 'user input' will create a specific graph for that selection
    if user_input == 'calories consumed':
        for item in x1:
            y2.append(2110)
        y2points = np.array(y2)
        plt.plot(y2points)
        plt.ylabel(f"\nOrange line = {user_input.title()}\nBlue line = Calorie Limit")
    elif user_input == 'weight':
        for item in x1:
            y2.append(185)
        y2points = np.array(y2)
        plt.plot(y2points)
        plt.ylabel(f"\nOrange line = {user_input.title()}\nBlue line = Weight Goal")
    elif user_input == 'bmi':
        for item in x1:
            y2.append(24.4)
        y2points = np.array(y2)
        plt.plot(y2points)
        plt.ylabel(f"\nOrange line = {user_input.title()}\nBlue line = BMI Goal")
    else:
        plt.ylabel(f"\n{user_input.title()}")

    y1points = np.array(y1)
    x1points = np.array(x1)
    plt.title("Fitness MiniCap")
    plt.xlabel("Dates")
    plt.plot(x1points, y1points)
    plt.grid()
    plt.show()
    return

# CRUD Loop
while True:
    selection = input(f'''
Press '1' to create a new entry
Press '2' to retrieve a previous entry
Press '3' to update a previous entry
Press '4' to delete a previous entry
Press '5' to print all entries
Press '6' to plot entries
Press any key to exit program
''')
    if selection == '1':
        create_entry()
    elif selection == '2':
        retrieve_entry()
    elif selection == '3':
        update_entry()
    elif selection == '4':
        delete_entry()
    elif selection == '5':
        print_entries()
    elif selection == '6':

# Allow user to plot any data within the dictionary
        while True:
            plot_selection = input(f'''
Type 'Calories consumed' to plot calories consumed
Type 'Calories burned' to plot calories burned
Type 'Total miles' to plot miles travelled
Type 'Weight lifted' to plot weight lifted
Type 'Weight' to plot weight
Type 'BMI' to plot BMI
Press any key to go back to the main menu 
''').lower()
            if plot_selection == 'calories consumed':
                plot_entry(plot_selection)
            elif plot_selection == 'calories burned':
                plot_entry(plot_selection)
            elif plot_selection == 'total miles':
                plot_entry(plot_selection)
            elif plot_selection == 'weight lifted':
                plot_entry(plot_selection)
            elif plot_selection == 'weight':
                plot_entry(plot_selection)
            elif plot_selection == 'bmi':
                plot_entry(plot_selection)
            else:
                break
    else:
        break

# Closing file
f.close()
# Writing function
with open("output_data.json", "w") as outfile:
    json.dump(data, outfile)
