def make_change():
    total = int(dollar * 100) 
    print(total)
    quarters = total // 25
    dimes = (total - (quarters * 25)) // 10
    nickels = (total - (quarters * 25 + dimes * 10)) // 5
    pennies = (total - (quarters * 25 + dimes * 10 + nickels * 5)) // 1
    d = {}
    if quarters > 0:
        d['quarters'] = quarters
    if dimes > 0:
        d['dimes'] = dimes
    if nickels > 0:
        d['nickels'] = nickels
    if pennies > 0:
        d['pennies'] = pennies
    print(d)
dollar = float(input('Enter a dollar amount: '))
make_change()