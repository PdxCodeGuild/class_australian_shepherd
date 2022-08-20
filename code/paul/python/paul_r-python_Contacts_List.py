#We need a contact list via a CSV file
#We have to open the file we create. See below (line 10 and see lab 10). Also, do NOT use the csv lib. Write the logic out.







with open('contacts.csv', 'r') as file:
    lines= file.read().split('\n')
    # print(lines)

contact_list= [] #<-------------This line specifically is from the lecture

def main_repl(): #<---------- From CRUD Notes
    while 1:
        sel_action = input('''\nHello, see below for options:
        1: Add a record
        2: Find a record
        3: Change a record
        4: Delete a record
        ''')
        if sel_action == 1:
            new_contact()
            
        elif sel_action == 2:
            find()
        elif sel_action == 3:
            change()
        elif sel_action == 4:
            remove()
        break
main_repl()

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
    
        
    info= {
            'name': name, 
            'favorite team': fav_team, 
            'best player': best_player
    }
    contact_list.append(info)
        
    
new_contact()

print(contact_list)

def find():
    for index in range(len(contact_list)):
        # print(contact_list[index]['name'])
        sel_name= input('Who are you looking for: ')
       
        if sel_name == contact_list[index]['name']:
            print(contact_list[index]['name'])
            print(contact_list[index]['favorite team'])
            print(contact_list[index]['best player'])
           
# find(input('Who are you looking for: '))

def change():
    sel_name= input("Who do you need to change: ")
    find(sel_name)
    which_att = input("Which Attribute: ")
    updated_record= input("Execute the change: ")
    
    for index in range(len(contact_list)):
        if sel_name == contact_list[index]['name']:
            if which_att == 'name':
                contact_list[index]['name'] = updated_record
                
            elif which_att == 'favorite team':
                contact_list[index]['favorite team'] = updated_record
            elif which_att == 'best player':
                contact_list[index]['best player'] = updated_record
    
    if which_att == 'name':
        find(updated_record)
    else:
        find(sel_name)
    
            
def remove():
    sel_name= input("Choose name to remove: ")
    find(sel_name)
    for index in range(len(contact_list)):
        if sel_name == contact_list[index]['name']:
            contact_list.pop(index)
            print(contact_list)
        break
            





        
           

        
        



        






  
    











    




    




