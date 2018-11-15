class Tiger():
    '''A Tiger has a name and an age and favorite food'''
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.favorite_food = "Cat Nip"

    def __str__(self):
        return ("{} is {} years old".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))
        if food == self.favorite_food:
            print("Give me more!")




tony = Tiger('Tony', 66)
print(tony)
tony.favorite_food = "Frosted Flakes™"
print("{}'s favorite food is {}".format(tony.name, tony.favorite_food))
tony.eat(tony.favorite_food)

hobbes = Tiger("Hobbes")
print(hobbes)
hobbes.age = 24
print(hobbes)
hobbes.eat("Fish")
