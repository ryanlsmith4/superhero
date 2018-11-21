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
        self.armors = []
        self.deaths = 0
        self.kills = 0


    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the
        list of abilities that already exists -- self.abilities.
        This means that self.abilities will be a list of abilities and weapons.
        '''
        self.abilities.append(weapon)


    def add_armor(self, armor):
        '''
        This method will add the armor object that is passed in to this method to
        the list of armor objects defined in the initializer as self.armors.
        '''
        self.armors.append(armor)


    def add_death(self):
        self.deaths += 1



    def add_kill(self, num_kills=1):
        '''This method keeps tabs on kills'''
        self.kills += num_kills

    def defend(self):
        '''
        This method runs the block method
        on each piece of armor and calculates
        the total defense
        '''
        total_block = 0
        if self.current_health == 0:
            return 0
        else:
            for armor in self.armors:
                total_block += armor.block()
                return total_block


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

        # self.current_health = self.current_health - damage


    def is_alive(self):
        '''
        this boolean function returns
        true if hero is alive and false if not
        '''
        if self.current_health > 0:
            # print("{} Has died in battle".format(self.name))
            return True
        else:
            return False


    def fight(self, opponent):
        '''
        Loop while both heros are alive then apply damage to
        each other check that both heros have < 0 health once
        a hero has 0 health finish fight
        '''
        while self.is_alive() and opponent.is_alive():
            # take damage from self and opponent
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        # check if self or opponent died
        # score kill for the death of the other one
        if not self.is_alive():
            self.add_death()
            opponent.add_kill()
            print("{} has died in battle".format(self.name))
        elif not opponent.is_alive():
            opponent.add_death()
            self.add_kill()
            print("{} has died in battle".format(opponent.name))



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

    def alive_heroes(self):
        '''

        '''
        alive_list = list()
        #find out if team one has heroes alive
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list


    def attack(self, other_team):
        '''
        This function should randomly select
        a living hero from each team and have
        them fight until one or both teams
        have no surviving heroes.
        '''
        # Loop as long as each team has at least 1 hero alive
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            #select random hero from alive heros in team 1 and 2
            random_hero_1 = random.choice(self.alive_heroes())
            random_hero_2 = random.choice(other_team.alive_heroes())
            #Have alive random heros fight until one is dead
            random_hero_1.fight(random_hero_2)







    def revive_heroes(self, health=100):
        '''method resets all heroes health to full'''
        for hero in self.heroes:
            Hero.current_health = health
            return Hero.current_health

    def stats(self):
        '''Method to print the K/d
        ratio for all Heroes
        '''
        for hero in Team.heroes:
            print("{}/{}".format(Hero.kills,Hero.deaths))


    def add_hero(self, hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(hero)

    #
    # def remove_hero(self, name):
    #         """
    #         Remove hero from heroes list.
    #         If Hero isn't found return 0.
    #         """
    #         index = 0
    #         for hero in self.heroes:
    #             if hero.name == name:
    #                 self.heroes.pop(index)
    #                 return
    #             index += 1
    #         return 0


## TODO: Figure out why this method won't work!!!!!!
    def remove_hero(self, name):
        '''
        Remove hero from heroes list
        '''
        if len(self.heroes) > 1:
            # print(len(self.heroes))
            self.heroes.remove(name)
            return self.heroes


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)


class Armor:


    def __init__(self, name, max_block):
        '''instantiate name and defense strength'''
        self.name = name
        self.max_block = max_block


    def block(self):
        '''
        Return a random value between 0 and
        the max_block hero initialized with
        '''
        return random.randint(0, self.max_block)

class Arena:
    def __init__(self):
        '''
        Declare variable
        '''
        self.team_one = None
        self.team_two = None

    def user_input(self, prompt):
        user_input = input(prompt)
            return user_input


    def create_ability(self):
            '''
        This method will allow a user to create an ability.

        Prompt the user for the necessary information to create a new ability object.

        return the new ability object.
        '''




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
    print("hero 1 is {} and has {} kills".format(hero.name , hero.kills))
    print("hero 2 is {} and has {} kills".format(hero2.name , hero2.kills))
