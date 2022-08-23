import random

sock_types = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}                                                  # create a globale variable with the dictionary of key value pairs starting at 0 pairs of each
sock_colors = ['black', 'white', 'blue']                                                                     # create a global variable list of each specific type of sock color
socks_list = ['ankle', 'crew', 'calf', 'thigh']                                                              # create a global variable list of each specific type of sock available

def create_tuples():                                                                                         # create a function to make tuples of sock_colors and sock_list and also put them in a dictionary with a 0 counter starter
    tuple_socks = []                                                                                         # declare a list for tuple_socks that's empty
    dictionary_socks = {}                                                                                    # declare a dictionary to assign the tuple_socks paired to values of 0 i.e ('black' 'crew': 0)

    for sock in socks_list:                                                                                  # loop through each sock in the sock list
        for sock_color in sock_colors:                                                                       # loop through each color in sock_colors
            tuple_socks.append((sock_color, sock))                                                           # append the tuple of each sock_color and sock to the empty tuple_sock list
    for tuple_sock in tuple_socks:                                                                           # loop through each tuple_sock tuple and give them the value 0 to start with
        dictionary_socks[tuple_sock] = 0                                                                     # this is where that ^ actually happens
    return dictionary_socks                                                                                  # return the final product tuples to the dictionary_socks
    # print(tuple_sock)
        

def random_socks():                                                                                          # create a function that makes a random_socks list
    socks = []                                                                                               # declare the empty socks list
    for i in range(100):                                                                                     # loop through the sock_types 100 times 
        socks.append(random.choice(list(sock_types)))                                                        # append the randomly picked socks in sock_types to the empty sock list
    return socks                                                                                             # return the final product to the socks list

def random_colored_socks(socks):                                                                             # create a funtion that takes the list of 100 randomly generated socks and assign them a randomly generated color from sock_colors
    colored_socks = []                                                                                       # declare the empty list for colored_socks i.e ('random color(black)', 'sock type(crew)')
    for sock in socks:                                                                                       # loop sthrough sock in socks(which are the 100 randomly generated socks from the function above)
        colored_socks.append((random.choice(sock_colors), sock))                                             # append the tuple of a randomly generated color for each sock to the colored_socks list
    return colored_socks                                                                                     # return the final product to the colored_socks list


def match_socks(socks, sock_types):                                                                          # create a function that matches the socks and colors and adds a counter to their value in the dictionary set for them
    for sock in socks:                                                                                       # loop through each sock in the socks
        for sock_type in sock_types.keys():                                                                  # loop through each sock_type in the sock_type keys
            if sock == sock_type:                                                                            # if the sock is equal to the sock type then...
                sock_types[sock_type] += 1                                                                   # add a counter to each value with a pair for each pair 
    return sock_types                                                                                        # return the final product to the function giving the tuples pairs value the end result of how many duplicates there are, an even or an odd amount makes no difference yet
        
def find_loners(sock_types):                                                                                 # create a function that takes in sock_types tuples matches counter
    loner = ''                                                                                               # declare a empty string variable called loners to destinguish the loners from the pairs
    pairs = ''                                                                                               # declare a empty string variable called pairs to destinguish the pairs from the loners
    for sock_type in sock_types.keys():                                                                      # loop through each tuple sock_type in sock_types keys and values
        if sock_types[sock_type] % 2 != 0:                                                                   # if the sock_type is not divisible by 2(meaning there is an odd amount and has found a single "loner") then...
            if type(sock_type) is tuple:                                                                     # then take that odd value single out and determain it's type() and if its a "tuple"
                loner = loner + f'\n{sock_types[sock_type] % 2} {sock_type[0]} {sock_type[1]} loner'         # then reassign loner to itself PLUS the statement of the sock_type loner for each tuple that has an odd number
            else:                                                                                            # otherwise
                loner = loner + f'\n{sock_types[sock_type] % 2} {sock_type} loner!'                          # OTHERWISE reassign loner to itself with this print statement
        if isinstance(sock_type, tuple):                                                                     # if the sock_type type() is a 'tuple' then
            pairs = pairs + f'\n{sock_types[sock_type] // 2} {sock_type[0]} {sock_type[1]} pairs'            # reassign pairs to itself plus adding the print statement showing the sock_type pairs total divide by 2 and the name plus color
        else:                                                                                                # OTHERWISE
            pairs = pairs + f'\n{sock_types[sock_type] // 2} {sock_type} pairs'                              # reassign pairs to itself plus adding the print statement showing the current number of pairs and the sock_type
    return loner + pairs                                                                                     # return the final product back to the variables "loner" and "pairs"

randomized_socks = random_socks()                                                                            # assigning the function of random_socks() to a variable to use while running the other functions below while checking the program
# VERSION 1 print()
print(find_loners(match_socks(randomized_socks, sock_types)))                                               # print the results of the functions being called with their individual processes happening 

print(f'\n')                                                                                                # dividing the first version of the lab between the second version
# VERSION 2 print()
print(find_loners(match_socks(random_colored_socks(randomized_socks), create_tuples())))                    # print the results of the functions being called with their individual processes happening
