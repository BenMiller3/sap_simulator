class Animal:

    def __init__(self, attack, health, tier):
        self.attack = attack
        self.health = health
        self.tier = tier

    def attacks(self):
        # add attack modifiers here
        return self.attack

    def take_damage(self, damage):
        # add defense modifiers here
        self.health -= damage

    def is_alive(self):
        return self.health > 0
