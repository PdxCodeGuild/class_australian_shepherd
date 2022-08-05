# MAKE CHANGE

#dollars_in = 0.67
dollars_in = float(input('Please enter a dollar amount: '))



def make_change(money):
  pennies = int(money * 100)
  quarters = pennies // 25
  dimes = (pennies - quarters * 25) // 10
  nickels = ((pennies - quarters * 25) - (dimes * 10)) // 5
  end_pennies = ((pennies - quarters * 25) - (dimes * 10)) % 5
  return f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {end_pennies} pennies.'

print(make_change(dollars_in))

'''
dollars_in = 1.36

pennies = int(dollars_in * 100)
quarters = pennies // 25
dimes = (pennies - quarters * 25) // 10
nickels = ((pennies - quarters * 25) - (dimes * 10)) // 5
end_pennies = ((pennies - quarters * 25) - (dimes * 10)) % 5

print(f'starting pennies = {pennies}')
print(f'quarters = {quarters}')
print(f'dimes = {dimes}')
print(f'nickles = {nickels}')
print(f'end pennies = {end_pennies}')
'''
