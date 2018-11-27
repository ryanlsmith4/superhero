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
        '''initialize starting values name of ability, and attack and
        ability strength
        '''
        self.name = name
        self.attack_strength = attack_strength


    def attack(self):
        '''Return attack value between 0 and the full attack'''
        return random.randint(0, self.attack_strength)


class Weapon(Ability):


    def attack(self):
        '''
        This method should return random values
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
        Creates a list of heroes who have health > 0

        '''
        alive_list = []
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
        for hero in self.heroes:
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
    def __init__(self, name):
        '''
        Declare variables
        '''
        self.team_one = None
        self.team_two = None


    def build_team(self):
        name = input('Enter a team name: ')
        new_team = Team(name)
        keep_adding_heroes = True
        while keep_adding_heroes:
            print('Adding a hero to {}...'.format(name))
            new_hero = Hero(input('Enter the name of the hero: '))
            new_hero.abilities = self.hero_additions('ability', new_hero.name)
            new_hero.abilities = self.hero_additions('weapon', new_hero.name)
            new_hero.armors = self.hero_additions('armor', new_hero.name)
            new_team.add_hero(new_hero)
            keep_adding_heroes = self.yes_or_no('Would you like to keep adding heroes to {}? Answer ( y/n ): '.format(name))
        return new_team

    def yes_or_no(self, message):
        """Method that returns false and will end a loop when user input n, will return True if user inputs y """
        user_res = input(message)
        if user_res.lower() == 'y':
            return True
        elif user_res.lower() == 'n':
            return False
        else:
            print('Input not recognized')
        return self.yes_or_no(message)

    def hero_additions(self, addition_type, hero_name):
        """Method that allows users to make additions to heros while building out the team (using Arena methods) """
        adds = []
        if self.yes_or_no('do you want to add {} to {}? answer( y/n ): '.format(addition_type, hero_name)):
            keep_asking = True
            addition = Ability if addition_type =='ability' else Weapon if addition_type == 'weapon' else Armor
            while keep_asking:
                name = input('What is this {} called?'.format(addition_type))
                block_or_attack = 'block' if addition_type == Armor else 'attack'
                strength = int(input("What is {}'s  {} strength?".format(name, block_or_attack)))
                adds.append(addition(name, strength))
                keep_asking = self.yes_or_no('Do you want to add another {}? Answer ( y/n ): '.format(addition_type))
            return adds


    def build_team_one(self):
        """Method builds out team one """
        print('Building team one ....')
        self.team_one =  self.build_team()
        return self.team_one


    def build_team_two(self):
        """allows user to create team two  """
        print('Building team two ...')
        self.team_two = self.build_team()
        return self.team_two

    def team_battle(self):
        """while loop for 2 teams to fight until all the heroes on one team are dead """
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            if self.team_one.alive_heroes():
                print('{} wins the battle!'.format(self.team_one.name))
                self.team_one.update_kills(len(self.team_two.heroes))
                return False
            else:
                print('{} wins the battle!'.format(self.team_two.name))
                self.team_two.update_kills(len(self.team_one.heroes))
                return False


    def show_stats(self):
        """Prints all heroes in arena stats(k/d ratio) """
        print('Printing stats')
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    arena = Arena('Big Arena')
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

#     def user_input(self, prompt):
#             user_input = input(prompt)
#             return user_input
#
#     def create_ability(self):
#         ability_name = self.user_input("Name your hero's ability: ")
#         ability_strength = self.user_input("Strength of ability: ")
#         ability = Abilities(str(ability_name), int(ability_strength))
#         return ability
#
#     def create_weapon(self):
#         weapon_name = self.user_input("Name your hero's weapon: ")
#         weapon_strength = self.user_input("Strength of weapon: ")
#         weapon = Weapon(str(weapon_name), int(weapon_strength))
#         return weapon
#
#
#     def create_armor(self):
#         armor_name = self.user_input("Name your hero's armor: ")
#         armor_strength = self.user_input("Strength of armor: ")
#         armor = Armor(str(armor_name), int(armor_strength))
#         return armor
#
#     def create_hero(self):
#         hero_name = self.user_input("Name your hero: ")
#         hero_health = self.user_input("Health of your Hero: ")
#         hero = Hero(str(hero_name), int(hero_health))
#
#         # add_armors = self.user_input("would you like to add armor? Y/N ")
#         # adding_armors = True
#         # while adding_armors:
#         #     if add_armors == "Y":
#         #         armor = create_armor()
#         #         hero.append(armor)
#         #     else: keep_adding = False
#         # add_weapons = self.user_input("Would you like to add weapons? Y/N")
#         #
#         # while
#
#
#     def add_equipment(self):
#         answer = self.user_input("Please add equipment, A for armors AB for abilities W for weapons and D for done: ")
#         adding_equipments = True
#         while adding_equipments:
#             if answer.Upper() == 'A':
#                 create_armor()
#
#
#
#
#
#
#
#
#
#     def team_battle(self):
#         deaths1 = 0
#         deaths2 = 0
#
#         while deaths1 < len(self.team_one.heroes) and deaths2 < len(self.team_two.heroes):
#         	self.team_one.attack(self.team_two)
#         	self.team_two.attack(self.team_one)
#         	for i in self.team_one.heroes:
#         		deaths1 += i.deaths
#         	for i in self.team_two.heroes:
#         		deaths2 += i.deaths
#
#     def show_stats(self):
#         print(self.team_one.name + " stats:")
#         self.team_one.stats()
#         print(self.team_two.name + " stats:")
#         self.team_two.stats()
#
#
#     def play_again(self):
#         answer = self.user_input("Play again (y/n)? ")
#         if answer == "y" or answer == "Y":
#         	self.team_one.revive_heroes()
#         	self.team_two.revive_heroes()
#         	game_loop(self)
#
#
# arena = Arena()
#
# def game_loop(arena):
#     arena.create_hero()
#
#
# game_loop(arena)
#
#
