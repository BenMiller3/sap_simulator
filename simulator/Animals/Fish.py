from simulator.Animals.Animal import Animal


class Fish(Animal):

    def __init__(self, attack=2, health=3):
        self.name = "Fish"
        self.description = "Level-up -> Give all friends +1/+1."
        self.tier = 1

        self.attack = attack
        self.health = health
