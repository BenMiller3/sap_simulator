import unittest
from simulator.Animals.Ant import Ant
from simulator.Animals.Beaver import Beaver
from simulator.Animals.Cricket import Cricket
from simulator.Animals.Duck import Duck
from simulator.Animals.Fish import Fish
from simulator.Animals.Horse import Horse
from simulator.Animals.Mosquito import Mosquito
from simulator.Animals.Otter import Otter
from simulator.Animals.Pig import Pig
from simulator.Animals.Sloth import Sloth
from simulator.Animals.ZombieCricket import ZombieCricket


class TestAnimalStats(unittest.TestCase):

    def test_ant_base_stats(self):
        ant = Ant()
        self.assertEqual(2, ant.attack)
        self.assertEqual(1, ant.health)

    def test_beaver_base_stats(self):
        beaver = Beaver()

        self.assertEqual(2, beaver.health)
        self.assertEqual(2, beaver.attack)

    def test_cricket_base_stats(self):
        cricket = Cricket()

        self.assertEqual(1, cricket.attack)
        self.assertEqual(2, cricket.health)

    def test_duck_base_stats(self):
        duck = Duck()

        self.assertEqual(1, duck.attack)
        self.assertEqual(2, duck.health)

    def test_fish_base_stats(self):
        fish = Fish()

        self.assertEqual(2, fish.attack)
        self.assertEqual(3, fish.health)

    def test_horse_base_stats(self):
        horse = Horse()

        self.assertEqual(2, horse.attack)
        self.assertEqual(1, horse.health)

    def test_mosquito_base_stats(self):
        mosquito = Mosquito()

        self.assertEqual(2, mosquito.attack)
        self.assertEqual(2, mosquito.health)

    def test_otter_base_stats(self):
        otter = Otter()

        self.assertEqual(1, otter.attack)
        self.assertEqual(2, otter.health)

    def test_pig_base_stats(self):
        pig = Pig()

        self.assertEqual(3, pig.attack)
        self.assertEqual(1, pig.health)

    def test_sloth_base_stats(self):
        sloth = Sloth()

        self.assertEqual(1, sloth.attack)
        self.assertEqual(1, sloth.health)

    def test_zombie_cricket_base_stats(self):
        zombie_cricket = ZombieCricket()

        self.assertEqual(1, zombie_cricket.attack)
        self.assertEqual(1, zombie_cricket.health)

    def test_tier_1_animals(self):
        tier_one_pets = [
            Ant(),
            Beaver(),
            Cricket(),
            Duck(),
            Fish(),
            Horse(),
            Mosquito(),
            Otter(),
            Pig(),
            Sloth(),
            ZombieCricket()
        ]

        for pet in tier_one_pets:
            self.assertEqual(1, pet.tier)


if __name__ == '__main__':
    unittest.main()
