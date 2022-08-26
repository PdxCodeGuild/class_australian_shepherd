# Class creates a user-defined data structure, which holds its own data members and member 
# functions, which can be accessed and used by creating an 
# instance of that class. A class is like a blueprint for an object


class Car:
    def __init__(self, make, model, name):
        self.make = make
        self.model = model
        self.driver = name
        
name = input("Please enter your name ")
make = input("Please enter your cars manufacture ")
model = input("Please enter your cars model: ")

your_car = Car(make, model, name)

print(f'\n{your_car.driver} drives a {your_car.make} {your_car.model}')

new_owner = input("\nYou just sold the car, what is the name of the person you sold it to? ")

your_car.driver = new_owner

print(f'{your_car.driver} drives a {your_car.make} {your_car.model}')
print('-------------------------------------------------------------------------')

# Use the car class to make a new instance of the Car. Both will still exist
neighbors_name = input('\nYour neighbor also has a car, what is that person name? ')
neighbors_make = input("Please enter your neighbors car manufacture ")
neighbors_model = input("Please enter your neighbors car model: ")

neighbors_car = Car(neighbors_make, neighbors_model, neighbors_name)

print(f"\n{neighbors_car.driver} drives a {neighbors_car.make} {neighbors_model}")
print(f'\n{your_car.driver} drives a {your_car.make} {your_car.model}')