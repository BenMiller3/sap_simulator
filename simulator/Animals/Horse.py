from simulator.Animals.Animal import Animal


class Horse(Animal):

    def __init__(self, attack=2, health=1):
        self.name = "Horse"
        self.description = "Friend summoned -> Give it +1 Attack until end of battle."
        self.tier = 1

        self.attack = attack
        self.health = health
