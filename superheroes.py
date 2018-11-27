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


    def show_stats(self):
        '''Prints stats for a individual hero'''
        print(self.kills)
        print(self.deaths)
        if self.deaths > 0:
            kd_ratio = self.kills/self.deaths
        else:
            kd_ratio = self.kills
            print("{} K/D Ratio: {}".format(self.name, kd_ratio))


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


    def update_kills(self, kills):
        '''
        Updates a heroes kill count for kills made in team battles
        '''
        for hero in self.heroes:
            hero.add_kill(kills)


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
            hero.show_stats()


    def add_hero(self, hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(hero)


    def remove_hero(self, name):
        '''
        Remove hero from heroes list
        1. check if the length of heroes list if greater than zero
        2. if length is zero, there are no heroes....return 0
        3. actually remove the correct hero if present
        '''

        if not (len(self.heroes) > 0):
            return 0

        else:
            for hero_obj in self.heroes:
                if hero_obj.name == name:
                    self.heroes.remove(hero_obj)
                else:
                    return 0


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
    arena = Arena('The Colosseum')
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
