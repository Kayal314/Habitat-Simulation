class Landform:
    """
    We define a landform as the 5-tuple (L, F, W, R, f), where:
        L = locations
        F = food availability
        W = water availability
        R = rabbit count
        f = fatality
    """

    def __init__(self, locations: list, food: float, water: float, rabbit_count: int, fatality: int):
        self.locations = locations
        self.__food = food
        self.__water = water
        self.__rabbit_count = rabbit_count
        self.__fatality = fatality

    def increment_rabbit_count(self):
        self.__rabbit_count += 1

    def decrement_rabbit_count(self):
        self.__rabbit_count -= 1

    def get_rabbit_count(self):
        return self.__rabbit_count

    def get_water_amount(self):
        return self.__water

    def get_food_amount(self):
        return self.__food

    def get_fatality(self):
        return self.__fatality


class Grassland(Landform):
    def __init__(self):
        super(Grassland, self).__init__([(100, 100), (200, 200), (300, 300)], 500, 0, 0, 0)


# TODO: initialize the following classes in the same way with actual values @Sriyansh
class Forest(Landform):
    pass


class Lake(Landform):
    pass


class Pond(Landform):
    pass


class Quagmire(Landform):
    pass


class Rugged(Landform):
    pass
