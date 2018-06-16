from random import randint

class Person:

    # Skill sets
    # highestSkillSet = mining, smithing, crafting
    # nextHighestSkillSet = construction, farming, strength
    # tribeSkillSet = fishing, cooking, archery

    # Initialise all of the starting variables.
    def __init__(self, name):
        self.strength = 6
        self.agility = 3
        self.accuracy = 3
        self.speed = 8
        self.energy = 10
        self.archery = 2
        self.magic = 4
        self.hunting = 3
        self.gathering = 4
        self.fishing = 4
        self.woodcutting = 4
        self.mining = 7
        self.smithing = 7
        self.cooking = 4
        self.farming = 6
        self.prayer = 4
        self.construction = 6
        self.creativity = 3
        self.alchemy = 4
        self.crafting = 7
        self.combat = 10
        self.sailing = 3
        self.name = name

    # Work function to start the work for the persons turn.
    def work(self):
        # 50% chance to work on highest skill set.
        # 25% chance to work on next highest skill set.
        # 25% chance to be influenced to work with tribe.
        randint()


