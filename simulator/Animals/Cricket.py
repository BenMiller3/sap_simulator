from simulator.Animals.Animal import Animal


class Cricket(Animal):

    def __init__(self, attack=1, health=2):
        self.name = "Cricket"
        self.description = "Faint: Summon a 1/1 Cricket."
        self.tier = 1

        self.attack = attack
        self.health = health
