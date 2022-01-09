from simulator.Animals.Animal import Animal


class Beaver(Animal):

    def __init__(self, attack=2, health=2):
        self.name = "Beaver"
        self.description = "Sell -> Give 2 random friends +1 Health."
        self.tier = 1

        self.attack = attack
        self.health = health
