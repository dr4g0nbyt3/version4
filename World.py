from enum import Enum

class Size(Enum):
    SMALL = 5
    MEDIUM = 10
    LARGE = 25

def generateMap(size):
    map = None
    #todo generate the map (2d array of map sections)
    return map

class World():

    def __init__(self, size):
        self.size = size
        self.map = generateMap(size)