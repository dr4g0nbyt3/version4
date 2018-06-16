from World import Size
import Person

def getTribes(size):
    tribes = []
    for i in range(size):
        tribes.append(Tribe(i))
    return tribes

class Tribe:

    # Skills: Social, Economic, Housing,

    # Initialise variables.
    def __init__(self, id):
        self.id = id
        self.size = 2
        self.population = 5
        self.sustainability = 2
        self.type = 1
        self.skillPredilection = 3
        self.property = []
        self.evolution = 1
        self.efficiency = 5
        self.mapSections = []

        self.people = []
        for p in range(self.population):
            self.people.append(Person())

    # Run the work function for all persons in the tribe on start.
    def work(self):
        # Labor Phase.
        for i in range(self.population):
            self.people[i].work

    # Run the grow function for the tribe.
    def grow(self, tile):
        self.size += 1
        self.property.append(tile)

    def attack(self):
        # Move militia
        move(self, militia)

    def prepareAttack(self):
        # Build militia
        train(self)
        grow(self, tileTowardsEnemy)

    def train(self):
        # Train soldiers.
        # List what you are able to train.
        combat(twohighestskilledcombatants)
        combat(highestskilledlowestskilledcombatants)
        combat(twohighestskilledcombatants)

    def addMapSection(self, mapSection):
        self.mapSections.append(mapSection)

    def spendTime(self):
        self.work()
        self.grow()
        self.train()
        self.prepareAttack()
        self.attack()


