from random import randint
import Environment
MAX_ALTITUDE = 1000
MIN_ALTITUDE = -1000


def generateMapSection(xPos, yPos):
    environment = randint(1, len(Environment.Type))
    altitude = randint(MIN_ALTITUDE, MAX_ALTITUDE)
    return MapSection(environment, altitude, xPos, yPos)

class MapSection():
    def __init__(self, environment, altitude, xPos, yPos):
        self.environment = environment
        self.altitude = altitude
        self.xPos = xPos
        self.yPos = yPos
