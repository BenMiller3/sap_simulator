from simulator.Animals.Animal import Animal


class Pig(Animal):

    def __init__(self, attack=3, health=1):
        self.name = "Pig"
        self.description = "Sell -> Gain an extra 1 gold."
        self.tier = 1

        self.attack = attack
        self.health = health
