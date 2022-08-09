#lab02b Vers2 #makechange

money = [
('half-dollar', 50),
('qaurter', 25),
('dime', 10),
('nickle', 5),
('penny', 1)
]

def make_change(user_choice):
    denom_string= ""
    user_choice= float(user_choice)
    pennies= user_choice *100

    for denom in money:
    
        coin_count= pennies // denom[1]
        pennies= pennies % denom[1]
        denom_string= denom_string  + str(coin_count) + " " + denom[0] +  " "
    return denom_string
    
user_choice= input("What's in your wallet: ")
print(make_change(user_choice))

#nothing follows











