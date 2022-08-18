# Optional Lab: Sock Sorter
# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loner.

import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']

sock_drawer = []

# sock_matches = {
#     'ankle': {
#         'pairs': 0,
#         'loner': 0
#     }, 
#     'crew': {
#         'pairs': 0,
#         'loner': 0
#     }, 
#     'calf': {
#         'pairs': 0,
#         'loner': 0
#     }, 
#     'thigh': {
#         'pairs': 0,
#         'loner': 0
#     }, 
# }
# # Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']
# for i in range(100):
#     sock_drawer.append(random.choice(sock_types))
# # Find the number of duplicates and loner for each sock type. Hint: dictionaries are helpful here.
# for sock in sock_drawer:
#     for sock_type in sock_matches:
#         if sock == sock_type:
#             if sock_matches[sock_type]['loner'] == 0:
#                 sock_matches[sock_type]['loner'] += 1
#             else:
#                 sock_matches[sock_type]['loner'] -= 1
#                 sock_matches[sock_type]['pairs'] += 1

# print(sock_matches)

# Version 2 
# Now you have a mix of types and colors. Represent socks using tuples containing one color and one type ('black', 'crew'). 
# Randomly generate these, and then group them into pairs.

sock_colors = ['black', 'white', 'blue']
for i in range(100):
    sock_combo = []
    sock_combo.append(random.choice(sock_colors)) 
    sock_combo.append(random.choice(sock_types))
    sock_drawer.append(tuple(sock_combo))
# print(sock_drawer)

sock_matches = {}

for sock in sock_drawer:
    if sock[1] not in sock_matches:
        sock_matches[sock[1]] = {f'{sock[0]} pairs': 0, f'{sock[0]} loner':0}
        sock_matches[sock[1]][f'{sock[0]} loner'] += 1
    else:
        if f'{sock[0]} loner' not in sock_matches[sock[1]]:
            sock_matches[sock[1]].update({f'{sock[0]} pairs': 0, f'{sock[0]} loner':0})
            sock_matches[sock[1]][f'{sock[0]} loner'] += 1
        else:
            if sock_matches[sock[1]][f'{sock[0]} loner'] == 0:
                sock_matches[sock[1]][f'{sock[0]} loner'] += 1
            else:
                sock_matches[sock[1]][f'{sock[0]} loner'] -= 1
                sock_matches[sock[1]][f'{sock[0]} pairs'] += 1

# print(f'\n{sock_matches}')

print('\nIn your drawer there are these socks:')
for sock in sock_matches:
    for i in range(len(sock_matches[sock])):
        if sock_matches[sock][list(sock_matches[sock])[i]] != 0:
            print(sock_matches[sock][list(sock_matches[sock])[i]], sock, list(sock_matches[sock])[i])