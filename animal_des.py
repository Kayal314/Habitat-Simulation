import abc
import random
import math


class Animal(abc.ABC):
    """
    Each animal is defined as a five-tuple (A, H, T, M, P, p) where:
        A = age
        H = hunger
        T = thirst
        M = urge to mate
        P = fear of predator
        p = position in the food chain
    """

    def __init__(self, hunger: float, thirst: float, mating_urge: float, predator_fear: float, position: int,
                 step: int):
        self.age = 0
        self.hunger = hunger
        self.thirst = thirst
        self.mating_urge = mating_urge
        self.predator_fear = predator_fear
        self.__position_in_food_chain = position
        self.X = random.randint(0, 1000)
        self.Y = random.randint(0, 800)
        self.age = 0
        self.STEP = step

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

    @abc.abstractmethod
    def update_self(self):
        pass

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
        self.X = self.X + self.STEP * math.cos(angle)
        self.Y = self.Y + self.STEP * math.sin(angle)

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
        super(Rabbit, self).__init__(1, 1, 0, 1, 1, 10)

    def find_food(self, **kwargs):
        grasslands = kwargs.get('grassland')
        forest = kwargs.get('forest')
        min_dist = 99999
        min_pos = self.get_location()
        for pos in grasslands.get_locations():
            dist = self.calculate_dist(pos)
            if dist < min_dist:
                min_dist = dist
                min_pos = pos
        for pos in forest.get_locations():
            dist = self.calculate_dist(pos) * self.predator_fear  # a fearful rabbit wouldn't prefer entering
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
        for pos in lakes.get_locations():
            dist = self.calculate_dist(pos)
            if dist < min_dist:
                min_dist = dist
                min_pos = pos
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
        is_successful = self.mating_urge > 5 and animal.mating_urge > 5
        self.mating_urge = 0
        animal.mating_urge = 0
        return is_successful

    def check_current_location(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        grassland = kwargs.get('grassland')
        forest = kwargs.get('forest')
        lake = kwargs.get('lake')
        pond = kwargs.get('pond')
        quagmire = kwargs.get('quagmire')
        rugged = kwargs.get('rugged')
        for loc in grassland.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.hunger > 0:
                    self.hunger -= 7
                    grassland.decrement_food()
                    return None
        for loc in forest.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.hunger > 0:
                    self.hunger -= 5
                    forest.decrement_food()
                    return None

        for loc in lake.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.thirst > 0:
                    self.thirst -= 7
                    lake.decrement_water()
                    return None

        for loc in pond.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.thirst > 0:
                    self.thirst -= 5
                    pond.decrement_water()
                    return None

        for loc in quagmire.get_locations():
            if self.calculate_dist(loc) < 100:
                self.hunger += 0.8
                self.thirst += 0.5
                return None

        for loc in rugged.get_locations():
            if self.calculate_dist(loc) < 100:
                self.hunger += 0.8
                self.thirst += 0.8
                return None
        for rabbit in rabbits:
            if self.calculate_dist(rabbit.get_location()) < 100:
                if self.mating_successful(rabbit):
                    new_born = Rabbit()
                    new_born.set_location((self.X + rabbit.X) / 2, (self.Y + rabbit.Y) / 2)
                    return new_born

    def check_if_dead(self):
        return self.thirst > 20 or self.hunger > 25 or self.age > 5

    def update_self(self):
        self.hunger += 0.5
        self.thirst += 0.6
        self.mating_urge += 0.4
        self.age += 0.1


class Fox(Animal):
    def __init__(self):
        super(Fox, self).__init__(1, 1, 0, 1, 1, 15)

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
        for pos in lakes.get_locations():
            dist = self.calculate_dist(pos)
            if dist < min_dist:
                min_dist = dist
                min_pos = pos
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
        is_successful = self.mating_urge > 5 and animal.mating_urge > 5
        self.mating_urge = 0
        animal.mating_urge = 0
        return is_successful

    def check_current_location(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        lake = kwargs.get('lake')
        pond = kwargs.get('pond')
        quagmire = kwargs.get('quagmire')
        rugged = kwargs.get('rugged')
        foxes = kwargs.get('fox')
        for rabbit in rabbits:
            if self.calculate_dist(rabbit.get_location()) < 100:
                if self.hunger > 0:
                    self.hunger -= 15
                    rabbit.age += 100  # kill the rabbit
                    return None

        for loc in lake.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.thirst > 0:
                    self.thirst -= 7
                    lake.decrement_water()
                    return None

        for loc in pond.get_locations():
            if self.calculate_dist(loc) < 100:
                if self.thirst > 0:
                    self.thirst -= 5
                    pond.decrement_water()
                    return None

        for loc in quagmire.get_locations():
            if self.calculate_dist(loc) < 100:
                self.hunger += 0.6
                self.thirst += 0.3
                return None

        for loc in rugged.get_locations():
            if self.calculate_dist(loc) < 100:
                self.hunger += 0.6
                self.thirst += 0.6
                return None

        for fox in foxes:
            if self.calculate_dist(fox.get_location()) < 100:
                if self.mating_successful(fox):
                    new_born = Fox()
                    new_born.set_location((self.X + fox.X) / 2, (self.Y + fox.Y) / 2)
                    return new_born

    def check_if_dead(self):
        return self.thirst > 30 or self.hunger > 35 or self.age > 3

    def update_self(self):
        self.hunger += 0.4
        self.thirst += 0.5
        self.mating_urge += 0.3
        self.age += 0.1
