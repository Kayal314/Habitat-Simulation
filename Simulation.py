import pygame
from habitat import Habitat
import time
from stats import *

background = pygame.image.load('map.png')
rabbit_img = pygame.image.load('Sprites/rabbit.png')
fox_img = pygame.image.load('Sprites/fox.png')
grave_img = pygame.image.load('Sprites/grave.png')
habitat = Habitat(20, 7)
rabbit_population = []
fox_population = []
grassland = []
lake = []
pond = []
forest = []
variance_of_genes_rabbit = []
variance_of_genes_fox = []


def show_foxes(foxes, screen):
    for fox in foxes:
        screen.blit(fox_img, fox.get_location())


def show_rabbits(rabbits, screen):
    for rabbit in rabbits:
        screen.blit(rabbit_img, rabbit.get_location())


def show_graves(animals, screen):
    for animal in animals:
        screen.blit(grave_img, animal.get_location())


def run_with_visualisation(num_times: int):
    pygame.init()
    screen = pygame.display.set_mode((1800, 1012))
    pygame.display.set_caption('Habitat Simulation')
    pygame.display.set_icon(pygame.image.load('Sprites/icon.png'))

    running = True
    count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if count == num_times:
            running = False
        count += 1
        screen.blit(background, (0, 0))
        show_rabbits(habitat.get_rabbits(), screen)
        show_foxes(habitat.get_foxes(), screen)
        time.sleep(0.5)
        rabbit_population.append(len(habitat.get_rabbits()))
        fox_population.append(len(habitat.get_foxes()))
        grassland.append(habitat.get_grassland_res())
        forest.append(habitat.get_forest_res())
        lake.append(habitat.get_lake_res())
        pond.append(habitat.get_pond_res())
        dead_animals = habitat.update()
        variance_of_genes_rabbit.append(find_genetic_variation_rabbit(habitat.get_rabbits()))
        variance_of_genes_fox.append(find_genetic_variation_fox(habitat.get_foxes()))
        pygame.display.update()
    plot_all(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)
    write(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)


def run_without_visualisation(num_times: int):
    for i in range(0, num_times):
        rabbit_population.append(len(habitat.get_rabbits()))
        fox_population.append(len(habitat.get_foxes()))
        grassland.append(habitat.get_grassland_res())
        forest.append(habitat.get_forest_res())
        lake.append(habitat.get_lake_res())
        pond.append(habitat.get_pond_res())
        dead_animals = habitat.update()
        variance_of_genes_rabbit.append(find_genetic_variation_rabbit(habitat.get_rabbits()))
        variance_of_genes_fox.append(find_genetic_variation_fox(habitat.get_foxes()))

    plot_animal_population(rabbit_population, fox_population)
    plot_resource_changes(grassland=grassland, forest=forest, pond=pond, lake=lake)
    plot_variance_fox(variance_of_genes_fox)
    plot_variance_rabbit(variance_of_genes_rabbit)
    write(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)


run_without_visualisation(100)
