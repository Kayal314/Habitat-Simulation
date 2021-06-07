import abc
import random
import math
from genetics import Genetics


class Animal(abc.ABC):
    """
    Each animal is defined as a five-tuple (A, H, T, M, p) where:
        A = age
        H = hunger
        T = thirst
        M = urge to mate
        p = position in the food chain
    """

    def __init__(self, hunger: float, thirst: float, mating_urge: float, position: int,
                 genetics: Genetics):
        self.age = 0
        self.hunger = hunger
        self.thirst = thirst
        self.mating_urge = mating_urge
        self.__position_in_food_chain = position
        self.X = random.randint(0, 1000)
        self.Y = random.randint(0, 800)
        self.age = 0
        self.genetics = genetics

    def get_position_in_food_chain(self):
        return self.__position_in_food_chain

    def find_current_need(self) -> str:
        if self.hunger >= self.thirst and self.hunger >= self.mating_urge:
            need = 'H'
        elif self.thirst >= self.hunger and self.thirst >= self.mating_urge:
            need = 'T'
        else:
            need = 'M'
        self.update_self()
        return need

    def get_location(self):
        return self.X, self.Y

    def set_location(self, x, y):
        self.X = x
        self.Y = y

    def calculate_dist(self, pos: tuple):
        return ((pos[0] - self.X) ** 2 + (pos[1] - self.Y) ** 2) ** 0.5

    def take_small_step(self, pos: tuple):
        if pos[0] == self.X:
            angle = math.pi / 2
        else:
            angle = math.atan((float(pos[1] - self.Y)) / (pos[0] - self.X))
        self.X = self.X + self.genetics.step_size * math.cos(angle)
        self.Y = self.Y + self.genetics.step_size * math.sin(angle)

    def update_self(self):
        self.hunger += self.genetics.hunger_resistance
        self.thirst += self.genetics.thirst_resistance
        self.mating_urge += self.genetics.mating_requirement
        self.age += 0.1

    @abc.abstractmethod
    def find_food(self, **kwargs):
        pass

    @abc.abstractmethod
    def find_water(self, **kwargs):
        pass

    @abc.abstractmethod
    def find_mate(self, **kwargs):
        pass

    @abc.abstractmethod
    def mating_successful(self, animal) -> bool:
        pass

    @abc.abstractmethod
    def check_current_location(self, **kwargs):
        pass

    @abc.abstractmethod
    def check_if_dead(self):
        pass


