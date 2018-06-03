from enum import Enum


class Type(Enum):
    PLAINS = 1
    MOUNTAINS = 2
    SWAMP = 3
    DESERT = 4
    TUNDRA = 5


class Environment:
    def __init__(self, type, animals):
        self.type = type
        self.animals = animals