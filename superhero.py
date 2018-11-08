class Hero:
     '''
     This is the base class for our heroes. It includes
     add_ability, attack, take_damage, is_alive,
     and fight.
     '''
    def __init__(self, name, starting_health=100, current_health, abilies):
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
        for ability in abilities:
            total += ability.attack()
        return total

    def take_damage(self, damage):
        '''
        Method for recieving damage from the
        attack take_damagegit inti
        '''
        damage = attack()
        damage -= self.current_health
        return self.current_health

    def is_alive(self):
        '''
        this boolean function returns
        true if hero is alive and false if not
        '''
        if self.current_health > 0:
            print("{} Has died in battle".format(self.name))
            return True
        else:
            return False
#TODO: Run a loop to attack opponent until someone dies.
        def fight(self, opponent):
            '''
            This function runs the fight loop
            '''
            while
