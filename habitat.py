from animal_des import *
from landscape import *


class Habitat:
    def __init__(self, initial_rabbit_count, initial_fox_count):
        self.__rabbits = []
        for i in range(0, initial_rabbit_count):
            self.__rabbits.append(Rabbit())
        self.__foxes = []
        for i in range(0, initial_fox_count):
            self.__foxes.append(Fox())
        self.__grassland = Grassland()
        self.__forest = Forest()
        self.__lake = Lake()
        self.__pond = Pond()
        self.__rugged = Rugged()
        self.__quagmire = Quagmire()

    def get_foxes(self):
        return self.__foxes

    def get_rabbits(self):
        return self.__rabbits

    def update(self):
        for rabbit in self.__rabbits:
            need = rabbit.find_current_need()
            if need.__eq__('H'):
                rabbit.find_food(grassland=self.__grassland, forest=self.__forest)
            elif need.__eq__('T'):
                rabbit.find_water(lake=self.__lake, pond=self.__pond)
            else:
                rabbit.find_mate(rabbit=self.__rabbits)
        self.grassland.food+= 1
        self.pond.water+=2
        self.forest.food+=1
        self.lake.water+=2

        # TODO: mechanism to display death of rabbit

        for fox in self.__foxes:
            need = fox.find_current_need()
            if need.__eq__('H'):
                fox.find_food(rabbit=self.__rabbits)
            elif need.__eq__('T'):
                fox.find_water(lake=self.__lake, pond=self.__pond)
            else:
                fox.find_mate(fox=self.__foxes)


        new_members_rabbit = []
        new_members_fox = []
        for rabbit in self.__rabbits:
            new_born = rabbit.check_current_location(grassland=self.__grassland, rabbit=self.__rabbits,
                                                     lake=self.__lake,
                                                     pond=self.__pond, quagmire=self.__quagmire, rugged=self.__rugged,
                                                     forest=self.__forest)
            if new_born:
                new_members_rabbit.append(new_born)
            if rabbit.check_if_dead():
                self.__rabbits.remove(rabbit)
        for fox in self.__foxes:
            new_born = fox.check_current_location(rabbit=self.__rabbits, lake=self.__lake,
                                                  pond=self.__pond, quagmire=self.__quagmire, rugged=self.__rugged,
                                                  fox=self.__foxes)
            if new_born:
                new_members_fox.append(new_born)
            if fox.check_if_dead():
                self.__foxes.remove(fox)

        self.__rabbits.extend(new_members_rabbit)
        self.__foxes.extend(new_members_fox)
