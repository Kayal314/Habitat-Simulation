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


rabbit_entropy=[]
fox_entropy=[]
rabbit_mad=[]
fox_mad=[]
rabbit_mead=[]
fox_mead=[]
rabbit_std=[]
fox_std=[]
rabbit_coeffvar=[]
fox_coeffvar=[]
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
        rabbit_mad.append(find_genetic_variation_rabbit_mad(habitat.get_rabbits()))
        fox_mad.append(find_genetic_variation_fox_mad(habitat.get_foxes()))
        rabbit_mead.append(find_genetic_variation_rabbit_mean_ad(habitat.get_rabbits()))
        fox_mead.append(find_genetic_variation_fox_mean_ad(habitat.get_foxes()))
        rabbit_std.append(find_genetic_variation_rabbit_std(habitat.get_rabbits()))
        fox_std.append(find_genetic_variation_fox_std(habitat.get_foxes()))
        rabbit_entropy.append(find_genetic_variation_rabbit_entropy(habitat.get_rabbits()))
        fox_entropy.append(find_genetic_variation_fox_entropy(habitat.get_foxes()))
        rabbit_coeffvar.append(find_genetic_variation_rabbit_coeff_var(habitat.get_rabbits()))
        fox_coeffvar.append(find_genetic_variation_fox_coeff_var(habitat.get_foxes()))
        pygame.display.update()
    plot_all(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)
    write(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)


def run_without_visualisation(num_times: int):
    for i in range(0, num_times):
        print(f'Iteration number : {i}')
        rabbit_population.append(len(habitat.get_rabbits()))
        fox_population.append(len(habitat.get_foxes()))
        grassland.append(habitat.get_grassland_res())
        forest.append(habitat.get_forest_res())
        lake.append(habitat.get_lake_res())
        pond.append(habitat.get_pond_res())
        dead_animals = habitat.update()
        rabbit_mad.append(find_genetic_variation_rabbit_mad(habitat.get_rabbits()))
        fox_mad.append(find_genetic_variation_fox_mad(habitat.get_foxes()))
        rabbit_mead.append(find_genetic_variation_rabbit_mean_ad(habitat.get_rabbits()))
        fox_mead.append(find_genetic_variation_fox_mean_ad(habitat.get_foxes()))
        rabbit_std.append(find_genetic_variation_rabbit_std(habitat.get_rabbits()))
        fox_std.append(find_genetic_variation_fox_std(habitat.get_foxes()))
        rabbit_entropy.append(find_genetic_variation_rabbit_entropy(habitat.get_rabbits()))
        fox_entropy.append(find_genetic_variation_fox_entropy(habitat.get_foxes()))
        rabbit_coeffvar.append(find_genetic_variation_rabbit_coeff_var(habitat.get_rabbits()))
        fox_coeffvar.append(find_genetic_variation_fox_coeff_var(habitat.get_foxes()))

    plot_animal_population(rabbit_population, fox_population)
    plot_resource_changes(grassland=grassland, forest=forest, pond=pond, lake=lake)
    plot_variance_rabbit(rabbit_mad, "Median Absolute Deviation of Traits of Rabbits")
    plot_variance_fox(fox_mad, "Median Absolute Deviation of Traits of Foxes")
    plot_variance_rabbit(rabbit_mead, "Mean Absolute Deviation of Traits of Rabbits")
    plot_variance_fox(fox_mead, "Mean Absolute Deviation of Traits of Foxes")
    plot_variance_rabbit(rabbit_std, "Standard Deviation of Traits of Rabbits")
    plot_variance_fox(fox_std, "Standard Deviation of Traits of Foxes")
    plot_variance_rabbit(rabbit_entropy, "Entropy of Traits of Rabbits")
    plot_variance_fox(fox_entropy, "Entropy of Traits of Foxes")
    plot_variance_rabbit(rabbit_coeffvar, "Coefficient of Variation of Traits of Rabbits")
    plot_variance_fox(fox_coeffvar, "Coefficient of Variation of Traits of Foxes")

    write(grassland=grassland, forest=forest, pond=pond, lake=lake, rabbit=rabbit_population, fox=fox_population)


run_without_visualisation(120)
