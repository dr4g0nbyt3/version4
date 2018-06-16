import Environment
import MapSection
import Tribe
import Person
import Pet
import numpy as np
from random import randint
from World import World
from World import Size

size = Size.SMALL


def placeTribes(map, tribes):
    taken = {}
    for i in range(tribes.size):
        placed = False
        while not placed:
            x = randint(0, size.value-1)
            y = randint(0, size.value-1)
            if (x, y) not in taken:
                taken[(x, y)] = True
                map[x, y] = tribes[i]
                tribes[i].setMapSection(map[x,y])  # double referenced - might not be good - see what's used the most.
                placed = True

def simulate(time, map, tribes):
    for i in range(time):
        for i in range(tribes.size):
            tribes[i].spendTime()


if __name__ == "__main__":
    print "Welcome to the environment evolution simulator."
    world = World(size)
    map = world.map

    tribes = Tribe.getTribes(size)
    placeTribes(map, tribes)
    simulate(1000, map, tribes)


