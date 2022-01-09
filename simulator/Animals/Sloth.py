from simulator.Animals.Animal import Animal


class Sloth(Animal):

    def __init__(self, attack=1, health=1):
        self.name = "Sloth"
        self.description = "Has no special ability. Is kind of lame combat-wise. But he truly believes in you!"
        self.tier = 1

        self.attack = attack
        self.health = health
