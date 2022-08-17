# CONTACT LIST


with open('lab11_contact.csv', 'r') as file:
    lines = file.read().split('\n')

###### need to create a function to write lines back into new csv (DONT GET THIS PART): ######

# Write to different csv
#with open('lab11_new_contact.csv', 'w') as file:
    #file.write(???)

lines.pop()

headers = lines[0]
headers = headers.split(',')

contact_list = []

for index in range(1, len(lines)):

  contact_info = lines[index].split(',')

  contact = {
    headers[0].title(): contact_info[0].title(),
    headers[1].title(): contact_info[1].title(),
    headers[2].title(): contact_info[2].title()
}

  contact_list.append(contact)













# NOTES ------------------

'''
# open and read CSV file and assign lines variable name to data
with open('lab11_contact.csv', 'r') as file:
    lines = file.read().split('\n')


# remove blank line from end
lines.pop()
#print(f'lines: {lines}')

# create list of header titles from first line of csv file
headers = lines[0]
headers = headers.split(',')
#print(f'headers: {headers}')

contact_list = []

# for loop to break up lines
for index in range(1, len(lines)):
  #print(f'lines[index]:{index} {lines[index]}')

  #break off each line of lines list into contact info list
  contact_info = lines[index].split(',')
  #print(f'contact info: {contact_info}')

  #plug everything into a single contact dictionary
  contact = {
    headers[0].title(): contact_info[0].title(),
    headers[1].title(): contact_info[1].title(),
    headers[2].title(): contact_info[2].title()
}
  #print(f'contact: {contact}')

  #append each contact to contact list
  contact_list.append(contact)

print(f'contact list: {contact_list}')
'''
