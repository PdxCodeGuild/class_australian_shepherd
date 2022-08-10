import random

winning_nums= []
user_pick= []


actual_numbers= 0

print("Welcome to pick six! Enter your six numbers below")


#Generate random numbers to compare to ticket purchases

for nums in range(1, 99):
    random_nums= random.randint(1, 99)
    winning_nums.append(random_nums)

def make_ticket():
    ticket = []
    for nums in range(6):
        random_nums= random.randint(1, 99)
        ticket.append(random_nums)

    return ticket
        
winning_ticket= make_ticket()
print(make_ticket()) 

def match_ticket(ticket, winning_ticket):
    num_dict= {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000 
    }
    matches= 0
    for i in range(len(ticket)):
        if ticket[i] == winning_ticket[i]:
            matches += 1
        earnings= num_dict[matches]
    return earnings







for i in range(100000):
    ticket= make_ticket()
    if ticket in make_ticket:

        print("You have won!")

    break
    




#Checking for matches

# for winners in winning_nums:
#     if user_pick_nums == winners:
#         actual_numbers= actual_numbers + 1

# print(f'There are {actual_numbers} winning numbers!')
# print(f'You have won!')



