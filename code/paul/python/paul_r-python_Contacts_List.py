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
    
        
    info= {
            'name': name, 
            'favorite team': fav_team, 
            'best player': best_player
    }
    contact_list.append(info)
        

def find():
    sel_name= input('Who are you looking for: ')
    for index in range(len(contact_list)):
        # print(contact_list[index]['name'])
        
       
        if sel_name == contact_list[index]['name']:
            print(contact_list[index]['name'])
            print(contact_list[index]['favorite team'])
            print(contact_list[index]['best player'])
          
# find(input('Who are you looking for: '))

def change():
    
    sel_name= input("Name: ")
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
    
    # if which_att == 'name':
    #     find(updated_record)
    # else:
    #     find(sel_name)


    
            
def remove():
    sel_name= input("Choose name to remove: ")
    for index in range(len(contact_list)):
        if sel_name == contact_list[index]['name']:
            contact_list.pop(index)
            # print(contact_list)
            break


def save():
    headers= keys
    
    output_string= headers[0] + ','+  headers[1]+ ','+ headers[2]  
    for index in range(len(contact_list)):
        person_dict= contact_list[index]
        # print(person_dict['name'])
        # moved '\n' to line 105 to prevent trailing new line. Prevents Erros in Loading CSV. -TA Micheal recommendation
        output_string += '\n' + person_dict['name'] + ',' + person_dict['favorite team'] + ',' + person_dict['best player'] 
        
        with open('contacts.csv', 'w') as file:
            file.write(output_string)
    


        
        
        
    # CVS's need a single string with comma seperated values
    # use your headers then loop oover your contacts
    # make one string where each line ends in '\n'. 
    # this is the new line character. DO not end in a comma
    # example
    # to_write = 'name,team,player\n'PJ,Braves,Acura jr'
    pass

            
def main_repl(): #<---------- From CRUD Notes
    while True:
        print(contact_list)
        sel_action = input('''\nHello, see below for options:
        1: Add a record
        2: Find a record
        3: Change a record
        4: Delete a record
        5: Save Changes
        ''')
        if sel_action == '1':
            new_contact()
            
        elif sel_action == '2':
            find()
        elif sel_action == '3':
            change()
        elif sel_action == '4':
            remove()
        elif sel_action == '5':
            save()

       
main_repl()




        
           

        
        



        






  
    











    




    




