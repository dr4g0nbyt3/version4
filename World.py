import numpy as np
from enum import Enum
import MapSection

class Size(Enum):
    SMALL = 5
    MEDIUM = 10
    LARGE = 25

def generateMap(size):
    map = np.empty([size, size], dtype=MapSection)
    for x in range(size):
        for y in range(size):
            map[x, y] = MapSection.generateMapSection(x, y)
    return map

class World():

    def __init__(self, size):
        self.size = size
        self.map = generateMap(size)