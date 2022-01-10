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

import random


class Farm:

    def generate_animal(self):
        tier_1_pets = [
            Ant(),
            Beaver(),
            Cricket(),
            Duck(),
            Fish(),
            Horse(),
            Mosquito(),
            Otter(),
            Pig(),
            Sloth()
        ]
        
        return random.choice(tier_1_pets)
