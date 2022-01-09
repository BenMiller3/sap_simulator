from simulator.Animals.Animal import Animal


class Otter(Animal):

    def __init__(self, attack=1, health=2):
        self.name = "Otter"
        self.description = "Buy -> Give a random friend +1/-1"
        self.tier = 1

        self.attack = attack
        self.health = health
