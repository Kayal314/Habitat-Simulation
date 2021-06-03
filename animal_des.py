import abc
import random
import math

STEP = 5


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

    def __init__(self, hunger: float, thirst: float, mating_urge: float, predator_fear: float, position: int):
        self.age = 0
        self.hunger = hunger
        self.thirst = thirst
        self.mating_urge = mating_urge
        self.predator_fear = predator_fear
        self.__position_in_food_chain = position
        self.X = random.randint(0, 1000)
        self.Y = random.randint(0, 800)
        self.image = None

    def set_image(self, image):
        self.image = image

    def get_position_in_food_chain(self):
        return self.__position_in_food_chain

    def find_current_need(self) -> str:
        if self.hunger >= self.thirst and self.hunger >= self.mating_urge and self.hunger >= self.predator_fear:
            return 'H'
        elif self.thirst >= self.hunger and self.thirst >= self.mating_urge and self.thirst >= self.predator_fear:
            return 'T'
        elif self.mating_urge >= self.hunger and self.mating_urge >= self.thirst and self.mating_urge >= \
                self.predator_fear:
            return 'M'

    def get_location(self):
        return self.X, self.Y

    def calculate_dist(self, pos: tuple):
        return ((pos[0] - self.X) ** 2 + (pos[1] - self.Y) ** 2) ** 0.5

    def take_small_step(self, pos: tuple):
        angle = math.atan((float(pos[1] - self.Y)) / (pos[0] - self.X))
        self.X = self.X + STEP * math.cos(angle)
        self.Y = self.Y + STEP * math.sin(angle)

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


class Rabbit(Animal):
    def __init__(self):
        super(Rabbit, self).__init__(1, 1, 0, 1, 1)

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
        return random.random() < 0.5
        # TODO: devise a mating mechanism

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
                    return Rabbit()



class Fox(Animal):
    def __init__(self):
        super(Fox, self).__init__(1, 1, 0, 1, 1)

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
        return random.random() < 0.4
        # TODO: devise a mating mechanism based of mating urge
        # if successful, then 0 the mating urge

    def check_current_location(self, **kwargs):
        rabbits = kwargs.get('rabbit')
        lake = kwargs.get('lake')
        pond = kwargs.get('pond')
        quagmire = kwargs.get('quagmire')
        rugged = kwargs.get('rugged')
        foxes = kwargs.get('fox')
        for rabbit in rabbits:
            if self.calculate_dist(rabbit.get_location) < 100:
                if self.hunger > 0:
                    self.hunger -= 15
                    rabbit.hunger += 1000  # kill off the rabbit
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
                    return Fox()

