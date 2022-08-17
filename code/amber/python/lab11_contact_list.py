# CONTACT LIST

# open and read CSV file and assign lines variable name to data
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')


# remove blank line from end
lines.pop()
#print(f'lines: {lines}')

# create list of header titles from first line of csv file
headers = lines[0]
headers = headers.split(',')
print(f'headers: {headers}')



###### need to create a function to write lines back into new csv
