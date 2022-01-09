from simulator.Animals.Animal import Animal


class Mosquito(Animal):

    def __init__(self, attack=2, health=2):
        self.name = "Mosquito"
        self.description = "Start of battle: Deal 1 damage to 1 random enemy"
        self.tier = 1

        self.attack = attack
        self.health = health