class Rabbit(Animal):
    def __init__(self):
        super(Rabbit, self).__init__(1, 1, 0, 1, Genetics())

    def find_food(self, **kwargs):
        grasslands = kwargs.get('grassland')
        forest = kwargs.get('forest')
        min_dist = 99999
        min_pos = self.get_location()
        if grasslands.food > 0:
            for pos in grasslands.get_locations():
                dist = self.calculate_dist(pos)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        if forest.food > 0:
            for pos in forest.get_locations():
                dist = self.calculate_dist(
                    pos) * self.genetics.predator_fear  # a fearful rabbit wouldn't prefer entering
                # a forest for food
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        self.take_small_step(min_pos)

    def find_water(self, **kwargs):
        lakes = kwargs.get('lake')
        ponds = kwargs.get('pond')
        min_dist = 99999
        min_pos = self.get_location()
        if lakes.water > 0:
            for pos in lakes.get_locations():
                dist = self.calculate_dist(pos)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        if ponds.water > 0:
            for pos in ponds.get_locations():
                dist = self.calculate_dist(pos)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        self.take_small_step(min_pos)

    def find_mate(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        min_dist = 99999
        min_pos = self.get_location()
        for rabbit in rabbits:
            dist = self.calculate_dist(rabbit.get_location())
            if dist < min_dist:
                min_dist = dist
                min_pos = rabbit.get_location()
        self.take_small_step(min_pos)

    def mating_successful(self, animal) -> bool:
        is_successful = self.mating_urge >= 1.5 and animal.mating_urge >= 1.5
        self.mating_urge = -1
        animal.mating_urge = -1
        return is_successful

    def check_current_location(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        grassland = kwargs.get('grassland')
        forest = kwargs.get('forest')
        lake = kwargs.get('lake')
        pond = kwargs.get('pond')
        quagmire = kwargs.get('quagmire')
        rugged = kwargs.get('rugged')
        if grassland.food > 0:
            for loc in grassland.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.hunger > 0 and grassland.food > 0:
                        self.hunger -= 15
                        grassland.decrement_food()
                        return None
        if forest.food > 0:
            for loc in forest.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.hunger > 0 and forest.food > 0:
                        self.hunger -= 10
                        forest.decrement_food()
                        return None
        if lake.water > 0:
            for loc in lake.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.thirst > 0:
                        self.thirst -= 30
                        lake.decrement_water()
                        return None
        if pond.water > 0:
            for loc in pond.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.thirst > 0:
                        self.thirst -= 20
                        pond.decrement_water()
                        return None

        for loc in quagmire.get_locations():
            if self.calculate_dist(loc) < 60:
                self.hunger += 2
                self.thirst += 3
                return None

        for loc in rugged.get_locations():
            if self.calculate_dist(loc) < 60:
                self.hunger += 3
                self.thirst += 4
                return None
        for rabbit in rabbits:
            if self.calculate_dist(rabbit.get_location()) < 100:
                if self.mating_successful(rabbit):
                    new_born = Rabbit()
                    new_born.genetics.step_size = int((rabbit.genetics.step_size + self.genetics.step_size) / 2.0)
                    new_born.genetics.mating_requirement = (rabbit.genetics.mating_requirement +
                                                            self.genetics.mating_requirement) / 2.0
                    new_born.genetics.thirst_resistance = (self.genetics.thirst_resistance +
                                                           rabbit.genetics.thirst_resistance) / 2.0
                    new_born.genetics.hunger_resistance = (self.genetics.hunger_resistance +
                                                           rabbit.genetics.hunger_resistance) / 2.0
                    new_born.genetics.predator_fear = (self.genetics.predator_fear +
                                                       rabbit.genetics.predator_fear) / 2.0
                    new_born.genetics.vision = int((self.genetics.vision +
                                                    rabbit.genetics.vision) / 2.0)

                    new_born.set_location((self.X + rabbit.X) / 2, (self.Y + rabbit.Y) / 2)
                    return new_born

    def check_if_dead(self):
        return self.thirst > 40 or self.hunger > 35 or self.age > 45


class Fox(Animal):
    def __init__(self):
        super(Fox, self).__init__(1, 1, 0, 1, Genetics())

    def find_food(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        min_dist = 99999
        min_pos = self.get_location()
        for rabbit in rabbits:
            dist = self.calculate_dist(rabbit.get_location())
            if dist < min_dist:
                min_dist = dist
                min_pos = rabbit.get_location()
        self.take_small_step(min_pos)

    def find_water(self, **kwargs):
        lakes = kwargs.get('lake')
        ponds = kwargs.get('pond')
        min_dist = 99999
        min_pos = self.get_location()
        if lakes.water > 0:
            for pos in lakes.get_locations():
                dist = self.calculate_dist(pos)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        if ponds.water > 0:
            for pos in ponds.get_locations():
                dist = self.calculate_dist(pos)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = pos
        self.take_small_step(min_pos)

    def find_mate(self, **kwargs):
        rabbits = kwargs.get('fox')
        min_dist = 99999
        min_pos = self.get_location()
        for rabbit in rabbits:
            dist = self.calculate_dist(rabbit.get_location())
            if dist < min_dist:
                min_dist = dist
                min_pos = rabbit.get_location()
        self.take_small_step(min_pos)

    def mating_successful(self, animal) -> bool:
        is_successful = self.mating_urge > 2 and animal.mating_urge > 2
        self.mating_urge = -1
        animal.mating_urge = -1
        return is_successful

    def check_current_location(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        lake = kwargs.get('lake')
        pond = kwargs.get('pond')
        quagmire = kwargs.get('quagmire')
        rugged = kwargs.get('rugged')
        foxes = kwargs.get('fox')
        for rabbit in rabbits:
            if self.calculate_dist(rabbit.get_location()) < self.genetics.hunting_skill:
                if self.hunger >= 0:
                    self.hunger -= 30
                    rabbit.age = 100  # kill the rabbit
                    return None
        if lake.water > 0:
            for loc in lake.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.thirst > 0:
                        self.thirst -= 35
                        lake.decrement_water()
                        return None
        if pond.water > 0:
            for loc in pond.get_locations():
                if self.calculate_dist(loc) < self.genetics.vision:
                    if self.thirst > 0:
                        self.thirst -= 20
                        pond.decrement_water()
                        return None

        for loc in quagmire.get_locations():
            if self.calculate_dist(loc) < 60:
                self.hunger += 2
                self.thirst += 3
                return None

        for loc in rugged.get_locations():
            if self.calculate_dist(loc) < 60:
                self.hunger += 3
                self.thirst += 3
                return None

        for fox in foxes:
            if self.calculate_dist(fox.get_location()) < self.genetics.vision:
                if self.mating_successful(fox):
                    new_born = Fox()
                    new_born.genetics.step_size = int((fox.genetics.step_size + self.genetics.step_size) / 2.0)
                    new_born.genetics.mating_requirement = (fox.genetics.mating_requirement +
                                                            self.genetics.mating_requirement) / 2.0
                    new_born.genetics.hunting_skill = int((fox.genetics.hunting_skill +
                                                           self.genetics.hunting_skill) / 2.0)
                    new_born.genetics.hunger_resistance = (fox.genetics.hunger_resistance +
                                                           self.genetics.hunger_resistance) / 2.0
                    new_born.genetics.thirst_resistance = (fox.genetics.thirst_resistance +
                                                           self.genetics.thirst_resistance) / 2.0
                    new_born.genetics.vision = int((fox.genetics.vision + self.genetics.vision) / 2.0)
                    new_born.set_location((self.X + fox.X) / 2, (self.Y + fox.Y) / 2)
                    return new_born

    def check_if_dead(self):
        return self.thirst > 40 or self.hunger > 40 or self.age > 32
