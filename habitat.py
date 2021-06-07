from animal_des import *
from landscape import *
import random


class Habitat:
    def __init__(self, initial_rabbit_count, initial_fox_count):
        self.__rabbits = []
        for i in range(0, initial_rabbit_count):
            new_rabbit = Rabbit()
            new_rabbit.genetics.step_size = random.randint(15, 25)
            new_rabbit.genetics.mating_requirement = random.random() * 2
            new_rabbit.genetics.hunger_resistance = random.random() / 2.0
            new_rabbit.genetics.thirst_resistance = random.random() / 2.0
            self.__rabbits.append(new_rabbit)
        self.__foxes = []
        for i in range(0, initial_fox_count):
            new_fox = Fox()
            new_fox.genetics.step_size = random.randint(10, 30)
            new_fox.genetics.mating_requirement = random.random() * 3
            new_fox.genetics.hunting_skill = random.randint(10, 100)
            new_fox.genetics.hunger_resistance = random.random()
            new_fox.genetics.thirst_resistance = random.random()
            self.__foxes.append(new_fox)
        self.__grassland = Grassland()
        self.__forest = Forest()
        self.__lake = Lake()
        self.__pond = Pond()
        self.__rugged = Rugged()
        self.__quagmire = Quagmire()

    def get_grassland_res(self):
        return self.__grassland.food

    def get_forest_res(self):
        return self.__forest.food

    def get_pond_res(self):
        return self.__pond.water

    def get_lake_res(self):
        return self.__lake.water

    def get_foxes(self):
        return self.__foxes

    def get_rabbits(self):
        return self.__rabbits

    def update(self) -> list:
        for rabbit in self.__rabbits:
            need = rabbit.find_current_need()
            if need.__eq__('H'):
                rabbit.find_food(grassland=self.__grassland, forest=self.__forest)
            elif need.__eq__('T'):
                rabbit.find_water(lake=self.__lake, pond=self.__pond)
            else:
                rabbit.find_mate(rabbit=self.__rabbits)

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
        dead_animals = []
        for rabbit in self.__rabbits:
            if rabbit.check_if_dead():
                dead_animals.append(rabbit)
                self.__rabbits.remove(rabbit)
            new_born = rabbit.check_current_location(grassland=self.__grassland, rabbit=self.__rabbits,
                                                     lake=self.__lake,
                                                     pond=self.__pond, quagmire=self.__quagmire, rugged=self.__rugged,
                                                     forest=self.__forest)
            if new_born:
                new_members_rabbit.append(new_born)
        for fox in self.__foxes:
            if fox.check_if_dead():
                dead_animals.append(fox)
                self.__foxes.remove(fox)
            new_born = fox.check_current_location(rabbit=self.__rabbits, lake=self.__lake,
                                                  pond=self.__pond, quagmire=self.__quagmire, rugged=self.__rugged,
                                                  fox=self.__foxes)
            if new_born:
                new_members_fox.append(new_born)

        self.__rabbits.extend(new_members_rabbit)
        self.__foxes.extend(new_members_fox)

        self.__pond.water += 0.6
        self.__lake.water += 0.5
        self.__grassland.food += 0.5
        self.__forest.food += 0.7

        return dead_animals
