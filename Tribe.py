class Tribe:

    # skills: Social, Economic, Housing,

    def __init__(self):
        self.size = 2
        self.population = 5
        self.sustainability = 2
        self.type = 1
        self.skillPredilection = 3
        self.property[tiles] = 1

        for p in range(self.population):
            self.persons.append(Person())

    def grow(self):
        self.size += 1
        self.population -= 1
