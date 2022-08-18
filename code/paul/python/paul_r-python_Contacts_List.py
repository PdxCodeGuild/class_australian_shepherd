#We need a contact list via a CSV file
#We have to open the file we create. See below (line 10 and see lab 10). Also, do NOT use the csv lib. Write the logic out.

with open('contacts.csv', 'r') as file:
    lines= file.read().split('\n')
    # print(lines)

contact_list= [] #<-------------This line specifically is from the lecture

keys= lines[0].split(',')
# print(keys)

for value in range(1, len(lines)):
    values= lines[value].split(',')
    contact= {
        keys[0]:values[0],
        keys[1]:values[1],
        keys[2]:values[2]}
    contact_list.append(contact)
    
# print(contact)
# print(contact_list)

#Create the function for a new record
def new_contact():
    name= input("Name: ")
    fav_team= input("Favorite Team: ")
    best_player= input("Best Player: ")
    for value in range(1, len(lines)):
        
        new_info= {
            'name': name, 
            'fav_team': fav_team, 
            'best_player': best_player
    }
    contact_list.append(new_info)

new_contact()
print(contact_list)






    




    




