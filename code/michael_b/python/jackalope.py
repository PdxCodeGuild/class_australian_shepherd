import random


total_population = 2
year = 0
index = 0


class Jackalope:
    def __init__(self, age):
        self.age = age
        self.index = random.randint(0, total_population * 10000 - 1)
        self.offspring = 2
        self.death_age = 10
        self.min_reproduction_age = 4
        self.max_reproduction_age = 8
        self.gave_birth = 0

    def reproduction(self):
        if (
            self.age <= self.max_reproduction_age
            and self.age >= self.min_reproduction_age
        ):  # if the jackalope is old enough to reproduce
            return True
        else:  # if the jackalope is not old enough to reproduce
            return False

    def age_one_year(self):
        if self.age == self.death_age:  # if the jackalope is old enough to die
            return False  # return False
        self.age += 1  # add 1 to the age of the jackalope
        return True  # return True

    def death(self):
        if self.age == self.death_age:
            # print(f"Jackalope age: {self.age}")
            return True
        return False

    def set_gave_birth(self, year):
        self.gave_birth = year
        return self.gave_birth

    def __str__(self):
        return f"Jackalope age: {self.age}"


jackalopes = []
jackalopes.append(Jackalope(0))  # Adam or Eve
jackalopes.append(Jackalope(0))  # Adam or Eve

while total_population <= 1000:  # 1000 is the max population
    if total_population >= 1000:
        break
    year += 1  # Add one to the year
    for jackalope1 in jackalopes:  # Age and kill each jackalope
        jackalope1.age_one_year()  # Age the jackalope one year
        if jackalope1.death():  # If the jackalope is dead
            total_population -= 1  # Subtract one from the population
            jackalopes.remove(jackalope1)  # Remove the jackalope from the list
            print(f"{jackalope1.index} died at age {jackalope1.age}")

    for jackalope1 in jackalopes:
        for jackalope2 in jackalopes:  # for each jackalope in the list
            if (
                total_population >= 1000
            ):  # If the population is 1000 or more, break the loop
                break

            if (
                jackalope2.reproduction()
                and not jackalope2.death()
                and not jackalope1.death()
                and jackalope1.reproduction()
                and jackalope2 != jackalope1
                and total_population <= 1000
                and (jackalope1.gave_birth != year and jackalope2.gave_birth != year)
            ):  # If the jackalope is able to reproduce and the population is less than 1000
                # print(f"{jackalope1.gave_birth} {jackalope2.gave_birth} {year}")
                total_population += (
                    jackalope2.offspring
                )  # Add the offspring to the population
                jackalopes.append(Jackalope(0))  # Add a new jackalope to the list
                jackalopes.append(Jackalope(0))  # Add a new jackalope to the list
                jackalope1.set_gave_birth(
                    year
                )  # Set the year the jackalope gave birth to the current year
                jackalope2.set_gave_birth(
                    year
                )  # Set the year the jackalope gave birth to the current year
                print(
                    f"{jackalope1.index} aged {jackalope1.age} and {jackalope2.index} aged {jackalope2.age} gave birth to 2 new jackalopes"
                )
                break

    print(f"Year: {year} Current population: {total_population}")


print(f"\nIt will take {year} years for {total_population} jackalopes to be created.")
