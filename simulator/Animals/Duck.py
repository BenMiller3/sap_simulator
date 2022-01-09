from simulator.Animals.Animal import Animal


class Duck(Animal):

    def __init__(self, attack=1, health=2):
        self.name = "Duck"
        self.description = "Sell -> Give shop pets +1 Health"
        self.tier = 1

        self.attack = attack
        self.health = health
