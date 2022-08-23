import random


class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack

    def attack_turn(self):
        damage = self.attack_power + random.randint(1, 20)
        return damage

    def take_health_damge(self, damage):
        self.health -= damage


name = input("Enter hero's name: ")
health = int(input("Enter hero's health: "))
attack = int(input("Enter hero's attack power: "))

hero = Character(name, health, attack)


name = input("Enter villain's name: ")
health = int(input("Enter villain's health: "))
attack = int(input("Enter villain's attack power: "))

villain = Character(name, health, attack)



while True:

    hero_damage_roll = hero.attack_turn()

    villain.take_health_damge(hero_damage_roll)
    print('Hero attacks...')
    print(f'Villain took {hero_damage_roll} dmg. Villain hp: {villain.health}')

    if villain.health <= 0:
        print('\nvillain fell')
        break

    villain_damage_roll = villain.attack_turn()

    hero.take_health_damge(villain_damage_roll)

    print('\nVillain attacks...')
    print(f'Hero took {villain_damage_roll} dmg. Hero hp: {hero.health}')

    if hero.health <= 0:
        print('\nhero fell')
        break

    

