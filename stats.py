import matplotlib.pyplot as plt
import numpy as np


def write_population(rabbit: list, fox: list, grassland: list, forest: list, pond: list, lake: list):
    f = open('population_graph', 'w')
    size = len(rabbit)
    for i in range(0, size):
        f.write(rabbit[i] + " " + fox[i] + " " + grassland[i] + " " + forest[i] + " " + pond[i] + " " + lake)


def plot_animal_population(rabbit: list, fox: list):
    x_coordinates = range(1, len(rabbit) + 1)
    plt.plot(x_coordinates, rabbit, color='#3daeff', label='rabbit population')
    plt.plot(x_coordinates, fox, color='#ff3679', label='fox population')
    plt.legend(['rabbit', 'fox'])
    plt.show()


def plot_resource_changes(grassland: list, forest: list, pond: list, lake: list):
    x_coordinates = range(1, len(grassland) + 1)
    plt.plot(x_coordinates, grassland, color='#21d9c3', label='grassland')
    plt.plot(x_coordinates, forest, color='#460991', label='forest')
    plt.plot(x_coordinates, pond, color='#088538', label='pond')
    plt.plot(x_coordinates, lake, color='#d6d30b', label='lake')
    plt.legend(['grassland', 'forest', 'pond', 'lake'])
    plt.show()


def plot_all(grassland: list, forest: list, pond: list, lake: list, rabbit: list, fox: list):
    x_coordinates = range(1, len(rabbit) + 1)
    plt.plot(x_coordinates, rabbit, linestyle='dashed', color='#3daeff', label='rabbit population')
    plt.plot(x_coordinates, fox, linestyle='dashed', color='#ff3679', label='fox population')
    plt.plot(x_coordinates, grassland, color='#21d9c3', label='grassland')
    plt.plot(x_coordinates, forest, color='#460991', label='forest')
    plt.plot(x_coordinates, pond, color='#088538', label='pond')
    plt.plot(x_coordinates, lake, color='#d6d30b', label='lake')
    plt.legend(['rabbit', 'fox', 'grassland', 'forest', 'pond', 'lake'])
    plt.show()


def write(grassland: list, forest: list, pond: list, lake: list, rabbit: list, fox: list):
    f = open('population_graph', 'w')
    size = len(rabbit)
    for i in range(0, size):
        f.write(str(rabbit[i]) + "," + str(fox[i]) + "," + str(grassland[i]) + "," + str(forest[i]) +
                "," + str(lake[i]) + "," + str(pond[i]) + "\n")
    f.close()


def find_genetic_variation_rabbit(rabbits: list) -> list:
    variance = []
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.mating_requirement)
    variance.append(np.std(data))
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.step_size)
    variance.append(np.std(data))
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.thirst_resistance)
    variance.append(np.std(data))
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.hunger_resistance)
    variance.append(np.std(data))
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.predator_fear)
    variance.append(np.std(data))
    data = []
    for rabbit in rabbits:
        data.append(rabbit.genetics.vision)
    variance.append(np.std(data))
    return variance


def find_genetic_variation_fox(foxes: list) -> list:
    variance = []
    data = []
    for fox in foxes:
        data.append(fox.genetics.mating_requirement)
    variance.append(np.std(data))
    data = []
    for fox in foxes:
        data.append(fox.genetics.step_size)
    variance.append(np.std(data))
    data = []
    for fox in foxes:
        data.append(fox.genetics.thirst_resistance)
    variance.append(np.std(data))
    data = []
    for fox in foxes:
        data.append(fox.genetics.hunger_resistance)
    variance.append(np.std(data))
    data = []
    for fox in foxes:
        data.append(fox.genetics.hunting_skill)
    variance.append(np.std(data))
    data = []
    for fox in foxes:
        data.append(fox.genetics.vision)
    variance.append(np.std(data))
    return variance


def plot_variance_rabbit(variance):
    variance = np.array(variance).transpose()
    x_coordinates = range(1, len(variance[0]) + 1)
    fig, part = plt.subplots(2,3)
    part[0][0].plot(x_coordinates, variance[0], color='#0bd6cc')
    part[0][0].set_title('Mating Requirement')
    part[0][1].plot(x_coordinates, variance[1], color='#a70bd6')
    part[0][1].set_title('Step Size')
    part[0][2].plot(x_coordinates, variance[2], color='#d60b63')
    part[0][2].set_title('Thirst Resistance')
    part[1][0].plot(x_coordinates, variance[3], color='#22d42b')
    part[1][0].set_title('Hunger Resistance')
    part[1][1].plot(x_coordinates, variance[4], color='#f56c22')
    part[1][1].set_title('Predator Fear')
    part[1][2].plot(x_coordinates, variance[5], color='#17453f')
    part[1][2].set_title('Vision Radius')
    plt.show()


def plot_variance_fox(variance):
    variance = np.array(variance).transpose()
    x_coordinates = range(1, len(variance[0]) + 1)
    fig, part = plt.subplots(2, 3)
    part[0][0].plot(x_coordinates, variance[0], color='#0bd6cc')
    part[0][0].set_title('Mating Requirement')
    part[0][1].plot(x_coordinates, variance[1], color='#a70bd6')
    part[0][1].set_title('Step Size')
    part[0][2].plot(x_coordinates, variance[2], color='#d60b63')
    part[0][2].set_title('Thirst Resistance')
    part[1][0].plot(x_coordinates, variance[3], color='#22d42b')
    part[1][0].set_title('Hunger Resistance')
    part[1][1].plot(x_coordinates, variance[4], color='#f56c22')
    part[1][1].set_title('Hunting Skill')
    part[1][2].plot(x_coordinates, variance[5], color='#17453f')
    part[1][2].set_title('Vision Radius')
    plt.show()
