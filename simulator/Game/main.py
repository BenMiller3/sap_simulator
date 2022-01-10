from simulator.Animals.Fish import Fish
from simulator.Animals.Beaver import Beaver
from simulator.Animals.Duck import Duck
from simulator.Animals.Farm import Farm


# five states
# before game begins -- solve that
# before attack
# attack
# post attack
# post faint action
# end of game

def main():
    farm = Farm()

    p1 = []
    p2 = []

    for i in range(3):
        p1.append(farm.generate_animal())
        p2.append(farm.generate_animal())

    versus(p1, p2)


def battle(first_animal, second_animal):
    print(f"{first_animal.name} {first_animal.attack}/{first_animal.health} vs. {second_animal.name} {second_animal.attack}/{second_animal.health}")
    first_animal.take_damage(second_animal.attacks())
    second_animal.take_damage(first_animal.attacks())


def print_winner(first_animals, second_animals):
    if first_animals:
        print("Player A wins!")
    elif second_animals:
        print("Player 2 Wins! :D")
    else:
        print("A DRAW :D")


def versus(first_animals, second_animals):
    while first_animals and second_animals:
        first = first_animals[0]
        second = second_animals[0]

        battle(first, second)

        if not first.is_alive():
            first_animals.pop(0)
        if not second.is_alive():
            second_animals.pop(0)

    print_winner(first_animals, second_animals)


if __name__ == '__main__':
    main()
