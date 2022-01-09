class Animal:

    def __init__(self, attack, health, tier):
        self.attack = attack
        self.health = health
        self.tier = tier

    def lose_health(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0
