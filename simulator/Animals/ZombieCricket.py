from simulator.Animals.Animal import Animal


class ZombieCricket(Animal):

    def __init__(self, attack=1, health=1):
        self.name = "Zombie Cricket"
        self.description = ""
        self.tier = 1

        self.attack = attack
        self.health = health
