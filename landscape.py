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
       super(Grassland, self).__init__([(953, 113), (467, 383), (899,522),(945,888),(1676,276)], 500, 0, 0, 0)


class Forest(Landform):
    def __init__(self):
       super(Forest, self).__init__([(348, 163), (1326, 259), (1705,586),(633,701),(290,856)], 500, 0, 0, 0)


class Lake(Landform):
    def __init__(self):
       super(Lake, self).__init__([(1591, 878), (346,587)], 500, 0, 0, 0)


class Pond(Landform):
    def __init__(self):
       super(Pond, self).__init__([(487,198),(1330,68),(1438,487)], 500, 0, 0, 0)


class Quagmire(Landform):
    def __init__(self):
       super(Quagmire, self).__init__([(98, 330), (1158, 533)], 500, 0, 0, 0)


class Rugged(Landform):
    def __init__(self):
       super(Rugged, self).__init__([(923,266),(1438,659)], 500, 0, 0, 0)
