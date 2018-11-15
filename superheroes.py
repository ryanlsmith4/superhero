import random


class Hero:
    '''
    This is the base class for our heroes. It includes
    add_ability, attack, take_damage, is_alive,
    and fight.
    '''
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []


    def add_ability(self, ability):
        '''
        This method appends new abilies to the self.abilies
        '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Method to add all abilities together to return the
        total attack damage
        '''
        total = 0
        for ability in range(len(self.abilities)):
            total += self.abilities[ability].attack()
        return total

    def take_damage(self, damage):
        '''
        Method for recieving damage from the
        attack take_damage
        '''
        self.current_health -= damage
        return self.current_health

    def is_alive(self):
        '''
        this boolean function returns
        true if hero is alive and false if not
        '''
        if self.current_health > 0:
            # print("{} Has died in battle".format(self.name))
            return True
        else:
            print("{} Has died in battle".format(self.name))
            return False
# TODO: Run a loop to attack opponent until someone dies.

    def fight(self, opponent):
        '''
        This function runs the fight loop
        '''
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if self.is_alive() == False or opponent.is_alive() == False:
                break



class Ability:
    def __init__(self, name, attack_strength):
        '''initialize starting values'''
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        '''Return attack value between 0 and the full attack'''
        return random.randint(0, self.attack_strength)

class Weapon(Ability):
    def attack(self):
        '''
        This method should return a random values
        between one half to the full attack power of the weapon.
        '''
        return random.randint((self.attack_strength//2), self.attack_strength)

class Team:
    def __init__(self, team_name):
        '''instantiate resources'''
        self.name = team_name
        self.heroes = []

    def add_hero(self, hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
            """
            Remove hero from heroes list.
            If Hero isn't found return 0.
            """
            index = 0
            for hero in self.heroes:
                if hero.name == name:
                    self.heroes.pop(index)
                    return
                index += 1
            return 0
## TODO: Figure out why this method won't work!!!!!!
    # def remove_hero(self, name):
    #     '''
    #     Remove hero from heroes list
    #     if hero isn't found return 0
    #     '''
    #     if len(self.heroes) < 1:
    #         print(len(self.heroes))
    #         self.heroes.remove(name)
    #         return self.heroes
    #     else:
    #         return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)





if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.name)
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 30)
    hero2.add_ability(ability2)
    ability2 = Ability("Drugs", 20)
    hero.fight(hero2)
