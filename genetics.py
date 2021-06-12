import random


class Genetics:
    def __init__(self):
        self.mating_requirement = 0
        self.step_size = 0
        self.hunting_skill = 0  # only for foxes
        self.thirst_resistance = 0
        self.hunger_resistance = 0
        self.predator_fear = 0  # only for rabbits
        self.vision = 0

    def __str__(self):
        details = str(self.mating_requirement) + ":" + str(self.step_size) + ":" + str(self.hunting_skill) + ":" \
                  + str(self.thirst_resistance) + ":" + str(self.hunger_resistance) + ":" + str(self.predator_fear) \
                  + str(self.vision)
        return details

    def __mul__(self, other):
        genetics = Genetics()
        rand = random.random()
        if rand < 0.5:
            genetics.mating_requirement = self.mating_requirement
        else:
            genetics.mating_requirement = other.mating_requirement
        rand = random.random()
        if rand < 0.5:
            genetics.step_size = self.step_size
        else:
            genetics.step_size = other.step_size
        rand = random.random()
        if rand < 0.5:
            genetics.hunting_skill = self.hunting_skill
        else:
            genetics.hunting_skill = other.hunting_skill
        rand = random.random()
        if rand < 0.5:
            genetics.thirst_resistance = self.thirst_resistance
        else:
            genetics.thirst_resistance = other.thirst_resistance
        rand = random.random()
        if rand < 0.5:
            genetics.hunger_resistance = self.hunger_resistance
        else:
            genetics.hunger_resistance = other.hunger_resistance
        rand = random.random()
        if rand < 0.5:
            genetics.predator_fear = self.predator_fear
        else:
            genetics.predator_fear = other.predator_fear
        rand = random.random()
        if rand < 0.5:
            genetics.vision = self.vision
        else:
            genetics.vision = other.vision
        return genetics
