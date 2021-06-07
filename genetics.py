class Genetics:
    def __init__(self):
        self.mating_requirement = 0
        self.step_size = 0
        self.hunting_skill = 0  # only for foxes
        self.thirst_resistance = 0
        self.hunger_resistance = 0

    def __str__(self):
        details = str(self.mating_requirement) + ":" + str(self.step_size) + ":" + str(self.hunting_skill) + ":" \
                  + str(self.thirst_resistance) + ":" + str(self.hunger_resistance)
        return details
