
# Open CSV and store information in the variable lines
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

print(lines)


dummy_data = lines[0]

# Write to different csv
with open('new_contacts.csv', 'w') as file:
        file.write(dummy_data)