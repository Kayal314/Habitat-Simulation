import abc
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
        self.X = 0
        self.Y = 0
        self.image = None

    def set_image(self, image):
        self.image = image

    def get_position_in_food_chain(self):
        return self.__position_in_food_chain

    def find_current_need(self) -> str:
        if self.hunger >= self.thirst and self.hunger >= self.mating_urge and self.hunger >= self.predator_fear:
            self.find_food()
            return 'H'
        elif self.thirst >= self.hunger and self.thirst >= self.mating_urge and self.thirst >= self.predator_fear:
            self.find_water()
            return 'T'
        elif self.mating_urge >= self.hunger and self.mating_urge >= self.thirst and self.mating_urge >= self.predator_fear:
            self.find_mate()
            return 'M'
        else:
            self.evade_predator()
            return 'P'

    def get_location(self):
        return self.X, self.Y

    def calculate_dist(self, pos: tuple):
        return (pos[0]-self.X)**2 + (pos[1]-self.Y)**2

    @abc.abstractmethod
    def find_food(self):
        pass

    @abc.abstractmethod
    def find_water(self):
        pass

    @abc.abstractmethod
    def find_mate(self):
        pass

    @abc.abstractmethod
    def evade_predator(self):
        pass

    @abc.abstractmethod
    def mating_successful(self, animal) -> bool:
        pass

    @abc.abstractmethod
    def move_to(self, position: tuple):
        pass
