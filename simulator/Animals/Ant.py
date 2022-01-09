from simulator.Animals.Animal import Animal


class Ant(Animal):

    def __init__(self, attack=2, health=1):
        self.name = "Ant"
        self.description = "Faint: Give a random friend +2/+1"
        self.tier = 1

        self.attack = attack
        self.health = health
