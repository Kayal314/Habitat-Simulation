class Landform:
    """
    We define a landform as the 3-tuple (L, F, W) where:
        L = locations
        F = food availability
        W = water availability
    """

    def __init__(self, locations: list, food: float, water: float):
        self.locations = locations
        self.food = food
        self.water = water

    def get_locations(self):
        return self.locations

    def get_water_amount(self):
        return self.water

    def get_food_amount(self):
        return self.food



class Grassland(Landform):
    def __init__(self):
        super(Grassland, self).__init__([(953, 113), (467, 383), (899, 522), (945, 888), (1676, 276)], 500, 0)

    def decrement_food(self):
        self.food -= 7


class Forest(Landform):
    def __init__(self):
        super(Forest, self).__init__([(348, 163), (1326, 259), (1705, 586), (633, 701), (290, 856)], 400, 50)

    def decrement_food(self):
        self.food -= 5


class Lake(Landform):
    def __init__(self):
        super(Lake, self).__init__([(1591, 878), (346, 587)], 0, 500)

    def decrement_water(self):
        self.water -= 7


class Pond(Landform):
    def __init__(self):
        super(Pond, self).__init__([(487, 198), (1330, 68), (1438, 487)], 0, 50)

    def decrement_water(self):
        self.water -= 5


class Quagmire(Landform):
    def __init__(self):
        super(Quagmire, self).__init__([(98, 330), (1158, 533)], 0, 0)


class Rugged(Landform):
    def __init__(self):
        super(Rugged, self).__init__([(923, 266), (1438, 659)], 0, 0)
